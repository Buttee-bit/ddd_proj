﻿# SDK Pullenti Lingvo, version 4.30, june 2025. Copyright (c) 2013-2025, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

import math
import io
from pullenti.unisharp.Utils import Utils
from pullenti.unisharp.Misc import RefOutArgWrapper
from pullenti.unisharp.Streams import Stream

from pullenti.morph.MorphGender import MorphGender
from pullenti.ner.core.internal.SerializerHelper import SerializerHelper
from pullenti.ner.MetaToken import MetaToken
from pullenti.ner.NumberSpellingType import NumberSpellingType
from pullenti.morph.MorphNumber import MorphNumber

class NumberToken(MetaToken):
    """ Метатокен - число (числительное). Причём задаваемое не только цифрами, но и словами, возможно, римская запись и др.
    Для получения см. методы NumberHelper.
    
    Числовой токен
    """
    
    def __init__(self, begin : 'Token', end : 'Token', val : str, typ_ : 'NumberSpellingType', kit_ : 'AnalysisKit'=None) -> None:
        super().__init__(begin, end, kit_)
        self.__m_value = None;
        self.__m_int_val = None
        self.__m_real_val = 0
        self.is_real = False
        self.typ = NumberSpellingType.DIGIT
        self.value = val
        self.typ = typ_
    
    @property
    def value(self) -> str:
        """ Числовое значение, представленное строкой. Если действительное, то с точкой - разделителем дробных.
        Может быть сколь угодно большим, что не умещаться в системные числовые типы long или double. """
        return self.__m_value
    @value.setter
    def value(self, value_) -> str:
        from pullenti.ner.core.NumberHelper import NumberHelper
        self.__m_value = (Utils.ifNotNull(value_, ""))
        if (len(self.__m_value) > 2 and self.__m_value.endswith(".0")): 
            self.__m_value = self.__m_value[0:0+len(self.__m_value) - 2]
        while len(self.__m_value) > 1 and self.__m_value[0] == '0' and self.__m_value[1] != '.':
            self.__m_value = self.__m_value[1:]
        n = 0
        wrapn3622 = RefOutArgWrapper(0)
        inoutres3623 = Utils.tryParseInt(self.__m_value, wrapn3622)
        n = wrapn3622.value
        if (inoutres3623): 
            self.__m_int_val = n
        else: 
            self.__m_int_val = (None)
        d = NumberHelper.string_to_double(self.__m_value)
        if (d is None): 
            self.__m_real_val = math.nan
        else: 
            self.__m_real_val = d
        return value_
    
    @property
    def int_value(self) -> int:
        """ Целочисленное 32-х битное значение.
        Число Value может быть большое и не умещаться в Int, тогда вернёт null.
        Если есть дробная часть, то тоже вернёт null.
        Long не используется, так как не поддерживается в Javascript. Если что - напрямую работайте с Value. """
        return self.__m_int_val
    @int_value.setter
    def int_value(self, value_) -> int:
        self.value = str(value_)
        return value_
    
    @property
    def real_value(self) -> float:
        """ Получить действительное значение из Value. Если не удалось, то NaN. """
        return self.__m_real_val
    @real_value.setter
    def real_value(self, value_) -> float:
        from pullenti.ner.core.NumberHelper import NumberHelper
        self.value = NumberHelper.double_to_string(value_)
        return value_
    
    def __str__(self) -> str:
        res = io.StringIO()
        print("{0} {1}".format(self.value, Utils.enumToString(self.typ)), end="", file=res, flush=True)
        if (self.morph is not None): 
            print(" {0}".format(str(self.morph)), end="", file=res, flush=True)
        return Utils.toStringStringIO(res)
    
    def get_normal_case_text(self, mc : 'MorphClass'=None, num : 'MorphNumber'=MorphNumber.UNDEFINED, gender : 'MorphGender'=MorphGender.UNDEFINED, keep_chars : bool=False) -> str:
        return str(self.value)
    
    def _serialize(self, stream : Stream) -> None:
        super()._serialize(stream)
        SerializerHelper.serialize_string(stream, self.__m_value)
        SerializerHelper.serialize_int(stream, self.typ)
    
    def _deserialize(self, stream : Stream, kit_ : 'AnalysisKit', vers : int) -> None:
        super()._deserialize(stream, kit_, vers)
        if (vers == 0): 
            buf = Utils.newArrayOfBytes(8, 0)
            stream.read(buf, 0, 8)
            lo = int.from_bytes(buf[0:0+8], byteorder="little")
            self.value = str(lo)
        else: 
            self.value = SerializerHelper.deserialize_string(stream)
        self.typ = (Utils.valToEnum(SerializerHelper.deserialize_int(stream), NumberSpellingType))
    
    def _corr_drob(self, val : float) -> None:
        t = self.end_token.next0_
        if (t is None): 
            return
        if (t.is_value("ДЕСЯТИ", None) and t.next0_ is not None and t.next0_.is_value("ТЫСЯЧНЫЙ", "ТИСЯЧНИЙ")): 
            self.end_token = t.next0_
            self.real_value = (((val) / (10000))) + self.real_value
            return
        if (t.is_value("ДЕСЯТИ", None) and t.next0_ is not None and t.next0_.is_value("МИЛЛИОННЫЙ", "МІЛЬЙОННИЙ")): 
            self.end_token = t.next0_
            self.real_value = (((val) / (10000000))) + self.real_value
            return
        if (t.is_value("ДЕСЯТЫЙ", "ДЕСЯТИЙ")): 
            self.end_token = t
            self.real_value = (((val) / (10))) + self.real_value
            return
        if (t.is_value("СТО", None) and t.next0_ is not None and t.next0_.is_value("ТЫСЯЧНЫЙ", "ТИСЯЧНИЙ")): 
            self.end_token = t.next0_
            self.real_value = (((val) / (100000))) + self.real_value
            return
        if (t.is_value("СТО", None) and t.next0_ is not None and t.next0_.is_value("МИЛЛИОННЫЙ", "МІЛЬЙОННИЙ")): 
            self.end_token = t.next0_
            self.real_value = (((val) / (100000000))) + self.real_value
            return
        if (t.is_value("СОТЫЙ", "СОТИЙ")): 
            self.end_token = t
            self.real_value = (((val) / (100))) + self.real_value
            return
        if (t.is_value("ТЫСЯЧНЫЙ", "ТИСЯЧНИЙ")): 
            self.end_token = t
            self.real_value = (((val) / (1000))) + self.real_value
            return
        if (t.is_value("ДЕСЯТИТЫСЯЧНЫЙ", "ДЕСЯТИТИСЯЧНИЙ") or (((isinstance(t, NumberToken)) and t.value == "10000"))): 
            self.end_token = t
            self.real_value = (((val) / (10000))) + self.real_value
            return
        if (t.is_value("СТОТЫСЯЧНЫЙ", "СТОТИСЯЧНИЙ") or (((isinstance(t, NumberToken)) and t.value == "100000"))): 
            self.end_token = t
            self.real_value = (((val) / (100000))) + self.real_value
            return
        if (t.is_value("МИЛЛИОННЫЙ", "МІЛЬЙОННИЙ")): 
            self.end_token = t
            self.real_value = (((val) / (1000000))) + self.real_value
            return
        if (t.is_value("ДЕСЯТИМИЛЛИОННЫЙ", "ДЕСЯТИМІЛЬЙОННИЙ") or (((isinstance(t, NumberToken)) and t.value == "10000000"))): 
            self.end_token = t
            self.real_value = (((val) / (10000000))) + self.real_value
            return
        if (t.is_value("СТОМИЛЛИОННЫЙ", "СТОМІЛЬЙОННИЙ") or (((isinstance(t, NumberToken)) and t.value == "100000000"))): 
            self.end_token = t
            self.real_value = (((val) / (10000000))) + self.real_value
            return
    
    @staticmethod
    def _new667(_arg1 : 'Token', _arg2 : 'Token', _arg3 : str, _arg4 : 'NumberSpellingType', _arg5 : 'MorphCollection') -> 'NumberToken':
        res = NumberToken(_arg1, _arg2, _arg3, _arg4)
        res.morph = _arg5
        return res