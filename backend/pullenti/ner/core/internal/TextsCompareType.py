# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru

from enum import IntEnum

class TextsCompareType(IntEnum):
    NONCOMPARABLE = 0
    EQUIVALENT = 1
    EARLY = 2
    LATER = 3
    IN = 4
    CONTAINS = 5
    INTERSECT = 6
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)