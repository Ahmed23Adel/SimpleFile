from basic_func import *
from location import *
from fileAbs import *


class FileEdit(FileAbs):
    def __init__(self, file_loc):
        self.file_loc = file_loc
        self.location = Location.create_by_rowCol(row=0, col=0)
        self.content = None

    def _open_file(self):
        self.__file = open(self.file_loc, 'r+')

    def close_file(self):
        self.__file.close()

    def read_first_char(self, tmp=True):
        if tmp:
            return self.__perform_read_tmp(self.__read_first_char)
        return self.__perform_read_perm(self.__read_first_char)

    def __read_first_char(self):
        c = self.__file.read(1)
        return c

    def read_first_word(self, tmp=True):
        if tmp:
            return self.__perform_read_tmp(self.__read_first_word)
        return self.__perform_read_perm(self.__read_first_word)

    def __read_first_word(self):
        first_line = next(iter(self.__file))
        first_word = first_line.split(" ")[0]
        return first_word

    def read_first_sentence(self, tmp=True, contain_ender=True):
        """The end of a complete sentence should be marked by a period(.), a question mark(?) or an exclamation
        point(!) """
        if tmp:
            return self.__perform_read_tmp(self.__read_first_sentence, contain_ender)
        return self.__perform_read_perm(self.__read_first_sentence, contain_ender)

    def __read_first_sentence(self, contain_ender):
        sentence_lst = []
        while True:
            try:
                line = next(iter(self.__file))
            except:
                break
            is_sentence, i = self.__is_sentence(line)
            if is_sentence:
                sentence_lst.append(line)
                sentence = "".join(sentence_lst)
                return sentence[:i + 1 if contain_ender else i]
            sentence_lst.append(line)
        raise TypeError("Couldn't not find \".\" nor \"?\" nor \"!\" ")

    def __is_sentence(self, s):
        if "." in s or "?" in s or "!" in s:
            dot_index, ques_index, exc_index = s.find("."), s.find("?"), s.find("!")
            final_index = dot_index if dot_index != -1 else ques_index if ques_index != -1 else exc_index
            return True, final_index
        return False, -1

    def read_first_paragraph(self, tmp, contain_ender):
        """
        Paragraph must have \n at last
        """
        if tmp:
            return self.__perform_read_tmp(self.__read_first_paragraph, contain_ender)
        return self.__perform_read_perm(self.__read_first_paragraph, contain_ender)

    def __read_first_paragraph(self, contain_ender=True):
        sentence_lst = []
        while True:
            try:
                line = next(iter(self.__file))
            except:
                break
            is_paragraph, i = self.__is_paragraph(line)
            if is_paragraph:
                sentence_lst.append(line)
                sentence = "".join(sentence_lst)
                return sentence[:i + 1 if contain_ender else i]
            sentence_lst.append(line)
        raise TypeError("Couldn't not find \".\" nor \"?\" nor \"!\" ")

    def __is_paragraph(self, s):
        if "\n" in s:
            dot_index = s.find("\n")
            return True, dot_index
        return False, -1

    def __perform_read_tmp(self, func, *args, **kwargs):
        self.location.move_me_tmp(self.__file, 0)
        op = func(*args, **kwargs)
        self.location.guide_me(self.__file)
        return op

    def __perform_read_perm(self, func, *args, **kwargs):
        self.location.move_me_perm(self.__file, 0)
        op = func(*args, **kwargs)
        self.location.guide_me(self.__file)
        return op

    def replace_char(self, c_old, c_new, cap=False, tmp=False):
        if len(c_old) > 1 or len(c_new) > 1:
            raise TypeError("Your input has more than just one char, if it's the case; please consider using "
                            "replace_word() func")
        if tmp:
            return self.__perform_update(self.__replace_char_tmp, c_old, c_new, cap)
        else:
            return self.__perform_update(self.__update_content, self.__replace_char_perm, c_old, c_new, cap)

    def __replace_char_tmp(self, c_old, c_new, cap):
        content = self.__file.read()
        if cap:
            content_new = content.replace(c_old, c_new)
            content_new = content_new.replace(c_old.capitalize(), c_new)
        else:
            content_new = content.replace(c_old, c_new)
        self.location.guide_me(self.__file)
        return content_new

    def __replace_char_perm(self, c_old, c_new, cap):
        content = self.__file.read()
        if cap:
            content_new = content.replace(c_old, c_new)
            content_new = content_new.replace(c_old.capitalize(), c_new)
        else:
            content_new = content.replace(c_old, c_new)
        with open(self.file_loc, 'w') as file:
            file.write(content_new)
        self.location.guide_me(self.__file)
        return content_new

    def __update_content(self, func, *args, **kwargs):
        new_content = func(*args, **kwargs)
        self.content = new_content
        return new_content

    def __perform_update(self, func, *args, **kwargs):
        self.location.move_me_to_beg(self.__file)
        op = func(*args, **kwargs)
        self.location.guide_me(self.__file)
        return op

    def __str__(self):
        if self.content is None:
            content = ""
            with open(self.file_loc, "r") as f:
                content = f.read()
            self.content = content
        # with open(self.file_loc, "r") as f:
        #     content = f.read()
        return self.content
