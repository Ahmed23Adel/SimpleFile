from locationAbs import *


class LocationRowCol(LocationAbs):

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.__rows_lens = []
        print("row", self.row)

    def get_location(self):
        raise NotImplementedError()

    def guide_me(self, file):
        file.seek(sum(self.__rows_lens) + self.col)

    def append_row(self, row_len):
        self.__rows_lens.append(row_len)

    def move_me_perm(self, file, index=None, row=None, col=None):
        if index is not None:
            file.seek(index)
            self.row = 0
            self.col = 1
            return
        if row is not None and col is not None:
            self.row = row
            self.col = col
            return
        raise TypeError("You have not specified neither row and col or index to move you to")
    def move_me_tmp(self, file, index):
        file.seek(index)

    def __str__(self):
        return "Location by row and col, Row = {}, Col = {}".format(self.row, self.col)
