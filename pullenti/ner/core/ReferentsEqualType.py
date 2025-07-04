﻿# SDK Pullenti Lingvo, version 4.30, june 2025. Copyright (c) 2013-2025, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

from enum import IntEnum

class ReferentsEqualType(IntEnum):
    """ Атрибут сравнения сущностей (методом Referent.CanBeEquals)
    Атрибут сравнения сущностей
    """
    WITHINONETEXT = 0
    """ Сущности в рамках одного текста """
    DIFFERENTTEXTS = 1
    """ Сущности из разных текстов """
    FORMERGING = 2
    """ Проверка для потенциального объединения сущностей """
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)