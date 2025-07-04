﻿# SDK Pullenti Lingvo, version 4.30, june 2025. Copyright (c) 2013-2025, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

from enum import IntEnum

class DatePointerType(IntEnum):
    """ Дополнительные указатели для дат """
    NO = 0
    BEGIN = 1
    """ В начале """
    CENTER = 2
    """ В середине """
    END = 3
    """ В конце """
    TODAY = 4
    """ В настоящее время, сегодня """
    WINTER = 5
    """ Зимой """
    SPRING = 6
    """ Весной """
    SUMMER = 7
    """ Летом """
    AUTUMN = 8
    """ Осенью """
    ABOUT = 9
    """ Около, примерно """
    UNDEFINED = 10
    """ Неопределено (например, 20__ года ) """
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)