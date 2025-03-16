# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru

import typing
from backend.pullenti.unisharp.Utils import Utils
from backend.pullenti.unisharp.Misc import RefOutArgWrapper

from backend.pullenti.ner.core.BracketParseAttr import BracketParseAttr
from backend.pullenti.ner.Token import Token
from backend.pullenti.ner.MetaToken import MetaToken
from backend.pullenti.ner.TextToken import TextToken
from backend.pullenti.ner.ReferentToken import ReferentToken
from backend.pullenti.ner.core.Termin import Termin
from backend.pullenti.ner.core.TerminParseAttr import TerminParseAttr
from backend.pullenti.ner.core.BracketHelper import BracketHelper
from backend.pullenti.ner.core.internal.PullentiNerCoreInternalResourceHelper import NerCoreInternalResourceHelper
from backend.pullenti.ner.core.TerminCollection import TerminCollection
from backend.pullenti.ner.transport.TransportKind import TransportKind
from backend.pullenti.ner.transport.internal.MetaTransport import MetaTransport
from backend.pullenti.ner.ProcessorService import ProcessorService
from backend.pullenti.ner.Referent import Referent
from backend.pullenti.ner.transport.internal.TransItemToken import TransItemToken
from backend.pullenti.ner.transport.TransportReferent import TransportReferent
from backend.pullenti.ner.geo.GeoReferent import GeoReferent
from backend.pullenti.ner.Analyzer import Analyzer

class TransportAnalyzer(Analyzer):
    """ Анализатор транспортных стредств """
    
    ANALYZER_NAME = "TRANSPORT"
    """ Имя анализатора ("TRANSPORT") """
    
    @property
    def name(self) -> str:
        return TransportAnalyzer.ANALYZER_NAME
    
    @property
    def caption(self) -> str:
        return "Транспорт"
    
    @property
    def description(self) -> str:
        return "Техника, автомобили, самолёты, корабли..."
    
    def clone(self) -> 'Analyzer':
        return TransportAnalyzer()
    
    @property
    def type_system(self) -> typing.List['ReferentClass']:
        return [MetaTransport._global_meta]
    
    @property
    def images(self) -> typing.List[tuple]:
        res = dict()
        res[Utils.enumToString(TransportKind.FLY)] = NerCoreInternalResourceHelper.get_bytes("fly.png")
        res[Utils.enumToString(TransportKind.SHIP)] = NerCoreInternalResourceHelper.get_bytes("ship.png")
        res[Utils.enumToString(TransportKind.SPACE)] = NerCoreInternalResourceHelper.get_bytes("space.png")
        res[Utils.enumToString(TransportKind.TRAIN)] = NerCoreInternalResourceHelper.get_bytes("train.png")
        res[Utils.enumToString(TransportKind.AUTO)] = NerCoreInternalResourceHelper.get_bytes("auto.png")
        res[MetaTransport.IMAGE_ID] = NerCoreInternalResourceHelper.get_bytes("transport.png")
        return res
    
    def create_referent(self, type0_ : str) -> 'Referent':
        if (type0_ == TransportReferent.OBJ_TYPENAME): 
            return TransportReferent()
        return None
    
    @property
    def used_extern_object_types(self) -> typing.List[str]:
        return [GeoReferent.OBJ_TYPENAME, "ORGANIZATION"]
    
    @property
    def progress_weight(self) -> int:
        return 5
    
    def process(self, kit : 'AnalysisKit') -> None:
        ad = kit.get_analyzer_data(self)
        models = TerminCollection()
        objs_by_model = dict()
        obj_by_names = TerminCollection()
        t = kit.first_token
        first_pass4246 = True
        while True:
            if first_pass4246: first_pass4246 = False
            else: t = t.next0_
            if (not (t is not None)): break
            if (t.is_ignored): 
                continue
            its = TransItemToken.try_parse_list(t, 10)
            if (its is None): 
                continue
            rts = self.__try_attach(its, False)
            if (rts is not None): 
                for rt in rts: 
                    cou = 0
                    tt = t.previous
                    first_pass4247 = True
                    while True:
                        if first_pass4247: first_pass4247 = False
                        else: tt = tt.previous; cou += 1
                        if (not (tt is not None and (cou < 1000))): break
                        tr = Utils.asObjectOrNull(tt.get_referent(), TransportReferent)
                        if (tr is None): 
                            continue
                        ok = True
                        for s in rt.referent.slots: 
                            if (tr.find_slot(s.type_name, s.value, True) is None): 
                                ok = False
                                break
                        if (ok): 
                            rt.referent = (tr)
                            break
                    rt.referent = ad.register_referent(rt.referent)
                    kit.embed_token(rt)
                    t = (rt)
                    for s in rt.referent.slots: 
                        if (s.type_name == TransportReferent.ATTR_MODEL): 
                            mod = str(s.value)
                            for k in range(2):
                                if (not str.isdigit(mod[0])): 
                                    li = [ ]
                                    wrapli3437 = RefOutArgWrapper(None)
                                    inoutres3438 = Utils.tryGetValue(objs_by_model, mod, wrapli3437)
                                    li = wrapli3437.value
                                    if (not inoutres3438): 
                                        li = list()
                                        objs_by_model[mod] = li
                                    if (not rt.referent in li): 
                                        li.append(rt.referent)
                                    models.add_string(mod, li, None, False)
                                if (k > 0): 
                                    break
                                brand = rt.referent.get_string_value(TransportReferent.ATTR_BRAND)
                                if (brand is None): 
                                    break
                                mod = "{0} {1}".format(brand, mod)
                        elif (s.type_name == TransportReferent.ATTR_NAME): 
                            obj_by_names.add(Termin._new89(str(s.value), rt.referent))
        if (len(objs_by_model) == 0 and len(obj_by_names.termins) == 0): 
            return
        t = kit.first_token
        first_pass4248 = True
        while True:
            if first_pass4248: first_pass4248 = False
            else: t = t.next0_
            if (not (t is not None)): break
            if (t.is_ignored): 
                continue
            br = BracketHelper.try_parse(t, BracketParseAttr.NO, 10)
            if (br is not None): 
                toks = obj_by_names.try_parse(t.next0_, TerminParseAttr.NO)
                if (toks is not None and toks.end_token.next0_ == br.end_token): 
                    rt0 = ReferentToken(Utils.asObjectOrNull(toks.termin.tag, Referent), br.begin_token, br.end_token)
                    kit.embed_token(rt0)
                    t = (rt0)
                    continue
            if (not (isinstance(t, TextToken))): 
                continue
            if (not t.chars.is_letter): 
                continue
            tok = models.try_parse(t, TerminParseAttr.NO)
            if (tok is None): 
                if (not t.chars.is_all_lower): 
                    tok = obj_by_names.try_parse(t, TerminParseAttr.NO)
                if (tok is None): 
                    continue
            if (not tok.is_whitespace_after): 
                if (tok.end_token.next0_ is None or not tok.end_token.next0_.is_char_of(",.)")): 
                    if (not BracketHelper.is_bracket(tok.end_token.next0_, False)): 
                        continue
            tr = None
            li = Utils.asObjectOrNull(tok.termin.tag, list)
            if (li is not None and len(li) == 1): 
                tr = li[0]
            else: 
                tr = (Utils.asObjectOrNull(tok.termin.tag, Referent))
            if (tr is not None): 
                tit = TransItemToken.try_parse(tok.begin_token.previous, None, False, True)
                if (tit is not None and tit.typ == TransItemToken.Typs.BRAND): 
                    tr.add_slot(TransportReferent.ATTR_BRAND, tit.value, False, 0)
                    tok.begin_token = tit.begin_token
                rt0 = ReferentToken(tr, tok.begin_token, tok.end_token)
                kit.embed_token(rt0)
                t = (rt0)
                continue
    
    def process_referent(self, begin : 'Token', param : str) -> 'ReferentToken':
        its = TransItemToken.try_parse_list(begin, 10)
        if (its is None): 
            return None
        rr = self.__try_attach(its, True)
        if (rr is not None and len(rr) > 0): 
            return rr[0]
        return None
    
    def __try_attach(self, its : typing.List['TransItemToken'], attach : bool) -> typing.List['ReferentToken']:
        tr = TransportReferent()
        i = 0
        t1 = None
        brand_is_doubt = False
        i = 0
        first_pass4249 = True
        while True:
            if first_pass4249: first_pass4249 = False
            else: i += 1
            if (not (i < len(its))): break
            if (its[i].typ == TransItemToken.Typs.NOUN): 
                if (tr.find_slot(TransportReferent.ATTR_TYPE, None, True) is not None): 
                    break
                if (its[i].kind != TransportKind.UNDEFINED): 
                    if (tr.kind != TransportKind.UNDEFINED and its[i].kind != tr.kind): 
                        break
                    else: 
                        tr.kind = its[i].kind
                tr.add_slot(TransportReferent.ATTR_TYPE, its[i].value, False, 0)
                if (its[i].alt_value is not None): 
                    tr.add_slot(TransportReferent.ATTR_TYPE, its[i].alt_value, False, 0)
                if (its[i].state is not None): 
                    tr._add_geo(its[i].state)
                t1 = its[i].end_token
                continue
            if (its[i].typ == TransItemToken.Typs.GEO): 
                if (its[i].state is not None): 
                    tr._add_geo(its[i].state)
                elif (its[i].ref is not None): 
                    tr._add_geo(its[i].ref)
                t1 = its[i].end_token
                continue
            if (its[i].typ == TransItemToken.Typs.BRAND): 
                if (tr.find_slot(TransportReferent.ATTR_BRAND, None, True) is not None): 
                    if (tr.find_slot(TransportReferent.ATTR_BRAND, its[i].value, True) is None): 
                        break
                if (its[i].kind != TransportKind.UNDEFINED): 
                    if (tr.kind != TransportKind.UNDEFINED and its[i].kind != tr.kind): 
                        break
                    else: 
                        tr.kind = its[i].kind
                tr.add_slot(TransportReferent.ATTR_BRAND, its[i].value, False, 0)
                t1 = its[i].end_token
                brand_is_doubt = its[i].is_doubt
                continue
            if (its[i].typ == TransItemToken.Typs.MODEL): 
                if (tr.find_slot(TransportReferent.ATTR_MODEL, None, True) is not None): 
                    break
                tr.add_slot(TransportReferent.ATTR_MODEL, its[i].value, False, 0)
                if (its[i].alt_value is not None): 
                    tr.add_slot(TransportReferent.ATTR_MODEL, its[i].alt_value, False, 0)
                t1 = its[i].end_token
                continue
            if (its[i].typ == TransItemToken.Typs.CLASS): 
                if (tr.find_slot(TransportReferent.ATTR_CLASS, None, True) is not None): 
                    break
                tr.add_slot(TransportReferent.ATTR_CLASS, its[i].value, False, 0)
                t1 = its[i].end_token
                continue
            if (its[i].typ == TransItemToken.Typs.NAME): 
                if (tr.find_slot(TransportReferent.ATTR_NAME, None, True) is not None): 
                    break
                tr.add_slot(TransportReferent.ATTR_NAME, its[i].value, False, 0)
                if (its[i].alt_value is not None): 
                    tr.add_slot(TransportReferent.ATTR_NAME, its[i].alt_value, False, 0)
                t1 = its[i].end_token
                continue
            if (its[i].typ == TransItemToken.Typs.NUMBER): 
                if (tr.find_slot(TransportReferent.ATTR_NUMBER, None, True) is not None): 
                    break
                if (its[i].kind != TransportKind.UNDEFINED): 
                    if (tr.kind != TransportKind.UNDEFINED and its[i].kind != tr.kind): 
                        break
                    else: 
                        tr.kind = its[i].kind
                tr.add_slot(TransportReferent.ATTR_NUMBER, its[i].value, False, 0)
                if (its[i].alt_value is not None): 
                    tr.add_slot(TransportReferent.ATTR_NUMBER_REGION, its[i].alt_value, False, 0)
                t1 = its[i].end_token
                continue
            if (its[i].typ == TransItemToken.Typs.ORG): 
                if (tr.find_slot(TransportReferent.ATTR_ORG, None, True) is not None): 
                    break
                if (not its[i].morph.case_.is_undefined and not its[i].morph.case_.is_genitive): 
                    break
                tr.add_slot(TransportReferent.ATTR_ORG, its[i].ref, True, 0)
                t1 = its[i].end_token
                continue
            if (its[i].typ == TransItemToken.Typs.DATE): 
                if (tr.find_slot(TransportReferent.ATTR_DATE, None, True) is not None): 
                    break
                tr.add_slot(TransportReferent.ATTR_DATE, its[i].ref, True, 0)
                t1 = its[i].end_token
                continue
            if (its[i].typ == TransItemToken.Typs.ROUTE): 
                if (tr.find_slot(TransportReferent.ATTR_ROUTEPOINT, None, True) is not None): 
                    break
                for o in its[i].route_items: 
                    tr.add_slot(TransportReferent.ATTR_ROUTEPOINT, o, False, 0)
                t1 = its[i].end_token
                continue
        if (not tr._check(attach, brand_is_doubt)): 
            return None
        res = list()
        res.append(ReferentToken(tr, its[0].begin_token, t1))
        if ((i < len(its)) and tr.kind == TransportKind.SHIP and its[i - 1].typ == TransItemToken.Typs.NAME): 
            while i < len(its): 
                if (its[i].typ != TransItemToken.Typs.NAME or not its[i].is_after_conjunction): 
                    break
                tr1 = TransportReferent()
                tr1.merge_slots(tr, True)
                tr1.add_slot(TransportReferent.ATTR_NAME, its[i].value, True, 0)
                res.append(ReferentToken(tr1, its[i].begin_token, its[i].end_token))
                i += 1
        elif (i == len(its) and its[len(its) - 1].typ == TransItemToken.Typs.NUMBER): 
            tt = t1.next0_
            while tt is not None: 
                if (not tt.is_comma_and): 
                    break
                nn = TransItemToken._attach_rus_auto_number(tt.next0_)
                if (nn is None): 
                    nn = TransItemToken._attach_number(tt.next0_, False)
                if (nn is None or nn.typ != TransItemToken.Typs.NUMBER): 
                    break
                tr1 = TransportReferent()
                for s in tr.slots: 
                    if (s.type_name != TransportReferent.ATTR_NUMBER): 
                        if (s.type_name == TransportReferent.ATTR_NUMBER_REGION and nn.alt_value is not None): 
                            continue
                        tr1.add_slot(s.type_name, s.value, False, 0)
                tr1.add_slot(TransportReferent.ATTR_NUMBER, nn.value, True, 0)
                if (nn.alt_value is not None): 
                    tr1.add_slot(TransportReferent.ATTR_NUMBER_REGION, nn.alt_value, True, 0)
                res.append(ReferentToken(tr1, nn.begin_token, nn.end_token))
                tt = nn.end_token
                tt = tt.next0_
        return res
    
    __m_inited = None
    
    @staticmethod
    def initialize() -> None:
        if (TransportAnalyzer.__m_inited): 
            return
        TransportAnalyzer.__m_inited = True
        MetaTransport.initialize()
        try: 
            Termin.ASSIGN_ALL_TEXTS_AS_NORMAL = True
            TransItemToken.initialize()
            Termin.ASSIGN_ALL_TEXTS_AS_NORMAL = False
        except Exception as ex: 
            raise Utils.newException(ex.__str__(), ex)
        ProcessorService.register_analyzer(TransportAnalyzer())