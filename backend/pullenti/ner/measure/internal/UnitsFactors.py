# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru

from enum import IntEnum

class UnitsFactors(IntEnum):
    # Степени десяток
    NO = 0
    KILO = 3
    MEGA = 6
    GIGA = 9
    TERA = 12
    DECI = -1
    CENTI = -2
    MILLI = -3
    MICRO = -6
    NANO = -9
    PICO = -12
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)