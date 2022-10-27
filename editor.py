from basic_func import *
from location import *
from file_abs import *


class FileEdit(FileAbs):
    def __init__(self, file_loc: str):
        """
        Open a file for editing. you can read, write, delete, and append while opening in that mode.
        Args:
            file_loc (str): file location of the file to edit.
        """
        self.file_loc: str = file_loc
        self.location: LocationIndex = Location.create_by_index(index = 0)
        self.content: str = None

    def _open_file(self) -> None:
        """
        Open a file for editing. you can read, write, delete, and append while opening in that mode.
        """
        self.__file = open(self.file_loc, 'r+')

    def close_file(self) -> None:
        """
        Close the file.
        """
        self.__file.close()

    def read_first_char(self, tmp=True)-> str:
        """
        Read the first character of the file.
        Args:
            tmp (bool): if False, it navigates the seek to the beginning of the file.
        Returns:
            str: the first character of the file.
        """
        if tmp:
            return self.__perform_read_tmp(self.__read_first_char)
        return self.__perform_read_perm(self.__read_first_char)

    def __read_first_char(self) -> str:
        """
        Read the first character of the file.
        Returns:
            str: the first character of the file.
        """
        c = self.__file.read(1)
        return c

    def read_first_word(self, tmp=True) -> str:
        """
        Read the first word of the file.
        Args:
            tmp (bool): if False, it navigates the seek to the beginning of the file.
        """
        if tmp:
            return self.__perform_read_tmp(self.__read_first_word)
        return self.__perform_read_perm(self.__read_first_word)

    def __read_first_word(self) -> str:
        """
        Read the first word of the file.
        Returns:
            str: the first word of the file.
        """
        first_line = next(iter(self.__file))
        first_word = first_line.split(" ")[0]
        return first_word

    def read_first_sentence(self, tmp=True, contain_ender=True) -> str:
        """
        Read the first sentence of the file.
        The end of a complete sentence should be marked by a period(.), a question mark(?) or an exclamation
        point(!)
        Args:
            tmp (bool): if False, it navigates the seek to the beginning of the file.
            contain_ender (bool): if True, it returns the sentence till ./!/?
        Returns:
            str: the first sentence of the file.
        """
        if tmp:
            return self.__perform_read_tmp(self.__read_first_sentence, contain_ender)
        return self.__perform_read_perm(self.__read_first_sentence, contain_ender)

    def __read_first_sentence(self, contain_ender: bool) -> str:
        """
        Read the first sentence of the file.
        The end of a complete sentence should be marked by a period(.), a question mark(?) or an exclamation
        point(!)
        Args:
            contain_ender (bool): if True, it returns the sentence till ./!/?
        """
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
        raise EOFError("Couldn't not find \".\" nor \"?\" nor \"!\" ")

    def __is_sentence(self, s: str) -> bool:
        """
        The end of a complete sentence should be marked by a period(.), a question mark(?) or an exclamation
        point(!)
        Args:
            s (str): a sentence.
        Returns:
            bool: True if s is a sentence, False otherwise
        """
        if "." in s or "?" in s or "!" in s:
            dot_index, ques_index, exc_index = s.find("."), s.find("?"), s.find("!")
            final_index = dot_index if dot_index != -1 else ques_index if ques_index != -1 else exc_index
            return True, final_index
        return False, -1

    def read_first_paragraph(self, tmp: bool, contain_ender: bool) -> str:
        """
        Read the first paragraph of the file.
        Paragraph must have \n at last
        Args:
            tmp (bool): if False, it navigates the seek to the beginning of the file.
            contain_ender (bool): if True, it returns the sentence till \n.
        """
        if tmp:
            return self.__perform_read_tmp(self.__read_first_paragraph, contain_ender)
        return self.__perform_read_perm(self.__read_first_paragraph, contain_ender)

    def __read_first_paragraph(self, contain_ender: bool = True) -> str:
        """
        Read the first paragraph of the file.
        Paragraph must have \n at last
        Args:
            contain_ender (bool): if True, it returns the sentence till \n.
        """
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
        raise EOFError("Couldn't not find \".\" nor \"?\" nor \"!\" ")

    def __is_paragraph(self, s: str )-> bool:
        """
        check if str is a paragraph
        The end of a complete paragraph should be marked by a period(.), a question mark(?) or an exclamation
        point(!)
        Args:
            s (str): a sentence.
        """
        if "\n" in s:
            dot_index = s.find("\n")
            return True, dot_index
        return False, -1

    def __perform_read_tmp(self, func, *args, **kwargs) -> str:
        """
        Wrapper function, it calls the given function, but first it navigates to the beginning of the file
        and then calls the given function, and finally it the return the seek to the original position.
        Args:
            func (function): the function to be called.
            *args: the arguments to be passed to the function.
            **kwargs: the keyword arguments to be passed to the function.
        """
        self.location.move_me_tmp(self.__file, 0)
        op = func(*args, **kwargs)
        self.location.guide_me(self.__file)
        return op

    def __perform_read_perm(self, func, *args, **kwargs) -> str:
        """
        Wrapper function, it calls the given function, but first it navigates to the beginning of the file
        and then calls the given function. and finally it the return the seek to 0.
        Args:
            func (function): the function to be called.
            *args: the arguments to be passed to the function.
            **kwargs: the keyword arguments to be passed to the function.
        """
        self.location.move_me_perm(self.__file, 0)
        op = func(*args, **kwargs)
        self.location.move_to(len(op))
        return op

    def replace_char(self, c_old: str, c_new: str, cap: bool = False, tmp: bool = False) -> str:
        """
        Replace the character c_old with c_new.
        Args:
            c_old (str): the character to be replaced.
            c_new (str): the character to replace it with.
            tmp (bool): if true, it replaces the character in the file, if False, returns a copy of new string without replacing it in the file
            cap: if true, replace the char and it c_old.Capitalization() with the new c_new
        """
        if len(c_old) > 1 or len(c_new) > 1:
            raise TypeError("Your input has more than just one char, if it's the case; please consider using "
                            "replace_word() func")
        if tmp:
            return self.__perform_update(self.__replace_char_tmp, c_old, c_new, cap)
        else:
            return self.__perform_update(self.__update_content, self.__replace_char_perm, c_old, c_new, cap)

    def __replace_char_tmp(self, c_old, c_new, cap) -> str:
        """
       Replace the character c_old with c_new, and return the edited string; withoug editing the file itself.
       Args:
           c_old (str): the character to be replaced.
           c_new (str): the character to replace it with.
           tmp (bool): if true, it replaces the character in the file, if False, returns a copy of new string without replacing it in the file
           cap: if true, replace the char and it c_old.Capitalization() with the new c_new
        """
        content = self.__file.read()
        if cap:
            content_new = content.replace(c_old, c_new)
            content_new = content_new.replace(c_old.capitalize(), c_new)
        else:
            content_new = content.replace(c_old, c_new)
        self.location.guide_me(self.__file)
        return content_new

    def __replace_char_perm(self, c_old, c_new, cap) -> str:
        """
       Replace the character c_old with c_new, and return the edited string; and edit the file itself.
       Args:
           c_old (str): the character to be replaced.
           c_new (str): the character to replace it with.
           tmp (bool): if true, it replaces the character in the file, if False, returns a copy of new string without replacing it in the file
           cap: if true, replace the char and it c_old.Capitalization() with the new c_new
        """
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

    def __update_content(self, func, *args, **kwargs) -> str:
        """
        content is the var in class editor that hold string held in the file, for not reading it multiple times
        if function updates anything in the file; it must call this function for updating the string once.
        or please consider calling this function at the end of multiple updates to the file.
        Args:
            func (function): the function to be called.
            *args: the arguments to be passed to the function.
            **kwargs: the keyword arguments to be passed to the function.
        return
        the string returned by the function

        """
        new_content = func(*args, **kwargs)
        self.content = new_content
        return new_content

    def __perform_update(self, func, *args, **kwargs) -> str:
        """
        For updating the file, the seek must be at 0 for reading it, so call this wrapper for doing that, and it shall
        call the function that updates the file
        Args:
            func (function): the function to be called.
            *args: the arguments to be passed to the function.
        Returns:
            return the string returned by the function
        """
        self.location.move_me_to_beg(self.__file)
        op = func(*args, **kwargs)
        self.location.guide_me(self.__file)
        return op

    def __str__(self):
        """
        Return the string of the file.
        """
        if self.content is None:
            content = ""
            with open(self.file_loc, "r") as f:
                content = f.read()
            self.content = content
        return "****** File Editor ****** at Location: {} and content is:\n{}".format(self.location.__str__(), self.content)
