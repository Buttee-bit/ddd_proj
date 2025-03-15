# SDK Pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

import typing
from pullenti.unisharp.Utils import Utils
from pullenti.unisharp.Misc import RefOutArgWrapper

from pullenti.ner.core.AnalyzerData import AnalyzerData

class DateAnalyzerData(AnalyzerData):
    
    def __init__(self) -> None:
        super().__init__()
        self.__m_hash = dict()
        self.dregime = False
    
    @property
    def referents(self) -> typing.List['Referent']:
        return self.__m_hash.values()
    
    def register_referent(self, referent : 'Referent') -> 'Referent':
        key = str(referent)
        dr = None
        wrapdr774 = RefOutArgWrapper(None)
        inoutres775 = Utils.tryGetValue(self.__m_hash, key, wrapdr774)
        dr = wrapdr774.value
        if (inoutres775): 
            return dr
        self.__m_hash[key] = referent
        return referent