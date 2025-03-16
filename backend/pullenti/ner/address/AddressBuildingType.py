# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru

from enum import IntEnum

class AddressBuildingType(IntEnum):
    """ Тип строения """
    UNDEFINED = 0
    BUILDING = 1
    """ Строение """
    CONSTRUCTION = 2
    """ Сооружение """
    LITER = 3
    """ Литера """
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)