# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru

import typing
from backend.pullenti.unisharp.Utils import Utils
from backend.pullenti.unisharp.Misc import RefOutArgWrapper

from backend.pullenti.ner.SourceOfAnalysis import SourceOfAnalysis
from backend.pullenti.ner.TextToken import TextToken
from backend.pullenti.morph.MorphGender import MorphGender
from backend.pullenti.ner.core.AnalysisKit import AnalysisKit
from backend.pullenti.ner.person.internal.PullentiNerPersonInternalResourceHelper import PullentiNerPersonInternalResourceHelper

class ShortNameHelper:
    
    class ShortnameVar:
        
        def __init__(self) -> None:
            self.name = None;
            self.gender = MorphGender.UNDEFINED
        
        def __str__(self) -> str:
            return self.name
        
        @staticmethod
        def _new3325(_arg1 : str, _arg2 : 'MorphGender') -> 'ShortnameVar':
            res = ShortNameHelper.ShortnameVar()
            res.name = _arg1
            res.gender = _arg2
            return res
    
    M_SHORTS_NAMES = None
    
    @staticmethod
    def get_shortnames_for_name(name : str) -> typing.List[str]:
        res = list()
        for kp in ShortNameHelper.M_SHORTS_NAMES.items(): 
            for v in kp[1]: 
                if (v.name == name): 
                    if (not kp[0] in res): 
                        res.append(kp[0])
        return res
    
    @staticmethod
    def get_names_for_shortname(shortname : str) -> typing.List['ShortnameVar']:
        res = [ ]
        wrapres3323 = RefOutArgWrapper(None)
        inoutres3324 = Utils.tryGetValue(ShortNameHelper.M_SHORTS_NAMES, shortname, wrapres3323)
        res = wrapres3323.value
        if (not inoutres3324): 
            return None
        else: 
            return res
    
    M_INITED = False
    
    @staticmethod
    def initialize() -> None:
        if (ShortNameHelper.M_INITED): 
            return
        ShortNameHelper.M_INITED = True
        obj = PullentiNerPersonInternalResourceHelper.get_string("ShortNames.txt")
        if (obj is not None): 
            kit = AnalysisKit(SourceOfAnalysis(obj))
            t = kit.first_token
            while t is not None: 
                if (t.is_newline_before): 
                    g = (MorphGender.FEMINIE if t.is_value("F", None) else MorphGender.MASCULINE)
                    t = t.next0_
                    nam = t.term
                    shos = list()
                    t = t.next0_
                    while t is not None: 
                        if (t.is_newline_before): 
                            break
                        else: 
                            shos.append(t.term)
                        t = t.next0_
                    for s in shos: 
                        li = None
                        wrapli3326 = RefOutArgWrapper(None)
                        inoutres3327 = Utils.tryGetValue(ShortNameHelper.M_SHORTS_NAMES, s, wrapli3326)
                        li = wrapli3326.value
                        if (not inoutres3327): 
                            li = list()
                            ShortNameHelper.M_SHORTS_NAMES[s] = li
                        li.append(ShortNameHelper.ShortnameVar._new3325(nam, g))
                    if (t is None): 
                        break
                    t = t.previous
                t = t.next0_
    
    # static constructor for class ShortNameHelper
    @staticmethod
    def _static_ctor():
        ShortNameHelper.M_SHORTS_NAMES = dict()

ShortNameHelper._static_ctor()