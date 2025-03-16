# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru

from enum import IntEnum

class NamedEntityKind(IntEnum):
    """ Категории мелких именованных сущностей """
    UNDEFINED = 0
    """ Неопределённая """
    PLANET = 1
    """ Планеты """
    LOCATION = 2
    """ Разные географические объекты (не города) - реки, моря, континенты ... """
    MONUMENT = 3
    """ Памятники и монументы """
    BUILDING = 4
    """ Выдающиеся здания """
    ART = 5
    """ Произведения искусства (книги, фильмы, спектакли ...) """
    AWARD = 6
    """ Награды, ордена, титулы (пока не реализовано) """
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)