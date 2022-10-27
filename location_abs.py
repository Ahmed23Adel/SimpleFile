from typing import TextIO


class LocationAbs(object):
    
    
    def __init__(self):
        pass

    def get_location(self):
        """
        Returns:
            int: the index of the file
        """
        raise NotImplementedError()

    def guide_me(self, file):
        """
        simply seek the file at last index saved.
        Args:
            file (TextIO): the file to move in to the original location by index
        """
        raise NotImplementedError()

    def check_for_index(self, index: int) -> None:
        """
        Checks if the given index is valid.
        """
        if index < 0:
            raise ValueError("Invalid index; index must be greater than 0")
    def move_me_to_beg(self, file) -> None:
        """
        simply seek to the beginning of the file.
        Args:
            file (TextIO): the file to move in to the original location by index
        """
        raise NotImplementedError()
    def move_me_tmp(self, __file: TextIO, __index: int) -> None:
        """
        simply seek the file at new index, but doesn't save given location.
        Args:
            __file (TextIO): the file to move in to the original location by index
            __index (int): the index of the file_loc
        """
        raise NotImplementedError()
    def move_me_perm(self, __file: TextIO, __index: int) -> None:
        """
        simply seek the file at new index, and update current index with the given one.
        Args:
            __file (TextIO): the file to move in to the original location by index
            __index (int): the index of the file_loc
        """
        raise NotImplementedError()
    def guide_me(self, file: TextIO) -> None:
        """
        simply seek the file at last index saved.
        Args:
            file (TextIO): the file to move in to the original location by index
        """
        raise NotImplementedError()
    def get_location(self) -> int:
        """
       Returns:
           int: the index of the file
       """
        raise NotImplementedError()
    def __str__(self) -> str:
        raise NotImplementedError()

    def move_to(self, __index) -> None:
        """
        simply seek to the given index.
        Args:
            __index (int): the index to stop at.
        """
        raise NotImplementedError()