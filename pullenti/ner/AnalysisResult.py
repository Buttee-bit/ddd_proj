﻿# SDK Pullenti Lingvo, version 4.30, june 2025. Copyright (c) 2013-2025, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

import typing
import io
from pullenti.unisharp.Utils import Utils
from pullenti.unisharp.Streams import Stream

class AnalysisResult:
    """ Результат анализа
    
    """
    
    def __init__(self) -> None:
        self.__m_sofa = None;
        self.__m_entities = list()
        self.first_token = None;
        self.ontology = None;
        self.base_language = None;
        self.tokens_count = 0
        self.__m_log = list()
        self.exceptions = list()
        self.is_timeout_breaked = False
        self.tag = None;
    
    @property
    def sofa(self) -> 'SourceOfAnalysis':
        """ Анализируемый текст """
        return self.__m_sofa
    @sofa.setter
    def sofa(self, value) -> 'SourceOfAnalysis':
        self.__m_sofa = value
        return value
    
    @property
    def entities(self) -> typing.List['Referent']:
        """ Выделенные сущности """
        return self.__m_entities
    
    @property
    def log0_(self) -> typing.List[str]:
        """ Это некоторые информационные сообщения """
        return self.__m_log
    
    def _add_exception(self, ex : Exception) -> None:
        str0_ = str(ex)
        for e0_ in self.exceptions: 
            if (str(e0_) == str0_): 
                return
        self.exceptions.append(ex)
        self.__m_log.append("ERROR: " + str(ex))
    
    def __str__(self) -> str:
        res = io.StringIO()
        print("Общая длина {0} знаков ({1} токенов)".format(len(self.sofa.text), self.tokens_count), end="", file=res, flush=True)
        if (self.base_language is not None): 
            print(", базовый язык {0}".format(str(self.base_language)), end="", file=res, flush=True)
        print(", найдено {0} сущностей".format(len(self.entities)), end="", file=res, flush=True)
        if (self.is_timeout_breaked): 
            print(", прервано по таймауту", end="", file=res)
        return Utils.toStringStringIO(res)
    
    def serialize(self, stream : Stream) -> None:
        pass
    
    def find_token_by_pos(self, pos : int, tfrom : 'Token'=None) -> 'Token':
        """ Найти в цепочке токенов токен по его позиции
        
        Args:
            pos(int): между BeginChar и EndChar
            tfrom(Token): с какого токена начинать поиск (null - FirstToken)
        
        Returns:
            Token: токен или null
        """
        t = Utils.ifNotNull(tfrom, self.first_token)
        while t is not None: 
            if (t.begin_char <= pos and pos <= t.end_char): 
                return t
            elif (t.begin_char > pos): 
                break
            t = t.next0_
        if (tfrom is None): 
            return None
        t = self.first_token
        while t != tfrom and t is not None: 
            if (t.begin_char <= pos and pos <= t.end_char): 
                return t
            elif (t.begin_char > pos): 
                break
            t = t.next0_
        return None