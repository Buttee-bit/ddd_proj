# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru

import io
from backend.pullenti.unisharp.Utils import Utils

from backend.pullenti.morph.MorphLang import MorphLang
from backend.pullenti.ner.titlepage.internal.TitleItemToken import TitleItemToken

class PersonRelation:
    
    def __init__(self) -> None:
        self.person = None;
        self.coefs = dict()
    
    @property
    def best(self) -> 'Types':
        res = TitleItemToken.Types.UNDEFINED
        max0_ = 0
        for v in self.coefs.items(): 
            if (v[1] > max0_): 
                res = v[0]
                max0_ = v[1]
            elif (v[1] == max0_): 
                res = TitleItemToken.Types.UNDEFINED
        return res
    
    def __str__(self) -> str:
        res = io.StringIO()
        print("{0} {1}".format(self.person.to_string_ex(True, MorphLang.UNKNOWN, 0), Utils.enumToString(self.best)), end="", file=res, flush=True)
        for v in self.coefs.items(): 
            print(" {0}({1})".format(v[1], Utils.enumToString(v[0])), end="", file=res, flush=True)
        return Utils.toStringStringIO(res)
    
    @staticmethod
    def _new3389(_arg1 : 'PersonReferent') -> 'PersonRelation':
        res = PersonRelation()
        res.person = _arg1
        return res