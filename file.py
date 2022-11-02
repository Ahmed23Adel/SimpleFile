from editor import *
from typing import TextIO
from loc_row_col import *
from sub_text import SubText
from reader import *


class SimpleFile(FileOpenerABC):

    def __init__(self, file_loc: str, open_mode: OpenMode = OpenMode.EDIT) -> None:
        """"
        Encapsulates moving from file editor to file viewer as Factory design pattern, you just need to sepcifiy the open mode
        Args
        file_loc (str): file location
        open_mode (OpenMode): open mode
        """
        self.file_loc = file_loc
        self.open_mode = open_mode
        self.__init_file()

    def __init_file(self) -> None:
        """
        Initializes the file manager, which is decided by open mode.
        """
        if self.open_mode == OpenMode.EDIT:
            self.fileManager = FileEdit(self.file_loc)
        if self.open_mode == OpenMode.READ:
            self.fileManager = FileReader(self.file_loc)
        self._open_file()

    def _open_file(self) -> None:
        """
        Open a file for editing. you can read, write, delete, and append while opening in that mode.
        """
        self.fileManager._open_file()

    def close(self) -> None:
        """
       Close the file.
       """
        return self.fileManager.close()

    def save_as(self, new_name: str) -> None:
        """
        Save the file as a new name.
        """
        return self.fileManager.save_as(new_name)

    def read_first_char(self, tmp=True) -> str:
        """
        Read the first character of the file.
        Arguments:
            tmp (bool): if False, it navigates the seek to the beginning of the file, if true, it will not.
        Returns:
            str: the first character of the file.
        """
        return self.fileManager.read_first_char(tmp)

    def read_first_n_chars(self, n: int, tmp: bool = True) -> SubText:
        """
        Read the first n characters of the file.
        Arguments:
            tmp (bool): if False, it navigates the seek to the beginning of the file,
            if true, it will not.
            n: number of paragraphs to read from the file.
        Returns:
            str: the first n characters of the file.

        """
        return self.fileManager.read_first_n_chars(n, tmp)

    def read_first_word(self, tmp: bool = True, skip_non_char: bool = True) -> str:
        """
        Read the first word of the file.
        Arguments:
            tmp (bool): if False, it navigates the seek to the beginning of the file, if true, it will not.
        """
        return self.fileManager.read_first_word(tmp, skip_non_char)

    def read_first_n_words(self, n: int = 0, tmp: bool = True, skip_non_char: bool = False) -> SubText:
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
        return self.fileManager.read_first_n_words(n, tmp, skip_non_char)

    def read_first_sentence(self, tmp: bool = True, contain_ender: bool = True) -> SubText:
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
        return self.fileManager.read_first_sentence(tmp, contain_ender)


    def read_first_n_sentences(self, n: int = 0, tmp: bool = True, contain_ender: bool = True) -> SubText:
        """
        Read the first n setnences of the file.
        Arguments:
            tmp (bool): if False, it navigates the seek to the beginning of the file,
            if true, it will not.
            n: number of setnences to read from the file.
        Returns:
            str: the first n setnences of the file.

        """
        return self.fileManager.read_first_n_sentences(n, tmp, contain_ender)

    def read_last_n_sentences(self, n: int, tmp: bool) -> str:
        """
        Read the last n setnences of the file.
        Arguments:
            tmp (bool): if False, it navigates the seek to the beginning of the file,
            if true, it will not.
            n: number of setnences to read from the file.
        Returns:
            str: the first n setnences of the file.

        """
        pass

    def read_first_paragraph(self, tmp: bool = True, contain_ender: bool = True) -> str:
        """
        Read the first paragraph of the file.
        Paragraph must have \n at last
        Args:
            tmp (bool): if False, it navigates the seek to the beginning of the file.
            contain_ender (bool): if True, it returns the sentence till \n.
        Returns:
            str: the first paragraph of the file.
        """
        return self.fileManager.read_first_paragraph(tmp, contain_ender)

    def read_last_paragraph(self, tmp: bool, contain_ender: bool) -> str:
        """
        Read the last paragraph of the file.
        Paragraph must have \n at last
        Args:
            tmp (bool): if False, it navigates the seek to the beginning of the file.
            contain_ender (bool): if True, it returns the sentence till \n.
        Returns:
            str: the first paragraph of the file.
        """
        pass

    def read_first_n_paragraph(self, n: int, tmp: bool = True, contain_ender: bool = True) -> SubText:
        """
        Read the first n paragraphs of the file.
        Arguments:
            tmp (bool): if False, it navigates the seek to the beginning of the file,
            if true, it will not.
            n: number of paragraphs to read from the file.
        Returns:
            str: the first n paragraphs of the file.

        """
        return self.fileManager.read_first_n_paragraph(n, tmp, contain_ender)

    def read_char_at(self, loc: Location, tmp: bool = True):
        """
        Read the character at the given location.
        Arguments:
            location (Location): the location of the character.
        Returns:
            str: the character at the given location.
        """
        return self.fileManager.read_char_at(tmp, loc)

    def read_word_at(self, loc: Location, skip_non_char: bool = False,  tmp: bool = True):
        """
        Read the word at the given location.
        Arguments:
            location (Location): the location of the character.
        Returns:
            str: the character at the given location.
        """
        return self.fileManager.read_word_at(loc, skip_non_char, tmp)

    def read_sentence_at(self, loc: Location, contain_ender: bool = True, tmp: bool = True) ->SubText:
        """
        Read the sentence at the given location.
        Arguments:
            location (Location): the location of the character.
        Returns:
            str: the character at the given location.
        """
        return self.fileManager.read_sentence_at(loc, contain_ender, tmp)

    def read_paragraph_at(self, loc: Location, tmp: bool = True, contain_ender: bool = True) ->SubText:
        """
        Read the paragraph at the given location.
        Arguments:
            location (Location): the location of the character.
        Returns:
            str: the character at the given location.
        """
        return self.fileManager.read_paragraph_at(loc, tmp, contain_ender)

    def read_next_char(self, skip_non_char: bool = False, raise_error: bool = True) -> SubText:
        """
        Get the next character, starting from the current position(which is sepcified by last index it went to)
        Args:
            None
        """
        return self.fileManager.read_next_char(skip_non_char, raise_error)

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
        return self.fileManager.read(start_loc, end_loc)

    def replace_char(self, c_old: str, c_new: str, cap: bool = False, tmp: bool = False) -> str:
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
        pass

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

    def read_next_word(self, skip_non_char: bool = True, raise_error: bool = False,
                       start_new_word: bool = True) -> SubText:
        """
        Get the next word, starting from the current position(which is sepcified by last index it went to)
        Args:
            skip_non_char: if true, the returned string doens't contain "." or "," for exampole. as it sticks
            to the word
            raise_error: if i hit the end of the file, it describes how you should handle it,
             if True: raise an exception
             if False: return SubText() of type file ended

        """
        return self.fileManager.read_next_word(skip_non_char, raise_error, start_new_word)

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

    def __str__(self):
        """
        Return the string of the file.
        """
        return self.fileManager.__str__()
