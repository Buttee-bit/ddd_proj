# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru


class ISemContainer:
    """ Интерфейс владельца семантического графа """
    
    @property
    def graph(self) -> 'SemGraph':
        """ Сам граф объектов и связей """
        return None
    
    @property
    def higher(self) -> 'ISemContainer':
        """ Вышестоящий элемент """
        return None
    
    @property
    def begin_char(self) -> int:
        """ Начальная позиция в тексте """
        return None
    
    @property
    def end_char(self) -> int:
        """ Конечная позиция в тексте """
        return None