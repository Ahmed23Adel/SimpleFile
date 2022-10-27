class FileAbs(object):
    def __init__(self):
        pass

    def read_first_char(self, tmp=True):
        raise NotImplementedError()
    
    def read_first_word(self, tmp=True):
        raise NotImplementedError()

    def read_first_sentence(self, tmp=True, contain_ender=True):
        raise NotImplementedError()

    def read_first_paragraph(self, tmp, contain_ender):
        raise NotImplementedError()

    def replace_char(self, c_old, c_new):
        raise NotImplementedError()


