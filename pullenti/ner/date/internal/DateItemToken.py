﻿# SDK Pullenti Lingvo, version 4.30, june 2025. Copyright (c) 2013-2025, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

import io
import datetime
import typing
from enum import IntEnum
from pullenti.unisharp.Utils import Utils
from pullenti.unisharp.Misc import RefOutArgWrapper

from pullenti.morph.MorphLang import MorphLang
from pullenti.ner.core.NounPhraseParseAttr import NounPhraseParseAttr
from pullenti.morph.MorphNumber import MorphNumber
from pullenti.ner.measure.internal.NumberWithUnitParseAttr import NumberWithUnitParseAttr
from pullenti.ner.core.NounPhraseHelper import NounPhraseHelper
from pullenti.ner.core.Termin import Termin
from pullenti.ner.core.NumberExType import NumberExType
from pullenti.ner.date.DateRangeReferent import DateRangeReferent
from pullenti.ner.core.TerminCollection import TerminCollection
from pullenti.ner.date.internal.DateTokenData import DateTokenData
from pullenti.ner.MetaToken import MetaToken
from pullenti.ner.Token import Token
from pullenti.ner.date.DatePointerType import DatePointerType
from pullenti.ner.core.TerminParseAttr import TerminParseAttr
from pullenti.ner.NumberToken import NumberToken
from pullenti.ner.core.BracketHelper import BracketHelper
from pullenti.ner.TextToken import TextToken
from pullenti.ner.core.NumberHelper import NumberHelper
from pullenti.ner.measure.internal.NumbersWithUnitToken import NumbersWithUnitToken
from pullenti.ner.NumberSpellingType import NumberSpellingType
from pullenti.ner.date.DateAnalyzer import DateAnalyzer

class DateItemToken(MetaToken):
    # Примитив, из которых состоит дата
    
    class DateItemType(IntEnum):
        NUMBER = 0
        YEAR = 1
        MONTH = 2
        DAY = 3
        DELIM = 4
        HOUR = 5
        MINUTE = 6
        SECOND = 7
        HALFYEAR = 8
        QUARTAL = 9
        POINTER = 10
        CENTURY = 11
        TENYEARS = 12
        
        @classmethod
        def has_value(cls, value):
            return any(value == item.value for item in cls)
    
    class FirstLastTyp(IntEnum):
        NO = 0
        FIRST = 1
        LAST = 2
        
        @classmethod
        def has_value(cls, value):
            return any(value == item.value for item in cls)
    
    def __init__(self, begin : 'Token', end : 'Token') -> None:
        super().__init__(begin, end, None)
        self.typ = DateItemToken.DateItemType.NUMBER
        self.string_value = None;
        self.int_value = 0
        self.ptr = DatePointerType.NO
        self.lang = None;
        self.new_age = 0
        self.relate = False
        self.ltyp = DateItemToken.FirstLastTyp.NO
        self.new_style = None
        self.__m_year = -1
        self.__m_can_by_month = -1
    
    def __str__(self) -> str:
        res = io.StringIO()
        print("{0} {1}".format(Utils.enumToString(self.typ), (self.string_value if self.int_value == 0 else str(self.int_value))), end="", file=res, flush=True)
        if (self.ptr != DatePointerType.NO): 
            print(" ({0})".format(Utils.enumToString(self.ptr)), end="", file=res, flush=True)
        if (self.ltyp != DateItemToken.FirstLastTyp.NO): 
            print(" {0}".format(Utils.enumToString(self.ltyp)), end="", file=res, flush=True)
        if (self.relate): 
            print(" relate", end="", file=res)
        if (self.new_style is not None): 
            for ns in self.new_style: 
                print(" (new style: {0})".format(str(ns)), end="", file=res, flush=True)
        return Utils.toStringStringIO(res)
    
    @property
    def year(self) -> int:
        if (self.__m_year > 0): 
            return self.__m_year
        if (self.int_value == 0): 
            return 0
        if (self.new_age == 0): 
            if (self.int_value < 16): 
                return 2000 + self.int_value
            if (self.int_value <= ((Utils.getDate(datetime.datetime.today()).year - 2000) + 5)): 
                return 2000 + self.int_value
            if (self.int_value < 100): 
                return 1900 + self.int_value
        return self.int_value
    @year.setter
    def year(self, value) -> int:
        self.__m_year = value
        return value
    
    @property
    def year0(self) -> int:
        if (self.new_age < 0): 
            return - self.year
        return self.year
    
    @property
    def can_be_year(self) -> bool:
        if (self.ltyp != DateItemToken.FirstLastTyp.NO): 
            return False
        if (self.typ == DateItemToken.DateItemType.YEAR): 
            return True
        if (self.typ == DateItemToken.DateItemType.MONTH or self.typ == DateItemToken.DateItemType.QUARTAL or self.typ == DateItemToken.DateItemType.HALFYEAR): 
            return False
        if (self.int_value >= 50 and (self.int_value < 100)): 
            return self.length_char == 2
        if ((self.int_value < 1000) or self.int_value > 2100): 
            return False
        return True
    
    @property
    def can_by_month(self) -> bool:
        if (self.ltyp != DateItemToken.FirstLastTyp.NO): 
            return False
        if (self.__m_can_by_month >= 0): 
            return self.__m_can_by_month == 1
        if (self.typ == DateItemToken.DateItemType.MONTH): 
            return True
        if (self.typ == DateItemToken.DateItemType.QUARTAL or self.typ == DateItemToken.DateItemType.HALFYEAR or self.typ == DateItemToken.DateItemType.POINTER): 
            return False
        return self.int_value > 0 and self.int_value <= 12
    @can_by_month.setter
    def can_by_month(self, value) -> bool:
        self.__m_can_by_month = (1 if value else 0)
        return value
    
    @property
    def can_be_day(self) -> bool:
        if ((self.typ == DateItemToken.DateItemType.MONTH or self.typ == DateItemToken.DateItemType.QUARTAL or self.typ == DateItemToken.DateItemType.HALFYEAR) or self.typ == DateItemToken.DateItemType.POINTER): 
            return False
        if (self.ltyp != DateItemToken.FirstLastTyp.NO): 
            return False
        return self.int_value > 0 and self.int_value <= 31
    
    @property
    def can_be_hour(self) -> bool:
        if (self.ltyp != DateItemToken.FirstLastTyp.NO): 
            return False
        if (self.typ != DateItemToken.DateItemType.NUMBER): 
            return self.typ == DateItemToken.DateItemType.HOUR
        if (self.length_char != 2): 
            if (self.length_char != 1 or self.int_value >= 24): 
                return False
            if (self.int_value == 0): 
                return True
            if (self.begin_token.next0_ is None or not self.begin_token.next0_.is_char_of(":.") or self.is_whitespace_after): 
                return False
            if (not (isinstance(self.begin_token.next0_.next0_, NumberToken))): 
                return False
            if (self.begin_token.next0_.next0_.length_char != 2): 
                return False
            if (self.begin_token.next0_.is_char('.')): 
                if (self.begin_token.previous is not None and self.begin_token.previous.is_value("В", None)): 
                    pass
                else: 
                    return False
            if (self.is_whitespace_before): 
                return True
            if (self.begin_token.previous is not None and self.begin_token.previous.is_char_of("(,")): 
                return True
            return False
        return self.int_value >= 0 and (self.int_value < 24)
    
    @property
    def can_be_minute(self) -> bool:
        if (self.ltyp != DateItemToken.FirstLastTyp.NO): 
            return False
        if (self.typ != DateItemToken.DateItemType.NUMBER): 
            return self.typ == DateItemToken.DateItemType.MINUTE
        if (self.length_char != 2): 
            return False
        return self.int_value >= 0 and (self.int_value < 60)
    
    @property
    def is_zero_headed(self) -> bool:
        return self.kit.sofa.text[self.begin_char] == '0'
    
    SPEED_REGIME = False
    
    @staticmethod
    def _prepare_all_data(t0 : 'Token') -> None:
        if (not DateItemToken.SPEED_REGIME): 
            return
        ad = DateAnalyzer._get_data(t0)
        if (ad is None): 
            return
        prevs = list()
        t = t0
        while t is not None: 
            prevs.clear()
            kk = 0
            tt0 = t
            tt = t.previous
            first_pass3889 = True
            while True:
                if first_pass3889: first_pass3889 = False
                else: tt = tt.previous; kk += 1
                if (not (tt is not None and (kk < 10))): break
                d0 = Utils.asObjectOrNull(tt.tag, DateTokenData)
                if (d0 is None): 
                    continue
                if (d0.dat is None): 
                    continue
                if (d0.dat.end_token.next0_ == tt0): 
                    prevs.insert(0, d0.dat)
                    tt0 = tt
                elif (d0.dat.end_char < tt.end_char): 
                    break
            d = Utils.asObjectOrNull(t.tag, DateTokenData)
            ter = DateItemToken.try_parse(t, prevs, False)
            if (ter is not None): 
                if (d is None): 
                    d = DateTokenData(t)
                d.dat = ter
            t = t.next0_
    
    @staticmethod
    def try_parse(t : 'Token', prev : typing.List['DateItemToken'], detail_regime : bool=False) -> 'DateItemToken':
        if (t is None): 
            return None
        ad = DateAnalyzer._get_data(t)
        if ((ad is not None and DateItemToken.SPEED_REGIME and ad.dregime) and not detail_regime): 
            d = Utils.asObjectOrNull(t.tag, DateTokenData)
            if (d is not None): 
                return d.dat
            return None
        if (ad is not None): 
            if (ad.level > 3): 
                return None
            ad.level += 1
        res = DateItemToken.__try_parse_int(t, prev, detail_regime)
        if (ad is not None): 
            ad.level -= 1
        return res
    
    @staticmethod
    def __try_parse_int(t : 'Token', prev : typing.List['DateItemToken'], detail_regime : bool) -> 'DateItemToken':
        t0 = t
        if (t0.is_char('_')): 
            t = t.next0_
            while t is not None: 
                if (t.is_newline_before): 
                    return None
                if (not t.is_char('_')): 
                    break
                t = t.next0_
        elif (BracketHelper.can_be_start_of_sequence(t0, True, False)): 
            ok = False
            t = t.next0_
            while t is not None: 
                if (BracketHelper.can_be_end_of_sequence(t, True, t0, False)): 
                    ok = True
                    break
                elif (not t.is_char('_')): 
                    break
                t = t.next0_
            if (not ok): 
                t = t0
            else: 
                t = t.next0_
                while t is not None: 
                    if (not t.is_char('_')): 
                        break
                    t = t.next0_
        elif ((isinstance(t0, TextToken)) and t0.is_value("THE", None)): 
            res0 = DateItemToken.__try_attach(t.next0_, prev, detail_regime)
            if (res0 is not None): 
                res0.begin_token = t
                return res0
        res = DateItemToken.__try_attach(t, prev, detail_regime)
        if (res is None): 
            return None
        res.begin_token = t0
        if (not res.is_whitespace_after and res.end_token.next0_ is not None and res.end_token.next0_.is_char('_')): 
            t = res.end_token.next0_
            while t is not None: 
                if (not t.is_char('_')): 
                    break
                else: 
                    res.end_token = t
                t = t.next0_
        if (res.typ == DateItemToken.DateItemType.YEAR or res.typ == DateItemToken.DateItemType.CENTURY or res.typ == DateItemToken.DateItemType.NUMBER): 
            tok = None
            ii = 0
            t = res.end_token.next0_
            if (t is not None and t.is_value("ДО", None)): 
                tok = DateItemToken.M_NEW_AGE.try_parse(t.next0_, TerminParseAttr.NO)
                ii = -1
            elif (t is not None and t.is_value("ОТ", "ВІД")): 
                tok = DateItemToken.M_NEW_AGE.try_parse(t.next0_, TerminParseAttr.NO)
                ii = 1
            else: 
                tok = DateItemToken.M_NEW_AGE.try_parse(t, TerminParseAttr.NO)
                ii = 1
            if (tok is not None): 
                res.new_age = (-1 if ii < 0 else 1)
                res.end_token = tok.end_token
                if (res.typ == DateItemToken.DateItemType.NUMBER): 
                    res.typ = DateItemToken.DateItemType.YEAR
        if (res.end_token.next0_ is not None and res.end_token.next0_.is_char('(')): 
            t1 = res.end_token.next0_.next0_
            li = DateItemToken.try_parse_list(t1, 20)
            if ((li is not None and len(li) > 0 and ((li[0].typ == DateItemToken.DateItemType.NUMBER or li[0].typ == DateItemToken.DateItemType.DAY))) and li[len(li) - 1].end_token.next0_ is not None and li[len(li) - 1].end_token.next0_.is_char(')')): 
                res.new_style = li
                res.end_token = li[len(li) - 1].end_token.next0_
                if (res.can_be_year and res.end_token.next0_ is not None and res.end_token.next0_.is_value("ГОД", "РІК")): 
                    res.end_token = res.end_token.next0_
                    res.typ = DateItemToken.DateItemType.YEAR
        return res
    
    @staticmethod
    def __is_new_age(t : 'Token') -> bool:
        if (t is None): 
            return False
        if (t.is_value("ДО", None)): 
            return DateItemToken.M_NEW_AGE.try_parse(t.next0_, TerminParseAttr.NO) is not None
        elif (t.is_value("ОТ", "ВІД")): 
            return DateItemToken.M_NEW_AGE.try_parse(t.next0_, TerminParseAttr.NO) is not None
        return DateItemToken.M_NEW_AGE.try_parse(t, TerminParseAttr.NO) is not None
    
    @staticmethod
    def __try_attach(t : 'Token', prev : typing.List['DateItemToken'], detail_regime : bool) -> 'DateItemToken':
        from pullenti.ner.measure.internal.MeasureToken import MeasureToken
        if (t is None): 
            return None
        nt = Utils.asObjectOrNull(t, NumberToken)
        begin = t
        end = t
        is_in_brack = False
        if (isinstance(t.next0_, NumberToken)): 
            nt0 = Utils.asObjectOrNull(t.next0_, NumberToken)
            can_year = nt0.int_value is not None and nt0.int_value >= 1800
            if (BracketHelper.can_be_start_of_sequence(t, can_year, False) and BracketHelper.can_be_end_of_sequence(t.next0_.next0_, can_year, None, False)): 
                nt = (Utils.asObjectOrNull(t.next0_, NumberToken))
                end = t.next0_.next0_
                is_in_brack = True
        if ((t.is_newline_before and BracketHelper.is_bracket(t, False) and (isinstance(t.next0_, NumberToken))) and BracketHelper.is_bracket(t.next0_.next0_, False)): 
            nt = (Utils.asObjectOrNull(t.next0_, NumberToken))
            end = t.next0_.next0_
            is_in_brack = True
        flt = DateItemToken.FirstLastTyp.NO
        if (t.is_value("ПЕРВЫЙ", None)): 
            flt = DateItemToken.FirstLastTyp.FIRST
        elif (t.is_value("ПОСЛЕДНИЙ", None)): 
            flt = DateItemToken.FirstLastTyp.LAST
        if (flt != DateItemToken.FirstLastTyp.NO and t.next0_ is not None): 
            t1 = t.next0_
            if (isinstance(t1, NumberToken)): 
                t1 = t1.next0_
            if (t1 is None): 
                return None
            dty = DateItemToken.DateItemType.NUMBER
            if (t1.is_value("ДЕНЬ", None)): 
                dty = DateItemToken.DateItemType.DAY
            elif (t1.is_value("МЕСЯЦ", "МІСЯЦЬ")): 
                dty = DateItemToken.DateItemType.MONTH
            elif (t1.is_value("КВАРТАЛ", None)): 
                dty = DateItemToken.DateItemType.QUARTAL
            elif (t1.is_value("ПОЛУГОДИЕ", "ПІВРІЧЧЯ") or t1.is_value("ПОЛГОДА", "ПІВРОКУ")): 
                dty = DateItemToken.DateItemType.HALFYEAR
            if (dty != DateItemToken.DateItemType.NUMBER): 
                res = DateItemToken._new826(t, t1, dty, flt, 1)
                if ((isinstance(t.next0_, NumberToken)) and t.next0_.int_value is not None): 
                    res.int_value = t.next0_.int_value
                return res
            if (t1.is_value("ГОД", "РІК") and NumberHelper.try_parse_roman(t1.next0_) is not None): 
                return DateItemToken._new827(t, t1, DateItemToken.DateItemType.POINTER, (DatePointerType.END if flt == DateItemToken.FirstLastTyp.LAST else DatePointerType.BEGIN))
        if (nt is not None): 
            if (nt.int_value is None): 
                return None
            if (nt.typ == NumberSpellingType.WORDS): 
                if (nt.morph.class0_.is_noun and not nt.morph.class0_.is_adjective): 
                    if (t.next0_ is not None and ((t.next0_.is_value("КВАРТАЛ", None) or t.next0_.is_value("ПОЛУГОДИЕ", None) or t.next0_.is_value("ПІВРІЧЧЯ", None)))): 
                        pass
                    else: 
                        return None
            if (NumberHelper.try_parse_age(nt) is not None): 
                return None
            if (not t.is_whitespace_before and t.previous is not None): 
                tt00 = t.previous
                if (tt00.is_hiphen and not tt00.is_whitespace_before and tt00.previous is not None): 
                    tt00 = tt00.previous
                if ((isinstance(tt00, TextToken)) and tt00.length_char == 2 and tt00.chars.is_all_upper): 
                    return None
            if (t.previous is not None and t.previous.is_value("SU", None)): 
                return None
            tt = None
            res = DateItemToken._new828(begin, end, DateItemToken.DateItemType.NUMBER, nt.int_value, nt.morph)
            if ((res.int_value == 20 and (isinstance(nt.next0_, NumberToken)) and nt.next0_.int_value is not None) and nt.next0_.length_char == 2 and prev is not None): 
                num = 2000 + nt.next0_.int_value
                if ((num < 2030) and len(prev) > 0 and prev[len(prev) - 1].typ == DateItemToken.DateItemType.MONTH): 
                    ok = False
                    if (nt.whitespaces_after_count == 1): 
                        ok = True
                    elif (nt.is_newline_after and nt.is_newline_after): 
                        ok = True
                    if (ok): 
                        nt = (Utils.asObjectOrNull(nt.next0_, NumberToken))
                        res.end_token = nt
                        res.int_value = num
            if (res.int_value == 20 or res.int_value == 201): 
                tt = t.next0_
                if (tt is not None and tt.is_char('_')): 
                    while tt is not None: 
                        if (not tt.is_char('_')): 
                            break
                        tt = tt.next0_
                    tt = DateItemToken.__test_year_rus_word(tt, False)
                    if (tt is not None): 
                        res.int_value = 0
                        res.end_token = tt
                        res.typ = DateItemToken.DateItemType.YEAR
                        return res
            if (res.int_value <= 12 and t.next0_ is not None and (t.whitespaces_after_count < 3)): 
                tt = t.next0_
                if (tt.is_value("ЧАС", None)): 
                    if (((isinstance(t.previous, TextToken)) and not t.previous.chars.is_letter and not t.is_whitespace_before) and (isinstance(t.previous.previous, NumberToken)) and not t.previous.is_whitespace_before): 
                        pass
                    else: 
                        res.typ = DateItemToken.DateItemType.HOUR
                        res.end_token = tt
                        tt = tt.next0_
                        if (tt is not None and tt.is_char('.')): 
                            res.end_token = tt
                            tt = tt.next0_
                first_pass3890 = True
                while True:
                    if first_pass3890: first_pass3890 = False
                    else: tt = tt.next0_
                    if (not (tt is not None)): break
                    if (tt.is_value("УТРО", "РАНОК")): 
                        res.end_token = tt
                        res.typ = DateItemToken.DateItemType.HOUR
                        return res
                    if (tt.is_value("ВЕЧЕР", "ВЕЧІР") and tt.morph.number == MorphNumber.SINGULAR): 
                        res.end_token = tt
                        res.int_value += 12
                        res.typ = DateItemToken.DateItemType.HOUR
                        return res
                    if (tt.is_value("ДЕНЬ", None) and tt.morph.number == MorphNumber.SINGULAR): 
                        res.end_token = tt
                        if (res.int_value < 10): 
                            res.int_value += 12
                        res.typ = DateItemToken.DateItemType.HOUR
                        return res
                    if (tt.is_value("НОЧЬ", "НІЧ") and tt.morph.number == MorphNumber.SINGULAR): 
                        res.end_token = tt
                        if (res.int_value == 12): 
                            res.int_value = 0
                        elif (res.int_value > 9): 
                            res.int_value += 12
                        res.typ = DateItemToken.DateItemType.HOUR
                        return res
                    if (tt.is_comma or tt.morph.class0_.is_adverb): 
                        continue
                    break
                if (res.typ == DateItemToken.DateItemType.HOUR): 
                    return res
            can_be_year_ = True
            if (prev is not None and len(prev) > 0 and prev[len(prev) - 1].typ == DateItemToken.DateItemType.MONTH): 
                pass
            elif ((prev is not None and len(prev) >= 4 and prev[len(prev) - 1].typ == DateItemToken.DateItemType.DELIM) and prev[len(prev) - 2].can_by_month): 
                pass
            elif (nt.next0_ is not None and ((nt.next0_.is_value("ГОД", "РІК")))): 
                if (res.int_value < 1000): 
                    can_be_year_ = False
            tt = DateItemToken.__test_year_rus_word(nt.next0_, False)
            if (tt is not None and DateItemToken.__is_new_age(tt.next0_)): 
                res.typ = DateItemToken.DateItemType.YEAR
                res.end_token = tt
            elif (can_be_year_): 
                if (res.can_be_year or res.typ == DateItemToken.DateItemType.NUMBER): 
                    tt = DateItemToken.__test_year_rus_word(nt.next0_, res.is_newline_before)
                    if ((tt) is not None): 
                        if ((tt.is_value("Г", None) and not tt.is_whitespace_before and t.previous is not None) and ((t.previous.is_value("КОРПУС", None) or t.previous.is_value("КОРП", None)))): 
                            pass
                        elif ((((nt.next0_.is_value("Г", None) and (t.whitespaces_before_count < 3) and t.previous is not None) and t.previous.is_value("Я", None) and t.previous.previous is not None) and t.previous.previous.is_char_of("\\/") and t.previous.previous.previous is not None) and t.previous.previous.previous.is_value("А", None)): 
                            return None
                        elif (nt.next0_.length_char == 1 and not res.can_be_year and ((prev is None or ((len(prev) > 0 and prev[len(prev) - 1].typ != DateItemToken.DateItemType.DELIM))))): 
                            pass
                        else: 
                            res.end_token = tt
                            res.typ = DateItemToken.DateItemType.YEAR
                            res.lang = tt.morph.language
                    if (((res.typ == DateItemToken.DateItemType.NUMBER and not t.is_newline_before and t.previous is not None) and t.previous.morph.class0_.is_preposition and t.previous.previous is not None) and t.previous.previous.is_value("ГОД", "")): 
                        res.typ = DateItemToken.DateItemType.YEAR
                    if (((nt.typ == NumberSpellingType.DIGIT and res.typ == DateItemToken.DateItemType.NUMBER and res.can_be_year) and t.previous is not None and t.previous.is_char('(')) and t.next0_ is not None and t.next0_.is_char(')')): 
                        res.typ = DateItemToken.DateItemType.YEAR
                elif (tt is not None and (nt.whitespaces_after_count < 2) and (nt.end_char - nt.begin_char) == 1): 
                    res.end_token = tt
                    res.typ = DateItemToken.DateItemType.YEAR
                    res.lang = tt.morph.language
            if (nt.previous is not None): 
                if (nt.previous.is_value("В", "У") or nt.previous.is_value("К", None) or nt.previous.is_value("ДО", None)): 
                    tt = DateItemToken.__test_year_rus_word(nt.next0_, False)
                    if ((tt) is not None): 
                        ok = False
                        if ((res.int_value < 100) and (isinstance(tt, TextToken)) and ((tt.term == "ГОДА" or tt.term == "РОКИ"))): 
                            pass
                        else: 
                            ok = True
                            if (nt.previous.is_value("ДО", None) and nt.next0_.is_value("Г", None)): 
                                cou = 0
                                ttt = nt.previous.previous
                                while ttt is not None and (cou < 10): 
                                    mt = MeasureToken.try_parse(ttt, None, False, False, False, False)
                                    if (mt is not None and mt.end_char > nt.end_char): 
                                        ok = False
                                        break
                                    ttt = ttt.previous; cou += 1
                        if (ok): 
                            res.end_token = tt
                            res.typ = DateItemToken.DateItemType.YEAR
                            res.lang = tt.morph.language
                            res.begin_token = nt.previous
                elif (((nt.previous.is_value("IN", None) or nt.previous.is_value("SINCE", None))) and res.can_be_year): 
                    uu = (NumbersWithUnitToken.try_parse(nt, None, NumberWithUnitParseAttr.NO) if nt.previous.is_value("IN", None) else None)
                    if (uu is not None and len(uu.units) > 0): 
                        pass
                    else: 
                        res.typ = DateItemToken.DateItemType.YEAR
                        res.begin_token = nt.previous
                elif (nt.previous.is_value("NEL", None) or nt.previous.is_value("DEL", None)): 
                    if (res.can_be_year): 
                        res.typ = DateItemToken.DateItemType.YEAR
                        res.lang = MorphLang.IT
                        res.begin_token = nt.previous
                elif (nt.previous.is_value("IL", None) and res.can_be_day): 
                    res.lang = MorphLang.IT
                    res.begin_token = nt.previous
            t1 = res.end_token.next0_
            if (t1 is not None): 
                if (t1.is_value("ЧАС", "ГОДИНА") or t1.is_value("HOUR", None) or t1.is_value("Ч", None)): 
                    if ((((prev is not None and len(prev) == 2 and prev[0].can_be_hour) and prev[1].typ == DateItemToken.DateItemType.DELIM and not prev[1].is_whitespace_after) and not prev[1].is_whitespace_after and res.int_value >= 0) and (res.int_value < 59)): 
                        prev[0].typ = DateItemToken.DateItemType.HOUR
                        res.typ = DateItemToken.DateItemType.MINUTE
                        res.end_token = t1
                    elif (res.int_value < 24): 
                        if (t1.next0_ is not None and t1.next0_.is_char('.')): 
                            t1 = t1.next0_
                        res.typ = DateItemToken.DateItemType.HOUR
                        res.end_token = t1
                elif ((res.int_value < 60) and (((t1.is_value("МИНУТА", "ХВИЛИНА") or t1.is_value("МИН", None) or t1.is_value("MINUTE", None)) or ((((t1.is_value("М", None) and prev is not None and len(prev) > 0) and prev[len(prev) - 1].typ == DateItemToken.DateItemType.HOUR)))))): 
                    if (t1.next0_ is not None and t1.next0_.is_char('.')): 
                        t1 = t1.next0_
                    res.typ = DateItemToken.DateItemType.MINUTE
                    res.end_token = t1
                elif ((res.int_value < 60) and ((t1.is_value("СЕКУНДА", None) or t1.is_value("СЕК", None) or t1.is_value("SECOND", None)))): 
                    if (t1.next0_ is not None and t1.next0_.is_char('.')): 
                        t1 = t1.next0_
                    res.typ = DateItemToken.DateItemType.SECOND
                    res.end_token = t1
                elif ((res.int_value < 30) and ((t1.is_value("ВЕК", "ВІК") or t1.is_value("СТОЛЕТИЕ", "СТОЛІТТЯ")))): 
                    res.typ = DateItemToken.DateItemType.CENTURY
                    res.end_token = t1
                elif ((res.int_value < 10) and ((t1.is_value("ДЕСЯТИЛЕТИЕ", "ДЕСЯТИЛІТТЯ") or t1.is_value("ДЕКАДА", None)))): 
                    res.typ = DateItemToken.DateItemType.TENYEARS
                    res.end_token = t1
                elif (res.int_value <= 4 and t1.is_value("КВАРТАЛ", None)): 
                    res.typ = DateItemToken.DateItemType.QUARTAL
                    res.end_token = t1
                elif (res.int_value <= 2 and ((t1.is_value("ПОЛУГОДИЕ", None) or t1.is_value("ПІВРІЧЧЯ", None)))): 
                    res.typ = DateItemToken.DateItemType.HALFYEAR
                    res.end_token = t1
            return res
        t0 = Utils.asObjectOrNull(t, TextToken)
        if (t0 is None): 
            return None
        txt = t0.get_source_text()
        if ((txt[0] == 'I' or txt[0] == 'X' or txt[0] == 'Х') or txt[0] == 'V' or ((t0.chars.is_latin_letter and t0.chars.is_all_upper))): 
            lat = NumberHelper.try_parse_roman(t)
            if (lat is not None and lat.end_token.next0_ is not None and lat.int_value is not None): 
                val = lat.int_value
                tt = lat.end_token.next0_
                if (tt.is_value("КВАРТАЛ", None) and val > 0 and val <= 4): 
                    return DateItemToken._new829(t, tt, DateItemToken.DateItemType.QUARTAL, val)
                if (tt.is_value("ПОЛУГОДИЕ", "ПІВРІЧЧЯ") and val > 0 and val <= 2): 
                    return DateItemToken._new829(t, lat.end_token.next0_, DateItemToken.DateItemType.HALFYEAR, val)
                if (tt.is_value("ВЕК", "ВІК") or tt.is_value("СТОЛЕТИЕ", "СТОЛІТТЯ")): 
                    return DateItemToken._new829(t, lat.end_token.next0_, DateItemToken.DateItemType.CENTURY, val)
                if (tt.is_value("ДЕСЯТИЛЕТИЕ", "ДЕСЯТИЛІТТЯ") or tt.is_value("ДЕКАДА", None)): 
                    return DateItemToken._new829(t, lat.end_token.next0_, DateItemToken.DateItemType.TENYEARS, val)
                if (((tt.is_value("В", None) or tt.is_value("ВВ", None))) and tt.next0_ is not None and tt.next0_.is_char('.')): 
                    if (prev is not None and len(prev) > 0 and prev[len(prev) - 1].typ == DateItemToken.DateItemType.POINTER): 
                        return DateItemToken._new829(t, tt.next0_, DateItemToken.DateItemType.CENTURY, val)
                    if (DateItemToken.__is_new_age(tt.next0_.next0_) or not tt.is_whitespace_before): 
                        return DateItemToken._new829(t, tt.next0_, DateItemToken.DateItemType.CENTURY, val)
                if (tt.is_hiphen): 
                    lat2 = NumberHelper.try_parse_roman(tt.next0_)
                    if (lat2 is not None and lat2.int_value is not None and lat2.end_token.next0_ is not None): 
                        if (lat2.end_token.next0_.is_value("ВЕК", "ВІК") or lat2.end_token.next0_.is_value("СТОЛЕТИЕ", "СТОЛІТТЯ")): 
                            ddd = DateItemToken.try_parse(tt.next0_, None, False)
                            return DateItemToken._new835(t, lat.end_token, DateItemToken.DateItemType.CENTURY, val, ((ddd.new_age if ddd is not None else 0)))
                pr0 = None
                ttt = tt
                first_pass3891 = True
                while True:
                    if first_pass3891: first_pass3891 = False
                    else: ttt = ttt.next0_
                    if (not (ttt is not None)): break
                    if (ttt.is_hiphen or ttt.is_comma_and): 
                        continue
                    mc = ttt.get_morph_class_in_dictionary()
                    if (mc.is_preposition): 
                        continue
                    nex = DateItemToken.try_parse(ttt, pr0, False)
                    if (nex is None): 
                        break
                    if (nex.typ == DateItemToken.DateItemType.POINTER): 
                        if (pr0 is None): 
                            pr0 = list()
                        pr0.append(nex)
                        ttt = nex.end_token
                        continue
                    if (nex.typ == DateItemToken.DateItemType.CENTURY or nex.typ == DateItemToken.DateItemType.QUARTAL): 
                        return DateItemToken._new835(t, lat.end_token, nex.typ, val, nex.new_age)
                    break
        if (t is None): 
            return None
        if (t is not None and t.is_value("НАПРИКІНЦІ", None)): 
            return DateItemToken._new837(t, t, DateItemToken.DateItemType.POINTER, DatePointerType.END, "конец")
        if (t is not None and t.is_value("ДОНЕДАВНА", None)): 
            return DateItemToken._new837(t, t, DateItemToken.DateItemType.POINTER, DatePointerType.TODAY, "сегодня")
        if (prev is None): 
            if (t is not None): 
                if (t.is_value("ОКОЛО", "БІЛЯ") or t.is_value("ПРИМЕРНО", "ПРИБЛИЗНО") or t.is_value("ABOUT", None)): 
                    return DateItemToken._new837(t, t, DateItemToken.DateItemType.POINTER, DatePointerType.ABOUT, "около")
            if (t.is_value("ОК", None) or t.is_value("OK", None)): 
                if (t.next0_ is not None and t.next0_.is_char('.')): 
                    return DateItemToken._new837(t, t.next0_, DateItemToken.DateItemType.POINTER, DatePointerType.ABOUT, "около")
                return DateItemToken._new837(t, t, DateItemToken.DateItemType.POINTER, DatePointerType.ABOUT, "около")
        tok = DateItemToken.M_SEASONS.try_parse(t, TerminParseAttr.NO)
        if ((tok is not None and (Utils.valToEnum(tok.termin.tag, DatePointerType)) == DatePointerType.SUMMER and t.morph.language.is_ru) and (isinstance(t, TextToken))): 
            str0_ = t.term
            if (str0_ != "ЛЕТОМ" and str0_ != "ЛЕТА" and str0_ != "ЛЕТО"): 
                tok = (None)
        if (tok is not None): 
            return DateItemToken._new827(t, tok.end_token, DateItemToken.DateItemType.POINTER, Utils.valToEnum(tok.termin.tag, DatePointerType))
        npt = NounPhraseHelper.try_parse(t, NounPhraseParseAttr.NO, 0, None)
        if (npt is not None): 
            tok = DateItemToken.M_SEASONS.try_parse(npt.end_token, TerminParseAttr.NO)
            if ((tok is not None and (Utils.valToEnum(tok.termin.tag, DatePointerType)) == DatePointerType.SUMMER and t.morph.language.is_ru) and (isinstance(t, TextToken))): 
                str0_ = t.term
                if (str0_ != "ЛЕТОМ" and str0_ != "ЛЕТА" and str0_ != "ЛЕТО"): 
                    tok = (None)
            if (tok is not None): 
                return DateItemToken._new827(t, tok.end_token, DateItemToken.DateItemType.POINTER, Utils.valToEnum(tok.termin.tag, DatePointerType))
            typ_ = DateItemToken.DateItemType.NUMBER
            if (npt.noun.is_value("КВАРТАЛ", None)): 
                typ_ = DateItemToken.DateItemType.QUARTAL
            elif (npt.end_token.is_value("ПОЛУГОДИЕ", "ПІВРІЧЧЯ")): 
                typ_ = DateItemToken.DateItemType.HALFYEAR
            elif (npt.end_token.is_value("ДЕСЯТИЛЕТИЕ", "ДЕСЯТИЛІТТЯ") or npt.end_token.is_value("ДЕКАДА", None)): 
                typ_ = DateItemToken.DateItemType.TENYEARS
            elif (npt.end_token.is_value("НАЧАЛО", "ПОЧАТОК")): 
                return DateItemToken._new837(t, npt.end_token, DateItemToken.DateItemType.POINTER, DatePointerType.BEGIN, "начало")
            elif (npt.end_token.is_value("СЕРЕДИНА", None)): 
                return DateItemToken._new837(t, npt.end_token, DateItemToken.DateItemType.POINTER, DatePointerType.CENTER, "середина")
            elif (npt.end_token.is_value("КОНЕЦ", None) or npt.end_token.is_value("КІНЕЦЬ", None) or npt.end_token.is_value("НАПРИКІНЕЦЬ", None)): 
                return DateItemToken._new837(t, npt.end_token, DateItemToken.DateItemType.POINTER, DatePointerType.END, "конец")
            elif (npt.end_token.is_value("ВРЕМЯ", None) and len(npt.adjectives) > 0 and npt.end_token.previous.is_value("НАСТОЯЩЕЕ", None)): 
                return DateItemToken._new837(t, npt.end_token, DateItemToken.DateItemType.POINTER, DatePointerType.TODAY, "сегодня")
            elif (npt.end_token.is_value("ЧАС", None) and len(npt.adjectives) > 0 and npt.end_token.previous.is_value("ДАНИЙ", None)): 
                return DateItemToken._new837(t, npt.end_token, DateItemToken.DateItemType.POINTER, DatePointerType.TODAY, "сегодня")
            if (typ_ != DateItemToken.DateItemType.NUMBER or detail_regime): 
                delta = 0
                ok = False
                if (len(npt.adjectives) > 0): 
                    if (npt.adjectives[0].is_value("ПОСЛЕДНИЙ", "ОСТАННІЙ")): 
                        return DateItemToken._new849(t0, npt.end_token, typ_, (4 if typ_ == DateItemToken.DateItemType.QUARTAL else (9 if typ_ == DateItemToken.DateItemType.TENYEARS else 2)), DateItemToken.FirstLastTyp.LAST)
                    if (npt.adjectives[0].is_value("ПРЕДЫДУЩИЙ", "ПОПЕРЕДНІЙ") or npt.adjectives[0].is_value("ПРОШЛЫЙ", None)): 
                        delta = -1
                    elif (npt.adjectives[0].is_value("СЛЕДУЮЩИЙ", None) or npt.adjectives[0].is_value("ПОСЛЕДУЮЩИЙ", None) or npt.adjectives[0].is_value("НАСТУПНИЙ", None)): 
                        delta = 1
                    elif (npt.adjectives[0].is_value("ЭТОТ", "ЦЕЙ") or npt.adjectives[0].is_value("ТЕКУЩИЙ", "ПОТОЧНИЙ")): 
                        delta = 0
                    else: 
                        return None
                    ok = True
                elif (npt.begin_token.is_value("ЭТОТ", "ЦЕЙ")): 
                    ok = True
                cou = 0
                tt = t.previous
                first_pass3892 = True
                while True:
                    if first_pass3892: first_pass3892 = False
                    else: tt = tt.previous
                    if (not (tt is not None)): break
                    if (cou > 200): 
                        break
                    dr = Utils.asObjectOrNull(tt.get_referent(), DateRangeReferent)
                    if (dr is None): 
                        continue
                    if (typ_ == DateItemToken.DateItemType.QUARTAL): 
                        ii = dr.quarter_number
                        if (ii < 1): 
                            continue
                        ii += delta
                        if ((ii < 1) or ii > 4): 
                            continue
                        return DateItemToken._new829(t0, npt.end_token, typ_, ii)
                    if (typ_ == DateItemToken.DateItemType.HALFYEAR): 
                        ii = dr.halfyear_number
                        if (ii < 1): 
                            continue
                        ii += delta
                        if ((ii < 1) or ii > 2): 
                            continue
                        return DateItemToken._new829(t0, npt.end_token, typ_, ii)
                if (ok and typ_ == DateItemToken.DateItemType.TENYEARS): 
                    return DateItemToken._new852(t0, npt.end_token, typ_, delta, True)
        term = t0.term
        if (not str.isalnum(term[0])): 
            if (t0.is_char_of(".\\/:") or t0.is_hiphen): 
                return DateItemToken._new853(t0, t0, DateItemToken.DateItemType.DELIM, term)
            elif (t0.is_char(',')): 
                return DateItemToken._new853(t0, t0, DateItemToken.DateItemType.DELIM, term)
            else: 
                return None
        if (term == "O" or term == "О"): 
            if ((isinstance(t.next0_, NumberToken)) and not t.is_whitespace_after and len(t.next0_.value) == 1): 
                return DateItemToken._new829(t, t.next0_, DateItemToken.DateItemType.NUMBER, t.next0_.int_value)
        if (str.isalpha(term[0])): 
            inf = DateItemToken.M_MONTHES.try_parse(t, TerminParseAttr.NO)
            if (inf is not None and inf.termin.tag is None): 
                inf = DateItemToken.M_MONTHES.try_parse(inf.end_token.next0_, TerminParseAttr.NO)
            if (inf is not None and t.is_value("MAYER", None)): 
                return None
            if (inf is not None and (isinstance(inf.termin.tag, int))): 
                return DateItemToken._new856(inf.begin_token, inf.end_token, DateItemToken.DateItemType.MONTH, inf.termin.tag, inf.termin.lang)
        return None
    
    DAYS_OF_WEEK = None
    
    M_NEW_AGE = None
    
    M_MONTHES = None
    
    M_SEASONS = None
    
    @staticmethod
    def initialize() -> None:
        if (DateItemToken.M_NEW_AGE is not None): 
            return
        DateItemToken.M_NEW_AGE = TerminCollection()
        tt = Termin._new857("НОВАЯ ЭРА", MorphLang.RU, True, "НОВОЙ ЭРЫ")
        tt.add_variant("НАША ЭРА", True)
        tt.add_abridge("Н.Э.")
        DateItemToken.M_NEW_AGE.add(tt)
        tt = Termin._new857("НОВА ЕРА", MorphLang.UA, True, "НОВОЇ ЕРИ")
        tt.add_variant("НАША ЕРА", True)
        tt.add_abridge("Н.Е.")
        DateItemToken.M_NEW_AGE.add(tt)
        tt = Termin("РОЖДЕСТВО ХРИСТОВО", MorphLang.RU, True)
        tt.add_abridge("Р.Х.")
        DateItemToken.M_NEW_AGE.add(tt)
        tt = Termin("РІЗДВА ХРИСТОВОГО", MorphLang.UA, True)
        tt.add_abridge("Р.Х.")
        DateItemToken.M_NEW_AGE.add(tt)
        DateItemToken.M_SEASONS = TerminCollection()
        DateItemToken.M_SEASONS.add(Termin._new703("ЗИМА", MorphLang.RU, True, DatePointerType.WINTER))
        DateItemToken.M_SEASONS.add(Termin._new703("WINTER", MorphLang.EN, True, DatePointerType.WINTER))
        t = Termin._new703("ВЕСНА", MorphLang.RU, True, DatePointerType.SPRING)
        t.add_variant("ПРОВЕСНА", True)
        DateItemToken.M_SEASONS.add(t)
        DateItemToken.M_SEASONS.add(Termin._new703("SPRING", MorphLang.EN, True, DatePointerType.SPRING))
        t = Termin._new703("ЛЕТО", MorphLang.RU, True, DatePointerType.SUMMER)
        DateItemToken.M_SEASONS.add(t)
        t = Termin._new703("ЛІТО", MorphLang.UA, True, DatePointerType.SUMMER)
        DateItemToken.M_SEASONS.add(t)
        t = Termin._new703("ОСЕНЬ", MorphLang.RU, True, DatePointerType.AUTUMN)
        DateItemToken.M_SEASONS.add(t)
        t = Termin._new703("AUTUMN", MorphLang.EN, True, DatePointerType.AUTUMN)
        DateItemToken.M_SEASONS.add(t)
        t = Termin._new703("ОСІНЬ", MorphLang.UA, True, DatePointerType.AUTUMN)
        DateItemToken.M_SEASONS.add(t)
        DateItemToken.M_MONTHES = TerminCollection()
        months = ["ЯНВАРЬ", "ФЕВРАЛЬ", "МАРТ", "АПРЕЛЬ", "МАЙ", "ИЮНЬ", "ИЮЛЬ", "АВГУСТ", "СЕНТЯБРЬ", "ОКТЯБРЬ", "НОЯБРЬ", "ДЕКАБРЬ"]
        i = 0
        while i < len(months): 
            t = Termin._new703(months[i], MorphLang.RU, True, i + 1)
            DateItemToken.M_MONTHES.add(t)
            i += 1
        months = ["СІЧЕНЬ", "ЛЮТИЙ", "БЕРЕЗЕНЬ", "КВІТЕНЬ", "ТРАВЕНЬ", "ЧЕРВЕНЬ", "ЛИПЕНЬ", "СЕРПЕНЬ", "ВЕРЕСЕНЬ", "ЖОВТЕНЬ", "ЛИСТОПАД", "ГРУДЕНЬ"]
        i = 0
        while i < len(months): 
            t = Termin._new703(months[i], MorphLang.UA, True, i + 1)
            DateItemToken.M_MONTHES.add(t)
            i += 1
        months = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
        i = 0
        while i < len(months): 
            t = Termin._new703(months[i], MorphLang.EN, True, i + 1)
            DateItemToken.M_MONTHES.add(t)
            i += 1
        months = ["GENNAIO", "FEBBRAIO", "MARZO", "APRILE", "MAGGIO", "GUINGO", "LUGLIO", "AGOSTO", "SETTEMBRE", "OTTOBRE", "NOVEMBRE", "DICEMBRE"]
        i = 0
        while i < len(months): 
            t = Termin._new703(months[i], MorphLang.IT, True, i + 1)
            DateItemToken.M_MONTHES.add(t)
            i += 1
        for m in ["ЯНВ", "ФЕВ", "ФЕВР", "МАР", "АПР", "ИЮН", "ИЮЛ", "АВГ", "СЕН", "СЕНТ", "ОКТ", "НОЯ", "НОЯБ", "ДЕК", "JAN", "FEB", "MAR", "APR", "JUN", "JUL", "AUG", "SEP", "SEPT", "OCT", "NOV", "DEC"]: 
            for ttt in DateItemToken.M_MONTHES.termins: 
                if (ttt.terms[0].canonical_text.startswith(m)): 
                    ttt.add_abridge(m)
                    DateItemToken.M_MONTHES.reindex(ttt)
                    break
        for m in ["OF"]: 
            DateItemToken.M_MONTHES.add(Termin(m, MorphLang.EN, True))
        DateItemToken.M_EMPTY_WORDS = dict()
        DateItemToken.M_EMPTY_WORDS["IN"] = MorphLang.EN
        DateItemToken.M_EMPTY_WORDS["SINCE"] = MorphLang.EN
        DateItemToken.M_EMPTY_WORDS["THE"] = MorphLang.EN
        DateItemToken.M_EMPTY_WORDS["NEL"] = MorphLang.IT
        DateItemToken.M_EMPTY_WORDS["DEL"] = MorphLang.IT
        DateItemToken.M_EMPTY_WORDS["IL"] = MorphLang.IT
        DateItemToken.DAYS_OF_WEEK = TerminCollection()
        te = Termin._new703("SUNDAY", MorphLang.EN, True, 7)
        te.add_abridge("SUN")
        te.add_variant("ВОСКРЕСЕНЬЕ", True)
        te.add_variant("ВОСКРЕСЕНИЕ", True)
        te.add_abridge("ВС")
        te.add_variant("НЕДІЛЯ", True)
        DateItemToken.DAYS_OF_WEEK.add(te)
        te = Termin._new703("MONDAY", MorphLang.EN, True, 1)
        te.add_abridge("MON")
        te.add_variant("ПОНЕДЕЛЬНИК", True)
        te.add_abridge("ПОН")
        te.add_variant("ПОНЕДІЛОК", True)
        DateItemToken.DAYS_OF_WEEK.add(te)
        te = Termin._new703("TUESDAY", MorphLang.EN, True, 2)
        te.add_abridge("TUE")
        te.add_variant("ВТОРНИК", True)
        te.add_abridge("ВТ")
        te.add_variant("ВІВТОРОК", True)
        DateItemToken.DAYS_OF_WEEK.add(te)
        te = Termin._new703("WEDNESDAY", MorphLang.EN, True, 3)
        te.add_abridge("WED")
        te.add_variant("СРЕДА", True)
        te.add_abridge("СР")
        te.add_variant("СЕРЕДА", True)
        DateItemToken.DAYS_OF_WEEK.add(te)
        te = Termin._new703("THURSDAY", MorphLang.EN, True, 4)
        te.add_abridge("THU")
        te.add_variant("ЧЕТВЕРГ", True)
        te.add_abridge("ЧТ")
        te.add_variant("ЧЕТВЕР", True)
        DateItemToken.DAYS_OF_WEEK.add(te)
        te = Termin._new703("FRIDAY", MorphLang.EN, True, 5)
        te.add_abridge("FRI")
        te.add_variant("ПЯТНИЦА", True)
        te.add_abridge("ПТ")
        te.add_variant("ПЯТНИЦЯ", True)
        DateItemToken.DAYS_OF_WEEK.add(te)
        te = Termin._new703("SATURDAY", MorphLang.EN, True, 6)
        te.add_abridge("SAT")
        te.add_variant("СУББОТА", True)
        te.add_abridge("СБ")
        te.add_variant("СУБОТА", True)
        DateItemToken.DAYS_OF_WEEK.add(te)
    
    M_EMPTY_WORDS = None
    
    @staticmethod
    def __test_year_rus_word(t0 : 'Token', ignore_newline : bool=False) -> 'Token':
        tt = t0
        if (tt is None): 
            return None
        if (tt.is_value("ГОД", None) or tt.is_value("РІК", None)): 
            return tt
        if (not ignore_newline and tt.previous is not None and tt.is_newline_before): 
            return None
        if ((tt.is_value("Г", None) and tt.next0_ is not None and tt.next0_.is_char_of("\\/.")) and tt.next0_.next0_ is not None and tt.next0_.next0_.is_value("Б", None)): 
            return None
        if (((tt.morph.language.is_ru and ((tt.is_value("ГГ", None) or tt.is_value("Г", None))))) or ((tt.morph.language.is_ua and ((tt.is_value("Р", None) or tt.is_value("РР", None)))))): 
            if (tt.next0_ is not None and tt.next0_.is_char('.')): 
                tt = tt.next0_
                if ((tt.next0_ is not None and (tt.whitespaces_after_count < 4) and ((((tt.next0_.is_value("Г", None) and tt.next0_.morph.language.is_ru)) or ((tt.next0_.morph.language.is_ua and tt.next0_.is_value("Р", None)))))) and tt.next0_.next0_ is not None and tt.next0_.next0_.is_char('.')): 
                    tt = tt.next0_.next0_
                return tt
            else: 
                return tt
        return None
    
    @staticmethod
    def try_parse_list(t : 'Token', max_count : int=20) -> typing.List['DateItemToken']:
        p = DateItemToken.try_parse(t, None, False)
        if (p is None): 
            return None
        if (p.typ == DateItemToken.DateItemType.DELIM): 
            return None
        res = list()
        res.append(p)
        tt = p.end_token.next0_
        while tt is not None:
            if (isinstance(tt, TextToken)): 
                if (tt.check_value(DateItemToken.M_EMPTY_WORDS) is not None): 
                    tt = tt.next0_
                    continue
            p0 = DateItemToken.try_parse(tt, res, False)
            if (p0 is None): 
                if (tt.is_newline_before): 
                    break
                if (tt.chars.is_latin_letter): 
                    break
                mc = tt.get_morph_class_in_dictionary()
                if (((mc.is_adjective or mc.is_pronoun)) and not mc.is_verb and not mc.is_adverb): 
                    tt = tt.next0_
                    continue
                if (tt.is_value("В", None)): 
                    p0 = DateItemToken.try_parse(tt.next0_, res, False)
                    if (p0 is not None and p0.can_be_year): 
                        p0.begin_token = tt
                    else: 
                        p0 = (None)
                if (p0 is None): 
                    break
            if (tt.is_newline_before): 
                if (p.typ == DateItemToken.DateItemType.MONTH and p0.can_be_year): 
                    pass
                elif (p.typ == DateItemToken.DateItemType.NUMBER and p.can_be_day and p0.typ == DateItemToken.DateItemType.MONTH): 
                    pass
                else: 
                    break
            if (p0.can_be_year and p0.typ == DateItemToken.DateItemType.NUMBER): 
                if (p.typ == DateItemToken.DateItemType.HALFYEAR or p.typ == DateItemToken.DateItemType.QUARTAL): 
                    p0.typ = DateItemToken.DateItemType.YEAR
                elif (p.typ == DateItemToken.DateItemType.POINTER and p0.int_value > 1990): 
                    p0.typ = DateItemToken.DateItemType.YEAR
            if ((p0.typ == DateItemToken.DateItemType.MONTH and len(res) == 2 and res[0].typ == DateItemToken.DateItemType.MONTH) and res[1].typ == DateItemToken.DateItemType.DELIM and res[1].begin_token.is_comma_and): 
                del res[1]
                return res
            p = p0
            res.append(p)
            if (max_count > 0 and len(res) >= max_count): 
                break
            tt = p.end_token.next0_
        for i in range(len(res) - 1, -1, -1):
            if (res[i].typ == DateItemToken.DateItemType.DELIM): 
                del res[i]
            else: 
                break
        if (len(res) > 0 and res[len(res) - 1].typ == DateItemToken.DateItemType.NUMBER): 
            nex = NumberHelper.try_parse_number_with_postfix(res[len(res) - 1].begin_token)
            if (nex is not None and nex.ex_typ != NumberExType.HOUR): 
                if (len(res) > 3 and res[len(res) - 2].typ == DateItemToken.DateItemType.DELIM and res[len(res) - 2].string_value == ":"): 
                    pass
                elif (res[len(res) - 1].can_be_year and nex.end_token == res[len(res) - 1].end_token): 
                    pass
                else: 
                    del res[len(res) - 1]
        if (len(res) == 0): 
            return None
        i = 1
        while i < (len(res) - 1): 
            if (res[i].typ == DateItemToken.DateItemType.DELIM and res[i].begin_token.is_comma): 
                if ((i == 1 and res[i - 1].typ == DateItemToken.DateItemType.MONTH and res[i + 1].can_be_year) and (i + 1) == (len(res) - 1)): 
                    del res[i]
            i += 1
        if (res[len(res) - 1].typ == DateItemToken.DateItemType.NUMBER): 
            rr = res[len(res) - 1]
            if (rr.can_be_year and len(res) > 1 and res[len(res) - 2].typ == DateItemToken.DateItemType.MONTH): 
                pass
            else: 
                npt = NounPhraseHelper.try_parse(rr.begin_token, NounPhraseParseAttr.NO, 0, None)
                if (npt is not None and npt.end_char > rr.end_char): 
                    del res[len(res) - 1]
                    if (len(res) > 0 and res[len(res) - 1].typ == DateItemToken.DateItemType.DELIM): 
                        del res[len(res) - 1]
        if (len(res) == 0): 
            return None
        if (len(res) == 2 and not res[0].is_whitespace_after): 
            if (not res[0].is_whitespace_before and not res[1].is_whitespace_after): 
                return None
        if (len(res) == 1 and (isinstance(res[0].tag, DateItemToken.FirstLastTyp)) and (Utils.valToEnum(res[0].tag, DateItemToken.FirstLastTyp)) == DateItemToken.FirstLastTyp.LAST): 
            return None
        last = res[len(res) - 1]
        if (last.typ == DateItemToken.DateItemType.YEAR and last.int_value > 9999): 
            if ((isinstance(last.begin_token, NumberToken)) and last.begin_token.length_char == 6): 
                mon = last.begin_token.get_source_text()[0:0+2]
                if (mon[0] == '0'): 
                    mon = mon[1:]
                year_ = last.begin_token.get_source_text()[2:]
                mm = 0
                yy = 0
                wrapmm880 = RefOutArgWrapper(0)
                inoutres881 = Utils.tryParseInt(mon, wrapmm880)
                wrapyy882 = RefOutArgWrapper(0)
                inoutres883 = Utils.tryParseInt(year_, wrapyy882)
                mm = wrapmm880.value
                yy = wrapyy882.value
                if (inoutres881 and inoutres883): 
                    if ((mm >= 1 and mm <= 12 and yy >= 1960) and yy <= 2099): 
                        res.insert(len(res) - 1, DateItemToken._new829(last.begin_token, last.begin_token, DateItemToken.DateItemType.MONTH, mm))
                        last.int_value = yy
                        if (len(res) == 4 and res[0].can_be_day and res[1].typ == DateItemToken.DateItemType.DELIM): 
                            res.insert(3, res[1])
        return res
    
    @staticmethod
    def _new826(_arg1 : 'Token', _arg2 : 'Token', _arg3 : 'DateItemType', _arg4 : 'FirstLastTyp', _arg5 : int) -> 'DateItemToken':
        res = DateItemToken(_arg1, _arg2)
        res.typ = _arg3
        res.ltyp = _arg4
        res.int_value = _arg5
        return res
    
    @staticmethod
    def _new827(_arg1 : 'Token', _arg2 : 'Token', _arg3 : 'DateItemType', _arg4 : 'DatePointerType') -> 'DateItemToken':
        res = DateItemToken(_arg1, _arg2)
        res.typ = _arg3
        res.ptr = _arg4
        return res
    
    @staticmethod
    def _new828(_arg1 : 'Token', _arg2 : 'Token', _arg3 : 'DateItemType', _arg4 : int, _arg5 : 'MorphCollection') -> 'DateItemToken':
        res = DateItemToken(_arg1, _arg2)
        res.typ = _arg3
        res.int_value = _arg4
        res.morph = _arg5
        return res
    
    @staticmethod
    def _new829(_arg1 : 'Token', _arg2 : 'Token', _arg3 : 'DateItemType', _arg4 : int) -> 'DateItemToken':
        res = DateItemToken(_arg1, _arg2)
        res.typ = _arg3
        res.int_value = _arg4
        return res
    
    @staticmethod
    def _new835(_arg1 : 'Token', _arg2 : 'Token', _arg3 : 'DateItemType', _arg4 : int, _arg5 : int) -> 'DateItemToken':
        res = DateItemToken(_arg1, _arg2)
        res.typ = _arg3
        res.int_value = _arg4
        res.new_age = _arg5
        return res
    
    @staticmethod
    def _new837(_arg1 : 'Token', _arg2 : 'Token', _arg3 : 'DateItemType', _arg4 : 'DatePointerType', _arg5 : str) -> 'DateItemToken':
        res = DateItemToken(_arg1, _arg2)
        res.typ = _arg3
        res.ptr = _arg4
        res.string_value = _arg5
        return res
    
    @staticmethod
    def _new849(_arg1 : 'Token', _arg2 : 'Token', _arg3 : 'DateItemType', _arg4 : int, _arg5 : object) -> 'DateItemToken':
        res = DateItemToken(_arg1, _arg2)
        res.typ = _arg3
        res.int_value = _arg4
        res.tag = _arg5
        return res
    
    @staticmethod
    def _new852(_arg1 : 'Token', _arg2 : 'Token', _arg3 : 'DateItemType', _arg4 : int, _arg5 : bool) -> 'DateItemToken':
        res = DateItemToken(_arg1, _arg2)
        res.typ = _arg3
        res.int_value = _arg4
        res.relate = _arg5
        return res
    
    @staticmethod
    def _new853(_arg1 : 'Token', _arg2 : 'Token', _arg3 : 'DateItemType', _arg4 : str) -> 'DateItemToken':
        res = DateItemToken(_arg1, _arg2)
        res.typ = _arg3
        res.string_value = _arg4
        return res
    
    @staticmethod
    def _new856(_arg1 : 'Token', _arg2 : 'Token', _arg3 : 'DateItemType', _arg4 : int, _arg5 : 'MorphLang') -> 'DateItemToken':
        res = DateItemToken(_arg1, _arg2)
        res.typ = _arg3
        res.int_value = _arg4
        res.lang = _arg5
        return res
    
    @staticmethod
    def _new1008(_arg1 : 'Token', _arg2 : 'Token', _arg3 : int) -> 'DateItemToken':
        res = DateItemToken(_arg1, _arg2)
        res.int_value = _arg3
        return res