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
    
    def read_first_char(self):
        self.fileManager.read_first_char()
    
    def read_first_word(self):
        self.fileManager.read_first_word()

    def read_first_sentence(self):
        self.fileManager.read_first_sentence()

    def read_first_paragraph(self):
        self.fileManager.read_first_paragraph()