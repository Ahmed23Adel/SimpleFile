from locationAbs import *


class LocationRowCol(LocationAbs):
    
    def __init__(self, row, col):
        self.row = row
        self.col = col
        print("row",self.row)


    def get_location(self):
        raise NotImplementedError()

    def guide_me(self, file):
        raise NotImplementedError()


            
            