# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru

from enum import IntEnum

class BlkTyps(IntEnum):
    UNDEFINED = 0
    INDEX = 1
    INDEXITEM = 2
    INTRO = 3
    LITERATURE = 4
    APPENDIX = 5
    CONSLUSION = 6
    MISC = 7
    CHAPTER = 8
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)