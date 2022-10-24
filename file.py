from editor import *
from loc_rowCol import *



class SimpleFile(FileAbs):
    
    def __init__(self, file_loc, open_mode = OpenMode.EDIT):
        self.file_loc = file_loc
        self.open_mode = open_mode
        self.__init_file()

    def __init_file(self):
        if self.open_mode == OpenMode.EDIT:
            self.fileManager = FileEdit( self.file_loc)
        self.__open_file()
        
    def __open_file(self):
        self.fileManager._open_file()
    
    def read_first_char(self, tmp=True):
        return self.fileManager.read_first_char(tmp)
    
    def read_first_word(self, tmp=True):
        return self.fileManager.read_first_word(tmp)

    def read_first_sentence(self, tmp=True, contain_ender=True):
        return self.fileManager.read_first_sentence(tmp, contain_ender)

    def read_first_paragraph(self, tmp=True, contain_ender=False):
        return self.fileManager.read_first_paragraph(tmp, contain_ender)