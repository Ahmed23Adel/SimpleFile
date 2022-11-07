from loc_row_col import *
from location_index import *
class Location(object):
    
    __create_key = object()
    def __init__(self,create_key):
        if not create_key == Location.__create_key :
            raise TypeError("Create by Location.Create_by_xxx")


    @classmethod
    def create_by_rowCol(cls, row, col):
        """
        Create Location by row and cold
        :param index:
        :return:LocationRowCol object
        """
        if row <0 or col <0:
            raise Exception("Row or column is less than zero, which is not valid index")
        return LocationRowCol(row,col)

    @classmethod
    def create_by_index(cls, index = 0):
        """
        Create Location by index
        :param index:
        :return:LocationIndex object
        """
        return LocationIndex(index)

    @classmethod
    def create_by_error(cls, index=0):
        """
        Create Location by index
        :param index:
        :return:LocationIndex object
        """
        return LocationIndex(index)


            