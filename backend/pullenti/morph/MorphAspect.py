# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru

from enum import IntEnum

class MorphAspect(IntEnum):
    """ Аспект (для глаголов)
    Аспект
    """
    UNDEFINED = 0
    """ Неопределено """
    PERFECTIVE = 1
    """ Совершенный """
    IMPERFECTIVE = 2
    """ Несовершенный """
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)