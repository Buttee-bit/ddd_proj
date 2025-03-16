# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru

from enum import IntEnum

class StreetKind(IntEnum):
    """ Классы улиц """
    UNDEFINED = 0
    """ Обычная улица-переулок-площадь """
    ROAD = 1
    """ Автодорога """
    RAILWAY = 2
    """ Железная дорога """
    METRO = 3
    """ Станция метро """
    AREA = 4
    """ Районы, кварталы """
    ORG = 5
    """ Территория организации или иного объекта """
    SPEC = 6
    """ Спецобъекты (будки, казармы) """
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)