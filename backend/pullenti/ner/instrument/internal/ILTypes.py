# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru

from enum import IntEnum

class ILTypes(IntEnum):
    UNDEFINED = 0
    APPENDIX = 1
    APPROVED = 2
    ORGANIZATION = 3
    REGNUMBER = 4
    DATE = 5
    GEO = 6
    PERSON = 7
    TYP = 8
    VERB = 9
    DIRECTIVE = 10
    QUESTION = 11
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)