# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru

from enum import IntEnum

class ComplexNumCompareType(IntEnum):
    """ Результат сравнения номеров """
    UNCOMPARABLE = 0
    """ Несравнимы """
    EQUALS = 1
    """ Равны """
    LESS = 2
    """ Первый раньше второго """
    GREAT = 3
    """ Второй раньше первого """
    COMPARABLE = 4
    """ Не помню, что это... """
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)