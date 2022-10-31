from enum import Enum
from functools import wraps
class OpenMode(Enum):
    EDIT = 0
    READ = 1
    READ_CPY = 2
    EDIT_COPY = 3

class SubTextKind(Enum):
    CHAR = 0
    WORD = 1
    SENTENCE = 2
    PARAGRAPH = 3
    FILE = 4
    FILE_ENDED = 5


    