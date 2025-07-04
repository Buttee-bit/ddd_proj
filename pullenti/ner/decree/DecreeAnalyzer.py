﻿# SDK Pullenti Lingvo, version 4.30, june 2025. Copyright (c) 2013-2025, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

import typing
import datetime
from pullenti.unisharp.Utils import Utils
from pullenti.unisharp.Misc import RefOutArgWrapper

from pullenti.morph.MorphGender import MorphGender
from pullenti.morph.MorphNumber import MorphNumber
from pullenti.ner.core.TerminParseAttr import TerminParseAttr
from pullenti.ner.core.Termin import Termin
from pullenti.morph.MorphClass import MorphClass
from pullenti.ner.decree.internal.DecreeChangeTokenTyp import DecreeChangeTokenTyp
from pullenti.ner.core.NounPhraseParseAttr import NounPhraseParseAttr
from pullenti.ner.NumberToken import NumberToken
from pullenti.ner.core.NounPhraseHelper import NounPhraseHelper
from pullenti.ner.ProcessorService import ProcessorService
from pullenti.ner.core.TerminCollection import TerminCollection
from pullenti.ner.Slot import Slot
from pullenti.ner.SourceOfAnalysis import SourceOfAnalysis
from pullenti.ner.core.ComplexNumToken import ComplexNumToken
from pullenti.ner.decree.internal.MetaDecreeChangeValue import MetaDecreeChangeValue
from pullenti.ner.decree.internal.MetaDecree import MetaDecree
from pullenti.ner.person.PersonReferent import PersonReferent
from pullenti.ner.core.internal.PullentiNerCoreInternalResourceHelper import PullentiNerCoreInternalResourceHelper
from pullenti.ner.decree.DecreeChangeKind import DecreeChangeKind
from pullenti.morph.LanguageHelper import LanguageHelper
from pullenti.ner.MetaToken import MetaToken
from pullenti.ner.core.BracketParseAttr import BracketParseAttr
from pullenti.ner.decree.internal.MetaDecreeChange import MetaDecreeChange
from pullenti.ner.decree.DecreeKind import DecreeKind
from pullenti.ner.Token import Token
from pullenti.ner.core.ReferentsEqualType import ReferentsEqualType
from pullenti.ner.ReferentToken import ReferentToken
from pullenti.ner.Referent import Referent
from pullenti.ner.TextToken import TextToken
from pullenti.ner.core.MiscHelper import MiscHelper
from pullenti.ner.date.DateReferent import DateReferent
from pullenti.ner.geo.GeoReferent import GeoReferent
from pullenti.ner.Analyzer import Analyzer
from pullenti.ner.core.BracketHelper import BracketHelper
from pullenti.ner.person.PersonPropertyReferent import PersonPropertyReferent
from pullenti.ner.core.GetTextAttr import GetTextAttr
from pullenti.ner.date.DateRangeReferent import DateRangeReferent
from pullenti.ner.org.OrganizationReferent import OrganizationReferent

class DecreeAnalyzer(Analyzer):
    """ Анализатор ссылок на НПА """
    
    class ThisDecree(MetaToken):
        
        def __init__(self, b : 'Token', e0_ : 'Token') -> None:
            super().__init__(b, e0_, None)
            self.typ = None;
            self.has_this_ref = False
            self.has_other_ref = False
            self.real = None;
        
        def __str__(self) -> str:
            return "{0} ({1})".format(Utils.ifNotNull(self.typ, "?"), ("This" if self.has_this_ref else (("Other" if self.has_other_ref else "?"))))
        
        def check_decree(self, r : 'DecreeReferent') -> bool:
            from pullenti.ner.SourceOfAnalysis import SourceOfAnalysis
            from pullenti.ner.decree.DecreeKind import DecreeKind
            from pullenti.ner.ProcessorService import ProcessorService
            from pullenti.ner.decree.DecreeReferent import DecreeReferent
            if (r is None): 
                return False
            if (self.real == r): 
                return True
            if (self.typ is not None): 
                if (r.typ == self.typ or r.typ0 == self.typ): 
                    return True
                if (r.kind == DecreeKind.KODEX and self.typ == "КОДЕКС"): 
                    return True
                for s in r.slots: 
                    if (s.type_name == DecreeReferent.ATTR_NAME): 
                        n = Utils.asObjectOrNull(s.value, str)
                        if (Utils.startsWithString(n, self.typ, True)): 
                            return True
                        arr = ProcessorService.get_empty_processor().process(SourceOfAnalysis(n), None, None)
                        if (arr is not None and arr.first_token is not None): 
                            if (arr.first_token.is_value(self.typ, None)): 
                                return True
                            if (arr.first_token.next0_ is not None): 
                                if (arr.first_token.next0_.is_value(self.typ, None)): 
                                    return True
            return False
        
        @staticmethod
        def try_attach_back(t : 'Token', base_typ : 'DecreeToken') -> 'ThisDecree':
            from pullenti.ner.TextToken import TextToken
            from pullenti.ner.decree.internal.DecreeToken import DecreeToken
            if (t is None): 
                return None
            ukaz = None
            tt = t
            first_pass3942 = True
            while True:
                if first_pass3942: first_pass3942 = False
                else: tt = tt.previous
                if (not (tt is not None)): break
                if (tt.is_char_of(",") or tt.morph.class0_.is_preposition or tt.morph.class0_.is_conjunction): 
                    continue
                if ((((((tt.is_value("ОПРЕДЕЛЕННЫЙ", "ПЕВНИЙ") or tt.is_value("ЗАДАННЫЙ", "ЗАДАНИЙ") or tt.is_value("ПРЕДУСМОТРЕННЫЙ", "ПЕРЕДБАЧЕНИЙ")) or tt.is_value("УКАЗАННЫЙ", "ЗАЗНАЧЕНИЙ") or tt.is_value("ПЕРЕЧИСЛЕННЫЙ", "ПЕРЕРАХОВАНИЙ")) or tt.is_value("ОПРЕДЕЛИТЬ", "ВИЗНАЧИТИ") or tt.is_value("ОПРЕДЕЛЯТЬ", None)) or tt.is_value("ЗАДАВАТЬ", "ЗАДАВАТИ") or tt.is_value("ПРЕДУСМАТРИВАТЬ", "ПЕРЕДБАЧАТИ")) or tt.is_value("УКАЗЫВАТЬ", "ВКАЗУВАТИ") or tt.is_value("УКАЗАТЬ", "ВКАЗАТИ")) or tt.is_value("СИЛА", "ЧИННІСТЬ")): 
                    ukaz = tt
                    continue
                if (tt == t): 
                    continue
                ttt = DecreeToken.is_keyword(tt, False)
                if (tt != ttt or not (isinstance(tt, TextToken))): 
                    break
                if (ttt.is_value("УСЛОВИЕ", None) or ttt.is_value("ПОЛОЖЕНИЕ", None) or ttt.is_value("ОПРЕДЕЛЕНИЕ", None)): 
                    continue
                if (ttt.is_value("ПОРЯДОК", None) and ukaz is not None): 
                    return None
                res = DecreeAnalyzer.ThisDecree(tt, tt)
                res.typ = tt.lemma
                t = tt.previous
                if (t is not None and ((t.morph.class0_.is_adjective or t.morph.class0_.is_pronoun))): 
                    if (t.is_value("НАСТОЯЩИЙ", "СПРАВЖНІЙ") or t.is_value("ТЕКУЩИЙ", "ПОТОЧНИЙ") or t.is_value("ДАННЫЙ", "ДАНИЙ")): 
                        res.has_this_ref = True
                        res.begin_token = t
                    elif ((t.is_value("ЭТОТ", "ЦЕЙ") or t.is_value("ВЫШЕУКАЗАННЫЙ", "ВИЩЕВКАЗАНИЙ") or t.is_value("УКАЗАННЫЙ", "ЗАЗНАЧЕНИЙ")) or t.is_value("НАЗВАННЫЙ", "НАЗВАНИЙ")): 
                        res.has_other_ref = True
                        res.begin_token = t
                if (not res.has_this_ref and tt.is_newline_after): 
                    return None
                if (base_typ is not None and base_typ.value == res.typ): 
                    res.has_this_ref = True
                return res
            if (ukaz is not None): 
                if (base_typ is not None and base_typ.value is not None and (("ДОГОВОР" in base_typ.value or "ДОГОВІР" in base_typ.value))): 
                    return DecreeAnalyzer.ThisDecree._new1416(ukaz, ukaz, True, base_typ.value)
            return None
        
        @staticmethod
        def try_attach(dtok : 'PartToken', base_typ : 'DecreeToken') -> 'ThisDecree':
            from pullenti.ner.core.NounPhraseParseAttr import NounPhraseParseAttr
            from pullenti.ner.core.NounPhraseHelper import NounPhraseHelper
            from pullenti.morph.MorphGender import MorphGender
            from pullenti.morph.MorphNumber import MorphNumber
            from pullenti.ner.ReferentToken import ReferentToken
            from pullenti.ner.decree.DecreeReferent import DecreeReferent
            from pullenti.ner.TextToken import TextToken
            from pullenti.ner.core.BracketHelper import BracketHelper
            from pullenti.ner.decree.internal.DecreeToken import DecreeToken
            t = dtok.end_token.next0_
            if (t is None): 
                return None
            if (t.is_newline_before): 
                if (t.chars.is_cyrillic_letter and t.chars.is_all_lower): 
                    pass
                else: 
                    return None
            t0 = t
            if (t.is_char('.') and t.next0_ is not None and not t.is_newline_after): 
                if (dtok.is_newline_before): 
                    return None
                t = t.next0_
            if (t.is_value("К", None) and t.next0_ is not None): 
                t = t.next0_
            if (t is not None and (isinstance(t.get_referent(), DecreeReferent))): 
                return None
            if (t.is_value("НОВЫЙ", None)): 
                return None
            tt = DecreeToken.is_keyword(t, False)
            br = False
            if (tt is None and BracketHelper.can_be_start_of_sequence(t, True, False)): 
                tt = DecreeToken.is_keyword(t.next0_, False)
                if ((isinstance(tt, TextToken)) and BracketHelper.can_be_end_of_sequence(tt.next0_, False, None, False)): 
                    br = True
                else: 
                    tt = (None)
            if (not (isinstance(tt, TextToken))): 
                if ((isinstance(tt, ReferentToken)) and (isinstance(tt.get_referent(), DecreeReferent))): 
                    return DecreeAnalyzer.ThisDecree._new1417(t, tt, Utils.asObjectOrNull(tt.get_referent(), DecreeReferent))
                return None
            if (tt.chars.is_all_lower): 
                if (DecreeToken.is_keyword(tt, True) is not None): 
                    if (tt != t and t.chars.is_capital_upper): 
                        pass
                    else: 
                        return None
            if (not (isinstance(t, TextToken))): 
                return None
            res = DecreeAnalyzer.ThisDecree(t0, (tt.next0_ if br else tt))
            res.typ = tt.lemma
            if (isinstance(tt.previous, TextToken)): 
                tt1 = tt.previous
                mc = tt1.get_morph_class_in_dictionary()
                if (mc.is_adjective and not mc.is_verb and not tt1.is_value("НАСТОЯЩИЙ", "СПРАВЖНІЙ")): 
                    nnn = NounPhraseHelper.try_parse(tt1, NounPhraseParseAttr.NO, 0, None)
                    if (nnn is not None): 
                        res.typ = nnn.get_normal_case_text(None, MorphNumber.UNDEFINED, MorphGender.UNDEFINED, False)
                    if (isinstance(tt1.previous, TextToken)): 
                        tt1 = tt1.previous
                        mc = tt1.get_morph_class_in_dictionary()
                        if (mc.is_adjective and not mc.is_verb and not tt1.is_value("НАСТОЯЩИЙ", "СПРАВЖНІЙ")): 
                            nnn = NounPhraseHelper.try_parse(tt1, NounPhraseParseAttr.NO, 0, None)
                            if (nnn is not None): 
                                res.typ = nnn.get_normal_case_text(None, MorphNumber.UNDEFINED, MorphGender.UNDEFINED, False)
            if (tt.is_char('.') and (isinstance(tt.previous, TextToken))): 
                res.typ = tt.previous.lemma
            if (t.morph.class0_.is_adjective or t.morph.class0_.is_pronoun): 
                if (t.is_value("НАСТОЯЩИЙ", "СПРАВЖНІЙ") or t.is_value("ТЕКУЩИЙ", "ПОТОЧНИЙ") or t.is_value("ДАННЫЙ", "ДАНИЙ")): 
                    res.has_this_ref = True
                elif ((t.is_value("ЭТОТ", "ЦЕЙ") or t.is_value("ВЫШЕУКАЗАННЫЙ", "ВИЩЕВКАЗАНИЙ") or t.is_value("УКАЗАННЫЙ", "ЗАЗНАЧЕНИЙ")) or t.is_value("НАЗВАННЫЙ", "НАЗВАНИЙ")): 
                    res.has_other_ref = True
            if (not tt.is_newline_after and not res.has_this_ref): 
                dt = DecreeToken.try_attach(tt.next0_, None, False)
                if (dt is not None and dt.typ != DecreeToken.ItemType.MISC): 
                    if (dt.typ != DecreeToken.ItemType.NAME): 
                        return None
            if (base_typ is not None and base_typ.value == res.typ): 
                res.has_this_ref = True
            return res
        
        @staticmethod
        def _new1416(_arg1 : 'Token', _arg2 : 'Token', _arg3 : bool, _arg4 : str) -> 'ThisDecree':
            res = DecreeAnalyzer.ThisDecree(_arg1, _arg2)
            res.has_this_ref = _arg3
            res.typ = _arg4
            return res
        
        @staticmethod
        def _new1417(_arg1 : 'Token', _arg2 : 'Token', _arg3 : 'DecreeReferent') -> 'ThisDecree':
            res = DecreeAnalyzer.ThisDecree(_arg1, _arg2)
            res.real = _arg3
            return res
    
    @staticmethod
    def _try_attach(dts : typing.List['DecreeToken'], base_typ : 'DecreeToken', ad : 'AnalyzerData') -> typing.List['ReferentToken']:
        from pullenti.ner.decree.DecreeReferent import DecreeReferent
        from pullenti.ner.decree.internal.DecreeToken import DecreeToken
        if (ad is None): 
            ad = DecreeAnalyzer.get_data(dts[0])
        if (ad.level > 2): 
            return None
        ad.level += 1
        res = DecreeAnalyzer.__try_attach(dts, base_typ, False, ad)
        if (res is None and ((len(dts) == 1 or ((len(dts) == 2 and dts[1].typ == DecreeToken.ItemType.ORG)))) and dts[0].typ_ref_back): 
            t = dts[0].begin_token.previous
            first_pass3943 = True
            while True:
                if first_pass3943: first_pass3943 = False
                else: t = t.previous
                if (not (t is not None)): break
                dr = Utils.asObjectOrNull(t.get_referent(), DecreeReferent)
                if (dr is None): 
                    continue
                if (isinstance(t.tag, str)): 
                    if ((Utils.asObjectOrNull(t.tag, str)) == "ignored"): 
                        continue
                if (dr.check_typename(dts[0].value)): 
                    pass
                elif (dr.owner is not None and dr.owner.check_typename(dts[0].value)): 
                    dr = dr.owner
                else: 
                    continue
                if (len(dts) == 2 and dts[1].ref is not None): 
                    org0_ = Utils.asObjectOrNull(dr.get_slot_value(DecreeReferent.ATTR_SOURCE), Referent)
                    if (org0_ is not None): 
                        if (not org0_.can_be_equals(dts[1].ref.referent, ReferentsEqualType.WITHINONETEXT)): 
                            continue
                res = list()
                res.append(ReferentToken(dr, dts[0].begin_token, dts[len(dts) - 1].end_token))
                break
        ad.level -= 1
        return res
    
    @staticmethod
    def __try_attach(dts : typing.List['DecreeToken'], base_typ : 'DecreeToken', after_decree : bool, ad : 'AnalyzerData') -> typing.List['ReferentToken']:
        from pullenti.ner.decree.DecreePartReferent import DecreePartReferent
        from pullenti.ner.decree.DecreeReferent import DecreeReferent
        from pullenti.ner.decree.internal.PartToken import PartToken
        from pullenti.ner.decree.internal.DecreeToken import DecreeToken
        if (dts is None or (len(dts) < 1)): 
            return None
        if (dts[0].typ == DecreeToken.ItemType.EDITION and len(dts) > 1): 
            del dts[0]
        if (len(dts) == 2 and dts[0].typ == DecreeToken.ItemType.ORG and dts[1].typ == DecreeToken.ItemType.TYP): 
            return None
        if (len(dts) == 2 and dts[0].typ == DecreeToken.ItemType.TYP and dts[1].typ == DecreeToken.ItemType.NUMBER): 
            if ((dts[0].length_char < 3) and not dts[0].is_whitespace_after and dts[0].is_doubtful): 
                return None
            if (dts[0].is_newline_after): 
                return None
        if (len(dts) == 1): 
            if (dts[0].typ == DecreeToken.ItemType.DECREEREF and dts[0].ref is not None): 
                if (base_typ is not None): 
                    re = dts[0].ref.get_referent()
                    dre = Utils.asObjectOrNull(re, DecreeReferent)
                    if (dre is None and (isinstance(re, DecreePartReferent))): 
                        dre = re.owner
                    if (dre is not None): 
                        if (not dre.check_typename(base_typ.value)): 
                            return None
                reli = list()
                reli.append(ReferentToken(dts[0].ref.referent, dts[0].begin_token, dts[0].end_token))
                return reli
        dec0 = None
        kodeks = False
        canbesingle = False
        max_empty = 30
        t = dts[0].begin_token.previous
        first_pass3944 = True
        while True:
            if first_pass3944: first_pass3944 = False
            else: t = t.previous
            if (not (t is not None)): break
            if (t.is_comma_and): 
                continue
            if (t.is_char(')')): 
                cou = 0
                t = t.previous
                while t is not None: 
                    if (t.is_char('(')): 
                        break
                    else: 
                        cou += 1
                        if (cou > 200): 
                            break
                    t = t.previous
                if (t is not None and t.is_char('(')): 
                    continue
                break
            max_empty -= 1
            if (max_empty < 0): 
                break
            if (not t.chars.is_letter): 
                continue
            dec0 = (Utils.asObjectOrNull(t.get_referent(), DecreeReferent))
            if (dec0 is not None): 
                if (DecreeToken.get_kind(dec0.typ, None) == DecreeKind.KODEX): 
                    kodeks = True
                elif (dec0.kind == DecreeKind.PUBLISHER): 
                    dec0 = (None)
            break
        dec = DecreeReferent()
        i = 0
        morph_ = None
        is_noun_doubt = False
        num_tok = None
        typ_tok = None
        i = 0
        first_pass3945 = True
        while True:
            if first_pass3945: first_pass3945 = False
            else: i += 1
            if (not (i < len(dts))): break
            if (dts[i].typ == DecreeToken.ItemType.TYP): 
                if (dts[i].value is None): 
                    break
                if (dts[i].is_newline_before): 
                    if (dec.date is not None or dec.number is not None): 
                        break
                if (dec.typ is not None): 
                    if (((dec.typ == "РЕШЕНИЕ" or dec.typ == "РІШЕННЯ")) and dts[i].value == "ПРОТОКОЛ"): 
                        pass
                    elif (((dec.typ == dts[i].value or dts[i].value == "ТЕХНИЧЕСКИЙ РЕГЛАМЕНТ")) and dec.typ == "ГОСТ"): 
                        if (((i + 1) < len(dts)) and dts[i + 1].typ == DecreeToken.ItemType.NUMBER): 
                            if (dec.number is not None): 
                                break
                            if (i > 0 and dts[i - 1].typ == DecreeToken.ItemType.NUMBER): 
                                break
                        continue
                    elif (dts[i].value == dec.typ): 
                        if ((i + 1) >= len(dts) or dts[i + 1].typ == DecreeToken.ItemType.NAME): 
                            continue
                        elif ((((i + 1) < len(dts)) and dts[i + 1].typ == DecreeToken.ItemType.NUMBER and dts[i - 1].typ == DecreeToken.ItemType.NAME) and dec.number is None): 
                            pass
                        else: 
                            break
                    else: 
                        break
                ki = DecreeToken.get_kind(dts[i].value, None)
                if (ki == DecreeKind.STANDARD): 
                    if (i > 0): 
                        if (len(dts) == 2 and dts[0].typ == DecreeToken.ItemType.NUMBER and dts[i].value == "ТЕХНИЧЕСКИЕ УСЛОВИЯ"): 
                            pass
                        else: 
                            return None
                if (ki == DecreeKind.KODEX): 
                    if (i > 0): 
                        break
                    if (dts[i].value != "ОСНОВЫ ЗАКОНОДАТЕЛЬСТВА" and dts[i].value != "ОСНОВИ ЗАКОНОДАВСТВА"): 
                        kodeks = True
                    else: 
                        kodeks = False
                else: 
                    kodeks = False
                morph_ = dts[i].morph
                dec.add_typ(dts[i])
                if (typ_tok is None): 
                    typ_tok = dts[i]
                if (dts[i].can_be_single_decree): 
                    canbesingle = True
                if (dts[i].full_value is not None): 
                    dec._add_name_str(dts[i].full_value, dts[i])
                is_noun_doubt = dts[i].is_doubtful
                if (is_noun_doubt and i == 0): 
                    if (PartToken.is_part_before(dts[i].begin_token)): 
                        is_noun_doubt = False
                if (dts[i].ref is not None): 
                    if (dec.find_slot(DecreeReferent.ATTR_GEO, None, True) is None): 
                        ss = dec.add_slot(DecreeReferent.ATTR_GEO, dts[i].ref.referent, False, 0)
                        ss.add_annotation(dts[i].ref)
                        dec.add_ext_referent(dts[i].ref)
                if (dts[i].src_ref is not None): 
                    ss = dec.add_slot(DecreeReferent.ATTR_SOURCE, dts[i].src_ref, False, 0)
                    ss.add_annotation(dts[i])
            elif (dts[i].typ == DecreeToken.ItemType.DATE): 
                if (dec.date is not None): 
                    break
                if (kodeks): 
                    if (i > 0 and dts[i - 1].typ == DecreeToken.ItemType.NUMBER): 
                        pass
                    elif (((i + 1) < len(dts)) and dts[i + 1].typ == DecreeToken.ItemType.NUMBER): 
                        pass
                    else: 
                        break
                if (i == (len(dts) - 1)): 
                    if (not dts[i].begin_token.is_value("ОТ", "ВІД")): 
                        ty = DecreeToken.get_kind(dec.typ, None)
                        if ((ty == DecreeKind.KONVENTION or ty == DecreeKind.CONTRACT or ty == DecreeKind.LICENSE) or dec.typ0 == "ПИСЬМО" or dec.typ0 == "ЛИСТ"): 
                            pass
                        else: 
                            break
                dec.add_date(dts[i])
                dec.add_ext_referent(dts[i].ref)
            elif (dts[i].typ == DecreeToken.ItemType.DATERANGE): 
                if (dec.kind != DecreeKind.PROGRAM): 
                    break
                dec.add_date(dts[i])
                dec.add_ext_referent(dts[i].ref)
            elif (dts[i].typ == DecreeToken.ItemType.EDITION): 
                if (dts[i].is_newline_before and not dts[i].begin_token.chars.is_all_lower and not dts[i].begin_token.is_char('(')): 
                    break
                if (((i + 2) < len(dts)) and dts[i + 1].typ == DecreeToken.ItemType.TYP): 
                    break
            elif (dts[i].typ == DecreeToken.ItemType.NUMBER): 
                if (kodeks): 
                    if (((i + 1) < len(dts)) and dts[i + 1].typ == DecreeToken.ItemType.DATE): 
                        pass
                    elif (i > 0 and dts[i - 1].typ == DecreeToken.ItemType.DATE): 
                        pass
                    else: 
                        break
                num_tok = dts[i]
                if (dts[i].is_delo): 
                    if (dec.case_number is not None): 
                        break
                    ss = dec.add_slot(DecreeReferent.ATTR_CASENUMBER, dts[i].value, True, 0)
                    ss.add_annotation(dts[i])
                    continue
                if (dec.number is not None): 
                    if (i > 2 and ((dts[i - 1].typ == DecreeToken.ItemType.OWNER or dts[i - 1].typ == DecreeToken.ItemType.ORG)) and dts[i - 2].typ == DecreeToken.ItemType.NUMBER): 
                        pass
                    else: 
                        break
                if (dts[i].is_newline_before): 
                    if (dec.typ is None and dec0 is None): 
                        break
                if (LanguageHelper.ends_with(dts[i].value, "ФЗ")): 
                    dec.typ = "ФЕДЕРАЛЬНЫЙ ЗАКОН"
                if (LanguageHelper.ends_with(dts[i].value, "ФКЗ")): 
                    dec.typ = "ФЕДЕРАЛЬНЫЙ КОНСТИТУЦИОННЫЙ ЗАКОН"
                if (dts[i].value is not None and Utils.startsWithString(dts[i].value, "ПР", True) and dec.typ is None): 
                    dec.typ = "ПОРУЧЕНИЕ"
                if (dec.typ is None): 
                    if (dec0 is None and not after_decree and base_typ is None): 
                        break
                dec.add_number(dts[i])
                if (dts[i].children is not None): 
                    cou = 0
                    for s in dec.slots: 
                        if (s.type_name == DecreeReferent.ATTR_SOURCE): 
                            cou += 1
                    if (cou == (len(dts[i].children) + 1)): 
                        for dd in dts[i].children: 
                            dec.add_number(dd)
                        dts[i].children = (None)
                continue
            elif (dts[i].typ == DecreeToken.ItemType.NAME): 
                if (dec.typ is None and dec.number is None and dec0 is None): 
                    if (dts[i].typ_kind == DecreeKind.CLASSIFIER or dts[i].typ_kind == DecreeKind.STANDARD): 
                        pass
                    elif ((i == 0 and ((i + 1) < len(dts)) and dts[i + 1].typ == DecreeToken.ItemType.TYP) and (dts[i + 1].whitespaces_before_count < 3)): 
                        pass
                    else: 
                        break
                if (dec.get_string_value(DecreeReferent.ATTR_NAME) is not None): 
                    if (kodeks): 
                        break
                    if (i > 0 and dts[i - 1].end_token.next0_ == dts[i].begin_token): 
                        pass
                    elif (dts[i].typ_kind == DecreeKind.CLASSIFIER): 
                        pass
                    else: 
                        break
                tt0 = dts[i].begin_token
                tt1 = dts[i].end_token
                if ((i > 0 and dts[i - 1].is_newline_after and ((i + 1) < len(dts))) and dts[i + 1].typ == DecreeToken.ItemType.TYP and (dts[i + 1].whitespaces_before_count < 3)): 
                    break
                if (BracketHelper.can_be_start_of_sequence(tt0, True, False) and BracketHelper.can_be_end_of_sequence(tt1, True, tt0, False)): 
                    tt0 = tt0.next0_
                    tt1 = tt1.previous
                    tt = tt0
                    while tt is not None and (tt.end_char < tt1.end_char): 
                        if (BracketHelper.can_be_start_of_sequence(tt, True, False)): 
                            br1 = BracketHelper.try_parse(tt, BracketParseAttr.NO, 100)
                            if (br1 is not None and br1.end_token == dts[i].end_token): 
                                tt1 = tt1.next0_
                                break
                        tt = tt.next0_
                nam = MiscHelper.get_text_value(tt0, tt1, GetTextAttr.RESTOREREGISTER)
                if (kodeks and not "КОДЕКС" in nam.upper()): 
                    nam = ("Кодекс " + nam)
                if (dts[i].full_value is not None): 
                    dec._add_name_str(dts[i].full_value, dts[i])
                dec._add_name_str(nam, MetaToken(tt0, tt1))
            elif (dts[i].typ == DecreeToken.ItemType.BETWEEN): 
                if (dec.kind != DecreeKind.CONTRACT): 
                    break
                for chh in dts[i].children: 
                    ss = dec.add_slot(DecreeReferent.ATTR_SOURCE, chh.ref.referent, False, 0)
                    ss.tag = chh.get_source_text()
                    ss.add_annotation(chh)
                    if (isinstance(chh.ref.referent, PersonPropertyReferent)): 
                        dec.add_ext_referent(chh.ref)
            elif (dts[i].typ == DecreeToken.ItemType.OWNER): 
                if (kodeks): 
                    break
                if (dec.name is not None): 
                    break
                if (((i == 0 or i == (len(dts) - 1))) and dts[i].begin_token.chars.is_all_lower): 
                    break
                if (i == 0 and len(dts) > 1 and dts[1].typ == DecreeToken.ItemType.TYP): 
                    break
                if (dec.find_slot(DecreeReferent.ATTR_SOURCE, None, True) is not None): 
                    pass
                if (dts[i].ref is not None): 
                    ty = DecreeToken.get_kind(dec.typ, None)
                    if (ty == DecreeKind.USTAV): 
                        if (not (isinstance(dts[i].ref.referent, OrganizationReferent))): 
                            break
                    ss = dec.add_slot(DecreeReferent.ATTR_SOURCE, dts[i].ref.referent, False, 0)
                    ss.tag = dts[i].get_source_text()
                    ss.add_annotation(dts[i])
                    if (isinstance(dts[i].ref.referent, PersonPropertyReferent)): 
                        dec.add_ext_referent(dts[i].ref)
                else: 
                    ss = dec.add_slot(DecreeReferent.ATTR_SOURCE, MiscHelper.convert_first_char_upper_and_other_lower(dts[i].value), False, 0)
                    ss.tag = dts[i].get_source_text()
                    ss.add_annotation(dts[i])
            elif (dts[i].typ == DecreeToken.ItemType.ORG): 
                if (kodeks): 
                    if (i != 1 or dts[i].whitespaces_before_count > 3): 
                        break
                    if (len(dts) == 2 or ((len(dts) == 3 and dts[2].typ == DecreeToken.ItemType.MISC))): 
                        pass
                    else: 
                        break
                    is_noun_doubt = False
                elif (dec.name is not None): 
                    break
                if (dec.find_slot(DecreeReferent.ATTR_SOURCE, None, True) is not None): 
                    if (i > 2 and dts[i - 1].typ == DecreeToken.ItemType.NUMBER and ((dts[i - 2].typ == DecreeToken.ItemType.ORG or dts[i - 2].typ == DecreeToken.ItemType.OWNER))): 
                        pass
                    elif (dts[i].begin_token.previous is not None and dts[i].begin_token.previous.is_and): 
                        pass
                    elif (i > 0 and ((dts[i - 1].typ == DecreeToken.ItemType.OWNER or dts[i - 1].typ == DecreeToken.ItemType.ORG))): 
                        pass
                    elif (i > 0 and dts[i - 1].typ == DecreeToken.ItemType.TYP and dts[i - 1].src_ref == dec.get_slot_value(DecreeReferent.ATTR_SOURCE)): 
                        pass
                    else: 
                        break
                ttt = Utils.asObjectOrNull(dts[i].begin_token, ReferentToken)
                if (ttt is not None and ttt == dts[i].end_token and ttt.begin_token != ttt.end_token): 
                    if ((isinstance(ttt.begin_token.get_referent(), OrganizationReferent)) and ttt.begin_token.next0_.is_comma): 
                        sl1 = dec.add_slot(DecreeReferent.ATTR_SOURCE, ttt.begin_token.get_referent(), False, 0)
                        sl1.tag = ttt.begin_token.get_source_text()
                        sl1.add_annotation(Utils.asObjectOrNull(ttt.begin_token, ReferentToken))
                sl = dec.add_slot(DecreeReferent.ATTR_SOURCE, dts[i].ref.referent, False, 0)
                sl.tag = dts[i].get_source_text()
                sl.add_annotation(dts[i])
                if (((i + 2) < len(dts)) and dts[i + 1].typ == DecreeToken.ItemType.UNKNOWN and (dts[i + 1].whitespaces_before_count < 2)): 
                    if (dts[i + 2].typ == DecreeToken.ItemType.NUMBER or dts[i + 2].typ == DecreeToken.ItemType.DATE): 
                        sl.tag = (MetaToken(dts[i].begin_token, dts[i + 1].end_token)).get_source_text()
                        i += 1
            elif (dts[i].typ == DecreeToken.ItemType.TERR): 
                if (dec.find_slot(DecreeReferent.ATTR_GEO, None, True) is not None): 
                    break
                if (i > 0 and dts[i - 1].typ == DecreeToken.ItemType.NAME): 
                    break
                if (dts[i].is_newline_before and ((i + 1) < len(dts)) and dts[i + 1].typ == DecreeToken.ItemType.DATE): 
                    break
                ss = dec.add_slot(DecreeReferent.ATTR_GEO, dts[i].ref.referent, False, 0)
                ss.add_annotation(dts[i])
            elif (dts[i].typ == DecreeToken.ItemType.UNKNOWN): 
                if (dec.find_slot(DecreeReferent.ATTR_SOURCE, None, True) is not None): 
                    break
                if (kodeks): 
                    break
                if ((dec.kind == DecreeKind.CONTRACT and i == 1 and ((i + 1) < len(dts))) and dts[i + 1].typ == DecreeToken.ItemType.NUMBER): 
                    dec._add_name_str(MiscHelper.get_text_value_of_meta_token(dts[i], GetTextAttr.KEEPREGISTER), dts[i])
                    continue
                if (i == 0): 
                    if (dec0 is None and not after_decree): 
                        break
                    ok1 = False
                    if (((i + 1) < len(dts)) and dts[i + 1].typ == DecreeToken.ItemType.NUMBER): 
                        ok1 = True
                    elif (((i + 2) < len(dts)) and dts[i + 1].typ == DecreeToken.ItemType.TERR and dts[i + 2].typ == DecreeToken.ItemType.NUMBER): 
                        ok1 = True
                    if (not ok1): 
                        break
                elif (dts[i - 1].typ == DecreeToken.ItemType.OWNER or dts[i - 1].typ == DecreeToken.ItemType.ORG): 
                    continue
                if ((i + 1) >= len(dts)): 
                    break
                if (dts[0].typ == DecreeToken.ItemType.TYP and dts[0].is_doubtful): 
                    break
                if (dts[i + 1].typ == DecreeToken.ItemType.NUMBER or dts[i + 1].typ == DecreeToken.ItemType.DATE or dts[i + 1].typ == DecreeToken.ItemType.NAME): 
                    ss = dec.add_slot(DecreeReferent.ATTR_SOURCE, dts[i].value, False, 0)
                    ss.tag = dts[i].get_source_text()
                    ss.add_annotation(dts[i])
                    continue
                if (dts[i + 1].typ == DecreeToken.ItemType.TERR): 
                    ss = dec.add_slot(DecreeReferent.ATTR_SOURCE, dts[i].value, False, 0)
                    ss.tag = dts[i].get_source_text()
                    ss.add_annotation(dts[i])
                    continue
                if (dts[i + 1].typ == DecreeToken.ItemType.OWNER): 
                    s = MiscHelper.get_text_value(dts[i].begin_token, dts[i + 1].end_token, GetTextAttr.FIRSTNOUNGROUPTONOMINATIVE)
                    dts[i].end_token = dts[i + 1].end_token
                    ss = dec.add_slot(DecreeReferent.ATTR_SOURCE, s, False, 0)
                    ss.tag = dts[i].get_source_text()
                    ss.add_annotation(dts[i])
                    i += 1
                    continue
                break
            elif (dts[i].typ == DecreeToken.ItemType.MISC): 
                if (i == 0 or kodeks): 
                    break
                if ((i + 1) >= len(dts)): 
                    if (BracketHelper.can_be_start_of_sequence(dts[i].end_token.next0_, True, False)): 
                        continue
                    if (i > 0 and dts[i - 1].typ == DecreeToken.ItemType.NUMBER): 
                        if (DecreeToken.try_attach_name(dts[i].end_token.next0_, None, True, False, False) is not None): 
                            continue
                elif (dts[i + 1].typ == DecreeToken.ItemType.NAME or dts[i + 1].typ == DecreeToken.ItemType.NUMBER or dts[i + 1].typ == DecreeToken.ItemType.DATE): 
                    continue
                break
            else: 
                break
        if (i == 0): 
            return None
        if (dec.typ is None or ((dec0 is not None and dts[0].typ != DecreeToken.ItemType.TYP))): 
            if (dec0 is not None): 
                if (dec.number is None and dec.date is None and dec.find_slot(DecreeReferent.ATTR_NAME, None, True) is None): 
                    return None
                if (dec.typ is None): 
                    dec.typ = dec0.typ
                if (dec.find_slot(DecreeReferent.ATTR_GEO, None, True) is None): 
                    dec.add_slot(DecreeReferent.ATTR_GEO, dec0.get_string_value(DecreeReferent.ATTR_GEO), False, 0)
                if (dec.find_slot(DecreeReferent.ATTR_DATE, None, True) is None and dec0.date is not None): 
                    dec.add_slot(DecreeReferent.ATTR_DATE, dec0.get_slot_value(DecreeReferent.ATTR_DATE), False, 0)
                sl = None
                if (dec.find_slot(DecreeReferent.ATTR_SOURCE, None, True) is None): 
                    sl = dec0.find_slot(DecreeReferent.ATTR_SOURCE, None, True)
                    if ((sl) is not None): 
                        ss = dec.add_slot(DecreeReferent.ATTR_SOURCE, sl.value, False, 0)
                        ss.tag = sl.tag
                        ss.merge_occurence(sl)
            elif (base_typ is not None and after_decree): 
                dec.add_typ(base_typ)
            else: 
                return None
        et = dts[i - 1].end_token
        if ((((not after_decree and len(dts) == i and i == 3) and dts[0].typ == DecreeToken.ItemType.TYP and dts[i - 1].typ == DecreeToken.ItemType.NUMBER) and dec.find_slot(DecreeReferent.ATTR_SOURCE, None, True) is not None and et.next0_ is not None) and et.next0_.is_comma and dec.number is not None): 
            tt = et.next0_
            while tt is not None: 
                if (not tt.is_char(',')): 
                    break
                ddd = DecreeToken.try_attach_list(tt.next0_, dts[0], 10, False)
                if (ddd is None or (len(ddd) < 2) or ddd[0].typ == DecreeToken.ItemType.TYP): 
                    break
                has_num = False
                for d in ddd: 
                    if (d.typ == DecreeToken.ItemType.NUMBER): 
                        has_num = True
                    elif (d.typ == DecreeToken.ItemType.TYP): 
                        has_num = False
                        break
                if (not has_num): 
                    break
                rtt = DecreeAnalyzer.__try_attach(ddd, dts[0], True, ad)
                if (rtt is None): 
                    break
                dec.merge_slots(rtt[0].referent, True)
                tt = rtt[0].end_token
                et = tt
                tt = tt.next0_
        if (((et.next0_ is not None and et.next0_.is_char('<') and (isinstance(et.next0_.next0_, ReferentToken))) and et.next0_.next0_.next0_ is not None and et.next0_.next0_.next0_.is_char('>')) and et.next0_.next0_.get_referent().type_name == "URI"): 
            et = et.next0_.next0_.next0_
        num = dec.number
        if ((dec.find_slot(DecreeReferent.ATTR_NAME, None, True) is None and (i < len(dts)) and dts[i].typ == DecreeToken.ItemType.TYP) and dec.kind == DecreeKind.PROJECT): 
            dts1 = list(dts)
            del dts1[0:0+i]
            rt1 = DecreeAnalyzer.__try_attach(dts1, None, True, ad)
            if (rt1 is not None): 
                dec._add_name_str(MiscHelper.get_text_value_of_meta_token(rt1[0], GetTextAttr.KEEPREGISTER), rt1[0])
                et = rt1[0].end_token
        if (dec.typ == "РУКОВОДЯЩИЙ ДОКУМЕНТ" and not et.is_newline_after): 
            typ1 = DecreeToken.try_attach(et.next0_, None, False)
            if (typ1 is not None and typ1.typ == DecreeToken.ItemType.TYP and typ1.value == dec.typ): 
                tt = typ1.end_token.next0_
                while tt is not None: 
                    if (tt.is_char('.') or tt.is_hiphen or tt.is_value("ОТРАСЛЬ", None)): 
                        pass
                    else: 
                        break
                    tt = tt.next0_
                dn = DecreeToken.try_attach_name(tt, dec.typ, False, False, False)
                if (dn is not None): 
                    if (dn.full_value is not None): 
                        dec._add_name_str(dn.full_value, dn)
                    if (dn.value is not None): 
                        dec._add_name_str(dn.value, dn)
                    et = dn.end_token
        if (dec.find_slot(DecreeReferent.ATTR_NAME, None, True) is None and not kodeks and et.next0_ is not None): 
            dn = DecreeToken.try_attach_name((et.next0_.next0_ if et.next0_.is_char(':') else et.next0_), dec.typ, False, False, False)
            if (dn is not None and et.next0_.chars.is_all_lower and num is not None): 
                if (ad is not None): 
                    for r in ad.referents: 
                        if (r.find_slot(DecreeReferent.ATTR_NUMBER, num, True) is not None): 
                            if (r.can_be_equals(dec, ReferentsEqualType.WITHINONETEXT)): 
                                if (r.find_slot(DecreeReferent.ATTR_NAME, dn.value, True) is None): 
                                    dn = (None)
                                break
            if (dts[i - 1].typ == DecreeToken.ItemType.TYP and dn is not None and et.is_newline_after): 
                dn = (None)
            if (dn is not None): 
                if (dec.kind == DecreeKind.PROGRAM): 
                    dn.begin_token = dts[0].begin_token
                    dn.full_value = MiscHelper.get_text_value_of_meta_token(dn, Utils.valToEnum((GetTextAttr.FIRSTNOUNGROUPTONOMINATIVESINGLE) | (GetTextAttr.KEEPREGISTER), GetTextAttr))
                    if (Utils.startsWithString(dn.full_value, "ГОСПРОГРАММА", True)): 
                        dn.full_value = ("Государственная программа" + dn.full_value[12:])
                if (dec.kind == DecreeKind.PROGRAM): 
                    tt1 = dn.end_token.previous
                    while tt1 is not None and tt1.begin_char > dn.begin_char: 
                        if (tt1.is_char(')') and tt1.previous is not None): 
                            tt1 = tt1.previous
                        if (isinstance(tt1.get_referent(), DateRangeReferent)): 
                            dec.add_slot(DecreeReferent.ATTR_DATE, tt1.get_referent(), False, 0)
                        elif ((isinstance(tt1.get_referent(), DateReferent)) and tt1.previous is not None and tt1.previous.is_value("ДО", None)): 
                            rt11 = tt1.kit.process_referent("DATE", tt1.previous, None)
                            if (rt11 is not None and (isinstance(rt11.referent, DateRangeReferent))): 
                                dec.add_slot(DecreeReferent.ATTR_DATE, rt11.referent, False, 0)
                                dec.add_ext_referent(rt11)
                                tt1 = tt1.previous
                            else: 
                                break
                        elif ((isinstance(tt1.get_referent(), DateReferent)) and tt1.previous is not None and ((tt1.previous.is_value("НА", None) or tt1.previous.is_value("В", None)))): 
                            dec.add_slot(DecreeReferent.ATTR_DATE, tt1.get_referent(), False, 0)
                            tt1 = tt1.previous
                        else: 
                            break
                        tt1 = tt1.previous
                        first_pass3946 = True
                        while True:
                            if first_pass3946: first_pass3946 = False
                            else: tt1 = (None if tt1 is None else tt1.previous)
                            if (not (tt1 is not None and tt1.begin_char > dn.begin_char)): break
                            if (tt1.morph.class0_.is_conjunction or tt1.morph.class0_.is_preposition): 
                                continue
                            if (tt1.is_value("ПЕРИОД", "ПЕРІОД") or tt1.is_value("ПЕРСПЕКТИВА", None)): 
                                continue
                            if (tt1.is_char('(')): 
                                continue
                            break
                        if (tt1 is not None and tt1.end_char > dn.begin_char): 
                            if (dn.full_value is None): 
                                dn.full_value = dn.value
                            dn.value = MiscHelper.get_text_value(dn.begin_token, tt1, Utils.valToEnum((GetTextAttr.FIRSTNOUNGROUPTONOMINATIVESINGLE) | (GetTextAttr.KEEPREGISTER), GetTextAttr))
                        tt1 = tt1.next0_
                        tt1 = (None if tt1 is None else tt1.previous)
                if (dn.full_value is not None): 
                    dec._add_name_str(dn.full_value, dn)
                if ((len(dts) == 1 and dec.kind != DecreeKind.PROGRAM and dts[0].typ == DecreeToken.ItemType.TYP) and dn.begin_token.morph.case_.is_genitive and not dn.begin_token.morph.class0_.is_preposition): 
                    str0_ = MiscHelper.get_text_value(dts[0].begin_token, dn.end_token, GetTextAttr.FIRSTNOUNGROUPTONOMINATIVE)
                    dec._add_name_str(str0_, MetaToken(dts[0].begin_token, dn.end_token))
                else: 
                    dec._add_name_str(dn.value, MetaToken(dts[0].begin_token, dn.end_token))
                et = dn.end_token
                br = False
                tt = et.next0_
                first_pass3947 = True
                while True:
                    if first_pass3947: first_pass3947 = False
                    else: tt = tt.next0_
                    if (not (tt is not None)): break
                    if (tt.is_char('(')): 
                        br = True
                        continue
                    if (tt.is_char(')') and br): 
                        et = tt
                        continue
                    if ((isinstance(tt.get_referent(), DateRangeReferent)) and dec.kind == DecreeKind.PROGRAM): 
                        dec.add_slot(DecreeReferent.ATTR_DATE, tt.get_referent(), False, 0)
                        et = tt
                        continue
                    dn = DecreeToken.try_attach(tt, None, False)
                    if (dn is None): 
                        break
                    if (dn.typ == DecreeToken.ItemType.DATE and dec.date is None): 
                        if (dec.add_date(dn)): 
                            tt = dn.end_token
                            et = tt
                            continue
                    if (dn.typ == DecreeToken.ItemType.NUMBER and dec.number is None): 
                        dec.add_number(dn)
                        tt = dn.end_token
                        et = tt
                        continue
                    if (dn.typ == DecreeToken.ItemType.DATERANGE and dec.kind == DecreeKind.PROGRAM): 
                        if (dec.add_date(dn)): 
                            tt = dn.end_token
                            et = tt
                            continue
                    if (dn.typ == DecreeToken.ItemType.TERR and dec.find_slot(DecreeReferent.ATTR_GEO, None, True) is None and dn.ref is not None): 
                        dec.add_slot(DecreeReferent.ATTR_GEO, dn.ref.referent, False, 0)
                        tt = dn.end_token
                        et = tt
                        continue
                    break
        if (dec.find_slot(DecreeReferent.ATTR_SOURCE, None, True) is None): 
            tt0 = dts[0].begin_token.previous
            if ((tt0 is not None and tt0.is_value("В", "У") and tt0.previous is not None) and (isinstance(tt0.previous.get_referent(), OrganizationReferent))): 
                ss = dec.add_slot(DecreeReferent.ATTR_SOURCE, tt0.previous.get_referent(), False, 0)
                ss.add_annotation(Utils.asObjectOrNull(tt0.previous, ReferentToken))
        if (not canbesingle and not dec._check_correction(is_noun_doubt)): 
            ty = dec.typ
            sl = None
            if (dec0 is not None and dec.date is not None and dec.find_slot(DecreeReferent.ATTR_SOURCE, None, True) is None): 
                sl = dec0.find_slot(DecreeReferent.ATTR_SOURCE, None, True)
            if (sl is not None and (((((ty == "ПОСТАНОВЛЕНИЕ" or ty == "ПОСТАНОВА" or ty == "ОПРЕДЕЛЕНИЕ") or ty == "ВИЗНАЧЕННЯ" or ty == "РЕШЕНИЕ") or ty == "РІШЕННЯ" or ty == "ПРИГОВОР") or ty == "ВИРОК"))): 
                dec.add_slot(sl.type_name, sl.value, False, 0).tag = sl.tag
            else: 
                eq_decs = 0
                dr0 = None
                if (num is not None): 
                    if (ad is not None): 
                        for r in ad.referents: 
                            if (r.find_slot(DecreeReferent.ATTR_NUMBER, num, True) is not None): 
                                if (r.can_be_equals(dec, ReferentsEqualType.WITHINONETEXT)): 
                                    eq_decs += 1
                                    dr0 = (Utils.asObjectOrNull(r, DecreeReferent))
                if (eq_decs == 1): 
                    dec.merge_slots(dr0, True)
                else: 
                    ok1 = False
                    if (num is not None): 
                        tt = dts[0].begin_token.previous
                        while tt is not None: 
                            if (tt.is_char_of(":,") or tt.is_hiphen or BracketHelper.can_be_start_of_sequence(tt, False, False)): 
                                pass
                            else: 
                                if (tt.is_value("ДАЛЕЕ", "ДАЛІ")): 
                                    ok1 = True
                                break
                            tt = tt.previous
                    if (not ok1): 
                        return None
        rt = ReferentToken(dec, dts[0].begin_token, et)
        if (len(dec.slots) == 2 and dec.slots[0].type_name == DecreeReferent.ATTR_TYPE and dec.slots[1].type_name == DecreeReferent.ATTR_NAME): 
            err = True
            tt = rt.begin_token
            while tt is not None and tt.end_char <= rt.end_char: 
                if (isinstance(tt.get_referent(), GeoReferent)): 
                    pass
                elif ((isinstance(tt, TextToken)) and tt.chars.is_letter and not tt.chars.is_all_lower): 
                    err = False
                    break
                tt = tt.next0_
            if (err): 
                return None
        if (morph_ is not None): 
            rt.morph = morph_
        if (rt.chars.is_all_lower): 
            if (dec.typ0 == "ДЕКЛАРАЦИЯ" or dec.typ0 == "ДЕКЛАРАЦІЯ"): 
                return None
            if (((dec.typ0 == "КОНСТИТУЦИЯ" or dec.typ0 == "КОНСТИТУЦІЯ")) and rt.begin_token == rt.end_token): 
                ok1 = False
                cou = 10
                tt = rt.begin_token.previous
                while tt is not None and cou > 0: 
                    if (tt.is_newline_after): 
                        break
                    pt = PartToken.try_attach(tt, None, False, False)
                    if (pt is not None and pt.typ != PartToken.ItemType.PREFIX and pt.end_token.next0_ == rt.begin_token): 
                        ok1 = True
                        break
                    tt = tt.previous; cou -= 1
                if (not ok1): 
                    return None
        if (num is not None and ((num.find('/') > 0 or num.find(',') > 0))): 
            cou = 0
            for s in dec.slots: 
                if (s.type_name == DecreeReferent.ATTR_NUMBER): 
                    cou += 1
            if (cou == 1): 
                owns = 0
                for s in dec.slots: 
                    if (s.type_name == DecreeReferent.ATTR_SOURCE): 
                        owns += 1
                if (owns > 1): 
                    nums = Utils.splitString(num, '/', False)
                    nums2 = Utils.splitString(num, ',', False)
                    str_num = None
                    ii = 0
                    while ii < len(dts): 
                        if (dts[ii].typ == DecreeToken.ItemType.NUMBER): 
                            str_num = dts[ii].get_source_text()
                            break
                        ii += 1
                    if (len(nums2) == owns and owns > 1): 
                        dec.add_slot(DecreeReferent.ATTR_NUMBER, None, True, 0)
                        for n in nums2: 
                            dec.add_slot(DecreeReferent.ATTR_NUMBER, n.strip(), False, 0).tag = str_num
                    elif (len(nums) == owns and owns > 1): 
                        dec.add_slot(DecreeReferent.ATTR_NUMBER, None, True, 0)
                        for n in nums: 
                            dec.add_slot(DecreeReferent.ATTR_NUMBER, n.strip(), False, 0).tag = str_num
        if (BracketHelper.can_be_start_of_sequence(rt.begin_token.previous, True, False) and BracketHelper.can_be_end_of_sequence(rt.end_token.next0_, True, rt.begin_token.previous, False)): 
            rt.begin_token = rt.begin_token.previous
            rt.end_token = rt.end_token.next0_
            dts1 = DecreeToken.try_attach_list(rt.end_token.next0_, None, 10, False)
            if (dts1 is not None and dts1[0].typ == DecreeToken.ItemType.DATE and dec.find_slot(DecreeReferent.ATTR_DATE, None, True) is None): 
                dec.add_date(dts1[0])
                rt.end_token = dts1[0].end_token
                if (len(dts1) > 1 and dts1[1].typ == DecreeToken.ItemType.NUMBER and dec.number is None): 
                    dec.add_number(dts1[1])
                    rt.end_token = dts1[1].end_token
        if (dec.kind == DecreeKind.STANDARD and dec.name is None and BracketHelper.can_be_start_of_sequence(rt.end_token.next0_, True, False)): 
            br = BracketHelper.try_parse(rt.end_token.next0_, BracketParseAttr.NO, 100)
            if (br is not None): 
                dec._add_name_str(MiscHelper.get_text_value_of_meta_token(br, GetTextAttr.KEEPREGISTER), br)
                rt.end_token = br.end_token
        if (dec.kind == DecreeKind.PROGRAM and dec.find_slot(DecreeReferent.ATTR_DATE, None, True) is None): 
            if (rt.begin_token.previous is not None and rt.begin_token.previous.is_value("ПАСПОРТ", None)): 
                cou = 0
                tt = rt.end_token.next0_
                first_pass3948 = True
                while True:
                    if first_pass3948: first_pass3948 = False
                    else: tt = (None if tt is None else tt.next0_)
                    if (not (tt is not None and (cou < 1000))): break
                    if (tt.is_value("СРОК", "ТЕРМІН") and tt.next0_ is not None and tt.next0_.is_value("РЕАЛИЗАЦИЯ", "РЕАЛІЗАЦІЯ")): 
                        pass
                    else: 
                        continue
                    tt = tt.next0_.next0_
                    if (tt is None): 
                        break
                    dtok = DecreeToken.try_attach(tt, None, False)
                    if (dtok is not None and dtok.typ == DecreeToken.ItemType.TYP and ((dtok.value == "ПРОГРАММА" or dtok.value == "ПРОГРАМА"))): 
                        tt = dtok.end_token.next0_
                    while tt is not None: 
                        if (tt.is_hiphen or tt.is_table_control_char or tt.is_value("ПРОГРАММА", "ПРОГРАМА")): 
                            pass
                        elif (isinstance(tt.get_referent(), DateRangeReferent)): 
                            dec.add_slot(DecreeReferent.ATTR_DATE, tt.get_referent(), False, 0)
                            break
                        else: 
                            break
                        tt = tt.next0_
                    break
        if (rt.end_token.next0_ is not None and rt.end_token.next0_.is_char('(')): 
            dt = None
            ok = False
            tt = rt.end_token.next0_.next0_
            first_pass3949 = True
            while True:
                if first_pass3949: first_pass3949 = False
                else: tt = tt.next0_
                if (not (tt is not None)): break
                r = tt.get_referent()
                if (isinstance(r, GeoReferent)): 
                    continue
                if (isinstance(r, DateReferent)): 
                    dt = (Utils.asObjectOrNull(r, DateReferent))
                    continue
                if (tt.morph.class0_.is_preposition): 
                    continue
                if (tt.morph.class0_.is_verb): 
                    continue
                if (tt.is_char(')') and dt is not None): 
                    dec.add_slot(DecreeReferent.ATTR_DATE, dt, False, 0)
                    rt.end_token = tt
                    ok = True
                break
            if (not ok): 
                dts1 = DecreeToken.try_attach_list(rt.end_token.next0_.next0_, None, 10, False)
                if (dts1 is not None): 
                    rtt = DecreeAnalyzer.__try_attach(dts1, typ_tok, True, ad)
                    if ((rtt is not None and len(rtt) == 1 and rtt[0].end_token.next0_ is not None) and rtt[0].end_token.next0_.is_char(')')): 
                        dec1 = Utils.asObjectOrNull(rtt[0].referent, DecreeReferent)
                        ok = dec.typ == dec1.typ
                        if ((ok and dec1.number is not None and dec.number is not None) and dec.number != dec1.number): 
                            ok = False
                        if ((ok and dec1.date is not None and dec.date is not None) and dec.date != dec1.date): 
                            ok = False
                        if (ok): 
                            dec.merge_slots(rtt[0].referent, True)
                            rt.end_token = rtt[0].end_token.next0_
                elif (dec.kind == DecreeKind.CLASSIFIER): 
                    br = BracketHelper.try_parse(rt.end_token.next0_, BracketParseAttr.NO, 100)
                    if (br is not None): 
                        rt.end_token = br.end_token
        if (dec.find_slot(DecreeReferent.ATTR_NAME, None, True) is None and not rt.is_newline_before): 
            tt0 = None
            cou = 40
            tt = rt.begin_token.previous
            while tt is not None and cou > 0: 
                if (BracketHelper.can_be_start_of_sequence(tt, True, False)): 
                    tt0 = tt
                elif ((isinstance(tt, TextToken)) and tt.chars.is_letter): 
                    tt0 = tt
                if (tt.is_newline_before): 
                    break
                tt = tt.previous; cou -= 1
            nam = DecreeToken.try_attach_name(tt0, dec.typ, False, False, False)
            if (nam is not None and (nam.end_char < rt.begin_char)): 
                if (nam.end_token.next0_ == rt.begin_token or ((nam.end_token.next0_.is_comma and nam.end_token.next0_.next0_ == rt.begin_token))): 
                    rt.begin_token = tt0
                    dec._add_name_str(nam.value, nam)
        if (dec.find_slot(DecreeReferent.ATTR_NAME, None, True) is None and not rt.is_newline_after): 
            if (rt.is_newline_before or ((rt.begin_token.previous is not None and rt.begin_token.previous.length_char == 1 and ((rt.begin_token.previous.is_newline_before or rt.begin_token.previous.is_table_control_char))))): 
                if (dec.kind == DecreeKind.STANDARD and dec.number is not None): 
                    nam = DecreeToken.try_attach_name_to_end_of_line(rt.end_token.next0_, False)
                    if (nam is not None): 
                        rt.end_token = nam.end_token
                        dec._add_name_str(nam.value, nam)
        rt_li = list()
        if (((i + 1) < len(dts)) and dts[i].typ == DecreeToken.ItemType.EDITION and not dts[i].is_newline_before): 
            del dts[0:0+i + 1]
            ed = DecreeAnalyzer.__try_attach(dts, base_typ, True, ad)
            if (ed is not None and len(ed) > 0): 
                rt_li.extend(ed)
                for e0_ in ed: 
                    dec.add_slot(DecreeReferent.ATTR_EDITION, e0_.referent, False, 0)
                rt.end_token = ed[len(ed) - 1].end_token
        elif (((i < (len(dts) - 1)) and i > 0 and dts[i - 1].typ == DecreeToken.ItemType.EDITION) and not dts[i - 1].is_newline_before): 
            del dts[0:0+i]
            ed = DecreeAnalyzer.__try_attach(dts, base_typ, True, ad)
            if (ed is not None and len(ed) > 0): 
                rt_li.extend(ed)
                for e0_ in ed: 
                    dec.add_slot(DecreeReferent.ATTR_EDITION, e0_.referent, False, 0)
                rt.end_token = ed[len(ed) - 1].end_token
        if (dec.kind == DecreeKind.LAW or dec.kind == DecreeKind.ORDER): 
            pass
        else: 
            rt22 = DecreeAnalyzer._try_attach_approved0(rt.end_token.next0_, ad, True, False, None)
            if (rt22 is not None): 
                rt.end_token = rt22.end_token
                dr00 = Utils.asObjectOrNull(rt22.referent, DecreeReferent)
                if (dr00.typ is None): 
                    for s in dr00.slots: 
                        if (s.type_name == DecreeReferent.ATTR_DATE or s.type_name == DecreeReferent.ATTR_SOURCE): 
                            if (dec.find_slot(s.type_name, None, True) is None): 
                                dec.add_slot(s.type_name, s.value, False, 0)
                    dr00 = (None)
                if (dr00 is not None): 
                    rt_li.append(rt22)
                    dec.add_slot(DecreeReferent.ATTR_OWNER, rt22.referent, False, 0)
        if (dts[0].typ == DecreeToken.ItemType.TYP and dts[0].typ_kind == DecreeKind.CLASSIFIER): 
            if (((rt.begin_token.previous is not None and rt.begin_token.previous.is_char(')') and (isinstance(rt.begin_token.previous.previous, TextToken))) and rt.begin_token.previous.previous.chars.is_all_upper and rt.begin_token.previous.previous.previous is not None) and rt.begin_token.previous.previous.previous.is_char('(')): 
                rt.begin_token = rt.begin_token.previous.previous.previous
                dec._add_name_str(rt.begin_token.next0_.term, MetaToken(rt.begin_token.next0_, rt.begin_token.next0_))
        rt_li.append(rt)
        if (num_tok is not None and num_tok.children is not None): 
            end = rt.end_token
            rt.end_token = num_tok.children[0].begin_token.previous
            if (rt.end_token.is_comma_and): 
                rt.end_token = rt.end_token.previous
            ii = 0
            while ii < len(num_tok.children): 
                dr1 = DecreeReferent()
                for s in rt.referent.slots: 
                    if (s.type_name == DecreeReferent.ATTR_NUMBER): 
                        dr1.add_slot(s.type_name, num_tok.children[ii].value, False, 0).tag = num_tok.children[ii].get_source_text()
                    else: 
                        ss = dr1.add_slot(s.type_name, s.value, False, 0)
                        if (ss is not None): 
                            ss.tag = s.tag
                rt1 = ReferentToken(dr1, num_tok.children[ii].begin_token, num_tok.children[ii].end_token)
                if (ii == (len(num_tok.children) - 1)): 
                    rt1.end_token = end
                rt_li.append(rt1)
                ii += 1
        if ((len(dts) == 2 and dts[0].typ == DecreeToken.ItemType.TYP and dts[0].typ_kind == DecreeKind.STANDARD) and dts[1].typ == DecreeToken.ItemType.NUMBER): 
            ttt = dts[1].end_token.next0_
            while ttt is not None: 
                if (not ttt.is_comma_and): 
                    break
                nu = DecreeToken.try_attach(ttt.next0_, dts[0], False)
                if (nu is None or nu.typ != DecreeToken.ItemType.NUMBER): 
                    break
                dr1 = DecreeReferent()
                dr1.typ = dec.typ
                dr1.add_number(nu)
                rt_li.append(ReferentToken(dr1, ttt.next0_, nu.end_token))
                if (not ttt.is_comma): 
                    break
                ttt = nu.end_token
                ttt = ttt.next0_
        return rt_li
    
    def __process_parts_and_changes(self, kit : 'AnalysisKit', base_typ : 'DecreeToken') -> None:
        from pullenti.ner.decree.DecreeReferent import DecreeReferent
        from pullenti.ner.decree.DecreePartReferent import DecreePartReferent
        from pullenti.ner.decree.internal.PartToken import PartToken
        from pullenti.ner.decree.DecreeChangeReferent import DecreeChangeReferent
        from pullenti.ner.decree.DecreeChangeValueReferent import DecreeChangeValueReferent
        from pullenti.ner.decree.internal.DecreeChangeToken import DecreeChangeToken
        ad = kit.get_analyzer_data(self)
        undefined_decrees = list()
        root_change = None
        root_change_ques = None
        last_change = None
        change_decree = None
        change_part = DecreePartReferent()
        change_stack = list()
        expire_regime = 0
        has_start_change = 0
        last_append2 = None
        has_change_keyword = False
        t = kit.first_token
        first_pass3950 = True
        while True:
            if first_pass3950: first_pass3950 = False
            else: t = t.next0_
            if (not (t is not None)): break
            if (t.is_ignored): 
                continue
            dts = None
            if (t.is_newline_before and t.is_char('(')): 
                pass
            dcht = None
            ok1 = t.is_newline_before
            if (not ok1): 
                if (root_change is not None and t.previous is not None and t.previous.is_char(':')): 
                    ok1 = True
            if (not ok1): 
                if ((isinstance(t.previous, ReferentToken)) and (isinstance(t.previous.get_referent(), DecreeChangeReferent))): 
                    ok1 = True
                    if (t.is_char_of(";,:.") and t.next0_ is not None): 
                        t = t.next0_
            if ((not ok1 and t.previous is not None and t.previous.is_table_control_char) and t.previous.is_newline_before): 
                ok1 = True
            if (ok1): 
                if (t.is_value("ИЗМЕНЕНИЯ", None)): 
                    pass
                if (t.is_value2("ДОПОЛНИТЕЛЬНОЕ", "СОГЛАШЕНИЕ")): 
                    has_change_keyword = True
                dcht = DecreeChangeToken.try_attach(t, (None if root_change is None else Utils.asObjectOrNull(root_change.referent, DecreeChangeReferent)), False, change_stack, False, False, None)
                if (dcht is not None): 
                    if (dcht.has_change_keyword): 
                        has_change_keyword = True
                    if (dcht.act_kind2 == DecreeChangeKind.APPEND and dcht.parts is not None): 
                        last_append2 = dcht
                    elif (last_append2 is not None and dcht.parts is not None and dcht.act_kind == DecreeChangeKind.UNDEFINED): 
                        dcht.new_parts = dcht.parts
                        dcht.parts = last_append2.parts
                        dcht.real_part = last_append2.real_part
                        if (dcht.real_part is not None): 
                            dcht.parts = (None)
                        dcht.act_kind = DecreeChangeKind.APPEND
            if (dcht is not None and ((dcht.is_start or dcht.change_val is not None)) and not dcht.ignorable): 
                if (dcht.typ == DecreeChangeTokenTyp.STARTMULTU): 
                    expire_regime = 0
                    has_start_change = 3
                    last_append2 = (None)
                    root_change = (None)
                elif (dcht.typ == DecreeChangeTokenTyp.SINGLE): 
                    dcht1 = DecreeChangeToken.try_attach(dcht.end_token.next0_, (None if root_change is None else Utils.asObjectOrNull(root_change.referent, DecreeChangeReferent)), False, change_stack, False, False, None)
                    if (dcht1 is not None and dcht1.is_start and not dcht1.ignorable): 
                        has_start_change = 2
                        if (dcht.decree_tok is not None and dcht.decree is not None): 
                            rt = ReferentToken(dcht.decree, dcht.decree_tok.begin_token, dcht.decree_tok.end_token)
                            kit.embed_token(rt)
                            t = (rt)
                            if (dcht.end_char == t.end_char): 
                                dcht.end_token = t
                elif (dcht.typ == DecreeChangeTokenTyp.STARTSINGLE and dcht.decree is not None and expire_regime == 0): 
                    ok = (dcht.has_change_keyword or last_change is not None or has_change_keyword) or dcht.change_val is not None or dcht.act_kind != DecreeChangeKind.UNDEFINED
                    if (not ok): 
                        tt2 = dcht.end_token.next0_
                        first_pass3951 = True
                        while True:
                            if first_pass3951: first_pass3951 = False
                            else: tt2 = tt2.next0_
                            if (not (tt2 is not None)): break
                            next0_ = DecreeChangeToken.try_attach(tt2, None, True, None, False, False, None)
                            if (next0_ is not None): 
                                if (next0_.change_val is not None or next0_.act_kind != DecreeChangeKind.UNDEFINED): 
                                    ok = True
                                break
                            if (tt2.is_comma): 
                                continue
                            if (tt2.is_value("ВНЕСТИ", None)): 
                                ok = True
                            break
                    if (ok): 
                        has_start_change = 2
                        has_change_keyword = True
                        if (dcht.decree_tok is not None): 
                            rt = ReferentToken(dcht.decree, dcht.decree_tok.begin_token, dcht.decree_tok.end_token)
                            kit.embed_token(rt)
                            t = (rt)
                            if (dcht.end_char == t.end_char): 
                                dcht.end_token = t
                    else: 
                        dts = (Utils.ifNotNull(dcht.parts, dcht.new_parts))
                if (dcht.typ == DecreeChangeTokenTyp.STARTSINGLE and root_change is not None and dcht.decree is None): 
                    has_start_change = 2
                elif ((dcht.typ == DecreeChangeTokenTyp.SINGLE and dcht.decree is not None and dcht.end_token.is_char(':')) and dcht.is_newline_after): 
                    has_start_change = 2
                if (has_start_change <= 0 and expire_regime == 0): 
                    dts = PartToken.try_attach_list(t, False, 40)
                    change_stack.clear()
                    if (dcht.act_kind == DecreeChangeKind.EXPIRE): 
                        expire_regime = 1
                    elif (dcht.act_kind == DecreeChangeKind.SUSPEND): 
                        expire_regime = 2
                    if (not dcht.ignorable): 
                        dts = (Utils.ifNotNull(dcht.parts, dcht.new_parts))
                else: 
                    if (dcht.decree is not None): 
                        if (change_decree != dcht.decree): 
                            root_change = (None)
                        change_decree = dcht.decree
                        change_part.slots.clear()
                        change_stack.clear()
                    if (dcht.act_kind == DecreeChangeKind.EXPIRE): 
                        expire_regime = 1
                    elif (dcht.act_kind == DecreeChangeKind.SUSPEND): 
                        expire_regime = 2
                    if (not dcht.ignorable): 
                        dts = dcht.parts
                        if ((dts is None and dcht.new_parts is not None and dcht.act_kind == DecreeChangeKind.UNDEFINED) and dcht.change_val is None): 
                            dts = dcht.new_parts
            else: 
                dts = PartToken.try_attach_list(t, False, 40)
                if ((dcht is None and t.is_newline_before and not t.is_char('(')) and not t.is_table_control_char): 
                    expire_regime = 0
                    has_start_change -= 1
            if (dts is not None and len(dts) > 0 and root_change is not None): 
                if (dts[0].begin_char < root_change.begin_char): 
                    dts = (None)
            if (dts is not None and len(dts) == 1): 
                if ((dts[0].typ == PartToken.ItemType.FORM or dts[0].typ == PartToken.ItemType.FORMULA or dts[0].typ == PartToken.ItemType.NAME) or dts[0].typ == PartToken.ItemType.TABLE or dts[0].typ == PartToken.ItemType.LIST): 
                    if (root_change is None and ((root_change_ques is None or len(dts[0].values) == 0))): 
                        dts = (None)
            if (dts is not None and len(dts) == 2 and dts[0].typ == PartToken.ItemType.PREFIX): 
                if ((dts[1].typ == PartToken.ItemType.FORM or dts[1].typ == PartToken.ItemType.FORMULA or dts[1].typ == PartToken.ItemType.NAME) or dts[1].typ == PartToken.ItemType.TABLE or dts[1].typ == PartToken.ItemType.LIST): 
                    if (root_change is None and ((root_change_ques is None or len(dts[0].values) == 0))): 
                        dts = (None)
            if (dts is not None and len(dts) >= 1): 
                if (dts[0].typ == PartToken.ItemType.FORM or dts[0].typ == PartToken.ItemType.TABLE or dts[0].typ == PartToken.ItemType.LIST): 
                    if (root_change is None and ((root_change_ques is None or len(dts[0].values) == 0))): 
                        dts = (None)
            if (dcht is not None and dts is not None and not dcht.ignorable): 
                for pp in dts: 
                    change_part._remove_slots(pp.typ)
            if (dcht is not None and dcht.new_parts is not None): 
                for pp in dcht.new_parts: 
                    change_part._remove_slots(pp.typ)
            rts = DecreeAnalyzer._try_attach_parts(dts, base_typ, (change_decree if has_start_change > 0 else None), root_change is not None)
            if (rts is not None): 
                pass
            if (dcht is not None and dcht.add_parts is not None): 
                for dts2 in dcht.add_parts: 
                    rts2 = DecreeAnalyzer._try_attach_parts(dts2, base_typ, (change_decree if has_start_change > 0 else None), root_change is not None)
                    if (rts2 is None or len(rts2) == 0): 
                        continue
                    if (rts is None): 
                        rts = rts2
                    else: 
                        rts.extend(rts2)
            dprs = None
            diaps = None
            begs = None
            ends = None
            if (rts is not None): 
                for kp in rts: 
                    dpr_list = Utils.asObjectOrNull(kp.tag, list)
                    if (dpr_list is None): 
                        continue
                    i = 0
                    first_pass3952 = True
                    while True:
                        if first_pass3952: first_pass3952 = False
                        else: i += 1
                        if (not (i < len(dpr_list))): break
                        dr = dpr_list[i]
                        if (dr.owner is None and dr.clause is not None and dr.local_typ is None): 
                            if (not dr in undefined_decrees): 
                                undefined_decrees.append(dr)
                        if ((dr.clause is None and dr.doc_part is not None and dr.part is None) and change_part.clause is not None): 
                            dr.part = dr.doc_part
                            dr.doc_part = None
                        if (dr.owner is not None and dr.clause is not None): 
                            for d in undefined_decrees: 
                                d.owner = dr.owner
                            undefined_decrees.clear()
                        ign_last = False
                        if (len(dts) == 1): 
                            if ((dts[0].typ == PartToken.ItemType.SENTENCE or dts[0].typ == PartToken.ItemType.INDENTION or dts[0].typ == PartToken.ItemType.FORMULA) or dts[0].typ == PartToken.ItemType.PREAMBLE): 
                                ign_last = True
                        if (dcht is not None and not dcht.ignorable): 
                            dr._add_high_level_info(change_part)
                        if (last_change is not None and len(last_change.owners) > 0): 
                            dr0 = Utils.asObjectOrNull(last_change.owners[0], DecreePartReferent)
                            if (dr0 is not None and dr.owner == dr0.owner): 
                                if (dr0.appendix is not None and dr.appendix is not None and dr0.appendix != dr.appendix): 
                                    last_change = (None)
                                    if (len(change_stack) == 1): 
                                        change_stack.insert(0, dr)
                                else: 
                                    mle = dr._get_min_level()
                                    if (mle == 1 and dr.doc_part is not None and dr0.doc_part is None): 
                                        dr.part = dr.doc_part
                                        dr.doc_part = None
                                        mle = dr._get_min_level()
                                    if (mle == 0 or mle <= PartToken._get_rank(PartToken.ItemType.CLAUSE)): 
                                        pass
                                    elif (dr.indention is not None and len(dr.slots) == 2): 
                                        dr._add_high_level_info(dr0)
                        if (dr.table_column is not None): 
                            if (root_change is not None): 
                                dr.table = "0"
                            else: 
                                continue
                        if (dr.table_row is not None): 
                            if (dr.table is None): 
                                if (root_change is not None): 
                                    dr.table = "0"
                                else: 
                                    continue
                        dr = (Utils.asObjectOrNull(ad.register_referent(dr), DecreePartReferent))
                        if (len(rts) == 1 and len(dpr_list) == 1): 
                            if (last_append2 is not None and last_append2.parts == dts): 
                                last_append2.real_part = dr
                            if (dcht is not None and dcht.parts == dts): 
                                dcht.real_part = dr
                            if (change_decree is not None): 
                                if (dr.owner is not None and dr.owner != change_decree): 
                                    pass
                                elif (len(change_stack) == 0 or ((dcht is not None and dcht.typ == DecreeChangeTokenTyp.SINGLE))): 
                                    change_stack.insert(0, dr)
                                    change_part = (Utils.asObjectOrNull(dr.clone(), DecreePartReferent))
                        if (dprs is None): 
                            dprs = list()
                        dprs.append(dr)
                        rt = None
                        if (i == 0): 
                            rt = ReferentToken._new950(dr, kp.begin_token, kp.end_token, kp.morph)
                        else: 
                            rt = ReferentToken(dr, t, t)
                        kit.embed_token(rt)
                        t = (rt)
                        if (len(dprs) > 1 and t.previous is not None and t.previous.is_hiphen): 
                            if (diaps is None): 
                                diaps = dict()
                            if (not dprs[len(dprs) - 2] in diaps): 
                                diaps[dprs[len(dprs) - 2]] = dprs[len(dprs) - 1]
                        if (begs is None): 
                            begs = dict()
                        if (not t.begin_char in begs): 
                            begs[t.begin_char] = t
                        else: 
                            begs[t.begin_char] = t
                        if (ends is None): 
                            ends = dict()
                        if (not t.end_char in ends): 
                            ends[t.end_char] = t
                        else: 
                            ends[t.end_char] = t
                        if (dcht is not None and not dcht.ignorable): 
                            if (dcht.begin_char == t.begin_char): 
                                dcht.begin_token = t
                            if (dcht.end_char == t.end_char): 
                                dcht.end_token = t
                            if (t.end_char > dcht.end_char): 
                                dcht.end_token = t
                            dcht.real_part = dr
            if (dts is not None and len(dts) > 0 and dts[len(dts) - 1].end_char > t.end_char): 
                t = dts[len(dts) - 1].end_token
            if (dcht is not None and ((has_start_change > 0 or expire_regime > 0)) and not dcht.ignorable): 
                if (dcht.end_char > t.end_char): 
                    t = dcht.end_token
                chrt = None
                if ((dcht.typ == DecreeChangeTokenTyp.SINGLE and dcht.decree is not None and dcht.end_token.is_char(':')) and dcht.act_kind == DecreeChangeKind.UNDEFINED): 
                    if (root_change is None or change_decree is None): 
                        dcht.typ = DecreeChangeTokenTyp.STARTMULTU
                    elif (change_decree != dcht.decree): 
                        dcht.typ = DecreeChangeTokenTyp.STARTMULTU
                if (dcht.typ == DecreeChangeTokenTyp.STARTMULTU and ((root_change_ques is None or root_change_ques.decree != dcht.decree))): 
                    root_change = (None)
                    change_stack.clear()
                    if (dcht.decree is not None): 
                        change_decree = dcht.decree
                    if (dprs is not None and len(dprs) > 0): 
                        if (change_decree is None and dprs[0].owner is not None): 
                            change_decree = dprs[0].owner
                        change_stack.insert(0, dprs[0])
                        change_part = (Utils.asObjectOrNull(dprs[0].clone(), DecreePartReferent))
                    if (((len(change_stack) > 0 or dcht.decree is not None)) and expire_regime == 0): 
                        rch = Utils.asObjectOrNull(ad.register_referent(DecreeChangeReferent._new1402(DecreeChangeKind.CONTAINER)), DecreeChangeReferent)
                        if (len(change_stack) > 0): 
                            rch.add_slot(DecreeChangeReferent.ATTR_OWNER, change_stack[0], False, 0)
                        else: 
                            rch.add_slot(DecreeChangeReferent.ATTR_OWNER, dcht.decree, False, 0)
                        if (dcht.app_ext_changes is not None): 
                            rch.add_slot("APP_CHANGES", (str(dcht.app_ext_changes.values[0]) if len(dcht.app_ext_changes.values) > 0 else ""), True, 0)
                        root_change = ReferentToken(rch, dcht.begin_token, dcht.end_token)
                        if (root_change.end_token.is_char(':')): 
                            root_change.end_token = root_change.end_token.previous
                        tt0 = dcht.begin_token.previous
                        while tt0 is not None: 
                            if (tt0.is_newline_before and (dcht.begin_char - tt0.begin_char) > 30): 
                                dcht0 = DecreeChangeToken.try_attach(tt0, None, False, None, False, False, None)
                                if ((dcht0 is not None and dcht0.typ == DecreeChangeTokenTyp.STARTSINGLE and dcht0.decree is not None) and dcht.decree is not None): 
                                    if (dcht0.decree.can_be_equals(dcht.decree, ReferentsEqualType.WITHINONETEXT) or dcht0.decree.can_be_equals(dcht.decree.owner, ReferentsEqualType.WITHINONETEXT)): 
                                        root_change.begin_token = dcht0.begin_token
                                break
                            tt0 = tt0.previous
                        kit.embed_token(root_change)
                        t = (root_change)
                        if (t.next0_ is not None and t.next0_.is_char(':')): 
                            t = t.next0_
                    if (expire_regime == 0): 
                        continue
                if (dcht.typ == DecreeChangeTokenTyp.SINGLE and dprs is not None and len(dprs) == 1): 
                    while len(change_stack) > 0:
                        if (dprs[0]._is_all_items_less_level(change_stack[0], True)): 
                            break
                        else: 
                            del change_stack[0]
                    change_stack.insert(0, dprs[0])
                    if (dprs[0].owner is not None and change_decree != dprs[0].owner): 
                        change_decree = dprs[0].owner
                        change_stack.clear()
                        change_stack.insert(0, dprs[0])
                    change_part = (Utils.asObjectOrNull(dprs[0].clone(), DecreePartReferent))
                    continue
                if (dprs is None and dcht.real_part is not None): 
                    dprs = list()
                    dprs.append(dcht.real_part)
                if ((dprs is None and dcht.act_kind == DecreeChangeKind.REMOVE and len(change_stack) > 0) and (isinstance(change_stack[0], DecreePartReferent))): 
                    dprs = list()
                    dprs.append(Utils.asObjectOrNull(change_stack[0], DecreePartReferent))
                prev_part = None
                prev = None
                tt2 = dcht.begin_token.previous
                first_pass3953 = True
                while True:
                    if first_pass3953: first_pass3953 = False
                    else: tt2 = tt2.previous
                    if (not (tt2 is not None)): break
                    if (isinstance(tt2.get_referent(), DecreePartReferent)): 
                        if (len(change_stack) > 0 and change_stack[0].parent_referent == tt2.get_referent().parent_referent): 
                            prev_part = (Utils.asObjectOrNull(tt2.get_referent(), DecreePartReferent))
                            break
                        if (len(change_stack) == 0 and tt2.get_referent().parent_referent == change_decree): 
                            prev_part = (Utils.asObjectOrNull(tt2.get_referent(), DecreePartReferent))
                            break
                    if (tt2.length_char == 1 or (isinstance(tt2, NumberToken))): 
                        continue
                    prev = (Utils.asObjectOrNull(tt2.get_referent(), DecreeChangeReferent))
                    if (prev is not None): 
                        prev_part = (Utils.asObjectOrNull(prev.get_slot_value(DecreeChangeReferent.ATTR_OWNER), DecreePartReferent))
                        if (prev_part is not None and prev_part.name_as_item is not None): 
                            prev_part = (None)
                            continue
                        if (root_change is not None and prev != root_change.referent and prev_part is None): 
                            change_stack.clear()
                    break
                if (dcht.has_anafor and dcht.parts is None and prev_part is not None): 
                    dcht.real_part = prev_part
                if (dcht.parts is None and dcht.new_parts is not None and dcht.act_kind == DecreeChangeKind.UNDEFINED): 
                    if (last_change is not None and last_change.kind == DecreeChangeKind.APPEND): 
                        dcht.act_kind = DecreeChangeKind.APPEND
                        dcht.real_part = (Utils.asObjectOrNull(last_change.parent_referent, DecreePartReferent))
                    elif (last_append2 is not None and last_append2.real_part is not None): 
                        dcht.act_kind = DecreeChangeKind.APPEND
                        dcht.real_part = last_append2.real_part
                if (dprs is not None and len(dprs) > 0): 
                    chrt = DecreeChangeToken.attach_referents(dprs[0], dcht)
                    if (chrt is None and expire_regime > 0): 
                        chrt = list()
                        dcr = DecreeChangeReferent._new1402((DecreeChangeKind.EXPIRE if expire_regime == 1 else DecreeChangeKind.SUSPEND))
                        chrt.append(ReferentToken(dcr, dcht.begin_token, dcht.end_token))
                    if (((chrt is None and dcht.act_kind == DecreeChangeKind.UNDEFINED and dcht.act_kind2 == DecreeChangeKind.UNDEFINED) and prev is not None and prev.kind == DecreeChangeKind.APPEND) and dcht.change_val is not None and prev_part is not None): 
                        dcht.act_kind = DecreeChangeKind.APPEND
                        if (dcht.new_parts is None): 
                            dcht.new_parts = dcht.parts
                        dcht.real_part = prev_part
                        dcht.parts = (None)
                        chrt = DecreeChangeToken.attach_referents(prev_part, dcht)
                elif (dcht.act_kind != DecreeChangeKind.EXPIRE): 
                    ee = False
                    if (dcht.part_typ == PartToken.ItemType.UNDEFINED): 
                        if (len(change_stack) == 0): 
                            ee = True
                            chrt = DecreeChangeToken.attach_referents(change_decree, dcht)
                        elif (prev_part is not None): 
                            ee = True
                            chrt = DecreeChangeToken.attach_referents(prev_part, dcht)
                    if (not ee): 
                        for ss in change_stack: 
                            if (ss._is_all_items_over_this_level(dcht.part_typ)): 
                                ee = True
                                chrt = DecreeChangeToken.attach_referents(ss, dcht)
                                break
                    if (not ee and change_decree is not None): 
                        dr = change_decree
                        if (prev_part is not None and prev_part.owner == dr): 
                            if (prev_part._is_all_items_over_this_level(dcht.part_typ)): 
                                dr = (prev_part)
                        ee = True
                        chrt = DecreeChangeToken.attach_referents(dr, dcht)
                    if (last_change is not None and not ee and len(last_change.owners) > 0): 
                        chrt = DecreeChangeToken.attach_referents(last_change.owners[0], dcht)
                if ((dprs is None and chrt is None and ((dcht.typ == DecreeChangeTokenTyp.VALUE or dcht.change_val is not None))) and len(change_stack) > 0): 
                    chrt = DecreeChangeToken.attach_referents((dcht.real_part if dcht.real_part is not None else ((change_stack[0] if prev_part is None or (isinstance(change_stack[0], DecreePartReferent)) else prev_part))), dcht)
                if (chrt is None and ((expire_regime > 0 or dcht.act_kind == DecreeChangeKind.EXPIRE or dcht.act_kind == DecreeChangeKind.SUSPEND)) and dprs is None): 
                    chrt = list()
                    if (dcht.decree is not None): 
                        dcr = DecreeChangeReferent._new1402(DecreeChangeKind.EXPIRE)
                        dcr.add_slot(DecreeChangeReferent.ATTR_OWNER, dcht.decree, False, 0)
                        chrt.append(ReferentToken(dcr, dcht.begin_token, dcht.end_token))
                    tt = dcht.end_token.next0_
                    first_pass3954 = True
                    while True:
                        if first_pass3954: first_pass3954 = False
                        else: tt = tt.next0_
                        if (not (tt is not None)): break
                        if (tt.next0_ is None): 
                            break
                        if (tt.is_char_of("(<")): 
                            br = BracketHelper.try_parse(tt, BracketParseAttr.NO, 100)
                            if (br is not None): 
                                tt = br.end_token
                                chrt[len(chrt) - 1].end_token = tt
                                continue
                        if (not tt.is_comma_and and not tt.is_char(';')): 
                            if (len(chrt) > 0): 
                                break
                        else: 
                            tt = tt.next0_
                        if (isinstance(tt.get_referent(), DecreeReferent)): 
                            dcr = DecreeChangeReferent._new1402((DecreeChangeKind.EXPIRE if expire_regime == 1 or dcht.act_kind == DecreeChangeKind.EXPIRE else DecreeChangeKind.SUSPEND))
                            dcr.add_slot(DecreeChangeReferent.ATTR_OWNER, tt.get_referent(), False, 0)
                            rt = ReferentToken(dcr, tt, tt)
                            if (tt.next0_ is not None and tt.next0_.is_char('(')): 
                                br = BracketHelper.try_parse(tt.next0_, BracketParseAttr.NO, 100)
                                if (br is not None): 
                                    tt = br.end_token
                                    rt.end_token = tt
                            chrt.append(rt)
                            continue
                        break
                if (chrt is None and dcht.decree is not None and root_change is None): 
                    if (root_change_ques is not None and root_change_ques.decree == dcht.decree and root_change_ques.typ == DecreeChangeTokenTyp.STARTMULTU): 
                        pass
                    else: 
                        root_change_ques = dcht
                if (chrt is not None): 
                    if (((dprs is not None and len(dprs) == 2 and len(chrt) == 2) and (isinstance(chrt[0].referent, DecreeChangeValueReferent)) and (isinstance(chrt[1].referent, DecreeChangeReferent))) and chrt[1].referent.kind == DecreeChangeKind.NEW): 
                        vals = DecreeChangeToken.split_value(chrt[0], dprs[0])
                        diap = None
                        if (diaps is None): 
                            diap = list()
                            diap.append(dprs[0])
                            diap.append(dprs[1])
                        elif (len(diaps) == 1): 
                            for kp in diaps.items(): 
                                diap = PartToken.try_create_between(kp[0], kp[1])
                                if (diap is not None): 
                                    diap.insert(0, dprs[0])
                                    diap.append(dprs[1])
                                break
                        if (diap is not None and vals is not None and len(vals) == len(diap)): 
                            i = 0
                            while i < len(diap): 
                                drc = DecreeChangeReferent()
                                drc.kind = DecreeChangeKind.NEW
                                if (i > 0 and ((i + 1) < len(diap))): 
                                    diap[i] = (Utils.asObjectOrNull(ad.register_referent(diap[i]), DecreePartReferent))
                                drc.add_slot(DecreeChangeReferent.ATTR_OWNER, diap[i], False, 0)
                                drc.add_slot(DecreeChangeReferent.ATTR_VALUE, vals[i].referent, False, 0)
                                rt = ReferentToken(drc, vals[i].begin_token, vals[i].end_token)
                                if (i == 0): 
                                    rt.begin_token = chrt[1].begin_token
                                else: 
                                    drc.add_slot("SPLIT", "true", False, 0)
                                vals.append(rt)
                                i += 1
                            chrt = vals
                            diaps = (None)
                            dprs = (None)
                    for rt in chrt: 
                        rt.referent = ad.register_referent(rt.referent)
                        if (isinstance(rt.referent, DecreeChangeReferent)): 
                            last_change = (Utils.asObjectOrNull(rt.referent, DecreeChangeReferent))
                            if (dprs is not None and len(dprs) > 0): 
                                change_part = (Utils.asObjectOrNull(dprs[0].clone(), DecreePartReferent))
                                ii = 0
                                ii = 0
                                while ii < (len(dprs) - 1): 
                                    last_change.add_slot(DecreeChangeReferent.ATTR_OWNER, dprs[ii], False, 0)
                                    ii += 1
                                if (diaps is not None): 
                                    for kp in diaps.items(): 
                                        diap = PartToken.try_create_between(kp[0], kp[1])
                                        if (diap is not None and len(diap) > 0): 
                                            kp[0].add_slot("RANGE", "START", False, 0)
                                            kp[1].add_slot("RANGE", "END", False, 0)
                                            for d in diap: 
                                                d.add_slot("RANGE", "MIDDLE", False, 0)
                                                dd = ad.register_referent(d)
                                                last_change.add_slot(DecreeChangeReferent.ATTR_OWNER, dd, False, 0)
                                while ii < len(dprs): 
                                    last_change.add_slot(DecreeChangeReferent.ATTR_OWNER, dprs[ii], False, 0)
                                    ii += 1
                        if (rt.begin_token is None or rt.end_token is None): 
                            continue
                        if (begs is not None and rt.begin_char in begs): 
                            rt.begin_token = begs[rt.begin_char]
                        if (ends is not None and rt.end_char in ends): 
                            rt.end_token = ends[rt.end_char]
                        if (root_change is None and root_change_ques is not None): 
                            rch = Utils.asObjectOrNull(ad.register_referent(DecreeChangeReferent._new1402(DecreeChangeKind.CONTAINER)), DecreeChangeReferent)
                            rch.add_slot(DecreeChangeReferent.ATTR_OWNER, root_change_ques.decree, False, 0)
                            root_change = ReferentToken(rch, root_change_ques.begin_token, root_change_ques.end_token)
                            if (root_change.end_token.is_char(':')): 
                                root_change.end_token = root_change.end_token.previous
                            kit.embed_token(root_change)
                            root_change_ques = (None)
                        if (root_change is not None and (isinstance(rt.referent, DecreeChangeReferent))): 
                            root_change.referent.add_slot(DecreeChangeReferent.ATTR_CHILD, rt.referent, False, 0)
                        kit.embed_token(rt)
                        t = (rt)
                        if (begs is None): 
                            begs = dict()
                        if (not t.begin_char in begs): 
                            begs[t.begin_char] = t
                        else: 
                            begs[t.begin_char] = t
                        if (ends is None): 
                            ends = dict()
                        if (not t.end_char in ends): 
                            ends[t.end_char] = t
                        else: 
                            ends[t.end_char] = t
    
    @staticmethod
    def _can_be_start_of_attach_approved(t : 'Token') -> 'Token':
        from pullenti.ner.decree.internal.PartToken import PartToken
        from pullenti.ner.decree.internal.DecreeToken import DecreeToken
        if (not (isinstance(t, TextToken))): 
            return None
        if (BracketHelper.can_be_start_of_sequence(t, True, False)): 
            if (t.next0_ is None): 
                return None
            if (t.next0_.chars.is_all_lower or not t.next0_.chars.is_letter): 
                return None
            return t
        if (isinstance(t, NumberToken)): 
            return None
        tt = DecreeToken.is_keyword(t, False)
        doubt = False
        if (tt is None and ((t.is_value("СОСТАВ", None) or t.is_value("СРОК", None)))): 
            if (t.previous is not None and t.previous.is_value("В", None)): 
                tt = t
                doubt = True
        key_tok = tt
        if (tt is not None): 
            if (t.is_value("НАСТОЯЩИЙ", None)): 
                return None
            if (t.is_value("ПЕРЕЧЕНЬ", None) and t.is_newline_before): 
                return None
            mc0 = t.get_morph_class_in_dictionary()
            if (mc0.is_pronoun): 
                return None
            tt = t
        changes = False
        if (tt is None or tt.next0_ is None): 
            if ((t.is_value("ИЗМЕНЕНИЕ", None) and (((isinstance(t.previous, NumberToken)) or t.is_newline_before)) and t.next0_ is not None) and t.next0_.is_comma): 
                tt1 = t.next0_.next0_
                if (tt1.is_value3("КОТОРЫЙ", "ВНОСИТЬСЯ", "В")): 
                    if (not t.is_newline_before or t.chars.is_all_lower): 
                        return t
                    tt = tt1.next0_.next0_.next0_
                    changes = True
                elif (tt1.is_value2("ВНОСИМЫЙ", "В")): 
                    tt1 = tt1.next0_.next0_
                    changes = True
                else: 
                    return None
            else: 
                return None
        else: 
            cou2 = 7
            if (doubt): 
                cou2 = 2
            tt2 = t.previous
            while tt2 is not None and cou2 > 0: 
                if ((tt2.is_value("ВНЕСТИ", None) or tt2.is_value("ВНОСИТЬ", None) or tt2.is_value("ИЗМЕНЕНИЕ", None)) or tt2.is_value("ДОПОЛНИТЬ", None) or tt2.is_value("ИЗЛОЖИТЬ", None)): 
                    changes = True
                    break
                if (tt2.is_newline_before): 
                    break
                if ((isinstance(tt2, NumberToken)) or tt2.length_char == 1): 
                    cou2 += 1
                pp = PartToken.try_attach(tt2, None, False, False)
                if (pp is not None and pp.end_token.next0_ == t): 
                    changes = True
                    break
                tt2 = tt2.previous; cou2 -= 1
        if (tt is None): 
            return None
        if (not changes): 
            if (not (isinstance(t, TextToken)) or not t.chars.is_cyrillic_letter or key_tok is None): 
                return None
            if (t.chars.is_all_lower): 
                if (t.previous is not None): 
                    if (t.previous.is_value("В", None) or t.previous.is_value("К", None)): 
                        if (key_tok.next0_ is not None and key_tok.next0_.is_comma): 
                            return None
                        return tt
                return None
        return tt
    
    @staticmethod
    def __check_changes_to(t : 'Token') -> 'Token':
        from pullenti.ner.decree.DecreeReferent import DecreeReferent
        if (t is not None and ((t.is_value("ПЕРЕЧЕНЬ", None) or t.is_value("СПИСОК", None)))): 
            t = t.next0_
        if (t is None or not t.is_value("ИЗМЕНЕНИЕ", None)): 
            return None
        t = t.next0_
        first_pass3955 = True
        while True:
            if first_pass3955: first_pass3955 = False
            else: t = t.next0_
            if (not (t is not None)): break
            if ((t.is_comma or t.is_value("КОТОРЫЙ", None) or t.is_value("ВНОСИТЬСЯ", None)) or t.is_value("ВНОСИМЫЙ", None) or t.is_value("В", None)): 
                continue
            if (isinstance(t.get_referent(), DecreeReferent)): 
                return t
            if (isinstance(t, ReferentToken)): 
                continue
            npt = NounPhraseHelper.try_parse(t, NounPhraseParseAttr.PARSEPREPOSITION, 0, None)
            if (npt is not None): 
                if (npt.end_token.is_value("РЕАЛИЗАЦИЯ", None) or npt.end_token.is_value("АКТ", None) or npt.end_token.is_value("ВОПРОС", None)): 
                    t = npt.end_token
                    continue
            if (t.previous.is_value("В", None)): 
                return t
            break
        return None
    
    @staticmethod
    def _try_attach_approved(t : 'Token', ad : 'AnalyzerData', aliases : 'TerminCollection'=None) -> 'ReferentToken':
        from pullenti.ner.decree.DecreeReferent import DecreeReferent
        from pullenti.ner.decree.internal.PartToken import PartToken
        from pullenti.ner.decree.internal.DecreeToken import DecreeToken
        if (t is None): 
            return None
        br = None
        if (BracketHelper.can_be_start_of_sequence(t, True, False)): 
            br = BracketHelper.try_parse(t, BracketParseAttr.NO, 100)
        elif ((isinstance(t.previous, TextToken)) and t.previous.length_char == 1 and BracketHelper.can_be_start_of_sequence(t.previous, True, False)): 
            br = BracketHelper.try_parse(t.previous, BracketParseAttr.NO, 100)
        if (br is not None): 
            if (br.length_char < 20): 
                return None
            rt0 = DecreeAnalyzer._try_attach_approved0(br.end_token.next0_, ad, False, True, aliases)
            if (rt0 is not None): 
                dr = Utils.asObjectOrNull(rt0.referent, DecreeReferent)
                rt0.begin_token = br.begin_token
                nam = MiscHelper.get_text_value_of_meta_token(br, GetTextAttr.RESTOREREGISTER)
                if (dr.typ is None): 
                    dt = DecreeToken.try_attach(br.begin_token.next0_, None, False)
                    if (dt is not None and dt.typ == DecreeToken.ItemType.TYP): 
                        dr.add_typ(dt)
                        if (dt.end_token.next0_ is not None and dt.end_token.next0_.is_value("О", None)): 
                            nam = MiscHelper.get_text_value(dt.end_token.next0_, br.end_token, GetTextAttr.RESTOREREGISTER)
                            br.begin_token = dt.end_token.next0_
                if (nam is not None): 
                    dr._add_name_str(nam, br)
                return rt0
        tt = DecreeAnalyzer._can_be_start_of_attach_approved(t)
        if (tt is None): 
            return None
        t = tt
        key_tok = DecreeToken.is_keyword(t, False)
        doubt = False
        if (key_tok is None and ((t.is_value("СОСТАВ", None) or t.is_value("СРОК", None) or t.is_value("ФОРМА", None)))): 
            key_tok = t
            doubt = True
        if (t.is_value("ГОСУДАРСТВЕННЫЙ", None)): 
            pass
        ch_tok = DecreeAnalyzer.__check_changes_to(t)
        if (ch_tok is not None and (isinstance(ch_tok.get_referent(), DecreeReferent))): 
            dr = Utils.asObjectOrNull(ch_tok.get_referent(), DecreeReferent)
            if (dr.owner is not None): 
                ch_tok.kit.debed_token(ch_tok)
        cou = 0
        alias = None
        aliast0 = None
        has_nl = False
        has_org = False
        has_verb = False
        last_tok = None
        keyword_after = ch_tok is not None
        has_wich = False
        has_register_after = False
        if ((t.previous is not None and t.previous.is_value("В", None) and t.previous.previous is not None) and t.previous.previous.is_value("ВНОСИТЬСЯ", None)): 
            keyword_after = True
        tt = tt.next0_
        first_pass3956 = True
        while True:
            if first_pass3956: first_pass3956 = False
            else: tt = tt.next0_
            if (not (tt is not None)): break
            cou += 1
            if (cou > 100): 
                break
            last_tok = tt
            if ((tt.is_comma_and or tt.is_char_of(";.") or BracketHelper.can_be_end_of_sequence(tt, False, None, False)) or tt.is_hiphen): 
                if (key_tok is not None and key_tok == tt.previous and not key_tok.is_value("СОСТАВ", None)): 
                    if (tt.next0_ is None): 
                        return None
                    mc0 = tt.next0_.get_morph_class_in_dictionary()
                    if (mc0.is_adjective): 
                        pass
                    else: 
                        return None
            if (tt.is_table_control_char): 
                break
            if ((isinstance(tt, TextToken)) and not tt.chars.is_letter and tt.length_char == 1): 
                if (not BracketHelper.is_bracket(tt, False) and not tt.is_char_of(",.:;№\\/") and not tt.is_hiphen): 
                    break
            if (tt.is_value2("ЯВЛЯЮЩИЙСЯ", "ПРИЛОЖЕНИЕМ") or tt.is_value2("ПРЕДУСМОТРЕННЫЙ", "ПРИЛОЖЕНИЕМ")): 
                keyword_after = True
                break
            if (tt.is_value("СЛЕДУЮЩИЙ", None)): 
                npt = NounPhraseHelper.try_parse(tt, NounPhraseParseAttr.NO, 0, None)
                if (npt is not None and npt.end_token.next0_ is not None and npt.end_token.next0_.is_char_of(":;")): 
                    keyword_after = True
                    if (key_tok is not None and key_tok.is_value("УСТАВ", None)): 
                        break
                    if (npt.end_token.is_value("ИЗМЕНЕНИЕ", None)): 
                        break
                    return None
            if (tt.is_value("КОТОРЫЙ", None)): 
                has_wich = True
            if (tt.is_newline_before): 
                if (tt.newlines_before_count > 1): 
                    break
                if (MiscHelper.check_image(tt) is not None): 
                    break
                if (isinstance(tt, NumberToken)): 
                    break
                if (tt.previous is not None and tt.previous.is_char_of(";.")): 
                    break
                if (tt.is_value("ИСТОЧНИК", None) or tt.is_value("ГАРАНТ", None) or tt.is_value("КОНСУЛЬТАНТПЛЮС", None)): 
                    break
                if (tt.is_char('(')): 
                    pass
                elif (not tt.chars.is_all_upper and tt.previous.chars.is_all_upper): 
                    break
                has_nl = True
                pp = PartToken.try_attach(tt, None, False, False)
                if (pp is not None): 
                    return None
            if ((((isinstance(tt, NumberToken)) and tt.value == "1")) or tt.is_value("ДРУГОЙ", None) or tt.is_value("ИНОЙ", None)): 
                if (tt.next0_ is not None and tt.next0_.is_value("СТОРОНА", None)): 
                    return None
            if (tt.is_char_of(":;")): 
                if (has_nl): 
                    break
                if (key_tok is not None and tt == key_tok.next0_): 
                    return None
                if (tt.is_newline_after): 
                    if (t.previous is not None and t.previous.is_value("В", None)): 
                        break
            if (tt.is_value2("В", "РЕДАКЦИИ")): 
                tt = tt.next0_
                continue
            if (tt.is_char('(') and tt.next0_ is not None): 
                dr1 = Utils.asObjectOrNull(tt.next0_.get_referent(), DecreeReferent)
                if (dr1 is not None): 
                    if (dr1.kind == DecreeKind.PUBLISHER): 
                        has_register_after = True
                        break
                tt0 = tt
                mt = DecreeAnalyzer._check_alias_after(tt)
                if (mt is not None): 
                    aliast0 = tt
                    alias = mt
                    tt = mt.end_token
                    if (tt.next0_ is not None and tt.next0_.is_comma_and and (t.end_char < tt0.previous.begin_char)): 
                        next0_ = DecreeAnalyzer._try_attach_approved(tt.next0_.next0_, ad, aliases)
                        if (next0_ is not None): 
                            nam = MiscHelper.get_text_value(t, tt0.previous, Utils.valToEnum((GetTextAttr.FIRSTNOUNGROUPTONOMINATIVE) | (GetTextAttr.RESTOREREGISTER), GetTextAttr))
                            if (nam is None or (len(nam) < 20) or len(nam) > 1000): 
                                return None
                            if (Utils.startsWithString(nam, "ПРАВИЛО ", True)): 
                                nam = ("Правила" + nam[7:])
                            elif (Utils.startsWithString(nam, "ОСНОВА ", True)): 
                                nam = ("Основы" + nam[6:])
                            dt = DecreeToken.try_attach(t, None, False)
                            dec0 = DecreeReferent()
                            if (dt is not None and dt.typ == DecreeToken.ItemType.TYP): 
                                dec0.add_typ(dt)
                            dec0._add_name_str(nam, MetaToken(t, tt0.previous))
                            dec0.owner = next0_.referent.owner
                            return ReferentToken._new952(dec0, t, tt, alias)
                    continue
            tok2 = DecreeToken.is_keyword(tt, False)
            if (tok2 is not None and tt.chars.is_capital_upper): 
                if (t.previous is not None and t.previous.is_value("В", None) and not has_verb): 
                    pass
                elif (not has_verb): 
                    pass
                else: 
                    break
            r = tt.previous.get_referent()
            if (r is not None and r.type_name == "ORGANIZATION" and tt == t.next0_): 
                has_org = True
            rt0 = DecreeAnalyzer._try_attach_approved0(tt, ad, True, False, aliases)
            if (rt0 is not None): 
                if (tt.is_char('(') and tt.next0_.is_value("ВВЕСТИ", None)): 
                    return None
                t1 = tt.previous
                if (aliast0 is not None): 
                    t1 = aliast0.previous
                if (t1.is_value("РЕДАКЦИЯ", None)): 
                    t1 = t1.previous
                if (t1.is_value("В", None)): 
                    t1 = t1.previous
                t00 = t
                if (t == t1): 
                    return None
                nam = MiscHelper.get_text_value(t, t1, Utils.valToEnum((GetTextAttr.FIRSTNOUNGROUPTONOMINATIVE) | (GetTextAttr.RESTOREREGISTER), GetTextAttr))
                if (nam is None): 
                    return None
                if (len(nam) > 1000): 
                    return None
                if (t.next0_ == t1 and (len(nam) < 20)): 
                    return None
                if (Utils.startsWithString(nam, "ПРАВИЛО ", True)): 
                    nam = ("Правила" + nam[7:])
                elif (Utils.startsWithString(nam, "ОСНОВА ", True)): 
                    nam = ("Основы" + nam[6:])
                dt = DecreeToken.try_attach(t, None, False)
                dec = Utils.asObjectOrNull(rt0.referent, DecreeReferent)
                if (dt is not None and dt.typ == DecreeToken.ItemType.TYP and rt0.referent.typ is None): 
                    dec.add_typ(dt)
                    if (dt.end_token.next0_ is not None and dt.end_token.next0_.is_value("О", "ПРО")): 
                        dec._add_name_str(nam, MetaToken(t00, t1))
                        t00 = dt.end_token.next0_
                        nam = MiscHelper.get_text_value(t00, t1, GetTextAttr.RESTOREREGISTER)
                    elif (t.is_value("КОНСТИТУЦИЯ", None)): 
                        nam = (None)
                if (nam is not None): 
                    dec._add_name_str(nam, (MetaToken(t00, t1) if t00.begin_char <= t1.begin_char else None))
                if (len(dec.slots) < 2): 
                    return None
                rt0.begin_token = t
                rt0.tag = (alias)
                if (dec.find_slot(DecreeReferent.ATTR_SOURCE, None, True) is None): 
                    if (t.previous is not None and t.previous.is_value("В", None) and (isinstance(t.previous.previous, ReferentToken))): 
                        if (isinstance(t.previous.previous.get_referent(), OrganizationReferent)): 
                            ss = dec.add_slot(DecreeReferent.ATTR_SOURCE, t.previous.previous.get_referent(), False, 0)
                            ss.add_annotation(Utils.asObjectOrNull(t.previous.previous, ReferentToken))
                return rt0
            br1 = BracketHelper.try_parse(tt, BracketParseAttr.NO, 100)
            if (br1 is not None): 
                tt = br1.end_token
                continue
            if (tt.is_char('.')): 
                break
            if (tt.is_newline_before and tt.previous is not None and tt.previous.is_char('.')): 
                break
            no_verb = False
            if ((isinstance(tt, TextToken)) and not has_wich): 
                if (tt.is_pure_verb): 
                    if (tt.previous.is_value("КОТОРЫЙ", None)): 
                        no_verb = True
                    elif (tt.morph.contains_attr("инф.", None)): 
                        no_verb = True
                    elif (tt.is_value("ПРИМЕНЯТЬСЯ", None)): 
                        no_verb = True
                    elif (tt.term.endswith("СЯ")): 
                        no_verb = True
                    else: 
                        break
            mc = tt.get_morph_class_in_dictionary()
            if ((mc.is_verb and not mc.is_adjective and not mc.is_preposition) and not no_verb): 
                if (tt.is_value("ВНОСИТЬСЯ", None)): 
                    pass
                else: 
                    has_verb = True
            if (has_org): 
                break
        if (((tt is not None or ((last_tok is not None and (cou < 30))))) and key_tok is not None and ((not t.chars.is_all_lower or ((t.previous is not None and t.previous.is_value("В", None)))))): 
            if (t.previous is not None and t.previous.is_value("ТЕКСТ", None)): 
                return None
            if (t.chars.is_all_lower and not keyword_after and not has_register_after): 
                return None
            cou = 500
            if (tt is None): 
                tt = last_tok.previous
            if (t.previous is None or t.begin_char >= tt.previous.begin_char): 
                return None
            typ = key_tok.get_normal_case_text(MorphClass.NOUN, MorphNumber.UNDEFINED, MorphGender.UNDEFINED, False)
            if (typ == "ПРАВИЛО"): 
                typ = "ПРАВИЛА"
            elif (typ == "ОСНОВА"): 
                typ = "ОСНОВЫ"
            nam = None
            nam2 = None
            ttt = t.previous
            first_pass3957 = True
            while True:
                if first_pass3957: first_pass3957 = False
                else: ttt = ttt.previous; cou -= 1
                if (not (ttt is not None and cou > 0)): break
                dr = Utils.asObjectOrNull(ttt.get_referent(), DecreeReferent)
                if (dr is None): 
                    continue
                if (dr.kind == DecreeKind.PUBLISHER): 
                    continue
                if (nam is None): 
                    nam = MiscHelper.get_text_value(t, tt.previous, GetTextAttr.FIRSTNOUNGROUPTONOMINATIVE)
                    if (nam is not None): 
                        if (nam.startswith("ПРАВИЛО")): 
                            nam2 = ("ПРАВИЛА" + nam[7:])
                        if (nam.startswith("ОСНОВА")): 
                            nam2 = ("ОСНОВЫ" + nam[6:])
                if (not dr.check_typename(typ)): 
                    ok = has_register_after
                    if ((last_tok is not None and last_tok.is_char(':') and last_tok.is_newline_after) and not doubt): 
                        ok = True
                    if (ok): 
                        dd = DecreeReferent()
                        dd._add_name_str(Utils.ifNotNull(nam2, nam), MetaToken(t, tt.previous))
                        if (dr.owner is not None): 
                            dd.owner = dr.owner
                        else: 
                            dd.owner = dr
                        return ReferentToken(dd, t, tt.previous)
                    continue
                if (dr.find_slot(DecreeReferent.ATTR_NAME, nam, True) is not None): 
                    return ReferentToken(dr, t, tt.previous)
                if (nam2 is not None and dr.find_slot(DecreeReferent.ATTR_NAME, nam2, True) is not None): 
                    return ReferentToken(dr, t, tt.previous)
                nnn = nam
                k = 1
                first_pass3958 = True
                while True:
                    if first_pass3958: first_pass3958 = False
                    else: k += 1
                    if (not (k < 5)): break
                    ii = nnn.rfind(',')
                    if (ii < 0): 
                        break
                    nnn = nnn[0:0+ii].strip()
                    if (dr.find_slot(DecreeReferent.ATTR_NAME, nnn, True) is None): 
                        continue
                    tte = tt.previous
                    while tte is not None: 
                        if (tte.is_comma): 
                            k -= 1
                            if (k == 0): 
                                if (t.begin_char <= tte.previous.begin_char): 
                                    return ReferentToken(dr, t, tte.previous)
                        tte = tte.previous
                    break
                if (dr.name is not None): 
                    term = Termin(dr.name)
                    tok = term.try_parse(t, TerminParseAttr.NO)
                    if (tok is not None): 
                        return ReferentToken(dr, t, tok.end_token)
                    nam0 = dr.name
                    i = 0
                    while (i < len(nam0)) and (i < len(nam)): 
                        if (nam0[i] != nam[i]): 
                            if (i >= 50): 
                                return ReferentToken(dr, t, tt.previous)
                            break
                        i += 1
            if (key_tok is not None and key_tok.is_value("УСТАВ", None) and key_tok.next0_ == tt.previous): 
                if ((isinstance(tt.previous.get_referent(), GeoReferent)) or (isinstance(tt.previous.get_referent(), OrganizationReferent))): 
                    nam = MiscHelper.get_text_value(t, tt.previous, GetTextAttr.FIRSTNOUNGROUPTONOMINATIVE)
                    dr = DecreeReferent()
                    dr.add_slot(DecreeReferent.ATTR_TYPE, "УСТАВ", False, 0)
                    dr.add_slot(DecreeReferent.ATTR_NAME, nam, False, 0)
                    return ReferentToken(dr, t, tt.previous)
        return None
    
    @staticmethod
    def _try_attach_approved0(t : 'Token', ad : 'AnalyzerData', must_be_comma : bool=True, name_in_brackets : bool=False, aliases : 'TerminCollection'=None) -> 'ReferentToken':
        from pullenti.ner.decree.DecreeReferent import DecreeReferent
        from pullenti.ner.decree.internal.DecreeToken import DecreeToken
        if (t is None): 
            return None
        if (isinstance(t.get_referent(), DecreeReferent)): 
            rt0 = DecreeAnalyzer._try_attach_approved0(t.begin_token, ad, True, False, None)
            if (rt0 is not None and rt0.end_char == t.end_char): 
                return ReferentToken(rt0.referent, t, t)
        if (t.next0_ is None): 
            return None
        t0 = t
        if (not t.is_char_of("(,") and not t.is_hiphen): 
            if (must_be_comma): 
                return None
        else: 
            t = t.next0_
        ok = False
        first_pass3959 = True
        while True:
            if first_pass3959: first_pass3959 = False
            else: t = t.next0_
            if (not (t is not None)): break
            if (t.is_comma_and or t.morph.class0_.is_preposition): 
                continue
            if ((isinstance(t.get_referent(), GeoReferent)) and t.get_referent().is_city): 
                continue
            if ((((((((t.is_value("УТВ", None) or t.is_value("УТВЕРЖДАТЬ", "СТВЕРДЖУВАТИ") or t.is_value("УТВЕРДИТЬ", "ЗАТВЕРДИТИ")) or t.is_value("УТВЕРЖДЕННЫЙ", "ЗАТВЕРДЖЕНИЙ") or t.is_value("РАТИФИЦИРОВАННЫЙ", None)) or t.is_value("ЗАТВЕРДЖУВАТИ", None) or t.is_value("СТВЕРДИТИ", None)) or t.is_value("ЗАТВЕРДИТИ", None) or t.is_value("ПРИНЯТЬ", "ПРИЙНЯТИ")) or t.is_value("ПРИНЯТЫЙ", "ПРИЙНЯТИЙ") or t.is_value("ВВОДИТЬ", "ВВОДИТИ")) or t.is_value("ВВЕСТИ", None) or t.is_value("ВВЕДЕННЫЙ", "ВВЕДЕНИЙ")) or t.is_value("ПОДПИСАТЬ", "ПІДПИСАТИ") or t.is_value("ПОДПИСЫВАТЬ", "ПІДПИСУВАТИ")) or t.is_value("ЗАКЛЮЧИТЬ", "УКЛАСТИ") or t.is_value("ЗАКЛЮЧАТЬ", "УКЛАДАТИ")): 
                ok = True
                if (t.next0_ is not None and t.next0_.is_char('.')): 
                    t = t.next0_
            elif (t.is_value("УСТАНОВЛЕННЫЙ", None)): 
                tt = t.previous
                if (tt is not None and tt.is_comma): 
                    tt = tt.previous
                if (tt is not None): 
                    if (tt.is_value("ПОРЯДОК", None)): 
                        break
                ok = True
            elif (t.is_value("ДЕЙСТВИЕ", None) or t.is_value("ДІЯ", None)): 
                pass
            elif (name_in_brackets and t0.is_hiphen): 
                ok = True
                break
            else: 
                break
        if (not ok): 
            return None
        if (t is None): 
            return None
        if (isinstance(t.get_referent(), DecreeReferent)): 
            dr = DecreeReferent()
            dr.owner = Utils.asObjectOrNull(t.get_referent(), DecreeReferent)
            if (dr.owner is None): 
                return None
            res0 = ReferentToken(dr, t, t)
            if (t0.is_char('(') and t.next0_ is not None and t.next0_.is_char(')')): 
                res0.end_token = t.next0_
            return res0
        kit = t.kit
        olev = None
        lev = 0
        wrapolev1408 = RefOutArgWrapper(None)
        inoutres1409 = Utils.tryGetValue(kit.misc_data, "dovr", wrapolev1408)
        olev = wrapolev1408.value
        if (not inoutres1409): 
            lev = 1
            kit.misc_data["dovr"] = lev
        else: 
            lev = (olev)
            if (lev > 2): 
                return None
            lev += 1
            kit.misc_data["dovr"] = (lev)
        try: 
            dts = DecreeToken.try_attach_list(t, None, 10, False)
            if (dts is None): 
                return None
            rt = DecreeAnalyzer._try_attach(dts, None, ad)
            if (rt is None): 
                has_date = 0
                has_num = 0
                has_own = 0
                has_typ = 0
                ii = 0
                ii = 0
                while ii < len(dts): 
                    if (dts[ii].typ == DecreeToken.ItemType.NUMBER): 
                        has_num += 1
                    elif ((dts[ii].typ == DecreeToken.ItemType.DATE and dts[ii].ref is not None and (isinstance(dts[ii].ref.referent, DateReferent))) and dts[ii].ref.referent.dt is not None): 
                        has_date += 1
                    elif (dts[ii].typ == DecreeToken.ItemType.OWNER or dts[ii].typ == DecreeToken.ItemType.ORG): 
                        has_own += 1
                    elif (dts[ii].typ == DecreeToken.ItemType.TYP): 
                        has_typ += 1
                    else: 
                        break
                    ii += 1
                if (ii >= len(dts) and has_own > 0 and ((has_date == 1 or has_num == 1))): 
                    dr = DecreeReferent()
                    for dt in dts: 
                        if (dt.typ == DecreeToken.ItemType.DATE): 
                            dr.add_date(dt)
                        elif (dt.typ == DecreeToken.ItemType.NUMBER): 
                            dr.add_number(dt)
                        elif (dt.typ == DecreeToken.ItemType.TYP): 
                            dr.add_slot(DecreeReferent.ATTR_TYPE, dt.value, False, 0)
                        else: 
                            val = dt.value
                            if (dt.ref is not None and dt.ref.referent is not None): 
                                val = (dt.ref.referent)
                            s = dr.add_slot(DecreeReferent.ATTR_SOURCE, val, False, 0)
                            s.tag = dt.get_source_text()
                            s.add_annotation(dt)
                            if (dt.ref is not None and (isinstance(dt.ref.referent, PersonPropertyReferent))): 
                                dr.add_ext_referent(dt.ref)
                    rt = list()
                    rt.append(ReferentToken(dr, dts[0].begin_token, dts[len(dts) - 1].end_token))
            if (((rt is None and len(dts) == 1 and dts[0].typ == DecreeToken.ItemType.DATE) and dts[0].ref is not None and (isinstance(dts[0].ref.referent, DateReferent))) and dts[0].ref.referent.dt is not None): 
                dr = DecreeReferent()
                dr.add_date(dts[0])
                rt = list()
                rt.append(ReferentToken(dr, dts[0].begin_token, dts[len(dts) - 1].end_token))
            if ((rt is None and len(dts) == 1 and dts[0].typ == DecreeToken.ItemType.TYP) and aliases is not None): 
                tok = aliases.try_parse(t, TerminParseAttr.NO)
                if (tok is not None): 
                    dr = DecreeReferent()
                    dr.owner = Utils.asObjectOrNull(tok.termin.tag, DecreeReferent)
                    rt = list()
                    rt.append(ReferentToken(dr, dts[0].begin_token, tok.end_token))
            if (rt is None): 
                return None
            if (t0.is_char('(') and rt[0].end_token.next0_ is not None and rt[0].end_token.next0_.is_char(')')): 
                rt[0].end_token = rt[0].end_token.next0_
            rt[0].begin_token = t0
            return rt[0]
        finally: 
            lev -= 1
            if (lev < 0): 
                lev = 0
            kit.misc_data["dovr"] = (lev)
    
    def __try_attach_pulishers(self, dts : typing.List['DecreeToken']) -> typing.List['ReferentToken']:
        from pullenti.ner.decree.DecreeReferent import DecreeReferent
        from pullenti.ner.decree.DecreePartReferent import DecreePartReferent
        from pullenti.ner.decree.internal.PartToken import PartToken
        from pullenti.ner.decree.internal.DecreeToken import DecreeToken
        i = 0
        t1 = None
        typ = None
        geo = None
        org0_ = None
        date_ = None
        i = 0
        while i < len(dts): 
            if (dts[i].typ == DecreeToken.ItemType.TYP and DecreeToken.get_kind(dts[i].value, None) == DecreeKind.PUBLISHER): 
                typ = dts[i]
                if (dts[i].ref is not None and (isinstance(dts[i].ref.get_referent(), GeoReferent))): 
                    geo = dts[i].ref
            elif (dts[i].typ == DecreeToken.ItemType.TERR): 
                geo = dts[i].ref
                t1 = dts[i].end_token
            elif (dts[i].typ == DecreeToken.ItemType.DATE): 
                date_ = dts[i]
                t1 = dts[i].end_token
            elif (dts[i].typ == DecreeToken.ItemType.ORG): 
                org0_ = dts[i].ref
                t1 = dts[i].end_token
            else: 
                break
            i += 1
        if (typ is None): 
            return None
        t = dts[i - 1].end_token.next0_
        if (t is None): 
            return None
        res = list()
        num = None
        t0 = dts[0].begin_token
        if (BracketHelper.can_be_end_of_sequence(t, False, None, False)): 
            t = t.next0_
            if (BracketHelper.can_be_start_of_sequence(t0.previous, False, False)): 
                t0 = t0.previous
        pub0 = None
        pub_part0 = None
        first_pass3960 = True
        while True:
            if first_pass3960: first_pass3960 = False
            else: t = t.next0_
            if (not (t is not None)): break
            if (t.is_char_of(",;.") or t.is_and): 
                continue
            dt = DecreeToken.try_attach(t, dts[0], False)
            if (dt is not None): 
                if (dt.typ == DecreeToken.ItemType.NUMBER): 
                    num = dt
                    pub0 = (None)
                    pub_part0 = (None)
                    if (t0 is None): 
                        t0 = t
                    t = dt.end_token
                    t1 = t
                    continue
                if (dt.typ == DecreeToken.ItemType.DATE): 
                    if (t0 is None): 
                        t0 = t
                    date_ = dt
                    pub0 = (None)
                    pub_part0 = (None)
                    t = dt.end_token
                    t1 = t
                    continue
                if (dt.typ != DecreeToken.ItemType.MISC and t.length_char > 2): 
                    break
            pt = PartToken.try_attach(t, None, False, False)
            if (pt is None and t.is_char('(')): 
                pt = PartToken.try_attach(t.next0_, None, False, False)
                if (pt is not None): 
                    if (pt.end_token.next0_ is not None and pt.end_token.next0_.is_char(')')): 
                        pt.end_token = pt.end_token.next0_
                    else: 
                        pt = (None)
            if (pt is not None): 
                if (pt.typ == PartToken.ItemType.PAGE): 
                    t = pt.end_token
                    continue
                if (pt.typ != PartToken.ItemType.CLAUSE and pt.typ != PartToken.ItemType.PART and pt.typ != PartToken.ItemType.PAGE): 
                    break
                if (num is None): 
                    break
                if (pub_part0 is not None): 
                    if (pt.typ == PartToken.ItemType.PART and pub_part0.part is None): 
                        pass
                    elif (pt.typ == PartToken.ItemType.CLAUSE and pub_part0.clause is None): 
                        pass
                    else: 
                        pub_part0 = (None)
                pub = pub0
                pub_part = pub_part0
                if (pub is None): 
                    pub = DecreeReferent()
                    pub.add_typ(typ)
                    if (geo is not None): 
                        ss = pub.add_slot(DecreeReferent.ATTR_GEO, geo.referent, False, 0)
                        ss.add_annotation(geo)
                    if (org0_ is not None): 
                        ss = pub.add_slot(DecreeReferent.ATTR_SOURCE, org0_.referent, False, 0)
                        ss.tag = org0_.get_source_text()
                        ss.add_annotation(org0_)
                    if (date_ is not None): 
                        pub.add_date(date_)
                    pub.add_number(num)
                    res.append(ReferentToken(pub, Utils.ifNotNull(t0, t), pt.begin_token.previous))
                if (pub_part is None): 
                    pub_part = DecreePartReferent._new1410(pub)
                    res.append(ReferentToken(pub_part, pt.begin_token, pt.end_token))
                pub0 = pub
                if (len(pt.values) == 1): 
                    if (pt.typ == PartToken.ItemType.CLAUSE): 
                        pub_part.add_slot(DecreePartReferent.ATTR_CLAUSE, pt.values[0].value, False, 0).tag = pt.values[0].source_value
                    elif (pt.typ == PartToken.ItemType.PART): 
                        pub_part.add_slot(DecreePartReferent.ATTR_PART, pt.values[0].value, False, 0).tag = pt.values[0].source_value
                elif (len(pt.values) > 1): 
                    ii = 0
                    while ii < len(pt.values): 
                        if (ii > 0): 
                            pub_part = DecreePartReferent._new1410(pub)
                            res.append(ReferentToken(pub_part, pt.values[ii].begin_token, pt.values[ii].end_token))
                        else: 
                            res[len(res) - 1].end_token = pt.values[ii].end_token
                        if (pt.typ == PartToken.ItemType.CLAUSE): 
                            pub_part.add_slot(DecreePartReferent.ATTR_CLAUSE, pt.values[ii].value, False, 0).tag = pt.values[ii].source_value
                        elif (pt.typ == PartToken.ItemType.PART): 
                            pub_part.add_slot(DecreePartReferent.ATTR_PART, pt.values[ii].value, False, 0).tag = pt.values[ii].source_value
                        ii += 1
                if (pub_part.clause == "6878"): 
                    pass
                pub_part0 = pub_part
                res[len(res) - 1].end_token = pt.end_token
                t0 = (None)
                t = pt.end_token
                continue
            if (isinstance(t, NumberToken)): 
                rt = t.kit.process_referent("DATE", t, None)
                if (rt is not None): 
                    date_ = DecreeToken._new1098(rt.begin_token, rt.end_token, DecreeToken.ItemType.DATE)
                    date_.ref = rt
                    pub0 = (None)
                    pub_part0 = (None)
                    if (t0 is None): 
                        t0 = t
                    t = rt.end_token
                    t1 = t
                    continue
                if (t.next0_ is not None and t.next0_.is_char(';')): 
                    if (pub_part0 is not None and pub_part0.clause is not None and pub0 is not None): 
                        pub_part = DecreePartReferent()
                        for s in pub_part0.slots: 
                            pub_part.add_slot(s.type_name, s.value, False, 0)
                        pub_part0 = pub_part
                        pub_part0.clause = str(t.value)
                        res.append(ReferentToken(pub_part0, t, t))
                        continue
            if (((isinstance(t, TextToken)) and t.chars.is_letter and (t.length_char < 3)) and (isinstance(t.next0_, NumberToken))): 
                t = t.next0_
                continue
            if ((t.is_char('(') and t.next0_ is not None and t.next0_.next0_ is not None) and t.next0_.next0_.is_char(')')): 
                t = t.next0_.next0_
                continue
            break
        if ((len(res) == 0 and date_ is not None and ((num is not None or typ.value.endswith("ГАЗЕТА")))) and t1 is not None): 
            pub = DecreeReferent()
            pub.add_typ(typ)
            if (geo is not None): 
                pub.add_slot(DecreeReferent.ATTR_GEO, geo.referent, False, 0)
            if (org0_ is not None): 
                pub.add_slot(DecreeReferent.ATTR_SOURCE, org0_.referent, False, 0).tag = org0_.get_source_text()
            if (date_ is not None): 
                pub.add_date(date_)
            pub.add_number(num)
            res.append(ReferentToken(pub, t0, t1))
        return res
    
    ANALYZER_NAME = "DECREE"
    """ Имя анализатора ("DECREE") """
    
    @property
    def name(self) -> str:
        return DecreeAnalyzer.ANALYZER_NAME
    
    @property
    def caption(self) -> str:
        return "Законы и указы"
    
    @property
    def description(self) -> str:
        return "Законы, указы, постановления, распоряжения и т.п."
    
    def clone(self) -> 'Analyzer':
        return DecreeAnalyzer()
    
    @property
    def type_system(self) -> typing.List['ReferentClass']:
        from pullenti.ner.decree.internal.MetaDecreePart import MetaDecreePart
        return [MetaDecree.GLOBAL_META, MetaDecreePart.GLOBAL_META, MetaDecreeChange.GLOBAL_META, MetaDecreeChangeValue.GLOBAL_META]
    
    @property
    def images(self) -> typing.List[tuple]:
        from pullenti.ner.decree.internal.MetaDecreePart import MetaDecreePart
        res = dict()
        res[MetaDecree.DECREE_IMAGE_ID] = PullentiNerCoreInternalResourceHelper.get_bytes("decree.png")
        res[MetaDecree.STANDADR_IMAGE_ID] = PullentiNerCoreInternalResourceHelper.get_bytes("decreestd.png")
        res[MetaDecreePart.PART_IMAGE_ID] = PullentiNerCoreInternalResourceHelper.get_bytes("part.png")
        res[MetaDecreePart.PART_LOC_IMAGE_ID] = PullentiNerCoreInternalResourceHelper.get_bytes("document_into.png")
        res[MetaDecree.PUBLISH_IMAGE_ID] = PullentiNerCoreInternalResourceHelper.get_bytes("publish.png")
        res[MetaDecreeChange.IMAGE_ID] = PullentiNerCoreInternalResourceHelper.get_bytes("decreechange.png")
        res[MetaDecreeChangeValue.IMAGE_ID] = PullentiNerCoreInternalResourceHelper.get_bytes("decreechangevalue.png")
        return res
    
    @property
    def used_extern_object_types(self) -> typing.List[str]:
        return [DateReferent.OBJ_TYPENAME, GeoReferent.OBJ_TYPENAME, OrganizationReferent.OBJ_TYPENAME, PersonReferent.OBJ_TYPENAME]
    
    def create_referent(self, type0_ : str) -> 'Referent':
        from pullenti.ner.decree.DecreeChangeReferent import DecreeChangeReferent
        from pullenti.ner.decree.DecreePartReferent import DecreePartReferent
        from pullenti.ner.decree.DecreeChangeValueReferent import DecreeChangeValueReferent
        from pullenti.ner.decree.DecreeReferent import DecreeReferent
        if (type0_ == DecreeReferent.OBJ_TYPENAME): 
            return DecreeReferent()
        if (type0_ == DecreePartReferent.OBJ_TYPENAME): 
            return DecreePartReferent()
        if (type0_ == DecreeChangeReferent.OBJ_TYPENAME): 
            return DecreeChangeReferent()
        if (type0_ == DecreeChangeValueReferent.OBJ_TYPENAME): 
            return DecreeChangeValueReferent()
        return None
    
    @property
    def progress_weight(self) -> int:
        return 10
    
    @staticmethod
    def get_data(t : 'Token') -> 'AnalyzerData':
        if (t is None): 
            return None
        return t.kit.get_analyzer_data_by_analyzer_name(DecreeAnalyzer.ANALYZER_NAME)
    
    def process(self, kit : 'AnalysisKit') -> None:
        from pullenti.ner.decree.DecreePartReferent import DecreePartReferent
        from pullenti.ner.decree.DecreeReferent import DecreeReferent
        from pullenti.ner.decree.internal.PartToken import PartToken
        from pullenti.ner.decree.internal.DecreeChangeToken import DecreeChangeToken
        from pullenti.ner.decree.internal.DecreeToken import DecreeToken
        ad = kit.get_analyzer_data(self)
        base_typ = None
        ref0 = None
        t = kit.first_token
        first_pass3961 = True
        while True:
            if first_pass3961: first_pass3961 = False
            else: t = t.next0_
            if (not (t is not None)): break
            r = t.get_referent()
            if (r is None): 
                continue
            if (not (isinstance(r, OrganizationReferent))): 
                continue
            rt = Utils.asObjectOrNull(t, ReferentToken)
            if (not rt.begin_token.chars.is_all_upper or rt.begin_token.length_char > 4): 
                continue
            dtr = DecreeToken.try_attach(rt.begin_token, None, False)
            if (dtr is None or dtr.typ_kind != DecreeKind.KODEX): 
                continue
            if (rt.begin_token == rt.end_token): 
                pass
            elif (rt.begin_token.next0_ == rt.end_token and (isinstance(rt.end_token.get_referent(), GeoReferent))): 
                pass
            else: 
                continue
            cou = 0
            tt = t.previous
            while tt is not None: 
                pt = PartToken.try_attach(tt, None, False, False)
                if (pt is not None and len(pt.values) > 0): 
                    t = kit.debed_token(rt)
                    break
                cou += 1
                if (cou > 10): 
                    break
                tt = tt.previous
        last_dec_dist = 0
        ignore_max_pos = 0
        t = kit.first_token
        first_pass3962 = True
        while True:
            if first_pass3962: first_pass3962 = False
            else: t = t.next0_; last_dec_dist += 1
            if (not (t is not None)): break
            if (t.is_newline_before and (isinstance(t, NumberToken)) and t.value == "88"): 
                pass
            if (t.is_ignored): 
                continue
            if (t.is_value2("СЛЕДУЮЩЕГО", "СОДЕРЖАНИЯ") or t.is_value2("СЛЕДУЮЩЕЙ", "РЕДАКЦИИ") or ((t.is_value2("НОВОЙ", "РЕДАКЦИИ") and t.next0_.next0_ is not None and t.next0_.next0_.is_char(':')))): 
                tt = t.next0_.next0_
                if (tt is not None and tt.is_char(':')): 
                    tt = tt.next0_
                if (BracketHelper.can_be_start_of_sequence(tt, True, False)): 
                    txt = DecreeChangeToken._try_parse_text(tt, False, False, None)
                    if (txt is not None): 
                        t = txt.end_token
                        continue
            if (t.is_value("СЛОВО", None) and BracketHelper.can_be_start_of_sequence(t.next0_, True, False)): 
                txt = DecreeChangeToken._try_parse_text(t.next0_, False, False, None)
                if (txt is not None): 
                    ignore_max_pos = txt.end_char
            if (t.is_value("УТВЕРЖДЕННЫЙ", None)): 
                pass
            dts = DecreeToken.try_attach_list(t, None, 10, last_dec_dist > 1000)
            if (dts is None or len(dts) == 0): 
                continue
            if (dts[0].is_newline_after and dts[0].is_newline_before): 
                ignore = False
                if (t == kit.first_token): 
                    ignore = True
                elif ((dts[0].typ == DecreeToken.ItemType.ORG and len(dts) > 1 and dts[1].typ == DecreeToken.ItemType.TYP) and dts[1].is_whitespace_after): 
                    ignore = True
                if (ignore): 
                    t = dts[len(dts) - 1].end_token
                    continue
            if (dts[0].typ == DecreeToken.ItemType.TYP and DecreeToken.get_kind(dts[0].value, None) == DecreeKind.PUBLISHER): 
                rts = self.__try_attach_pulishers(dts)
                if (rts is not None): 
                    i = 0
                    while i < len(rts): 
                        rtt = rts[i]
                        if (isinstance(rtt.referent, DecreePartReferent)): 
                            rtt.referent.owner = Utils.asObjectOrNull(ad.register_referent(rtt.referent.owner), DecreeReferent)
                        rtt.referent = ad.register_referent(rtt.referent)
                        if (rtt.begin_char < ignore_max_pos): 
                            rtt.tag = ("ignored")
                        kit.embed_token(rtt)
                        t = (rtt)
                        if ((isinstance(rtt.referent, DecreeReferent)) and ((i + 1) < len(rts)) and (isinstance(rts[i + 1].referent, DecreePartReferent))): 
                            rts[i + 1].begin_token = t
                        last_dec_dist = 0
                        i += 1
                    tt1 = t.next0_
                    if (tt1 is not None and tt1.is_char(')')): 
                        tt1 = tt1.next0_
                continue
            if (base_typ is None): 
                for dd in dts: 
                    if (dd.typ == DecreeToken.ItemType.TYP): 
                        base_typ = dd
                        break
            if ((len(dts) == 1 and dts[0].typ == DecreeToken.ItemType.TYP and dts[0].value != "КОНСТИТУЦИЯ") and not dts[0].typ_ref_back): 
                continue
            if (dts[0].value == "РЕГЛАМЕНТ"): 
                if (len(dts) < 3): 
                    continue
                if (dts[1].typ == DecreeToken.ItemType.TYP): 
                    continue
            rtli = DecreeAnalyzer._try_attach(dts, base_typ, ad)
            multi = False
            if ((rtli is None and len(dts) == 2 and dts[0].typ == DecreeToken.ItemType.TYP) and ((dts[1].typ == DecreeToken.ItemType.ORG or dts[1].typ == DecreeToken.ItemType.OWNER))): 
                tt2 = dts[1].end_token.next0_
                first_pass3963 = True
                while True:
                    if first_pass3963: first_pass3963 = False
                    else: tt2 = tt2.next0_
                    if (not (tt2 is not None)): break
                    if (tt2.is_char_of(";:-")): 
                        continue
                    if (tt2.is_newline_before): 
                        cn = ComplexNumToken.try_parse(tt2, None, False, False)
                        if (cn is not None): 
                            tt2 = cn.end_token.next0_
                        if (tt2 is None): 
                            break
                    dts2 = DecreeToken.try_attach_list(tt2, None, 4, False)
                    if (dts2 is None or len(dts2) != 3): 
                        break
                    if (dts2[2].typ != DecreeToken.ItemType.NAME): 
                        break
                    if (dts2[0].typ == DecreeToken.ItemType.NUMBER and dts2[1].typ == DecreeToken.ItemType.DATE): 
                        pass
                    elif (dts2[1].typ == DecreeToken.ItemType.NUMBER and dts2[0].typ == DecreeToken.ItemType.DATE): 
                        pass
                    else: 
                        break
                    ddd = list()
                    ddd.extend(dts)
                    ddd.extend(dts2)
                    rtli2 = DecreeAnalyzer._try_attach(ddd, base_typ, ad)
                    if (rtli2 is None or len(rtli2) != 1): 
                        break
                    rtli2[0].begin_token = tt2
                    if (rtli is None): 
                        rtli = list()
                    rtli.append(rtli2[0])
                    tt2 = rtli2[0].end_token
                    multi = True
            if (rtli is not None): 
                ii = 0
                while ii < len(rtli): 
                    rt = rtli[ii]
                    last_dec_dist = 0
                    dec0 = rt.referent
                    rt.referent = ad.register_referent(rt.referent)
                    if (not multi): 
                        jj = ii + 1
                        while jj < len(rtli): 
                            for s in rtli[jj].referent.slots: 
                                if (s.value == dec0): 
                                    s.value = rt.referent
                            jj += 1
                    ref0 = rt.referent
                    kit.embed_token(rt)
                    t = (rt)
                    if (rt.begin_char < ignore_max_pos): 
                        rt.tag = ("ignored")
                    if ((ii + 1) < len(rtli)): 
                        if (rt.end_token.next0_ == rtli[ii + 1].begin_token): 
                            rtli[ii + 1].begin_token = rt
                    ii += 1
            elif (len(dts) == 1 and dts[0].typ == DecreeToken.ItemType.TYP): 
                if (dts[0].chars.is_capital_upper and not dts[0].is_doubtful): 
                    last_dec_dist = 0
                    if (base_typ is not None and dts[0].ref is not None): 
                        drr = Utils.asObjectOrNull(dts[0].ref.get_referent(), DecreeReferent)
                        if (drr is not None): 
                            if (base_typ.value == drr.typ0 or base_typ.value == drr.typ): 
                                continue
                    rt0 = DecreeToken._find_back_typ(dts[0].begin_token.previous, dts[0].value)
                    if (rt0 is not None): 
                        rt = ReferentToken(rt0.referent, dts[0].begin_token, dts[0].end_token)
                        kit.embed_token(rt)
                        t = (rt)
                        rt.tag = (rt0.referent)
        if (len(ad.referents) > 0): 
            t = kit.first_token
            first_pass3964 = True
            while True:
                if first_pass3964: first_pass3964 = False
                else: t = t.next0_
                if (not (t is not None)): break
                if (t.is_ignored): 
                    continue
                dr = Utils.asObjectOrNull(t.get_referent(), DecreeReferent)
                if (dr is None): 
                    continue
                li = None
                tt = t.next0_
                while tt is not None: 
                    if (not tt.is_comma_and): 
                        break
                    if (tt.next0_ is None or not (isinstance(tt.next0_.get_referent(), DecreeReferent))): 
                        break
                    if (li is None): 
                        li = list()
                        li.append(dr)
                    dr = (Utils.asObjectOrNull(tt.next0_.get_referent(), DecreeReferent))
                    li.append(dr)
                    dr.tag = None
                    tt = tt.next0_
                    if (dr.date is not None): 
                        dts = DecreeToken.try_attach_list(tt.begin_token, None, 10, False)
                        if (dts is not None): 
                            for dt in dts: 
                                if (dt.typ == DecreeToken.ItemType.DATE): 
                                    dr.tag = (dr)
                    tt = tt.next0_
                if (li is None): 
                    continue
                i = 0
                for i in range(len(li) - 1, 0, -1):
                    if (li[i].typ == li[i - 1].typ): 
                        if (li[i].date is not None and li[i].tag is not None and li[i - 1].date is None): 
                            li[i - 1].add_slot(DecreeReferent.ATTR_DATE, li[i].get_slot_value(DecreeReferent.ATTR_DATE), False, 0)
                else: i = 0
                i = 0
                while i < (len(li) - 1): 
                    if (li[i].typ == li[i + 1].typ): 
                        sl = li[i].find_slot(DecreeReferent.ATTR_SOURCE, None, True)
                        if (sl is not None and li[i + 1].find_slot(DecreeReferent.ATTR_SOURCE, None, True) is None): 
                            li[i + 1].add_slot(sl.type_name, sl.value, False, 0)
                    i += 1
                i = 0
                while i < len(li): 
                    if (li[i].name is not None): 
                        break
                    i += 1
                if (i == (len(li) - 1)): 
                    for i in range(len(li) - 1, 0, -1):
                        if (li[i - 1].typ == li[i].typ): 
                            li[i - 1]._add_name(li[i])
                    else: i = 0
        aliases = TerminCollection()
        t = kit.first_token
        first_pass3965 = True
        while True:
            if first_pass3965: first_pass3965 = False
            else: t = t.next0_; last_dec_dist += 1
            if (not (t is not None)): break
            if (t.is_ignored): 
                continue
            if (t.is_value2("СЛЕДУЮЩЕГО", "СОДЕРЖАНИЯ") or t.is_value2("СЛЕДУЮЩЕЙ", "РЕДАКЦИИ") or ((t.is_value2("НОВОЙ", "РЕДАКЦИИ") and t.next0_.next0_ is not None and t.next0_.next0_.is_char(':')))): 
                tt = t.next0_.next0_
                if (tt is not None and tt.is_char(':')): 
                    tt = tt.next0_
                if (BracketHelper.can_be_start_of_sequence(tt, True, False)): 
                    txt = DecreeChangeToken._try_parse_text(tt, False, False, None)
                    if (txt is not None): 
                        t = txt.end_token
                        continue
            if (t.is_value("СЛОВО", None) and BracketHelper.can_be_start_of_sequence(t.next0_, True, False)): 
                txt = DecreeChangeToken._try_parse_text(t.next0_, False, False, None)
                if (txt is not None): 
                    t = txt.end_token
                    continue
            check_alias_token = None
            rt = DecreeAnalyzer._try_attach_approved(t, ad, aliases)
            if (t.is_value("СОСТАВ", None)): 
                pass
            if (rt is not None): 
                rt.referent = ad.register_referent(rt.referent)
                kit.embed_token(rt)
                t = (rt)
                if (isinstance(rt.tag, MetaToken)): 
                    term = Termin()
                    term.init_by(rt.tag.begin_token, rt.tag.end_token.previous, rt.referent, False)
                    aliases.add(term)
            if (isinstance(t.get_referent(), DecreeReferent)): 
                rt = (Utils.asObjectOrNull(t, ReferentToken))
                if (rt.referent.kind == DecreeKind.PUBLISHER): 
                    continue
                if ((t.next0_ is not None and t.next0_.is_char_of("(,") and (isinstance(t.next0_.next0_, ReferentToken))) and (isinstance(t.next0_.next0_.get_referent(), DecreeReferent)) and t.next0_.next0_.get_referent().kind == DecreeKind.PUBLISHER): 
                    check_alias_token = t.next0_.next0_.next0_
                    if (check_alias_token is not None and check_alias_token.is_char(')')): 
                        check_alias_token = check_alias_token.next0_
            elif (isinstance(t, TextToken)): 
                tok = aliases.try_parse(t, TerminParseAttr.NO)
                if (tok is not None): 
                    dec0 = Utils.asObjectOrNull(tok.termin.tag, DecreeReferent)
                    rt0 = ReferentToken(Utils.asObjectOrNull(tok.termin.tag, Referent), tok.begin_token, tok.end_token)
                    if (dec0 is not None and (isinstance(rt0.end_token.next0_, ReferentToken)) and (isinstance(rt0.end_token.next0_.get_referent(), GeoReferent))): 
                        geo0 = Utils.asObjectOrNull(dec0.get_slot_value(DecreeReferent.ATTR_GEO), GeoReferent)
                        geo1 = Utils.asObjectOrNull(rt0.end_token.next0_.get_referent(), GeoReferent)
                        if (geo0 is None): 
                            dec0.add_slot(DecreeReferent.ATTR_GEO, geo1, False, 0)
                            rt0.end_token = rt0.end_token.next0_
                        elif (geo0 == geo1): 
                            rt0.end_token = rt0.end_token.next0_
                        else: 
                            continue
                    kit.embed_token(rt0)
                    t = (rt0)
                    rt0.misc_attrs = 1
                    last_dec_dist = 0
                    continue
                dts = DecreeToken.try_attach_list(t, None, 2, False)
                if (dts is not None and dts[0].typ == DecreeToken.ItemType.TYP): 
                    rtli = DecreeAnalyzer._try_attach(dts, None, ad)
                    if (rtli is not None and len(rtli) == 1): 
                        rt = rtli[0]
                        rt.referent = ad.register_referent(rt.referent)
                        kit.embed_token(rt)
                        t = (rt)
            if (rt is not None): 
                mt = DecreeAnalyzer._check_alias_after(Utils.ifNotNull(check_alias_token, t.next0_))
                if (mt is not None): 
                    if (isinstance(mt.tag, DecreeReferent)): 
                        if (rt.referent != (Utils.asObjectOrNull(mt.tag, DecreeReferent))): 
                            kit.replace_referent(Utils.asObjectOrNull(mt.tag, DecreeReferent), rt.referent)
                        if (check_alias_token is None): 
                            rt = ReferentToken(t.get_referent(), t, mt.end_token)
                            kit.embed_token(rt)
                            t = (rt)
                    else: 
                        etok = mt.end_token.previous
                        if ((mt.begin_token.next0_ is not None and mt.begin_token.next0_.is_comma_and and mt.begin_token.next0_.next0_ == mt.end_token.previous.previous) and mt.end_token.previous.is_value("СООТВЕТСТВЕННО", None)): 
                            tt = Utils.asObjectOrNull(mt.begin_token.next0_.next0_, TextToken)
                            nam = Utils.ifNotNull(rt.referent.get_string_value("NAME"), "")
                            if (nam.startswith("ОБ УТВЕРЖДЕНИИ ") and tt is not None): 
                                ar0 = ProcessorService.get_empty_processor().process(SourceOfAnalysis(nam), None, None)
                                nam = MiscHelper.get_text_value(ar0.first_token.next0_.next0_, ar0.find_token_by_pos(len(nam) - 1, None), GetTextAttr.FIRSTNOUNGROUPTONOMINATIVE)
                                if (nam.startswith(tt.term)): 
                                    r1 = DecreeReferent()
                                    r1.owner = Utils.asObjectOrNull(rt.referent, DecreeReferent)
                                    r1.add_slot(DecreeReferent.ATTR_NAME, nam, False, 0)
                                    r1 = (Utils.asObjectOrNull(ad.register_referent(r1), DecreeReferent))
                                    rt1 = ReferentToken(r1, tt, tt)
                                    kit.embed_token(rt1)
                                    term1 = Termin()
                                    term1.init_by(tt, tt, r1, False)
                                    aliases.add(term1)
                                    etok = mt.begin_token.next0_
                        term = Termin()
                        term.init_by(mt.begin_token, etok, rt.referent, False)
                        aliases.add(term)
                        if (check_alias_token is None): 
                            rt = ReferentToken(t.get_referent(), t, mt.end_token)
                            kit.embed_token(rt)
                            t = (rt)
        self.__process_parts_and_changes(kit, base_typ)
        t = kit.first_token
        while t is not None: 
            if (t.tag is not None and (isinstance(t, ReferentToken)) and (isinstance(t.tag, DecreeReferent))): 
                t = kit.debed_token(t)
                if (t is None): 
                    break
            t = t.next0_
    
    @staticmethod
    def _check_alias_after(t : 'Token') -> 'MetaToken':
        from pullenti.ner.decree.DecreePartReferent import DecreePartReferent
        from pullenti.ner.decree.DecreeReferent import DecreeReferent
        if ((t is not None and t.is_char('<') and t.next0_ is not None) and t.next0_.next0_ is not None and t.next0_.next0_.is_char('>')): 
            t = t.next0_.next0_.next0_
        if (t is None or t.next0_ is None or not t.is_char('(')): 
            return None
        if (t.next0_.get_referent() is not None): 
            dr = Utils.asObjectOrNull(t.next0_.get_referent(), DecreeReferent)
            if (dr is None and (isinstance(t.next0_.get_referent(), DecreePartReferent))): 
                dr = t.next0_.get_referent().owner
            if (dr is not None and dr.kind == DecreeKind.PUBLISHER): 
                br = BracketHelper.try_parse(t, BracketParseAttr.NO, 100)
                if (br is not None and br.end_token.next0_ is not None and br.end_token.next0_.is_char('(')): 
                    t = br.end_token.next0_
                    if (t.next0_ is None): 
                        return None
        t = t.next0_
        if (t.is_value("ДАЛЕЕ", "ДАЛІ")): 
            pass
        else: 
            return None
        t = t.next0_
        if (t is not None and not t.chars.is_letter): 
            t = t.next0_
        if (t is None): 
            return None
        if ((isinstance(t.get_referent(), DecreeReferent)) and t.next0_ is not None and t.next0_.is_char(')')): 
            return MetaToken._new658(t, t.next0_, t.get_referent())
        t1 = None
        tt = t
        while tt is not None: 
            if (tt.is_newline_before): 
                break
            elif (tt.is_char(')')): 
                t1 = tt.previous
                break
            tt = tt.next0_
        if (t1 is None): 
            return None
        return MetaToken(t, t1.next0_)
    
    @staticmethod
    def _get_decree(t : 'Token') -> 'DecreeReferent':
        from pullenti.ner.decree.DecreePartReferent import DecreePartReferent
        from pullenti.ner.decree.DecreeReferent import DecreeReferent
        if (not (isinstance(t, ReferentToken))): 
            return None
        r = t.get_referent()
        if (isinstance(r, DecreeReferent)): 
            return Utils.asObjectOrNull(r, DecreeReferent)
        if (isinstance(r, DecreePartReferent)): 
            return r.owner
        return None
    
    @staticmethod
    def _check_other_typ(t : 'Token', first : bool) -> 'Token':
        from pullenti.ner.decree.internal.DecreeToken import DecreeToken
        if (t is None): 
            return None
        dit = DecreeToken.try_attach(t, None, False)
        npt = None
        if (dit is None): 
            npt = NounPhraseHelper.try_parse(t, NounPhraseParseAttr.NO, 0, None)
            if (npt is not None and npt.begin_token != npt.end_token): 
                dit = DecreeToken.try_attach(npt.end_token, None, False)
        if (dit is not None and dit.typ == DecreeToken.ItemType.TYP): 
            if (dit.chars.is_capital_upper or first): 
                dit.end_token.tag = (dit.value)
                return dit.end_token
            else: 
                return None
        if (npt is not None): 
            t = npt.end_token
        if (t.chars.is_capital_upper or first): 
            if (t.previous is not None and t.previous.is_char('.') and not first): 
                return None
            tt = DecreeToken.is_keyword(t, False)
            if (tt is not None): 
                return tt
        return None
    
    def process_referent(self, begin : 'Token', param : str) -> 'ReferentToken':
        from pullenti.ner.decree.internal.DecreeToken import DecreeToken
        rt = DecreeAnalyzer._try_attach_approved(begin, None, None)
        if (rt is not None): 
            return rt
        dpli = DecreeToken.try_attach_list(begin, None, 10, True)
        if (dpli is not None): 
            lii = DecreeAnalyzer._try_attach(dpli, None, None)
            if (lii is not None and len(lii) > 0): 
                return lii[0]
        dp = DecreeToken.try_attach(begin, None, False)
        if (dp is not None and dp.typ == DecreeToken.ItemType.TYP): 
            return ReferentToken(None, dp.begin_token, dp.end_token)
        return None
    
    M_INITED = None
    
    @staticmethod
    def initialize() -> None:
        from pullenti.ner.decree.internal.MetaDecreePart import MetaDecreePart
        from pullenti.ner.decree.internal.DecreeChangeToken import DecreeChangeToken
        from pullenti.ner.decree.internal.DecreeToken import DecreeToken
        if (DecreeAnalyzer.M_INITED): 
            return
        DecreeAnalyzer.M_INITED = True
        MetaDecree.initialize()
        MetaDecreePart.initialize()
        MetaDecreeChange.initialize()
        MetaDecreeChangeValue.initialize()
        try: 
            Termin.ASSIGN_ALL_TEXTS_AS_NORMAL = False
            DecreeChangeToken._initialize()
            DecreeToken.initialize()
            Termin.ASSIGN_ALL_TEXTS_AS_NORMAL = False
        except Exception as ex: 
            raise Utils.newException(ex.__str__(), ex)
        ProcessorService.register_analyzer(DecreeAnalyzer())
    
    @staticmethod
    def _try_attach_parts(parts : typing.List['PartToken'], base_typ : 'DecreeToken', _def_owner : 'Referent', in_changes : bool=False) -> typing.List['MetaToken']:
        from pullenti.ner.decree.DecreeChangeReferent import DecreeChangeReferent
        from pullenti.ner.decree.DecreePartReferent import DecreePartReferent
        from pullenti.ner.decree.DecreeReferent import DecreeReferent
        from pullenti.ner.decree.internal.PartToken import PartToken
        from pullenti.ner.decree.internal.DecreeToken import DecreeToken
        from pullenti.ner.instrument.internal.InstrToken1 import InstrToken1
        from pullenti.ner.instrument.internal.InstrToken import InstrToken
        if (parts is None or len(parts) == 0): 
            return None
        i = 0
        j = 0
        if (base_typ is not None): 
            if (base_typ.value == "ПОЛОЖЕНИЕ" or base_typ.value == "ОПРЕДЕЛЕНИЕ"): 
                base_typ = (None)
        jj = 0
        while jj < (len(parts) - 1): 
            if (parts[jj].typ == PartToken.ItemType.NAME and parts[jj].delim_after and ((jj == 0 or parts[jj - 1].delim_after))): 
                parts0 = list(parts)
                if (jj > 0): 
                    del parts0[0:0+jj]
                del parts0[0]
                res11 = DecreeAnalyzer._try_attach_parts(parts0, base_typ, _def_owner, in_changes)
                if (res11 is not None): 
                    named = list()
                    snamed = list()
                    for rr in res11: 
                        pli = Utils.asObjectOrNull(rr.tag, list)
                        if (pli is not None): 
                            for ppp in pli: 
                                pp2 = DecreePartReferent()
                                pp2.name_as_item = "0"
                                pp2._add_named_level_info(ppp)
                                if (not str(pp2) in snamed): 
                                    named.append(pp2)
                                    snamed.append(str(pp2))
                    res11.insert(0, MetaToken(parts[0].begin_token, parts[0].end_token))
                    res11[0].tag = (named)
                    if (jj > 0): 
                        parts0.clear()
                        parts0.extend(parts)
                        del parts0[jj:jj+len(parts) - jj]
                        res00 = DecreeAnalyzer._try_attach_parts(parts0, base_typ, _def_owner, False)
                        if (res00 is not None): 
                            res11[0:0] = res00
                    return res11
            jj += 1
        if ((parts[0].typ == PartToken.ItemType.NAME and parts[0].morph.number == MorphNumber.PLURAL and len(parts) > 2) and parts[1].delim_after): 
            res0 = list()
            i = 1
            while i < len(parts): 
                parts0 = list()
                j = i
                while j < len(parts): 
                    parts0.append(parts[j])
                    if (parts[j].delim_after): 
                        break
                    j += 1
                i = j
                res11 = DecreeAnalyzer._try_attach_parts(parts0, base_typ, _def_owner, in_changes)
                if (res11 is not None): 
                    for rr in res11: 
                        pli = Utils.asObjectOrNull(rr.tag, list)
                        if (pli is not None): 
                            for ppp in pli: 
                                ppp.name_as_item = "0"
                        if (rr.begin_token == parts[1].begin_token): 
                            rr.begin_token = parts[0].begin_token
                        res0.append(rr)
                i += 1
            return res0
        if (len(parts) == 1 and parts[0].typ == PartToken.ItemType.NAME and not in_changes): 
            return None
        tt = parts[len(parts) - 1].end_token.next0_
        if (_def_owner is not None and tt is not None): 
            if (BracketHelper.is_bracket(tt, False)): 
                br = BracketHelper.try_parse(tt, BracketParseAttr.NO, 100)
                if (br is not None and br.end_token.next0_ is not None): 
                    tt = br.end_token.next0_
            if (isinstance(tt.get_referent(), DecreeReferent)): 
                _def_owner = (None)
            elif (tt.is_value("К", None) and tt.next0_ is not None and (isinstance(tt.next0_.get_referent(), DecreeReferent))): 
                _def_owner = (None)
        if ((len(parts) == 1 and parts[0].is_newline_before and parts[0].begin_token.chars.is_letter) and not parts[0].begin_token.chars.is_all_lower): 
            t1 = parts[0].end_token.next0_
            br = BracketHelper.try_parse(t1, BracketParseAttr.NO, 100)
            if (br is not None): 
                t1 = br.end_token.next0_
            if (t1 is not None and (isinstance(t1.get_referent(), DecreeReferent)) and not parts[0].is_newline_after): 
                pass
            elif ((t1 is not None and t1.is_value("К", None) and t1.next0_ is not None) and (isinstance(t1.next0_.get_referent(), DecreeReferent)) and not parts[0].is_newline_after): 
                pass
            else: 
                li = InstrToken1.parse(parts[0].begin_token, True, None, 0, None, False, 0, False, False)
                if (li is not None and li.has_verb): 
                    if ((len(parts) == 1 and parts[0].typ == PartToken.ItemType.PART and "резолют" in str(parts[0])) and parts[0].is_newline_before): 
                        return None
                else: 
                    return None
        this_dec = None
        is_program = False
        is_add_agree = False
        if (parts[len(parts) - 1].typ != PartToken.ItemType.SUBPROGRAM and parts[len(parts) - 1].typ != PartToken.ItemType.ADDAGREE): 
            this_dec = DecreeAnalyzer.ThisDecree.try_attach(parts[len(parts) - 1], base_typ)
            if (this_dec is not None): 
                if (this_dec.check_decree(Utils.asObjectOrNull(_def_owner, DecreeReferent))): 
                    pass
                elif ((isinstance(_def_owner, DecreeReferent)) and ((parts[0].typ == PartToken.ItemType.APPENDIX or parts[len(parts) - 1].typ == PartToken.ItemType.APPENDIX))): 
                    pass
                else: 
                    _def_owner = (None)
            if (this_dec is None and _def_owner is None): 
                this_dec = DecreeAnalyzer.ThisDecree.try_attach_back(parts[0].begin_token, base_typ)
            if (this_dec is None and parts[0].typ == PartToken.ItemType.NAME and not in_changes): 
                return None
            if (this_dec is None): 
                for p in parts: 
                    if (p.typ == PartToken.ItemType.PART): 
                        has_clause = False
                        for pp in parts: 
                            if (pp != p): 
                                if (PartToken._get_rank(pp.typ) >= PartToken._get_rank(PartToken.ItemType.CLAUSE)): 
                                    has_clause = True
                        if (isinstance(_def_owner, DecreePartReferent)): 
                            if (_def_owner.clause is not None): 
                                has_clause = True
                        if (not has_clause): 
                            p.typ = PartToken.ItemType.DOCPART
                        elif ((((p == parts[len(parts) - 1] and p.end_token.next0_ is not None and len(p.values) == 1) and (isinstance(p.end_token.next0_.get_referent(), DecreeReferent)) and (isinstance(p.begin_token, TextToken))) and p.begin_token.term == "ЧАСТИ" and (isinstance(p.end_token, NumberToken))) and p.begin_token.next0_ == p.end_token): 
                            p.typ = PartToken.ItemType.DOCPART
        elif (parts[len(parts) - 1].typ == PartToken.ItemType.ADDAGREE): 
            is_add_agree = True
        else: 
            if (len(parts) > 1): 
                del parts[0:0+len(parts) - 1]
            is_program = True
        def_owner = Utils.asObjectOrNull(_def_owner, DecreeReferent)
        doc_part = None
        if (isinstance(_def_owner, DecreePartReferent)): 
            def_owner = _def_owner.owner
            doc_part = _def_owner.doc_part
        res = list()
        has_prefix = False
        if (parts[0].typ == PartToken.ItemType.PREFIX): 
            del parts[0]
            has_prefix = True
            if (len(parts) == 0): 
                return None
        if ((len(parts) == 1 and this_dec is None and parts[0].typ != PartToken.ItemType.SUBPROGRAM) and parts[0].typ != PartToken.ItemType.ADDAGREE): 
            if (parts[0].is_doubt): 
                return None
            if (parts[0].is_newline_before and len(parts[0].values) <= 1): 
                tt1 = parts[0].end_token
                if (tt1.next0_ is None): 
                    return None
                tt1 = tt1.next0_
                if (BracketHelper.can_be_start_of_sequence(tt1, False, False)): 
                    br = BracketHelper.try_parse(tt1, BracketParseAttr.NO, 100)
                    if (br is not None and br.end_token.next0_ is not None): 
                        tt1 = br.end_token.next0_
                if (tt1.is_char(',')): 
                    pass
                elif (isinstance(tt1.get_referent(), DecreeReferent)): 
                    pass
                elif (tt1.is_value("К", None) and tt1.next0_ is not None and (isinstance(tt1.next0_.get_referent(), DecreeReferent))): 
                    pass
                elif (DecreeAnalyzer._check_other_typ(tt1, True) is not None): 
                    pass
                elif (_def_owner is None): 
                    return None
                elif (MiscHelper.can_be_start_of_sentence(tt1)): 
                    return None
                elif (tt1.is_char('.')): 
                    return None
        asc = list()
        desc = list()
        typs = list()
        i = 1
        while i < (len(parts) - 1): 
            if (parts[i].typ == PartToken.ItemType.SENTENCE): 
                parts.append(parts[i])
                del parts[i]
                break
            i += 1
        asc_count = 0
        desc_count = 0
        terminators = 0
        i = 0
        while i < (len(parts) - 1): 
            if (not parts[i].has_terminator): 
                if (parts[i].can_be_next_narrow(parts[i + 1])): 
                    asc_count += 1
                if (parts[i + 1].can_be_next_narrow(parts[i])): 
                    desc_count += 1
            elif ((asc_count > 0 and len(parts[i].values) == 1 and len(parts[i + 1].values) == 1) and parts[i].can_be_next_narrow(parts[i + 1])): 
                asc_count += 1
            elif ((desc_count > 0 and len(parts[i].values) == 1 and len(parts[i + 1].values) == 1) and parts[i + 1].can_be_next_narrow(parts[i])): 
                desc_count += 1
            else: 
                terminators += 1
            i += 1
        if (terminators == 0 and ((((desc_count > 0 and asc_count == 0)) or ((desc_count == 0 and asc_count > 0))))): 
            i = 0
            while i < (len(parts) - 1): 
                parts[i].has_terminator = False
                i += 1
        i = 0
        first_pass3966 = True
        while True:
            if first_pass3966: first_pass3966 = False
            else: i += 1
            if (not (i < len(parts))): break
            if (parts[i].typ == PartToken.ItemType.PREFIX): 
                continue
            asc.clear()
            asc.append(parts[i])
            typs.clear()
            typs.append(parts[i].typ)
            j = (i + 1)
            while j < len(parts): 
                if (((len(parts[j].values) == 0 and parts[j].typ != PartToken.ItemType.PREAMBLE and parts[j].typ != PartToken.ItemType.NOTICE) and parts[j].typ != PartToken.ItemType.TABLE and parts[j].typ != PartToken.ItemType.FOOTNOTE) and parts[j].typ != PartToken.ItemType.FORM): 
                    break
                elif (not parts[j].typ in typs and parts[j - 1].can_be_next_narrow(parts[j])): 
                    if (parts[j - 1].delim_after and terminators == 0): 
                        if (desc_count > asc_count): 
                            break
                        if (((j + 1) < len(parts)) and not parts[j].delim_after and not parts[j].has_terminator): 
                            break
                        if (parts[j - 1].typ == PartToken.ItemType.ITEM and parts[j].typ == PartToken.ItemType.SUBITEM): 
                            if (len(parts[j].values) > 0 and "." in str(parts[j].values[0])): 
                                break
                    asc.append(parts[j])
                    typs.append(parts[j].typ)
                    if (parts[j].has_terminator): 
                        break
                else: 
                    break
                j += 1
            desc.clear()
            desc.append(parts[i])
            typs.clear()
            typs.append(parts[i].typ)
            j = (i + 1)
            while j < len(parts): 
                if (((len(parts[j].values) == 0 and parts[j].name is None and parts[j].typ != PartToken.ItemType.PREAMBLE) and parts[j].typ != PartToken.ItemType.NOTICE and parts[j].typ != PartToken.ItemType.FOOTNOTE) and parts[j].typ != PartToken.ItemType.TABLE and parts[j].typ != PartToken.ItemType.FORM): 
                    break
                elif (((not parts[j].typ in typs or parts[j].typ == PartToken.ItemType.SUBITEM)) and parts[j].can_be_next_narrow(parts[j - 1])): 
                    if (parts[j - 1].delim_after and terminators == 0): 
                        if (desc_count <= asc_count): 
                            break
                    desc.append(parts[j])
                    typs.append(parts[j].typ)
                    if (parts[j].has_terminator): 
                        break
                elif (((not parts[j].typ in typs and parts[j - 1].can_be_next_narrow(parts[j]) and (j + 1) == (len(parts) - 1)) and parts[j + 1].can_be_next_narrow(parts[j]) and parts[j + 1].can_be_next_narrow(parts[j - 1])) and not parts[j].has_terminator): 
                    desc.insert(len(desc) - 1, parts[j])
                    typs.append(parts[j].typ)
                elif (not parts[j].typ in typs and parts[j].typ == PartToken.ItemType.SENTENCE): 
                    desc.insert(0, parts[j])
                    typs.append(parts[j].typ)
                    break
                elif ((not parts[j].typ in typs and j == (len(parts) - 1) and parts[0].can_be_next_narrow(parts[j])) and j == 2): 
                    desc.insert(0, parts[j])
                    typs.append(parts[j].typ)
                    break
                else: 
                    break
                j += 1
            desc.reverse()
            li = (desc if len(asc) < len(desc) else asc)
            j = 0
            while j < len(li): 
                li[j].ind = 0
                j += 1
            while True:
                dr = DecreePartReferent()
                tt00 = parts[i].begin_token
                tt11 = parts[(i + len(li)) - 1].end_token
                if (tt00.begin_char > tt11.end_char): 
                    tt00 = tt11
                    tt11 = parts[i].begin_token
                rt = ReferentToken(dr, tt00, tt11)
                if (parts[i].name is not None): 
                    dr.add_slot(DecreePartReferent.ATTR_NAME, parts[i].name, False, 0)
                rt.morph = parts[i].morph
                res.append(rt)
                sl_list = list()
                for p in li: 
                    if (dr.name is None and p.name is not None): 
                        dr._add_name(p.name)
                    nam = PartToken._get_attr_name_by_typ(p.typ)
                    if (nam is not None): 
                        sl = Slot._new1414(nam, p, 1)
                        sl_list.append(sl)
                        if (p.ind < len(p.values)): 
                            sl.value = p.values[p.ind]
                            if (Utils.isNullOrEmpty(p.values[p.ind].value)): 
                                sl.value = "0"
                        else: 
                            sl.value = "0"
                    if (p.ind > 0): 
                        rt.begin_token = p.values[p.ind].begin_token
                    if ((p.ind + 1) < len(p.values)): 
                        rt.end_token = p.values[p.ind].end_token
                for p in parts: 
                    for s in sl_list: 
                        if (s.tag == p): 
                            dr.add_slot(s.type_name, s.value, False, 0)
                            break
                for j in range(len(li) - 1, -1, -1):
                    li[j].ind += 1
                    if (li[j].ind >= len(li[j].values)): 
                        li[j].ind = 0
                    else: 
                        break
                else: j = -1
                if (j < 0): 
                    break
            if (len(res) == 1): 
                ii = i
                while ii < len(li): 
                    if (res[0].begin_char > li[ii].begin_char): 
                        res[0].begin_token = li[ii].begin_token
                    if (res[0].end_char < li[ii].end_char): 
                        res[0].end_token = li[ii].end_token
                    ii += 1
            i += (len(li) - 1)
        if (len(res) == 0): 
            return None
        for j in range(len(res) - 1, 0, -1):
            d0 = Utils.asObjectOrNull(res[j].referent, DecreePartReferent)
            d = Utils.asObjectOrNull(res[j - 1].referent, DecreePartReferent)
            if (d0.appendix is not None and d.appendix is None): 
                d.appendix = d0.appendix
            if (d0.doc_part is not None and d.doc_part is None): 
                d.doc_part = d0.doc_part
            elif (doc_part is not None and d.doc_part is None): 
                d.doc_part = doc_part
            if (d0.chapter is not None and d.chapter is None): 
                d.chapter = d0.chapter
            if (d0.section is not None and d.section is None): 
                d.section = d0.section
            if (d0.sub_section is not None and d.sub_section is None): 
                d.sub_section = d0.sub_section
            if (d0.clause is not None and d.clause is None): 
                d.clause = d0.clause
            if (d0.item is not None and d.item is None and ((d.sub_item is not None or d.indention is not None))): 
                if (d0.clause is not None and d0.clause != d.clause): 
                    pass
                else: 
                    d.item = d0.item
            if ((d0.sub_item is not None and d.sub_item is None and d.indention is not None) and d.item == d0.item): 
                d.sub_item = d0.sub_item
        else: j = 0
        if (len(res) == 1 and doc_part is not None and res[0].referent.doc_part is None): 
            res[0].referent.doc_part = doc_part
        tt = parts[i - 1].end_token
        owner = def_owner
        if (owner is not None and not in_changes and parts[0].anafor_ref is not None): 
            tt3 = parts[0].begin_token.previous
            first_pass3967 = True
            while True:
                if first_pass3967: first_pass3967 = False
                else: tt3 = tt3.previous
                if (not (tt3 is not None)): break
                if (tt3.is_comma): 
                    continue
                if (isinstance(tt3.get_referent(), DecreeReferent)): 
                    owner = (Utils.asObjectOrNull(tt3.get_referent(), DecreeReferent))
                break
        te = tt.next0_
        if ((te is not None and owner is None and te.is_char('(')) and parts[0].typ != PartToken.ItemType.SUBPROGRAM and parts[0].typ != PartToken.ItemType.ADDAGREE): 
            br = BracketHelper.try_parse(te, BracketParseAttr.NO, 100)
            if (br is not None): 
                if (te.next0_.morph.class0_.is_adverb): 
                    pass
                elif (isinstance(te.next0_.get_referent(), DecreeReferent)): 
                    if (owner is None and te.next0_.next0_ == br.end_token): 
                        owner = (Utils.asObjectOrNull(te.next0_.get_referent(), DecreeReferent))
                        te = br.end_token
                else: 
                    s = MiscHelper.get_text_value_of_meta_token(br, GetTextAttr.NO)
                    if (s is not None): 
                        rt = res[len(res) - 1]
                        rt.referent._add_name(s)
                        rt.end_token = br.end_token
                        te = rt.end_token.next0_
        if (te is not None and te.is_char_of(",;")): 
            te = te.next0_
        if (owner is None and (isinstance(te, ReferentToken))): 
            owner = Utils.asObjectOrNull(te.get_referent(), DecreeReferent)
            if ((owner) is not None): 
                res[len(res) - 1].end_token = te
        if (owner is None): 
            j = 0
            while j < i: 
                owner = parts[j].decree
                if ((owner) is not None): 
                    break
                j += 1
        if (te is not None and te.is_value("К", None) and te.next0_ is not None): 
            if (isinstance(te.next0_.get_referent(), DecreeReferent)): 
                te = te.next0_
                res[len(res) - 1].end_token = te
                owner = (Utils.asObjectOrNull(te.get_referent(), DecreeReferent))
            elif ((owner is not None and this_dec is not None and this_dec.end_char > te.end_char) and (res[len(res) - 1].end_char < this_dec.end_char)): 
                res[len(res) - 1].end_token = this_dec.end_token
        if (owner is None and this_dec is not None): 
            tt0 = res[0].begin_token
            if (tt0.previous is not None and tt0.previous.is_char('(')): 
                tt0 = tt0.previous
            if (tt0.previous is not None): 
                owner = Utils.asObjectOrNull(tt0.previous.get_referent(), DecreeReferent)
                if ((owner) is not None): 
                    if (this_dec.typ == owner.typ0): 
                        this_dec = (None)
                    else: 
                        owner = (None)
        if (owner is None and this_dec is not None and this_dec.real is not None): 
            owner = this_dec.real
        if (owner is not None and parts[0].typ == PartToken.ItemType.SUBPROGRAM and owner.kind != DecreeKind.PROGRAM): 
            owner = (None)
        if (owner is not None and parts[0].typ == PartToken.ItemType.ADDAGREE and owner.kind != DecreeKind.CONTRACT): 
            owner = (None)
        owner_paer = None
        loc_typ = None
        if ((this_dec is None or not this_dec.has_this_ref)): 
            anafor_ref = None
            for p in parts: 
                anafor_ref = p.anafor_ref
                if ((anafor_ref) is not None): 
                    break
            is_change_word_after = False
            tt2 = res[len(res) - 1].end_token.next0_
            if (tt2 is not None): 
                if (((tt2.is_char(':') or tt2.is_value("ДОПОЛНИТЬ", None) or tt2.is_value("СЛОВО", None)) or tt2.is_value("ИСКЛЮЧИТЬ", None) or tt2.is_value("ИЗЛОЖИТЬ", None)) or tt2.is_value("СЧИТАТЬ", None) or tt2.is_value("ПРИЗНАТЬ", None)): 
                    is_change_word_after = True
            tt2 = parts[0].begin_token.previous
            if (tt2 is not None): 
                if (((tt2.is_value("ДОПОЛНИТЬ", None) or tt2.is_value("ИСКЛЮЧИТЬ", None) or tt2.is_value("ИЗЛОЖИТЬ", None)) or tt2.is_value("СЧИТАТЬ", None) or tt2.is_value("УСТАНОВЛЕННЫЙ", None)) or tt2.is_value("ОПРЕДЕЛЕННЫЙ", None)): 
                    is_change_word_after = True
            cou = 0
            ugol_delo = False
            brack_level = 0
            bt = None
            coef_before = 0
            is_over_brr = False
            if (parts[0].begin_token.previous is not None and parts[0].begin_token.previous.is_char('(')): 
                if (parts[len(parts) - 1].end_token.next0_ is not None and parts[len(parts) - 1].end_token.next0_.is_char(')')): 
                    if (len(parts) == 1 and parts[0].typ == PartToken.ItemType.APPENDIX): 
                        pass
                    else: 
                        is_over_brr = True
                        if (owner is not None and DecreeAnalyzer._get_decree(parts[0].begin_token.previous.previous) is not None): 
                            owner = (None)
            tt = parts[0].begin_token.previous
            first_pass3968 = True
            while True:
                if first_pass3968: first_pass3968 = False
                else: tt = tt.previous; coef_before += 1
                if (not (tt is not None)): break
                if (tt.is_newline_after): 
                    coef_before += 2
                    if (((anafor_ref is None and not is_over_brr and not ugol_delo) and not is_change_word_after and not is_program) and not is_add_agree): 
                        if (this_dec is None): 
                            if (not tt.is_table_control_char): 
                                break
                if (this_dec is not None and this_dec.has_this_ref): 
                    break
                if (tt.is_table_control_char): 
                    break
                if (tt.morph.class0_.is_preposition): 
                    coef_before -= 1
                    continue
                if (isinstance(tt, TextToken)): 
                    if (BracketHelper.can_be_end_of_sequence(tt, False, None, False)): 
                        brack_level += 1
                        continue
                    if (BracketHelper.can_be_start_of_sequence(tt, False, False)): 
                        if (tt.is_char('(') and tt == parts[0].begin_token.previous): 
                            pass
                        else: 
                            brack_level -= 1
                            coef_before -= 1
                        continue
                if (tt.is_newline_before): 
                    brack_level = 0
                cou += 1
                if (cou > 100): 
                    if (((ugol_delo or is_program or is_add_agree) or anafor_ref is not None or this_dec is not None) or is_over_brr): 
                        if (cou > 1000): 
                            break
                    elif (is_change_word_after): 
                        if (cou > 250): 
                            break
                    else: 
                        break
                if (cou < 4): 
                    if (tt.is_value("УГОЛОВНЫЙ", "КРИМІНАЛЬНИЙ") and tt.next0_ is not None and tt.next0_.is_value("ДЕЛО", "СПРАВА")): 
                        ugol_delo = True
                if (tt.is_char_of(".")): 
                    coef_before += 50
                    if (tt.is_newline_after): 
                        coef_before += 100
                    continue
                if (brack_level > 0): 
                    continue
                dr = DecreeAnalyzer._get_decree(tt)
                if (dr is not None): 
                    if (dr.kind == DecreeKind.PUBLISHER): 
                        if ((tt.end_char + 3) < parts[0].begin_char): 
                            continue
                    if (ugol_delo and ((dr.name == "УГОЛОВНЫЙ КОДЕКС" or dr.name == "КРИМІНАЛЬНИЙ КОДЕКС"))): 
                        coef_before = 0
                    if (dr.kind == DecreeKind.PROGRAM): 
                        if (is_program): 
                            bt = tt
                            break
                        else: 
                            continue
                    if (dr.kind == DecreeKind.CONTRACT): 
                        if (is_add_agree): 
                            bt = tt
                            break
                        elif (this_dec is not None and ((dr.typ == this_dec.typ or dr.typ0 == this_dec.typ))): 
                            bt = tt
                            break
                        else: 
                            continue
                    if (this_dec is not None): 
                        dpr = Utils.asObjectOrNull(tt.get_referent(), DecreePartReferent)
                        if (this_dec.typ == dr.typ or this_dec.typ == dr.typ0): 
                            this_dec.real = dr
                        elif (dr.name is not None and this_dec.typ is not None and dr.name.startswith(this_dec.typ[0:0+len(this_dec.typ) - 1])): 
                            this_dec.real = dr
                            words = Utils.splitString(dr.name, ' ', False)
                            ii = 1
                            while ii < len(words): 
                                if (this_dec.end_token.next0_ is not None and this_dec.end_token.next0_.is_value(words[ii], None)): 
                                    this_dec.end_token = this_dec.end_token.next0_
                                else: 
                                    break
                                ii += 1
                        elif ((this_dec.has_other_ref and dpr is not None and dpr.clause is not None) and ((this_dec.typ == "СТАТЬЯ" or this_dec.typ == "СТАТТЯ"))): 
                            for r in res: 
                                dpr0 = Utils.asObjectOrNull(r.referent, DecreePartReferent)
                                if (dpr0.clause is None): 
                                    dpr0.clause = dpr.clause
                                    dpr0.owner = dpr.owner
                                    owner = dpr0.owner
                        else: 
                            continue
                    elif (is_change_word_after): 
                        if (owner is None): 
                            coef_before = 0
                        elif (owner == DecreeAnalyzer._get_decree(tt)): 
                            coef_before = 0
                    bt = tt
                    break
                if (dr is not None): 
                    continue
                if (isinstance(tt.get_referent(), DecreeChangeReferent)): 
                    break
                dpr2 = Utils.asObjectOrNull(tt.get_referent(), DecreePartReferent)
                if (dpr2 is not None): 
                    if (this_dec is not None): 
                        if (this_dec.typ != dpr2.local_typ): 
                            continue
                    bt = tt
                    break
                dit = DecreeToken.try_attach(tt, None, False)
                if (dit is not None and dit.typ == DecreeToken.ItemType.TYP): 
                    if (this_dec is not None): 
                        continue
                    if (dit.chars.is_capital_upper or anafor_ref is not None): 
                        bt = tt
                        break
            cou = 0
            at = None
            coef_after = 0
            aloc_typ = None
            tt0 = parts[len(parts) - 1].end_token.next0_
            has_newline = False
            ttt = parts[len(parts) - 1].begin_token
            while ttt.end_char < parts[len(parts) - 1].end_char: 
                if (ttt.is_newline_after): 
                    has_newline = True
                ttt = ttt.next0_
            tt = tt0
            first_pass3969 = True
            while True:
                if first_pass3969: first_pass3969 = False
                else: tt = tt.next0_; coef_after += 1
                if (not (tt is not None)): break
                if (owner is not None and coef_after > 0): 
                    break
                if (tt.is_newline_before): 
                    break
                if (tt.is_table_control_char): 
                    break
                if (tt.is_value("СМ", None)): 
                    break
                if (anafor_ref is not None): 
                    break
                if (this_dec is not None): 
                    if (tt != tt0): 
                        break
                    if (this_dec.real is not None): 
                        break
                if (InstrToken._check_entered(tt) is not None): 
                    break
                if (tt.morph.class0_.is_preposition or tt.is_comma_and): 
                    coef_after -= 1
                    continue
                if (tt.morph.class0_.equals(MorphClass.VERB)): 
                    break
                if (BracketHelper.can_be_end_of_sequence(tt, False, None, False)): 
                    break
                pts = PartToken.try_attach_list(tt, False, 40)
                if (pts is not None): 
                    tt = pts[len(pts) - 1].end_token
                    coef_after -= 1
                    ttnn = tt.next0_
                    if (ttnn is not None and ttnn.is_char('.')): 
                        ttnn = ttnn.next0_
                    dit = DecreeToken.try_attach(ttnn, None, False)
                    if (dit is not None and dit.typ == DecreeToken.ItemType.TYP): 
                        loc_typ = dit.value
                        break
                    continue
                if (BracketHelper.can_be_start_of_sequence(tt, False, False)): 
                    br = BracketHelper.try_parse(tt, BracketParseAttr.NO, 100)
                    if (br is not None): 
                        coef_after -= 1
                        tt = br.end_token
                        continue
                cou += 1
                if (cou > 100): 
                    break
                if (cou > 1 and has_newline): 
                    break
                if (tt.is_char_of(".")): 
                    coef_after += 50
                    if (tt.is_newline_after): 
                        coef_after += 100
                    continue
                if (isinstance(tt.get_referent(), DecreeChangeReferent)): 
                    break
                dr = Utils.asObjectOrNull(tt.get_referent(), DecreeReferent)
                if (dr is not None and dr.kind != DecreeKind.PUBLISHER): 
                    if (dr.kind == DecreeKind.PROGRAM): 
                        if (is_program): 
                            at = tt
                            break
                        else: 
                            continue
                    if (dr.kind == DecreeKind.CONTRACT): 
                        if (is_add_agree): 
                            at = tt
                            break
                        else: 
                            continue
                    at = tt
                    break
                if (is_program or is_add_agree): 
                    break
                if (dr is not None): 
                    continue
                tte2 = DecreeAnalyzer._check_other_typ(tt, tt == tt0)
                if (tte2 is not None): 
                    at = tte2
                    if (tt == tt0 and this_dec is not None and this_dec.real is None): 
                        if (this_dec.typ == (Utils.asObjectOrNull(at.tag, str))): 
                            at = (None)
                        else: 
                            this_dec = (None)
                    break
            if (bt is not None and at is not None): 
                if (coef_before < coef_after): 
                    at = (None)
                elif ((isinstance(bt, ReferentToken)) and (isinstance(at, TextToken))): 
                    at = (None)
                else: 
                    bt = (None)
            if (owner is None): 
                if (at is not None): 
                    owner = DecreeAnalyzer._get_decree(at)
                    if (isinstance(at, TextToken)): 
                        if (isinstance(at.tag, str)): 
                            loc_typ = (Utils.asObjectOrNull(at.tag, str))
                        else: 
                            loc_typ = at.lemma
                elif (bt is not None): 
                    owner = DecreeAnalyzer._get_decree(bt)
                    owner_paer = (Utils.asObjectOrNull(bt.get_referent(), DecreePartReferent))
                    if (owner_paer is not None and loc_typ is None): 
                        loc_typ = owner_paer.local_typ
            elif (coef_after == 0 and at is not None): 
                owner1 = DecreeAnalyzer._get_decree(at)
                if (owner1 is not None): 
                    owner = owner1
            elif (coef_before == 0 and bt is not None): 
                owner = DecreeAnalyzer._get_decree(bt)
                owner_paer = (Utils.asObjectOrNull(bt.get_referent(), DecreePartReferent))
                if (owner_paer is not None and loc_typ is None): 
                    loc_typ = owner_paer.local_typ
            if (((bt is not None and len(parts) == 1 and parts[0].typ == PartToken.ItemType.DOCPART) and (isinstance(bt.get_referent(), DecreePartReferent)) and bt.get_referent().clause is not None) and len(res) == 1 and owner == bt.get_referent().owner): 
                for s in res[0].referent.slots: 
                    if (s.type_name == DecreePartReferent.ATTR_DOCPART): 
                        s.type_name = DecreePartReferent.ATTR_PART
                res[0].referent._add_high_level_info(Utils.asObjectOrNull(bt.get_referent(), DecreePartReferent))
        if (owner is None): 
            if (this_dec is None and loc_typ is None): 
                if ((len(parts) == 1 and len(parts[0].values) == 1 and parts[0].typ == PartToken.ItemType.APPENDIX) and parts[0].begin_token.chars.is_capital_upper): 
                    pass
                elif ((parts[0].begin_token.previous is not None and parts[0].begin_token.previous.is_char('(') and parts[len(parts) - 1].end_token.next0_ is not None) and parts[len(parts) - 1].end_token.next0_.is_char(')')): 
                    if (parts[0].typ == PartToken.ItemType.PAGE): 
                        return None
                elif (in_changes): 
                    pass
                else: 
                    return None
            for r in res: 
                dr = Utils.asObjectOrNull(r.referent, DecreePartReferent)
                if (this_dec is not None): 
                    dr.local_typ = this_dec.typ
                    if (this_dec.begin_char > r.end_char and r == res[len(res) - 1]): 
                        r.end_token = this_dec.end_token
                elif (loc_typ is not None): 
                    if (loc_typ == "СТАТЬЯ" and dr.clause is not None): 
                        pass
                    elif (loc_typ == "ГЛАВА" and dr.chapter is not None): 
                        pass
                    elif (loc_typ == "ПАРАГРАФ" and dr.paragraph is not None): 
                        pass
                    elif (loc_typ == "ЧАСТЬ" and dr.part is not None): 
                        pass
                    else: 
                        dr.local_typ = loc_typ
                        if (r == res[len(res) - 1] and not r.is_newline_after): 
                            ttt1 = r.end_token.next0_
                            if (ttt1 is not None and ttt1.is_comma): 
                                ttt1 = ttt1.next0_
                            at = DecreeAnalyzer._check_other_typ(ttt1, True)
                            if (at is not None and (Utils.asObjectOrNull(at.tag, str)) == loc_typ): 
                                r.end_token = at
        else: 
            for r in res: 
                dr = Utils.asObjectOrNull(r.referent, DecreePartReferent)
                dr.owner = owner
                if (this_dec is not None and this_dec.real == owner): 
                    if (this_dec.begin_char > r.end_char and r == res[len(res) - 1]): 
                        r.end_token = this_dec.end_token
        if (len(res) > 0): 
            rt = res[len(res) - 1]
            tt = rt.end_token.next0_
            if (owner is not None and tt is not None and tt.get_referent() == owner): 
                rt.end_token = tt
                tt = tt.next0_
            if (tt is not None and ((tt.is_hiphen or tt.is_char(':')))): 
                tt = tt.next0_
            br = BracketHelper.try_parse(tt, (BracketParseAttr.CANBEMANYLINES if is_program else BracketParseAttr.NO), 100)
            if (br is not None and tt.is_newline_before): 
                br = (None)
            if (br is not None): 
                ok = True
                if (br.open_char == '('): 
                    if (parts[0].typ == PartToken.ItemType.SUBPROGRAM): 
                        ok = False
                    elif (PartToken.try_attach(tt.next0_, None, False, False) is not None): 
                        ok = False
                    else: 
                        ttt = tt.next0_
                        while ttt is not None and (ttt.end_char < br.end_char): 
                            if (ttt == tt.next0_ and tt.next0_.morph.class0_.is_adverb): 
                                ok = False
                            if ((isinstance(ttt.get_referent(), DecreeReferent)) or (isinstance(ttt.get_referent(), DecreePartReferent))): 
                                ok = False
                            if (ttt.is_value("РЕДАКЦИЯ", None) and ttt == br.end_token.previous): 
                                ok = False
                            ttt = ttt.next0_
                if (ok): 
                    s = MiscHelper.get_text_value_of_meta_token(br, GetTextAttr.NO)
                    if (s is not None): 
                        rt.referent._add_name(s)
                        rt.end_token = br.end_token
                        if ((isinstance(rt.end_token.next0_, ReferentToken)) and rt.end_token.next0_.get_referent() == owner): 
                            rt.end_token = rt.end_token.next0_
            elif ((is_program and len(parts[0].values) > 0 and tt is not None) and tt.is_table_control_char and MiscHelper.can_be_start_of_sentence(tt.next0_)): 
                tt1 = tt.next0_
                while tt1 is not None: 
                    if (tt1.is_table_control_char): 
                        s = MiscHelper.get_text_value(tt.next0_, tt1.previous, GetTextAttr.NO)
                        if (s is not None): 
                            rt.referent._add_name(s)
                            rt.end_token = tt1
                        break
                    elif (tt1.is_newline_before): 
                        break
                    tt1 = tt1.next0_
            if (this_dec is not None): 
                if (this_dec.end_char > res[len(res) - 1].end_char): 
                    res[len(res) - 1].end_token = this_dec.end_token
        if (owner_paer is not None and this_dec is None): 
            ii = 0
            while ii < len(res): 
                res[ii].referent._add_high_level_info((owner_paer if ii == 0 else Utils.asObjectOrNull(res[ii - 1].referent, DecreePartReferent)))
                ii += 1
        if (len(res) == 1 and res[0].referent.name is None): 
            if ((res[0].begin_token.previous is not None and res[0].begin_token.previous.is_char('(') and res[0].end_token.next0_ is not None) and res[0].end_token.next0_.is_char(')')): 
                if (BracketHelper.can_be_end_of_sequence(res[0].begin_token.previous.previous, False, None, False)): 
                    beg = None
                    tt = res[0].begin_token.previous.previous.previous
                    while tt is not None: 
                        if (tt.is_newline_after): 
                            break
                        if (BracketHelper.can_be_start_of_sequence(tt, False, False)): 
                            br = BracketHelper.try_parse(tt, BracketParseAttr.NO, 100)
                            if (br is not None and ((br.end_char + 10) < res[0].begin_char)): 
                                break
                            if (tt.next0_.chars.is_letter and not tt.next0_.chars.is_all_lower): 
                                beg = tt
                        tt = tt.previous
                    if (beg is not None): 
                        res[0].referent._add_name(MiscHelper.get_text_value(beg, res[0].begin_token.previous.previous, GetTextAttr.NO))
                        res[0].begin_token = beg
                        res[0].end_token = res[0].end_token.next0_
        if (is_program): 
            for i in range(len(res) - 1, -1, -1):
                pa = Utils.asObjectOrNull(res[i].referent, DecreePartReferent)
                if (pa.subprogram is None): 
                    continue
                if (pa.owner is None or pa.name is None or pa.owner.kind != DecreeKind.PROGRAM): 
                    del res[i]
            else: i = -1
        if (is_add_agree): 
            for i in range(len(res) - 1, -1, -1):
                pa = Utils.asObjectOrNull(res[i].referent, DecreePartReferent)
                if (pa.addagree is None): 
                    continue
                if (pa.owner is None or pa.owner.kind != DecreeKind.CONTRACT): 
                    del res[i]
            else: i = -1
        if (not in_changes): 
            for i in range(len(res) - 1, -1, -1):
                pa = Utils.asObjectOrNull(res[i].referent, DecreePartReferent)
                if (pa.name_as_item is None and pa.formula is None): 
                    continue
                if (len(pa.slots) == 2 and pa.owner is None): 
                    del res[i]
            else: i = -1
        if (len(res) == 1 and len(parts) == 1 and parts[0].add_names is not None): 
            res[0].end_token = parts[0].add_names[0].begin_token.previous
            for br in parts[0].add_names: 
                dp = Utils.asObjectOrNull(res[0].referent.clone(), DecreePartReferent)
                dp.add_slot(DecreePartReferent.ATTR_NAME, None, True, 0)
                dp._add_name(MiscHelper.get_text_value_of_meta_token(br, GetTextAttr.NO))
                res.append(ReferentToken(dp, br.begin_token, br.end_token))
        res1 = list()
        i = 0
        while i < len(res): 
            li = list()
            j = i
            while j < len(res): 
                if (res[j].begin_token != res[i].begin_token): 
                    break
                else: 
                    li.append(Utils.asObjectOrNull(res[j].referent, DecreePartReferent))
                j += 1
            et = None
            if (j < len(res)): 
                et = res[j].begin_token.previous
            else: 
                et = res[len(res) - 1].end_token
            while et.begin_char > res[i].begin_char:
                if (et.is_char(',') or et.morph.class0_.is_conjunction or et.is_hiphen): 
                    et = et.previous
                elif (MiscHelper.check_number_prefix(et) is not None): 
                    et = et.previous
                else: 
                    break
            res1.append(MetaToken._new1415(res[i].begin_token, (et if et.begin_char >= res[i].begin_char else res[i].begin_token), li, res[i].morph))
            i = (j - 1)
            i += 1
        return res1