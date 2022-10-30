from location_index import *
from basic_func import *
class SubText():

    def __init__(self, kind: SubTextKind, text: str = None, loc_start: LocationIndex = None, loc_end: LocationIndex = None, ):
        if kind == SubTextKind.FILE_ENDED:
            self.kind = kind
            return
        self.value = text
        self.loc_start = loc_start
        self.loc_end = loc_end
        self.kind = kind



    def __str__(self):
        if self.kind == SubTextKind.FILE_ENDED:
            return "The file has ended"
        return "{} object starting at: {}, and ending at: {}, and has value: {}".format(self.kind, self.loc_start, self.loc_end,self.value)


