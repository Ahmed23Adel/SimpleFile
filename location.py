from loc_rowCol import *

class Location(object):
    
    __create_key = object()
    def __init__(self,create_key):
        if not create_key == Location.__create_key :
            raise TypeError("Create by Location.Create_by_xxx")


    @classmethod
    def create_by_rowCol(cls, row, col):
        if row <0 or col <0:
            raise Exception("Row or column is less than zero, which is not valid index")
        return LocationRowCol(row,col)

    def guide_me(self,file):
        raise NotImplementedError()

    def move_to(self):
        raise NotImplementedError()

            