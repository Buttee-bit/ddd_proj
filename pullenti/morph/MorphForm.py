﻿# SDK Pullenti Lingvo, version 4.30, june 2025. Copyright (c) 2013-2025, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

from enum import IntEnum

class MorphForm(IntEnum):
    """ Форма """
    UNDEFINED = 0
    """ Не определена """
    SHORT = 1
    """ Краткая форма """
    SYNONYM = 2
    """ Синонимичная форма """
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)