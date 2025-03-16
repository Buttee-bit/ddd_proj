# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru

from enum import IntEnum

class AddressHouseType(IntEnum):
    """ Тип дома """
    UNDEFINED = 0
    ESTATE = 1
    """ Владение """
    HOUSE = 2
    """ Просто дом """
    HOUSEESTATE = 3
    """ Домовладение """
    SPECIAL = 4
    """ Специальное здание (типа АЗС) """
    UNFINISHED = 5
    """ Объект незавершенного строительства """
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)