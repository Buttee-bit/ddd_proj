# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru

import typing
from backend.pullenti.unisharp.Utils import Utils

from backend.pullenti.ner.core.GetTextAttr import GetTextAttr
from backend.pullenti.ner.core.MiscHelper import MiscHelper
from backend.pullenti.semantic.ISemContainer import ISemContainer
from backend.pullenti.semantic.SemGraph import SemGraph
from backend.pullenti.semantic.SemFragmentType import SemFragmentType
from backend.pullenti.semantic.SemObjectType import SemObjectType

class SemFragment(ISemContainer):
    """ Фрагмент блока (предложение)
    
    """
    
    def __init__(self, blk : 'SemBlock') -> None:
        self.__m_graph = SemGraph()
        self.m_higher = None;
        self.typ = SemFragmentType.UNDEFINED
        self.is_or = False
        self.begin_token = None;
        self.end_token = None;
        self.alt_fragments = list()
        self.rank = 0
        self.tag = None;
        self.m_higher = blk
    
    @property
    def graph(self) -> 'SemGraph':
        """ Объекты фрагмента (отметим, что часть объектов, связанных с этим блоком,
        могут находиться в графах вышележащих уровней).
        
        """
        return self.__m_graph
    
    @property
    def higher(self) -> 'ISemContainer':
        return self.m_higher
    
    @property
    def block(self) -> 'SemBlock':
        """ Владелец фрагмента """
        return self.m_higher
    
    @property
    def root_objects(self) -> typing.List['SemObject']:
        """ Список объектов SemObject, у которых нет связей. При нормальном разборе
        такой объект должен быть один - это обычно предикат. """
        res = list()
        for o in self.__m_graph.objects: 
            if (len(o.links_to) == 0): 
                res.append(o)
        return res
    
    @property
    def can_be_error_structure(self) -> bool:
        cou = 0
        vcou = 0
        for o in self.__m_graph.objects: 
            if (len(o.links_to) == 0): 
                if (o.typ == SemObjectType.VERB): 
                    vcou += 1
                cou += 1
        if (cou <= 1): 
            return False
        return vcou < cou
    
    @property
    def spelling(self) -> str:
        """ Текст фрагмента """
        return MiscHelper.get_text_value(self.begin_token, self.end_token, GetTextAttr.KEEPREGISTER)
    
    @property
    def begin_char(self) -> int:
        return (0 if self.begin_token is None else self.begin_token.begin_char)
    
    @property
    def end_char(self) -> int:
        return (0 if self.end_token is None else self.end_token.end_char)
    
    def __str__(self) -> str:
        if (self.typ != SemFragmentType.UNDEFINED): 
            return "{0}: {1}".format(Utils.enumToString(self.typ), Utils.ifNotNull(self.spelling, "?"))
        else: 
            return Utils.ifNotNull(self.spelling, "?")