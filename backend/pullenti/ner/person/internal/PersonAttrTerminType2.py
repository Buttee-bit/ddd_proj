# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru

from enum import IntEnum

class PersonAttrTerminType2(IntEnum):
    UNDEFINED = 0
    IO = 1
    GRADE = 2
    ABBR = 3
    ADJ = 4
    IGNOREDADJ = 5
    IO2 = 6
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)