﻿# SDK Pullenti Lingvo, version 4.30, june 2025. Copyright (c) 2013-2025, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

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