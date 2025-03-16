# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru

from enum import IntEnum

class TransportKind(IntEnum):
    """ Категории транспортных средств """
    UNDEFINED = 0
    """ Неопределено """
    AUTO = 1
    """ Автомобильные """
    TRAIN = 2
    """ Железнодорожные """
    SHIP = 3
    """ Водные """
    FLY = 4
    """ Воздушние """
    SPACE = 5
    """ Космические """
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)