from file_abs import *
from typing import Tuple


class FileReader(FileOpenerABC):

    def __init__(self, file_loc: str):
        super(FileReader, self).__init__(file_loc)

    def _open_file(self) -> None:
        """
        Open a file for editing. you can read, write, delete, and append while opening in that mode.
        """
        super(FileReader, self)._open_file()

    def close(self) -> None:
        """
       Close the file.
       """
        super(FileReader, self).close()

    def save_as(self, new_name: str) -> None:
        """
        Save the file as a new name, please give complete path
        """
        super(FileReader, self).save_as(new_name)

    def read_first_char(self, tmp: bool) -> SubText:
        """
        Read the first character of the file.
        Arguments:
            tmp (bool): if False, it navigates the seek to the beginning of the file, if true, it will not.
        Returns:
            str: the first character of the file.
        """
        if tmp:
            return self.__perform_read_first_tmp(self.__read_first_char)
        return self.__perform_read_first_tmp(self.__read_first_char)

    def __read_first_char(self) -> SubText:
        """
        Read the first character of the file.
        Returns:
            str: the first character of the file.
        """
        return self.__read_first_n_chars(1)

    def read_first_n_chars(self, n: int, tmp: bool) -> SubText:
        """
        Read the first n characters of the file.
        Arguments:
            tmp (bool): if False, it navigates the seek to the beginning of the file,
            if true, it will not.
            n: number of paragraphs to read from the file.
        Returns:
            str: the first n characters of the file.

        """
        if tmp:
            return self.__perform_read_first_tmp(self.__read_first_n_chars, n)
        return self.__perform_read_first_tmp(self.__read_first_n_chars, n)

    def __read_first_n_chars(self, n: int) -> SubText:
        """
        Read the first n characters of the file.
        Arguments:
            tmp (bool): if False, it navigates the seek to the beginning of the file,
            if true, it will not.
            n: number of paragraphs to read from the file.
        Returns:
            str: the first n characters of the file.

        """
        c = self._file.read(n)
        return SubText(SubTextKind.CHAR, c, loc_start=LocationIndex(1), loc_end=LocationIndex(2))

    def read_first_word(self, tmp: bool, skip_non_char: bool) -> SubText:
        """
        Read the first word of the file.
        Arguments:
            tmp (bool): if False, it navigates the seek to the beginning of the file, if true, it will not.
            skip_non_char (bool): ex, word is "Phantom," if True it returns "Phantom" without"," if False,
            it returns it with ",".
        """
        if tmp:
            return self.__perform_read_first_tmp(self.__read_first_word, skip_non_char)
        return self.__perform_read_first_perm(self.__read_first_word, skip_non_char)

    def __read_first_word(self, skip_non_char: bool) -> SubText:
        """
        Read the first word of the file.
        Returns:
            str: the first word of the file.
        """
        first_line = next(iter(self._file))
        first_word = first_line.split(" ")[0]
        while skip_non_char and not first_word[-1].isalpha():
            first_word = first_word[:-1]
        return SubText(SubTextKind.WORD, first_word, LocationIndex(0), LocationIndex(len(first_word)))

    def read_first_n_words(self, n: int, tmp: bool, skip_non_char: bool) -> SubText:
        """
        Read the first n words of the file.
        Arguments:
            tmp (bool): if False, it navigates the seek to the beginning of the file,
            if true, it will not.
            n: number of words to read from the file.
            skip_non_char (bool): ex, word is "Phantom," if True it returns "Phantom" without"," if False,
            it returns it with ",".
        Returns:
            str: the first n words of the file.

        """
        if tmp:
            return self.__perform_read_first_tmp(self.__read_first_n_words, n, skip_non_char)
        return self.__perform_read_first_perm(self.__read_first_n_words, n, skip_non_char)

    def __read_first_n_words(self, n: int, skip_non_char: bool) -> SubText:
        """
        Read the first n words of the file.
        Arguments:
            tmp (bool): if False, it navigates the seek to the beginning of the file,
            if true, it will not.
            n: number of words to read from the file.
            skip_non_char (bool): ex, word is "Phantom," if True it returns "Phantom" without"," if False,
            it returns it with ",".
        Returns:
            str: the first n words of the file.

        """
        first_line = next(iter(self._file))
        first_n_word = first_line.split(" ")[:n]
        while skip_non_char and not first_n_word[-1].isalpha():
            first_n_word[-1] = first_n_word[-1][:-1]
        final_words = " ".join(first_n_word)
        return SubText(SubTextKind.WORD, final_words, LocationIndex(0), LocationIndex(len(final_words)))

    def read_first_sentence(self, tmp: bool, contain_ender: bool) -> SubText:
        """
        Read the first sentence of the file.
        The end of a complete sentence should be marked by a period(.), a question mark(?) or an exclamation
        point(!)
        Arguments:
            tmp (bool): if False, it navigates the seek to the beginning of the file.
            contain_ender (bool): if True, it returns the sentence till ./!/?
        Returns:
            str: the first sentence of the file.
        """
        if tmp:
            return self.__perform_read_first_tmp(self.__read_first_sentence, contain_ender)
        return self.__perform_read_first_perm(self.__read_first_sentence, contain_ender)

    def __read_first_sentence(self, contain_ender: bool) -> SubText:
        """
        Read the first sentence of the file.
        The end of a complete sentence should be marked by a period(.), a question mark(?) or an exclamation
        point(!)
        Args:
            contain_ender (bool): if True, it returns the sentence till ./!/?
        """
        line_lst = []
        while True:
            try:
                line = next(iter(self._file))
            except:
                break
            is_sentence, i = self.__is_sentence(line)
            if is_sentence:
                sentence = line[:i + 1 if contain_ender else i]
                line_lst.append(sentence)
                fina_sentence = "".join(line_lst)
                return SubText(SubTextKind.SENTENCE, fina_sentence, LocationIndex(0), LocationIndex(len(fina_sentence)))
            else:
                line_lst.append(line)
        raise EOFError("Couldn't not find \".\" nor \"?\" nor \"!\" ")

    def read_first_n_sentences(self, n: int, tmp: bool, contain_ender: bool) -> SubText:
        """
        Read the first n setnences of the file.
        Arguments:
            tmp (bool): if False, it navigates the seek to the beginning of the file,
            if true, it will not.
            n: number of setnences to read from the file.
            contain_ender (bool): if True, it returns the sentence till "." or "?" or "!".
        Returns:
            str: the first n setnences of the file.

        """
        if tmp:
            return self.__perform_read_first_tmp(self.__read_first_n_sentences, n, contain_ender)
        return self.__perform_read_first_perm(self.__read_first_n_sentences, n, contain_ender)

    def __read_first_n_sentences(self, n: int, contain_ender: bool) -> SubText:
        """
        Read the first n setnences of the file.
        Arguments:
            tmp (bool): if False, it navigates the seek to the beginning of the file,
            if true, it will not.
            n: number of setnences to read from the file.
            contain_ender (bool): if True, it returns the sentence till "." or "?" or "!".
        Returns:
            str: the first n setnences of the file.

        """
        line_lst = []
        sentence_lst = []
        counter_sentences = 0
        while True:
            try:
                line = next(iter(self._file))
            except:
                break
            is_sentence, i = self.__is_sentence(line)
            if is_sentence:
                sentence = line
                line_lst.append(sentence)
                fina_sentence = "".join(line_lst)
                sentence_lst.append(fina_sentence)
                counter_sentences += 1
                line_lst = []
            else:
                line_lst.append(line)
            if counter_sentences == n:
                final_n_sens = "".join(sentence_lst)
                final_n_sens = final_n_sens[: -1 if contain_ender else -2]
                return SubText(SubTextKind.SENTENCE, final_n_sens, LocationIndex(0), LocationIndex(len(final_n_sens)) )
        raise EOFError("Couldn't not find \".\" nor \"?\" nor \"!\" ")

    def __is_sentence(self, s: str) -> Tuple:
        """
        The end of a complete sentence should be marked by a period(.), a question mark(?) or an exclamation
        point(!)
        Args:
            s (str): a sentence.
        Returns:
            bool: True if s is a sentence, False otherwise
        """
        if "." in s or "?" in s or "!" in s:
            dot_index, ques_index, exec_index = s.find("."), s.find("?"), s.find("!")

            is_valid = lambda x: True if x != -1 else False
            indxs = [dot_index, ques_index, exec_index]
            indxs = [x for x in indxs if is_valid(x)]
            final_index = min(indxs)
            return True, final_index
        return False, -1

    def read_first_paragraph(self, tmp: bool, contain_ender: bool) -> SubText:
        """
        Read the first paragraph of the file.
        Paragraph must have \n at last
        Args:
            tmp (bool): if False, it navigates the seek to the beginning of the file.
            contain_ender (bool): if True, it returns the sentence till \n.
        Returns:
            str: the first paragraph of the file.
        """
        if tmp:
            return self.__perform_read_first_tmp(self.__read_first_paragraph, contain_ender)
        return self.__perform_read_first_perm(self.__read_first_paragraph, contain_ender)

    def __read_first_paragraph(self, contain_ender: bool = True) -> SubText:
        """
        Read the first paragraph of the file.
        Paragraph must have \n at last
        Args:
            contain_ender (bool): if True, it returns the sentence till \n.
        """
        sentence_lst = []
        while True:
            try:
                line = next(iter(self._file))
            except:
                break
            is_paragraph, i = self.__is_paragraph(line)
            if is_paragraph:
                sentence_lst.append(line)
                sentence = "".join(sentence_lst)
                final_par = sentence[:i + 1 if contain_ender else i]
                return SubText(SubTextKind.PARAGRAPH, final_par, LocationIndex(0), LocationIndex(len(final_par)))
            sentence_lst.append(line)

        raise EOFError("Couldn't not find \"\\n\"")

    def __is_paragraph(self, s: str) -> Tuple:
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

    def read_first_n_paragraph(self, n: int, tmp: bool, contain_ender: bool) -> SubText:
        """
        Read the first n paragraphs of the file.
        Arguments:
            tmp (bool): if False, it navigates the seek to the beginning of the file,
            if true, it will not.
            n: number of paragraphs to read from the file.
        Returns:
            str: the first n paragraphs of the file.

        """
        if tmp:
            return self.__perform_read_first_tmp(self.__read_first_n_paragraph, n, contain_ender)
        return self.__perform_read_first_perm(self.__read_first_n_paragraph, n, contain_ender)

    def __read_first_n_paragraph(self, n: int, contain_ender: bool) -> SubText:
        sentence_lst = []
        par_lst = []
        par_counter =0
        while True:
            try:
                line = next(iter(self._file))
            except:
                break
            is_paragraph, i = self.__is_paragraph(line)
            if is_paragraph:
                sentence_lst.append(line)
                sentence = "".join(sentence_lst)
                final_par = sentence
                par_lst.append(final_par)
                par_counter += 1
                sentence_lst = []
            else:
                sentence_lst.append(line)
            if par_counter == n:
                final_par = "".join(par_lst)
                final_par = final_par[: -1 if contain_ender else -2]
                return SubText(SubTextKind.PARAGRAPH, final_par, LocationIndex(0), LocationIndex(len(final_par)))

        raise ValueError("Couldn't find paragraph")

    def read_char_at(self, location: Location):
        """
        Read the character at the given location.
        Arguments:
            location (Location): the location of the character.
        Returns:
            str: the character at the given location.
        """
        pass

    def read_word_at(self, location: Location):
        """
        Read the word at the given location.
        Arguments:
            location (Location): the location of the character.
        Returns:
            str: the character at the given location.
        """
        pass

    def read_sentence_at(self, location: Location):
        """
        Read the sentence at the given location.
        Arguments:
            location (Location): the location of the character.
        Returns:
            str: the character at the given location.
        """
        pass

    def read_paragraph_at(self, location: Location):
        """
        Read the paragraph at the given location.
        Arguments:
            location (Location): the location of the character.
        Returns:
            str: the character at the given location.
        """
        pass

    def read_next_char(self, skip_non_char: bool = False, raise_error: bool = True) -> SubText:
        """
        Get the next character, starting from the current position(which is sepcified by last index it went to)
        Args:
            None
        """
        if raise_error:
            return self.__read_next_char(skip_non_char, self.__file_ended_raise)
        else:
            return self.__read_next_char(skip_non_char, self.__file_ended_no_raise)

    def __read_next_char(self, skip_non_char: bool, raise_error_response):
        if self.location.is_fil_ended(self.file_len):
            return raise_error_response()

        current_char = self._file.read(1)
        self.location.move_by(1)
        if skip_non_char and not current_char.isalpha():
            return self.__read_next_char(skip_non_char, raise_error_response)
        current_loc = self.location.get_location()
        self.last_char = current_char
        return SubText(SubTextKind.CHAR, current_char, LocationIndex(current_loc), LocationIndex(current_loc + 1))

    def read_next_word(self, skip_non_char: bool, raise_error: bool, start_new_word: bool) -> SubText:
        """
        Get the next word, starting from the current position(which is sepcified by last index it went to)
        Args:
            None

        """
        if raise_error:
            return self.__read_next_word(skip_non_char, self.__file_ended_raise)
        else:
            return self.__read_next_word(skip_non_char, self.__file_ended_no_raise)

    def __read_next_word(self, skip_non_char: bool, raise_error_response):
        if self.location.is_fil_ended(self.file_len):
            return raise_error_response()
        init_loc = self.location.get_location()
        word_lst = []
        while True:
            current_char = self._file.read(1)
            if current_char == " ":
                self.location.move_by(1)
                break
            if current_char == "":
                break
            if word_lst and not current_char.isalpha() and skip_non_char:
                self.location.move_by(1)
                continue
            word_lst.append(current_char)
        word = "".join(word_lst)
        self.location.move_by(len(word))
        return SubText(SubTextKind.WORD, word, LocationIndex(init_loc), LocationIndex(init_loc + len(word)))

    def read_last_n_paragraph(self, n: int, tmp: bool) -> str:
        """
        Read the last n paragraphs of the file.
        Arguments:
            tmp (bool): if False, it navigates the seek to the beginning of the file,
            if true, it will not.
            n: number of paragraphs to read from the file.
        Returns:
            str: the first n paragraphs of the file.

        """
        pass

    def read(self, start_loc: Location, end_loc: Location):
        """
        Read the text in the file starting from start_loc adn ending at end_loc.
        Arguments:
            start_loc (Location): the start location of the file.
            end_loc (Location): the end location of the file.
        """
        pass

    def __perform_read_first_tmp(self, func, *args, **kwargs) -> SubText:
        """
        Wrapper function, it calls the given function, but first it navigates to the beginning of the file
        and then calls the given function, and finally it the return the seek to the original position.
        Args:
            func (function): the function to be called.
            *args: the arguments to be passed to the function.
            **kwargs: the keyword arguments to be passed to the function.
        """
        self.location.move_me_tmp(self._file, 0)
        op = func(*args, **kwargs)
        self.location.guide_me(self._file)
        return op

    def __perform_read_first_perm(self, func, *args, **kwargs) -> SubText:
        """
        Wrapper function, it calls the given function, but first it navigates to the beginning of the file
        and then calls the given function. and finally it the return the seek to 0.
        Args:
            func (function): the function to be called.
            *args: the arguments to be passed to the function.
            **kwargs: the keyword arguments to be passed to the function.
        """
        self.location.move_me_perm(self._file, 0)
        op = func(*args, **kwargs)
        self.location.move_to(len(op) + 1)
        return op

    def replace_char(self, c_old: str, c_new: str, cap: bool, tmp: bool) -> str:
        """
        Replace a character in the file.
        Arguments:
            c_old (str): the character to be replaced.
            c_new (str): the character to replace it with.
            tmp (bool): if true, it replaces the character in the file, if False, returns a copy of new string without replacing it in the file
            cap: if true, replace the char and it c_old.Capitalization() with the new c_new
        Returns:
            str: the replaced string.

        """
        raise TypeError("Replacing is not allowed while using Reader model")

    def replace_char(self, c_old_loc: Location, c_new: str, cap: bool, tmp: bool) -> str:
        """
        Replace a character in the file.
        Arguments:
            c_old_loc (str): location at which you want to replace the char there with the c_new.
            c_new (str): the character to replace it with.
            tmp (bool): if true, it replaces the character in the file, if False, returns a copy of new string without replacing it in the file
            cap: if true, replace the char and it c_old.Capitalization() with the new c_new
        Returns:
            str: the replaced string.

        """
        pass

    def replace_word(self, word_old: str, word_new: str, tmp: bool) -> str:
        """
        Replace a character in the file.
        Arguments:
            word_old (str): the word to be replaced.
            word_new (str): the word to replace it with.
            tmp (bool): if true, it replaces the character in the file, if False, returns a copy of new string without replacing it in the file
        Returns:
            str: the replaced string.

        """
        pass

    def replace_word(self, word_old_loc: Location, word_new: str, tmp: bool) -> str:
        """
        Replace a character in the file. it will look forward untill it finds the first " "(space).
        Arguments:
            word_old_loc (str): location at which you want to replace the char there with the word_old.
            word_new (str): the word to replace it with.
            tmp (bool): if true, it replaces the character in the file, if False, returns a copy of new string without replacing it in the file
        Returns:
            str: the replaced string.

        """
        pass

    def replace_sentence(self, sen_old: str, sen_new: str, tmp: bool) -> str:
        """
        Replace a character in the file.
        Arguments:
            sen_old (str): the sentence to be replaced.
            sen_new (str): the sentence to replace it with.
            tmp (bool): if true, it replaces the character in the file, if False, returns a copy of new string without replacing it in the file
        Returns:
            str: the replaced string.

        """
        pass

    def replace_sentence(self, sen_old_loc: str, sen_new: str, tmp: bool) -> str:
        """
        Replace a character in the file. it will look forward untill it finds the first "." "!" or "?"
        Arguments:
            sen_old_loc (str): location at which you want to replace the char there with the sen_old.
            sen_new (str): the sentence to replace it with.
            tmp (bool): if true, it replaces the character in the file, if False, returns a copy of new string without replacing it in the file
        Returns:
            str: the replaced string.

        """
        pass

    def replace_paragraph(self, par_old: str, par_new: str, tmp: bool) -> str:
        """
        Replace a character in the file.
        Arguments:
            par_old (str): the word to be replaced.
            sen_new (str): the word to replace it with.
            tmp (bool): if true, it replaces the character in the file, if False, returns a copy of new string without replacing it in the file
        Returns:
            str: the replaced string.

        """
        pass

    def replace_paragraph(self, par_old_old: Location, str, par_new: str, tmp: bool) -> str:
        """
        Replace a character in the file., it will look forward untill it finds the first "\n"
        Arguments:
            par_old_old (str):  location at which you want to replace the char there with the par_old.
            sen_new (str): the word to replace it with.
            tmp (bool): if true, it replaces the character in the file, if False, returns a copy of new string without replacing it in the file
        Returns:
            str: the replaced string.

        """
        pass

    def replace_by_loc(self, loc_start: Location, loc_end: Location, new_text: str):
        """
        Replace text starting at the given location by loc_start, and ending at the given location by loc_end.
        Arguments:
            loc_start (str): start location that will hold the string to be replaced.
            loc_end (str): end location that will hold the string to be replaced.
            new_text: new text to be inserted starting from loc_start.
        Returns:
            str: the replaced string.

        """
        pass

    def append(self, text):
        """
        Append text to the end of the file.
        Arguments:
            text (str): the text to append.
        """
        pass

    def read_next_sentence(self, skip_non_char: bool, raise_error: bool, start_new_word: bool = True) -> SubText:
        """
       Get the next sentence, starting from the current position(which is sepcified by last index it went to)
       Paragraph must have \n at last
       Args:
           kip_non_char: if true, the returned string doens't contain "." or "," for exampole. as it sticks
            to the word
            raise_error: if i hit the end of the file, it describes how you should handle it,
             if True: raise an exception
             if False: return SubText() of type file ended
       """
        pass

    def read_next_paragraph(self, skip_non_char: bool, raise_error: bool, start_new_word: bool = True) -> SubText:
        """
       Get the next paragraph, starting from the current position(which is sepcified by last index it went to)
       Paragraph must have \n at last
       Args:
           kip_non_char: if true, the returned string doens't contain "." or "," for exampole. as it sticks
            to the word
            raise_error: if i hit the end of the file, it describes how you should handle it,
             if True: raise an exception
             if False: return SubText() of type file ended
       """
        pass

    def delete_char_at(self, loc: Location, tmp: bool) -> SubText:
        """
        Delete the character at given location.
        Arguments:
            loc (Location): the location of the paragraph to be deleted
        """
        pass

    def delete_word_at(self, loc: Location, tmp: bool) -> SubText:
        """
        Delete the word at given location.
        Arguments:
            loc (Location): the location of the paragraph to be deleted
        """
        pass

    def delete_sentence_at(self, loc: Location, tmp: bool) -> SubText:
        """
        Delete the sentence at given location.
        Arguments:
            loc (Location): the location of the paragraph to be deleted
        """
        pass

    def delete_paragraph_at(self, loc: Location, tmp: bool) -> SubText:
        """
        Delete the paragraph at given location.
        Arguments:
            loc (Location): the location of the paragraph to be deleted
        """
        pass

    def delete(self, start_loc: Location, end_loc: Location, tmp: bool) -> SubText:
        """
        Delete the text between start_loc and end_loc.
        Arguments:
            start_loc (Location): starting location of the paragraph to be deleted
            end_loc (Location): ending location of the paragraph to be deleted
        """
        pass

    def apply_on_char(self, tmp: bool, func, *args, **kwargs) -> SubText:
        """
        apply a function on every char in the file

        """
        pass

    def apply_on_word(self, tmp: bool, func, *args, **kwargs) -> SubText:
        """
        apply a function on every word in the file

        """
        pass

    def apply_on_sentence(self, tmp: bool, func, *args, **kwargs) -> SubText:
        """
        apply a function on every sentence in the file

        """
        pass

    def apply_on_paragraph(self, tmp: bool, func, *args, **kwargs) -> SubText:
        """
        apply a function on every paragraph in the file

        """
        pass

    def apply_on_row(self, func, tmp: bool, *args, **kwargs) -> SubText:
        """
        apply a function on every row of the file

        """
        pass

    def turn_all_to_capital(self, tmp: bool) -> SubText:
        """
        turn all the chars in the file to capital
        Returns:
              copy of edited file
        """
        pass

    def turn_all_to_small(self, tmp: bool) -> SubText:
        """
        turn all the chars in the file to capital
        Returns:
              copy of edited file
        """
        pass

    def capitalize_start_sentence(self, tmp: bool) -> SubText:
        """
        capitiliza the start of each sentence
        Returns:
              copy of edited file
        """
        pass

    def capitalize_start_paragraph(self, tmp: bool) -> SubText:
        """
        capitiliza the start of each paragraph
        Returns:
              copy of edited file
        """
        pass

    def capitalize_start_sen_par(self, tmp: bool) -> SubText:
        """
        capitiliza the start of each sentence and paragraph
        Returns:
              copy of edited file
        """
        pass

    def turn_to_capital_at(self, at: Location, tmp: bool) -> SubText:
        """
        capitiliza the start of each sentence and paragraph
        Returns:
              copy of edited file
        """
        pass

    def find(self, searchable: bool) -> List:
        """
        Find the first occurrence of the given string in the file.
        if not found it returns -1
        Arguments:
            searchable (bool): string to search for.
        Returns:
            location of the first occurrence of the string in the file.
        """
        pass

    def index(self, searchable: bool) -> List:
        """
        Find the first occurrence of the given string in the file.
        like find, but if not found, raises an exception
        Arguments:
            searchable (bool): string to search for.
        Returns:
            location of the first occurrence of the string in the file.
        """
        pass

    def get_one_hot_encoding_chars(self, nmpy: bool, get_lst_of_char: bool) -> List:
        """
        Get the one-hot encoding of the chars in the file.
        Arguments:
            numpy   (bool): if True returns one hot encoding as numpy array, and chars will be returned as list if get_lst_of_char is True
        Returns:
            Numpy array of
        """
        pass

    def get_one_hot_encoding_chars_dict(self, nmpy: bool, get_lst_of_char: bool) -> List:
        """
        Get the one-hot encoding of the chars in the file, as dict
        Arguments:
            numpy   (bool): if True returns one hot encoding as numpy array, and chars will be returned as list if get_lst_of_char is True
        Returns:
            Numpy array of
        """
        pass

    def get_one_hot_encoding_words(self, nmpy: bool, get_lst_of_char: bool) -> List:
        """
        Get the one-hot encoding of the words in the file.
        Arguments:
            numpy   (bool): if True returns one hot encoding as numpy array, and chars will be returned as list if get_lst_of_char is True
        Returns:
            Numpy array of
        """
        pass

    def get_one_hot_encoding_words_dict(self, nmpy: bool, get_lst_of_char: bool) -> List:
        """
        Get the one-hot encoding of the words in the file, as dict
        Arguments:
            numpy   (bool): if True returns one hot encoding as numpy array, and chars will be returned as list if get_lst_of_char is True
        Returns:
            Numpy array of
        """
        pass

    def __file_ended_no_raise(self) -> SubText:
        return SubText(SubTextKind.FILE_ENDED)

    def __file_ended_raise(self) -> SubText:
        raise ValueError("File ended")
