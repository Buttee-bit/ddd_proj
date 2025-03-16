# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru


from backend.pullenti.semantic.SemAttributeType import SemAttributeType

class SemAttribute:
    """ Семантический атрибут """
    
    def __init__(self) -> None:
        self.typ = SemAttributeType.UNDEFINED
        self.spelling = None;
        self.not0_ = False
    
    def __str__(self) -> str:
        return self.spelling
    
    @staticmethod
    def _new3655(_arg1 : bool, _arg2 : 'SemAttributeType', _arg3 : str) -> 'SemAttribute':
        res = SemAttribute()
        res.not0_ = _arg1
        res.typ = _arg2
        res.spelling = _arg3
        return res
    
    @staticmethod
    def _new3687(_arg1 : str, _arg2 : 'SemAttributeType', _arg3 : bool) -> 'SemAttribute':
        res = SemAttribute()
        res.spelling = _arg1
        res.typ = _arg2
        res.not0_ = _arg3
        return res
    
    @staticmethod
    def _new3689(_arg1 : 'SemAttributeType', _arg2 : str) -> 'SemAttribute':
        res = SemAttribute()
        res.typ = _arg1
        res.spelling = _arg2
        return res