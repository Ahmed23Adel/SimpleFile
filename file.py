from editor import *
from typing import TextIO
from loc_row_col import *


class SimpleFile(FileAbs):

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
        self.__open_file()

    def __open_file(self) -> None:
        """
        let file manager(editor, viewer) to open the file
        """
        self.fileManager._open_file()

    def read_first_char(self, tmp=True)-> str:
        """
       Read the first character of the file.
       Args:
           tmp (bool): if False, it navigates the seek to the beginning of the file.
       Returns:
           str: the first character of the file.
        """
        return self.fileManager.read_first_char(tmp)

    def read_first_word(self, tmp=True) -> str:
        """
        Read the first word of the file.
        Args:
            tmp (bool): if False, it navigates the seek to the beginning of the file.
        """
        return self.fileManager.read_first_word(tmp)

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
        return self.fileManager.read_first_sentence(tmp, contain_ender)

    def read_first_paragraph(self, tmp: bool, contain_ender: bool) -> str:
        """
        Read the first paragraph of the file.
        Paragraph must have \n at last
        Args:
            tmp (bool): if False, it navigates the seek to the beginning of the file.
            contain_ender (bool): if True, it returns the sentence till \n.
        """
        return self.fileManager.read_first_paragraph(tmp, contain_ender)

    def replace_char(self, c_old: str, c_new: str, cap: bool = False, tmp: bool = False) -> str:
        """
        Replace the character c_old with c_new.
        Args:
            c_old (str): the character to be replaced.
            c_new (str): the character to replace it with.
            tmp (bool): if true, it replaces the character in the file, if False, returns a copy of new string without replacing it in the file
            cap: if true, replace the char and it c_old.Capitalization() with the new c_new
        Returns:
            String copy of editied file
        """
        return self.fileManager.replace_char(c_old, c_new, tmp = tmp, cap = cap)

    def __str__(self):
        """
        Return the string of the file.
        """
        return self.fileManager.__str__()
