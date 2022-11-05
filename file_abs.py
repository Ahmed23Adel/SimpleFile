from abc import ABC, abstractmethod
from typing import overload
from location import *
from sub_text import *
from typing import List
class FileOpenerABC(ABC):
    def __init__(self, file_loc: str):
        self.file_loc: str = file_loc
        self.location: LocationIndex = Location.create_by_index(index=0)
        self.content: str = None
        self.last_char = ""

    @abstractmethod
    def _open_file(self) -> None:
        """
        Open a file for editing. you can read, write, delete, and append while opening in that mode.
        """
        self._file = open(self.file_loc, 'r+')
        file_len = open(self.file_loc, 'r+')
        utf8_text = file_len.read()  # TODO move it to another thread
        unicode_data = utf8_text.encode('utf8')
        self.file_len = len(unicode_data)
        file_len.close()
        self.content = utf8_text

    @abstractmethod
    def close(self) -> None:
        """
       Close the file.
       """
        self._file.close()
        self.location=None
        self.content=None
        self.last_char = ""
    def save_as(self, new_name: str) -> None:
        """
        Save the file as a new name.
        """
        try:
            with open(new_name, "a+") as f:
                f.write(self.content)
        except PermissionError as e:
            raise PermissionError(e,
                                  ", The problem might be that you haven't given the complete path for the new created file")

    @abstractmethod
    def read_first_char(self, tmp: bool) -> SubText:
        """
        Read the first character of the file.
        Arguments:
            tmp (bool): if False, it navigates the seek to the beginning of the file, if true, it will not.
        Returns:
            str: the first character of the file.
        """
        pass

    @abstractmethod
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
        pass

    @abstractmethod
    def read_first_word(self, tmp: bool, skip_non_char: bool) -> SubText:
        """
        Read the first word of the file.
        Arguments:
            tmp (bool): if False, it navigates the seek to the beginning of the file, if true, it will not.
        """
        pass

    @abstractmethod
    def read_first_n_sentences(self, n: int, tmp: bool, contain_ender: bool) -> SubText:
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


    @abstractmethod
    def read_first_sentence(self, tmp: bool, contain_ender: bool) -> str:
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
        pass

    @abstractmethod
    def read_first_n_sentences(self, n: int, tmp: bool) -> SubText:
        """
        Read the first n setnences of the file.
        Arguments:
            tmp (bool): if False, it navigates the seek to the beginning of the file,
            if true, it will not.
            n: number of setnences to read from the file.
        Returns:
            str: the first n setnences of the file.

        """
        pass

    @abstractmethod
    def read_first_paragraph(self, tmp: bool, contain_ender: bool) -> str:
        """
        Read the first paragraph of the file.
        Paragraph must have \n at last
        Args:
            tmp (bool): if False, it navigates the seek to the beginning of the file.
            contain_ender (bool): if True, it returns the sentence till \n.
        Returns:
            str: the first paragraph of the file.
        """
        pass


    @abstractmethod
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
        pass

    @abstractmethod
    def read_char_at(self, location: Location) -> SubText:
        """
        Read the character at the given location.
        Arguments:
            location (Location): the location of the character.
        Returns:
            str: the character at the given location.
        """
        pass

    @abstractmethod
    def read_word_at(self, loc: Location, skip_non_char: bool,  tmp: bool ) -> SubText:
        """
        Read the word at the given location.
        Arguments:
            location (Location): the location of the character.
        Returns:
            str: the character at the given location.
        """
        pass

    @abstractmethod
    def read_sentence_at(self, loc: Location, contain_ender: bool, tmp: bool):
        """
        Read the sentence at the given location.
        Arguments:
            location (Location): the location of the character.
        Returns:
            str: the character at the given location.
        """
        pass

    @abstractmethod
    def read_paragraph_at(self, loc: Location, tmp: bool, contain_ender: bool):
        """
        Read the paragraph at the given location.
        Arguments:
            location (Location): the location of the character.
        Returns:
            str: the character at the given location.
        """
        pass

    @abstractmethod
    def read_next_char(self, skip_non_char: bool = False, raise_error: bool = True) -> SubText:
        """
        Get the next character, starting from the current position(which is sepcified by last index it went to)
        Args:
            None
        """
        pass

    @abstractmethod
    def read(self, start_loc: Location, end_loc: Location):
        """
        Read the text in the file starting from start_loc adn ending at end_loc.
        Arguments:
            start_loc (Location): the start location of the file.
            end_loc (Location): the end location of the file.
        """
        pass

    @abstractmethod
    def replace_char(self, c_old: str, c_new: str, cap: bool, tmp: bool) -> SubText:
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

    @abstractmethod
    def replace_char_at(self, c_old_loc: Location, c_new: str, tmp: bool) -> SubText:
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

    @abstractmethod
    def replace(self, text_old: str, text_new: str, tmp: bool) -> SubText:
        pass

    @abstractmethod
    def replace_by_loc(self, loc_start: Location, loc_end: Location, new_text: str, tmp: bool) -> SubText:
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

    @abstractmethod
    def append(self, text, tmp: bool):
        """
        Append text to the end of the file.
        Arguments:
            text (str): the text to append.
        """
        pass

    @abstractmethod
    def read_next_word(self, skip_non_char: bool, raise_error: bool, start_new_word: bool = True) -> SubText:
        """
        Get the next word, starting from the current position(which is sepcified by last index it went to)
        Args:
            skip_non_char: if true, the returned string doens't contain "." or "," for exampole. as it sticks
            to the word
            raise_error: if i hit the end of the file, it describes how you should handle it,
             if True: raise an exception
             if False: return SubText() of type file ended

        """
        pass

    @abstractmethod
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

    @abstractmethod
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
    @abstractmethod
    def delete_char_at(self, loc: Location, tmp: bool) -> SubText:
        """
        Delete the character at given location.
        Arguments:
            loc (Location): the location of the paragraph to be deleted
        """
        pass

    @abstractmethod
    def delete_word_at(self, loc: Location, tmp: bool) -> SubText:
        """
        Delete the word at given location.
        Arguments:
            loc (Location): the location of the paragraph to be deleted
        """
        pass

    @abstractmethod
    def delete(self, start_loc: Location, end_loc: Location, tmp: bool) -> SubText:
        """
        Delete the text between start_loc and end_loc.
        Arguments:
            start_loc (Location): starting location of the paragraph to be deleted
            end_loc (Location): ending location of the paragraph to be deleted
        """
        pass

    @abstractmethod
    def apply_on_char(self, tmp: bool, func, *args, **kwargs) -> SubText:
        """
        apply a function on every char in the file

        """
        pass

    @abstractmethod
    def apply_on_word(self, tmp: bool, func, *args, **kwargs) -> SubText:
        """
        apply a function on every word in the file

        """
        pass

    @abstractmethod
    def apply_on_sentence(self, tmp: bool, func, *args, **kwargs) -> SubText:
        """
        apply a function on every sentence in the file

        """
        pass

    @abstractmethod
    def apply_on_paragraph(self, tmp: bool, func, *args, **kwargs) -> SubText:
        """
        apply a function on every paragraph in the file

        """
        pass

    @abstractmethod
    def apply_on_row(self, func, tmp: bool, *args, **kwargs) -> SubText:
        """
        apply a function on every row of the file

        """
        pass

    @abstractmethod
    def turn_all_to_capital(self, tmp: bool) -> SubText:
        """
        turn all the chars in the file to capital
        Returns:
              copy of edited file
        """
        pass

    @abstractmethod
    def turn_all_to_small(self, tmp: bool) -> SubText:
        """
        turn all the chars in the file to capital
        Returns:
              copy of edited file
        """
        pass

    @abstractmethod
    def capitalize_start_sentence(self, tmp: bool) -> SubText:
        """
        capitiliza the start of each sentence
        Returns:
              copy of edited file
        """
        pass

    @abstractmethod
    def capitalize_start_paragraph(self, tmp: bool) -> SubText:
        """
        capitiliza the start of each paragraph
        Returns:
              copy of edited file
        """
        pass

    @abstractmethod
    def capitalize_start_sen_par(self, tmp: bool) -> SubText:
        """
        capitiliza the start of each sentence and paragraph
        Returns:
              copy of edited file
        """
        pass

    @abstractmethod
    def turn_to_capital_at(self, at: Location, tmp: bool) -> SubText:
        """
        capitiliza the start of each sentence and paragraph
        Returns:
              copy of edited file
        """
        pass

    @abstractmethod
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

    @abstractmethod
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

    @abstractmethod
    def get_one_hot_encoding_chars(self, nmpy: bool, get_lst_of_char: bool) -> List:
        """
        Get the one-hot encoding of the chars in the file.
        Arguments:
            numpy   (bool): if True returns one hot encoding as numpy array, and chars will be returned as list if get_lst_of_char is True
        Returns:
            Numpy array of
        """
        pass

    @abstractmethod
    def get_one_hot_encoding_chars_dict(self, nmpy: bool, get_lst_of_char: bool) -> List:
        """
        Get the one-hot encoding of the chars in the file, as dict
        Arguments:
            numpy   (bool): if True returns one hot encoding as numpy array, and chars will be returned as list if get_lst_of_char is True
        Returns:
            Numpy array of
        """
        pass

    @abstractmethod
    def get_one_hot_encoding_words(self, nmpy: bool, get_lst_of_char: bool) -> List:
        """
        Get the one-hot encoding of the words in the file.
        Arguments:
            numpy   (bool): if True returns one hot encoding as numpy array, and chars will be returned as list if get_lst_of_char is True
        Returns:
            Numpy array of
        """
        pass

    @abstractmethod
    def get_one_hot_encoding_words_dict(self, nmpy: bool, get_lst_of_char: bool) -> List:
        """
        Get the one-hot encoding of the words in the file, as dict
        Arguments:
            numpy   (bool): if True returns one hot encoding as numpy array, and chars will be returned as list if get_lst_of_char is True
        Returns:
            Numpy array of
        """
        pass



