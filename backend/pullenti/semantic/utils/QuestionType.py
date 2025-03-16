# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru

from enum import IntEnum

class QuestionType(IntEnum):
    """ Абстрактные вопросы модели управления """
    UNDEFINED = 0
    """ Обычный вопрос """
    WHERE = 1
    """ Где """
    WHEREFROM = 2
    """ Откуда """
    WHERETO = 4
    """ Куда """
    WHEN = 8
    """ Когда """
    WHATTODO = 0x10
    """ Что делать (инфинитив за группой) """
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)