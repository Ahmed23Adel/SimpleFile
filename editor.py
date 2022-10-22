from basic_func import *
from location import *
from fileAbs import *

class FileEdit(FileAbs):
    def __init__(self, file_loc):
        self.file_loc = file_loc
        self.location = Location.create_by_rowCol(row=0,col=0)

    def _open_file(self):
        self.__file = open(self.file_loc)

    def read_first_char(self):
        raise NotImplementedError()
    
    def read_first_word(self):
        raise NotImplementedError()

    def read_first_sentence(self):
        raise NotImplementedError()

    def read_first_paragraph(self):
        raise NotImplementedError()


    
