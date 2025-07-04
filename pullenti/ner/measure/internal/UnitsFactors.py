﻿# SDK Pullenti Lingvo, version 4.30, june 2025. Copyright (c) 2013-2025, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

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