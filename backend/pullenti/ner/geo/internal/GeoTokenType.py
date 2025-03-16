# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru

from enum import IntEnum

class GeoTokenType(IntEnum):
    ANY = 0
    ORG = 1
    STREET = 2
    CITY = 3
    TERR = 4
    STRONG = 5
    HOUSE = 6
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)