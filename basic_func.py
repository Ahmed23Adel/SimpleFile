from enum import Enum
from functools import wraps
class OpenMode(Enum):
    EDIT = 0
    VIEW = 1
    EDIT_COPY = 2

class SubTextKind(Enum):
    CHAR = 0
    WORD = 1
    SENTENCE = 2
    PARAGRAPH = 3
    FILE_ENDED = 4


    