﻿# SDK Pullenti Lingvo, version 4.30, june 2025. Copyright (c) 2013-2025, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

import typing
import math

from pullenti.ner.Token import Token
from pullenti.ner.MetaToken import MetaToken
from pullenti.ner.core.NumberExType import NumberExType
from pullenti.ner.Referent import Referent
from pullenti.ner.TextToken import TextToken
from pullenti.ner.core.ReferentsEqualType import ReferentsEqualType
from pullenti.ner.NumberToken import NumberToken
from pullenti.ner.ReferentToken import ReferentToken
from pullenti.ner.core.NumberParseAttr import NumberParseAttr
from pullenti.ner.core.internal.ResourceHelper2 import ResourceHelper2
from pullenti.ner.money.internal.MoneyMeta import MoneyMeta
from pullenti.ner.core.NumberHelper import NumberHelper
from pullenti.ner.money.MoneyReferent import MoneyReferent
from pullenti.ner.Analyzer import Analyzer
from pullenti.ner.ProcessorService import ProcessorService

class MoneyAnalyzer(Analyzer):
    """ Анализатор для денежных сумм """
    
    ANALYZER_NAME = "MONEY"
    """ Имя анализатора ("MONEY") """
    
    @property
    def name(self) -> str:
        return MoneyAnalyzer.ANALYZER_NAME
    
    @property
    def caption(self) -> str:
        return "Деньги"
    
    @property
    def description(self) -> str:
        return "Деньги..."
    
    def clone(self) -> 'Analyzer':
        return MoneyAnalyzer()
    
    @property
    def progress_weight(self) -> int:
        return 1
    
    @property
    def type_system(self) -> typing.List['ReferentClass']:
        return [MoneyMeta.GLOBAL_META]
    
    @property
    def images(self) -> typing.List[tuple]:
        res = dict()
        res[MoneyMeta.IMAGE_ID] = ResourceHelper2.get_bytes("money2.png")
        res[MoneyMeta.IMAGE2ID] = ResourceHelper2.get_bytes("moneyerr.png")
        return res
    
    @property
    def used_extern_object_types(self) -> typing.List[str]:
        return ["GEO", "DATE"]
    
    def create_referent(self, type0_ : str) -> 'Referent':
        if (type0_ == MoneyReferent.OBJ_TYPENAME): 
            return MoneyReferent()
        return None
    
    def process(self, kit : 'AnalysisKit') -> None:
        ad = kit.get_analyzer_data(self)
        t = kit.first_token
        first_pass4179 = True
        while True:
            if first_pass4179: first_pass4179 = False
            else: t = t.next0_
            if (not (t is not None)): break
            if (t.is_ignored): 
                continue
            mon = MoneyAnalyzer.try_parse(t, False)
            if (mon is not None): 
                mon.referent = ad.register_referent(mon.referent)
                kit.embed_token(mon)
                t = (mon)
                continue
    
    @staticmethod
    def try_parse(t : 'Token', rev : bool=False) -> 'ReferentToken':
        if (t is None): 
            return None
        if (isinstance(t, NumberToken)): 
            pass
        elif (t.length_char != 1): 
            return None
        elif (t.is_char_of(":;.,-")): 
            return None
        nex = NumberHelper.try_parse_number_with_postfix(t)
        if (nex is None or nex.ex_typ != NumberExType.MONEY): 
            if ((isinstance(t, NumberToken)) and (isinstance(t.next0_, TextToken)) and (isinstance(t.next0_.next0_, NumberToken))): 
                if (t.next0_.is_hiphen or t.next0_.morph.class0_.is_preposition): 
                    res1 = NumberHelper.try_parse_number_with_postfix(t.next0_.next0_)
                    if (res1 is not None and res1.ex_typ == NumberExType.MONEY): 
                        res0 = MoneyReferent()
                        if ((t.next0_.is_hiphen and res1.real_value == 0 and res1.end_token.next0_ is not None) and res1.end_token.next0_.is_char('(')): 
                            nex2 = NumberHelper.try_parse_number_with_postfix(res1.end_token.next0_.next0_)
                            if ((nex2 is not None and nex2.ex_typ_param == res1.ex_typ_param and nex2.end_token.next0_ is not None) and nex2.end_token.next0_.is_char(')')): 
                                if (nex2.value == t.value): 
                                    res0.currency = nex2.ex_typ_param
                                    res0.add_slot(MoneyReferent.ATTR_VALUE, nex2.value, True, 0)
                                    return ReferentToken(res0, t, nex2.end_token.next0_)
                                if (isinstance(t.previous, NumberToken)): 
                                    if (nex2.value == (((t.previous.real_value * (1000)) + t.value))): 
                                        res0.currency = nex2.ex_typ_param
                                        res0.add_slot(MoneyReferent.ATTR_VALUE, nex2.value, True, 0)
                                        return ReferentToken(res0, t.previous, nex2.end_token.next0_)
                                    elif (isinstance(t.previous.previous, NumberToken)): 
                                        if (nex2.real_value == (((t.previous.previous.real_value * (1000000)) + (t.previous.real_value * (1000)) + t.real_value))): 
                                            res0.currency = nex2.ex_typ_param
                                            res0.add_slot(MoneyReferent.ATTR_VALUE, nex2.value, True, 0)
                                            return ReferentToken(res0, t.previous.previous, nex2.end_token.next0_)
                        res0.currency = res1.ex_typ_param
                        res0.add_slot(MoneyReferent.ATTR_VALUE, t.value, False, 0)
                        return ReferentToken(res0, t, t)
            if (rev): 
                return None
            nnn = NumberHelper.try_parse_real_number(t, NumberParseAttr.NO)
            if (nnn is not None and nnn.end_token != t): 
                if (nnn.end_token.next0_ is not None and nnn.end_token.next0_.is_char('(')): 
                    nnn2 = NumberHelper.try_parse_real_number(nnn.end_token.next0_.next0_, NumberParseAttr.NO)
                    if ((nnn2 is not None and nnn2.value == nnn.value and nnn2.end_token.next0_ is not None) and nnn2.end_token.next0_.is_char(')')): 
                        tt = nnn2.end_token.next0_.next0_
                        first_pass4180 = True
                        while True:
                            if first_pass4180: first_pass4180 = False
                            else: tt = tt.next0_
                            if (not (tt is not None)): break
                            if (((tt.is_comma_and or tt.is_value("В", None) or tt.is_value("ТОМ", None)) or tt.is_value("ВКЛЮЧАЯ", None) or tt.is_value("ЧИСЛО", None)) or tt.is_value("НДС", None)): 
                                continue
                            rt = MoneyAnalyzer.try_parse(tt, True)
                            if (rt is not None): 
                                res1 = MoneyReferent()
                                res1.currency = rt.referent.currency
                                val1 = nnn.value
                                if (val1.find('.') > 0): 
                                    val1 = val1[0:0+val1.find('.')]
                                res1.add_slot(MoneyReferent.ATTR_VALUE, val1, True, 0)
                                re1 = math.floor(round(((nnn.real_value - res1.value)) * (100), 6))
                                if (re1 != 0): 
                                    res1.add_slot(MoneyReferent.ATTR_REST, str(re1), True, 0)
                                return ReferentToken(res1, t, nnn2.end_token.next0_)
                            if ((isinstance(tt, NumberToken)) or tt.length_char == 1): 
                                continue
                            break
            return None
        res = MoneyReferent()
        res.currency = nex.ex_typ_param
        val = nex.value
        if (val.find('.') > 0): 
            val = val[0:0+val.find('.')]
        res.add_slot(MoneyReferent.ATTR_VALUE, val, True, 0)
        re = math.floor(round(((nex.real_value - res.value)) * (100), 6))
        if (re != 0 or nex.is_real): 
            res.add_slot(MoneyReferent.ATTR_REST, str(re), True, 0)
        if (nex.real_value != nex.alt_real_value): 
            if (math.floor(res.value) != math.floor(nex.alt_real_value)): 
                val = NumberHelper.double_to_string(nex.alt_real_value)
                if (val.find('.') > 0): 
                    val = val[0:0+val.find('.')]
                res.add_slot(MoneyReferent.ATTR_ALTVALUE, val, True, 0)
            re = (math.floor(round(((nex.alt_real_value - (math.floor(nex.alt_real_value)))) * (100), 6)))
            if (re != res.rest and re != 0): 
                res.add_slot(MoneyReferent.ATTR_ALTREST, str(re), True, 0)
        if (nex.alt_rest_money > 0): 
            res.add_slot(MoneyReferent.ATTR_ALTREST, str(nex.alt_rest_money), True, 0)
        t1 = nex.end_token
        if (t1.next0_ is not None and t1.next0_.is_char('(')): 
            rt = MoneyAnalyzer.try_parse(t1.next0_.next0_, False)
            if ((rt is not None and rt.referent.can_be_equals(res, ReferentsEqualType.WITHINONETEXT) and rt.end_token.next0_ is not None) and rt.end_token.next0_.is_char(')')): 
                t1 = rt.end_token.next0_
            else: 
                rt = MoneyAnalyzer.try_parse(t1.next0_, False)
                if (rt is not None and rt.referent.can_be_equals(res, ReferentsEqualType.WITHINONETEXT)): 
                    t1 = rt.end_token
        if (res.alt_value is not None and res.alt_value > res.value): 
            if (t.whitespaces_before_count == 1 and (isinstance(t.previous, NumberToken))): 
                delt = math.floor((res.alt_value - res.value))
                if ((((res.value < 1000) and ((delt % 1000)) == 0)) or (((res.value < 1000000) and ((delt % 1000000)) == 0))): 
                    t = t.previous
                    res.add_slot(MoneyReferent.ATTR_VALUE, res.get_string_value(MoneyReferent.ATTR_ALTVALUE), True, 0)
                    res.add_slot(MoneyReferent.ATTR_ALTVALUE, None, True, 0)
        return ReferentToken(res, t, t1)
    
    def process_referent(self, begin : 'Token', param : str) -> 'ReferentToken':
        return MoneyAnalyzer.try_parse(begin, False)
    
    __m_inited = None
    
    @staticmethod
    def initialize() -> None:
        if (MoneyAnalyzer.__m_inited): 
            return
        MoneyAnalyzer.__m_inited = True
        MoneyMeta.initialize()
        ProcessorService.register_analyzer(MoneyAnalyzer())