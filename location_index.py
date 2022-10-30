from location_abs import *


class LocationIndex(LocationAbs):

    def __init__(self, index: int = 0) -> None:
        """
        Specifies the location by index. it encapsulates some relevant functions for simple movement in the file.
        Args:
            index (int): index of the file
        """
        self.check_for_index(index)
        self.index = index

    def get_location(self) -> int:
        """
        Returns:
            int: the index of the file
        """
        return self.index

    def guide_me(self, file: TextIO) -> None:
        """
        simply seek the file at last index saved.
        Args:
            file (TextIO): the file to move in to the original location by index
        """
        file.seek(self.index)

    def move_me_perm(self, __file: TextIO, __index: int) -> None:
        """
        simply seek the file at new index, and update current index with the given one.
        Args:
            __file (TextIO): the file to move in to the original location by index
            __index (int): the index of the file_loc
        """
        self.check_for_index(__index)
        self.index = __index
        __file.seek(self.index)

    def move_me_tmp(self, __file: TextIO, __index: int) -> None:
        """
        simply seek the file at new index, but doesn't save given location.
        Args:
            __file (TextIO): the file to move in to the original location by index
            __index (int): the index of the file_loc
        """
        self.check_for_index(__index)
        __file.seek(__index)

    def move_me_to_beg(self, file) -> None:
        """
        simply seek to the beginning of the file.
        Args:
            file (TextIO): the file to move in to the original location by index
        """
        self.move_me_tmp(file, 0)

    def move_to(self, __index) -> None:
        """
        simply seek to the given index.
        Args:
            __index (int): the index to stop at.
        """
        self.index = __index

    def move_by(self, __by: int) -> None:
        # print("Move by ", __by)
        self.index += __by
        # print("At ", self.index)

    def is_fil_ended(self, file_length: int) -> bool:

        return self.index == file_length

    def __str__(self) -> str:
        """
        returns the string representation of the LocationIndex object.
        Args:
            None
        """
        return "Location by Index at {}".format(self.index)
