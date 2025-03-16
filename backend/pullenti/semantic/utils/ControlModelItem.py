# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru

import io
from backend.pullenti.unisharp.Utils import Utils

from backend.pullenti.semantic.core.SemanticRole import SemanticRole
from backend.pullenti.semantic.utils.ControlModelItemType import ControlModelItemType

class ControlModelItem:
    """ Элемент модели управления """
    
    def __init__(self) -> None:
        self.typ = ControlModelItemType.WORD
        self.word = None;
        self.links = dict()
        self.nominative_can_be_agent_and_pacient = False
        self.ignorable = False
    
    def __str__(self) -> str:
        res = io.StringIO()
        if (self.ignorable): 
            print("IGNORE ", end="", file=res)
        if (self.typ != ControlModelItemType.WORD): 
            print("{0}: ".format(Utils.enumToString(self.typ)), end="", file=res, flush=True)
        else: 
            print("{0}: ".format(Utils.ifNotNull(self.word, "?")), end="", file=res, flush=True)
        for li in self.links.items(): 
            if (li[1] == SemanticRole.AGENT): 
                print("аг:", end="", file=res)
            elif (li[1] == SemanticRole.PACIENT): 
                print("пац:", end="", file=res)
            elif (li[1] == SemanticRole.STRONG): 
                print("сильн:", end="", file=res)
            print("{0}? ".format(li[0].spelling), end="", file=res, flush=True)
        return Utils.toStringStringIO(res)