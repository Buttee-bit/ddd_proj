﻿# SDK Pullenti Lingvo, version 4.30, june 2025. Copyright (c) 2013-2025, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

from enum import IntEnum

class MorphVoice(IntEnum):
    """ Залог (для глаголов)
    Залог
    """
    UNDEFINED = 0
    """ Неопределено """
    ACTIVE = 1
    """ Действительный """
    PASSIVE = 2
    """ Страдательный """
    MIDDLE = 4
    """ Средний """
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)