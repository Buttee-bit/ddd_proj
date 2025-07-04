﻿# SDK Pullenti Lingvo, version 4.30, june 2025. Copyright (c) 2013-2025, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

import xml.etree
import io
import typing
from enum import IntEnum
from pullenti.unisharp.Utils import Utils
from pullenti.unisharp.Misc import RefOutArgWrapper
from pullenti.unisharp.Streams import MemoryStream
from pullenti.unisharp.Streams import Stream

from pullenti.ner.geo.GeoReferent import GeoReferent
from pullenti.ner.person.PersonReferent import PersonReferent
from pullenti.ner.core.GetTextAttr import GetTextAttr
from pullenti.morph.MorphNumber import MorphNumber
from pullenti.morph.MorphCase import MorphCase
from pullenti.morph.MorphGender import MorphGender
from pullenti.morph.LanguageHelper import LanguageHelper
from pullenti.ner.core.TerminParseAttr import TerminParseAttr
from pullenti.ner.geo.internal.GeoOwnerHelper import GeoOwnerHelper
from pullenti.morph.MorphWordForm import MorphWordForm
from pullenti.ner.mail.internal.MailLine import MailLine
from pullenti.ner.core.BracketParseAttr import BracketParseAttr
from pullenti.morph.MorphLang import MorphLang
from pullenti.morph.MorphClass import MorphClass
from pullenti.ner.MetaToken import MetaToken
from pullenti.ner.core.BracketHelper import BracketHelper
from pullenti.morph.MorphBaseInfo import MorphBaseInfo
from pullenti.ner.Token import Token
from pullenti.ner.core.ComplexNumToken import ComplexNumToken
from pullenti.ner.core.TerminToken import TerminToken
from pullenti.ner.MorphCollection import MorphCollection
from pullenti.morph.internal.MorphDeserializer import MorphDeserializer
from pullenti.ner.person.internal.PullentiNerPersonInternalResourceHelper import PullentiNerPersonInternalResourceHelper
from pullenti.ner.ReferentToken import ReferentToken
from pullenti.ner.core.Termin import Termin
from pullenti.ner.Referent import Referent
from pullenti.ner.person.internal.PersonAttrTerminType2 import PersonAttrTerminType2
from pullenti.morph.MorphologyService import MorphologyService
from pullenti.ner.person.internal.PersonAttrTerminType import PersonAttrTerminType
from pullenti.ner.person.internal.PersonAttrTermin import PersonAttrTermin
from pullenti.ner.core.TerminCollection import TerminCollection
from pullenti.ner.core.NounPhraseParseAttr import NounPhraseParseAttr
from pullenti.ner.TextToken import TextToken
from pullenti.ner.core.NounPhraseHelper import NounPhraseHelper
from pullenti.ner.NumberToken import NumberToken
from pullenti.ner.geo.GeoAnalyzer import GeoAnalyzer
from pullenti.ner.person.PersonPropertyKind import PersonPropertyKind
from pullenti.ner.core.NumberHelper import NumberHelper
from pullenti.ner.core.MiscHelper import MiscHelper
from pullenti.ner.person.PersonPropertyReferent import PersonPropertyReferent
from pullenti.ner.person.internal.PersonTokenData import PersonTokenData
from pullenti.ner.person.internal.PersonItemToken import PersonItemToken
from pullenti.ner.person.PersonAnalyzer import PersonAnalyzer

class PersonAttrToken(ReferentToken):
    
    class PersonAttrAttachAttrs(IntEnum):
        NO = 0
        AFTERZAMESTITEL = 1
        ONLYKEYWORD = 2
        INPROCESS = 4
        
        @classmethod
        def has_value(cls, value):
            return any(value == item.value for item in cls)
    
    @staticmethod
    def initialize() -> None:
        if (PersonAttrToken.M_TERMINS is not None): 
            return
        t = None
        PersonAttrToken.M_TERMINS = TerminCollection()
        PersonAttrToken.M_TERMINS.add(PersonAttrTermin._new3148("ТОВАРИЩ", PersonAttrTerminType.PREFIX))
        PersonAttrToken.M_TERMINS.add(PersonAttrTermin._new3149("ТОВАРИШ", MorphLang.UA, PersonAttrTerminType.PREFIX))
        for s in ["ГОСПОДИН", "ГРАЖДАНИН", "УРОЖЕНЕЦ", "ВЫХОДЕЦ ИЗ", "МИСТЕР", "СЭР", "СЕНЬОР", "МОНСЕНЬОР", "СИНЬОР", "МЕСЬЕ", "МСЬЕ", "ДОН", "МАЭСТРО", "МЭТР"]: 
            t = PersonAttrTermin._new3150(s, PersonAttrTerminType.PREFIX, MorphGender.MASCULINE)
            if (s == "ГРАЖДАНИН"): 
                t.add_abridge("ГР.")
                t.add_abridge("ГРАЖД.")
                t.add_abridge("ГР-Н")
            PersonAttrToken.M_TERMINS.add(t)
        for s in ["ПАН", "ГРОМАДЯНИН", "УРОДЖЕНЕЦЬ", "ВИХОДЕЦЬ З", "МІСТЕР", "СЕР", "СЕНЬЙОР", "МОНСЕНЬЙОР", "МЕСЬЄ", "МЕТР", "МАЕСТРО"]: 
            t = PersonAttrTermin._new3151(s, MorphLang.UA, PersonAttrTerminType.PREFIX, MorphGender.MASCULINE)
            if (s == "ГРОМАДЯНИН"): 
                t.add_abridge("ГР.")
                t.add_abridge("ГР-Н")
            PersonAttrToken.M_TERMINS.add(t)
        for s in ["ГОСПОЖА", "ПАНИ", "ГРАЖДАНКА", "УРОЖЕНКА", "СЕНЬОРА", "СЕНЬОРИТА", "СИНЬОРА", "СИНЬОРИТА", "МИСС", "МИССИС", "МАДАМ", "МАДЕМУАЗЕЛЬ", "ФРАУ", "ФРОЙЛЯЙН", "ЛЕДИ", "ДОННА"]: 
            t = PersonAttrTermin._new3150(s, PersonAttrTerminType.PREFIX, MorphGender.FEMINIE)
            if (s == "ГРАЖДАНКА"): 
                t.add_abridge("ГР.")
                t.add_abridge("ГРАЖД.")
                t.add_abridge("ГР-КА")
            PersonAttrToken.M_TERMINS.add(t)
        for s in ["ПАНІ", "ГРОМАДЯНКА", "УРОДЖЕНКА", "СЕНЬЙОРА", "СЕНЬЙОРА", "МІС", "МІСІС", "МАДАМ", "МАДЕМУАЗЕЛЬ", "ФРАУ", "ФРОЙЛЯЙН", "ЛЕДІ"]: 
            t = PersonAttrTermin._new3151(s, MorphLang.UA, PersonAttrTerminType.PREFIX, MorphGender.FEMINIE)
            if (s == "ГРОМАДЯНКА"): 
                t.add_abridge("ГР.")
                t.add_abridge("ГР-КА")
            PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3151("MISTER", MorphLang.EN, PersonAttrTerminType.PREFIX, MorphGender.MASCULINE)
        t.add_abridge("MR")
        t.add_abridge("MR.")
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3151("MISSIS", MorphLang.EN, PersonAttrTerminType.PREFIX, MorphGender.FEMINIE)
        t.add_abridge("MRS")
        t.add_abridge("MSR.")
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3151("MISS", MorphLang.EN, PersonAttrTerminType.PREFIX, MorphGender.FEMINIE)
        t.add_abridge("MS")
        t.add_abridge("MS.")
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3148("БЕЗРАБОТНЫЙ", PersonAttrTerminType.POSITION)
        t.add_variant("НЕ РАБОТАЮЩИЙ", False)
        t.add_variant("НЕ РАБОТАЕТ", False)
        t.add_variant("ВРЕМЕННО НЕ РАБОТАЮЩИЙ", False)
        t.add_variant("ВРЕМЕННО НЕ РАБОТАЕТ", False)
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3149("БЕЗРОБІТНИЙ", MorphLang.UA, PersonAttrTerminType.POSITION)
        t.add_variant("НЕ ПРАЦЮЮЧИЙ", False)
        t.add_variant("НЕ ПРАЦЮЄ", False)
        t.add_variant("ТИМЧАСОВО НЕ ПРАЦЮЮЧИЙ", False)
        t.add_variant("ТИМЧАСОВО НЕ ПРАЦЮЄ", False)
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3159("ЗАМЕСТИТЕЛЬ", "заместитель", PersonAttrTerminType2.IO2, PersonAttrTerminType.POSITION)
        t.add_variant("ЗАМЕСТИТЕЛЬНИЦА", False)
        t.add_abridge("ЗАМ.")
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3160("ЗАСТУПНИК", MorphLang.UA, "заступник", PersonAttrTerminType2.IO2, PersonAttrTerminType.POSITION)
        t.add_variant("ЗАСТУПНИЦЯ", False)
        t.add_abridge("ЗАМ.")
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3159("УПОЛНОМОЧЕННЫЙ", "уполномоченный", PersonAttrTerminType2.IO2, PersonAttrTerminType.POSITION)
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3160("УПОВНОВАЖЕНИЙ", MorphLang.UA, "уповноважений", PersonAttrTerminType2.IO2, PersonAttrTerminType.POSITION)
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3159("ЭКС-УПОЛНОМОЧЕННЫЙ", "экс-уполномоченный", PersonAttrTerminType2.IO2, PersonAttrTerminType.POSITION)
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3160("ЕКС-УПОВНОВАЖЕНИЙ", MorphLang.UA, "екс-уповноважений", PersonAttrTerminType2.IO2, PersonAttrTerminType.POSITION)
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3165("ИСПОЛНЯЮЩИЙ ОБЯЗАННОСТИ", PersonAttrTerminType2.IO, PersonAttrTerminType.POSITION)
        t.add_abridge("И.О.")
        t.acronym = "ИО"
        t.canonic_text = t.acronym
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3166("ВИКОНУЮЧИЙ ОБОВЯЗКИ", MorphLang.UA, PersonAttrTerminType2.IO, PersonAttrTerminType.POSITION)
        t.add_abridge("В.О.")
        t.acronym = "ВО"
        t.canonic_text = t.acronym
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3165("ВРЕМЕННО ИСПОЛНЯЮЩИЙ ОБЯЗАННОСТИ", PersonAttrTerminType2.IO, PersonAttrTerminType.POSITION)
        t.add_abridge("ВР.И.О.")
        t.acronym = "ВРИО"
        t.canonic_text = t.acronym
        PersonAttrToken.M_TERMIN_VRIO = t
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3148("ЗАВЕДУЮЩИЙ", PersonAttrTerminType.POSITION)
        t.add_abridge("ЗАВЕД.")
        t.add_abridge("ЗАВ.")
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3149("ЗАВІДУВАЧ", MorphLang.UA, PersonAttrTerminType.POSITION)
        t.add_abridge("ЗАВІД.")
        t.add_abridge("ЗАВ.")
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3148("СОТРУДНИК", PersonAttrTerminType.POSITION)
        t.add_abridge("СОТРУДН.")
        t.add_abridge("СОТР.")
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3149("СПІВРОБІТНИК", MorphLang.UA, PersonAttrTerminType.POSITION)
        t.add_abridge("СПІВРОБ.")
        t.add_abridge("СПІВ.")
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3148("АКАДЕМИК", PersonAttrTerminType.POSITION)
        t.add_abridge("АКАД.")
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3149("АКАДЕМІК", MorphLang.UA, PersonAttrTerminType.POSITION)
        t.add_abridge("АКАД.")
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3148("ЧЛЕН-КОРРЕСПОНДЕНТ", PersonAttrTerminType.POSITION)
        t.add_abridge("ЧЛ.-КОРР.")
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3149("ЧЛЕН-КОРЕСПОНДЕНТ", MorphLang.UA, PersonAttrTerminType.POSITION)
        t.add_abridge("ЧЛ.-КОР.")
        t.add_abridge("ЧЛ.-КОРР.")
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3148("ДОЦЕНТ", PersonAttrTerminType.POSITION)
        t.add_abridge("ДОЦ.")
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3148("ПРОФЕССОР", PersonAttrTerminType.POSITION)
        t.add_abridge("ПРОФ.")
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3149("ПРОФЕСОР", MorphLang.UA, PersonAttrTerminType.POSITION)
        t.add_abridge("ПРОФ.")
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3149("PROFESSOR", MorphLang.EN, PersonAttrTerminType.POSITION)
        t.add_abridge("PROF.")
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3165("КАНДИДАТ", PersonAttrTerminType2.GRADE, PersonAttrTerminType.POSITION)
        t.add_abridge("КАНД.")
        t.add_abridge("КАН.")
        t.add_abridge("К-Т")
        t.add_abridge("К.")
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3165("ДОКТОР", PersonAttrTerminType2.GRADE, PersonAttrTerminType.POSITION)
        t.add_abridge("ДОКТ.")
        t.add_abridge("ДОК.")
        t.add_abridge("Д-Р")
        t.add_abridge("Д.")
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3149("DOCTOR", MorphLang.EN, PersonAttrTerminType.PREFIX)
        t.add_abridge("DR")
        t.add_abridge("DR.")
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3148("ДОКТОРАНТ", PersonAttrTerminType.POSITION)
        PersonAttrToken.M_TERMINS.add(t)
        t = PersonAttrTermin._new3149("ДОКТОРАНТ", MorphLang.UA, PersonAttrTerminType.POSITION)
        PersonAttrToken.M_TERMINS.add(t)
        for s in ["КФН", "КТН", "КХН"]: 
            t = PersonAttrTermin._new3185(s, "кандидат наук", PersonAttrTerminType.POSITION, PersonAttrTerminType2.ABBR)
            PersonAttrToken.M_TERMINS.add(t)
        for s in ["ГЛАВНЫЙ", "МЛАДШИЙ", "СТАРШИЙ", "ВЕДУЩИЙ", "НАУЧНЫЙ"]: 
            t = PersonAttrTermin._new3165(s, PersonAttrTerminType2.ADJ, PersonAttrTerminType.POSITION)
            t.add_all_abridges(0, 0, 2)
            PersonAttrToken.M_TERMINS.add(t)
        for s in ["ГОЛОВНИЙ", "МОЛОДШИЙ", "СТАРШИЙ", "ПРОВІДНИЙ", "НАУКОВИЙ"]: 
            t = PersonAttrTermin._new3187(s, PersonAttrTerminType2.ADJ, PersonAttrTerminType.POSITION, MorphLang.UA)
            t.add_all_abridges(0, 0, 2)
            PersonAttrToken.M_TERMINS.add(t)
        for s in ["НЫНЕШНИЙ", "НОВЫЙ", "CURRENT", "NEW"]: 
            t = PersonAttrTermin._new3165(s, PersonAttrTerminType2.IGNOREDADJ, PersonAttrTerminType.POSITION)
            PersonAttrToken.M_TERMINS.add(t)
        for s in ["НИНІШНІЙ", "НОВИЙ"]: 
            t = PersonAttrTermin._new3187(s, PersonAttrTerminType2.IGNOREDADJ, PersonAttrTerminType.POSITION, MorphLang.UA)
            PersonAttrToken.M_TERMINS.add(t)
        for s in ["ТОГДАШНИЙ", "БЫВШИЙ", "ПРЕДЫДУЩИЙ", "FORMER", "PREVIOUS", "THEN"]: 
            t = PersonAttrTermin._new3165(s, PersonAttrTerminType2.IO, PersonAttrTerminType.POSITION)
            PersonAttrToken.M_TERMINS.add(t)
        for s in ["ТОДІШНІЙ", "КОЛИШНІЙ"]: 
            t = PersonAttrTermin._new3187(s, PersonAttrTerminType2.IO, PersonAttrTerminType.POSITION, MorphLang.UA)
            PersonAttrToken.M_TERMINS.add(t)
        dat = PullentiNerPersonInternalResourceHelper.get_bytes("attr_ru.dat")
        if (dat is None): 
            raise Utils.newException("Not found resource file attr_ru.dat in Person analyzer", None)
        PersonAttrToken.__load_attrs(PersonAttrToken.M_TERMINS, dat, MorphLang.RU)
        dat = PullentiNerPersonInternalResourceHelper.get_bytes("attr_en.dat")
        if ((dat) is None): 
            raise Utils.newException("Not found resource file attr_en.dat in Person analyzer", None)
        PersonAttrToken.__load_attrs(PersonAttrToken.M_TERMINS, dat, MorphLang.EN)
        PersonAttrToken.__load_attrs(PersonAttrToken.M_TERMINS, PullentiNerPersonInternalResourceHelper.get_bytes("attr_ua.dat"), MorphLang.UA)
        PersonAttrToken.M_TERMINS_GRADE = TerminCollection()
        gr_full = ["архитектуры", "биологических наук", "ветеринарных наук", "военных наук", "географических наук", "геолого-минералогических наук", "искусствоведения", "исторических наук", "культурологии", "медицинских наук", "педагогических наук", "политических наук", "психологических наук", "сельскохозяйственных наук", "социологических наук", "теологических наук", "технических наук", "фармацевтических наук", "физико-математических наук", "филологических наук", "философских наук", "химических наук", "экономических наук", "юридических наук"]
        gr_sh1 = ["архитектуры", "биол. наук", "ветеринар. наук", "воен. наук", "геогр. наук", "геол.-минерал. наук", "искусствоведения", "ист. наук", "культурологии", "мед. наук", "пед. наук", "полит. наук", "психол. наук", "с.-х. наук", "социол. наук", "теол. наук", "техн. наук", "фарм. наук", "физ.-мат. наук", "филол. наук", "филос. наук", "хим. наук", "экон. наук", "юрид. наук"]
        gr_sh2 = ["арх.", "б.н.", "вет.н.", "воен.н.", "г.н.", "г.-м.н.", "иск.", "и.н.", "культ.", "м.н.", "пед. н.", "полит. н.", "п. н.", "с.-х. н.", "социол. н.", "теол. н.", "т. н.", "фарм. н.", "ф.-м. н.", "ф. н.", "филос. н.", "х. н.", "э. н.", "ю. н."]
        i = 0
        while i < len(gr_full): 
            t = PersonAttrTermin(gr_full[i].upper())
            t.add_abridge(gr_sh1[i].upper())
            t.add_abridge(gr_sh2[i].upper())
            PersonAttrToken.M_TERMINS_GRADE.add(t)
            i += 1
    
    M_TERMINS = None
    
    M_TERMIN_VRIO = None
    
    M_TERMINS_GRADE = None
    
    @staticmethod
    def __deflate(zip0_ : bytearray) -> bytearray:
        with MemoryStream() as unzip: 
            data_ = MemoryStream(zip0_)
            data_.position = 0
            MorphDeserializer.deflate_gzip(data_, unzip)
            data_.close()
            return unzip.toarray()
    
    @staticmethod
    def __load_attrs(termins : 'TerminCollection', dat : bytearray, lang : 'MorphLang') -> None:
        if (dat is None or len(dat) == 0): 
            return
        with MemoryStream(PersonAttrToken.__deflate(dat)) as tmp: 
            tmp.position = 0
            xml0_ = None # new XmlDocument
            xml0_ = Utils.parseXmlFromStream(tmp)
            for x in xml0_.getroot(): 
                a = Utils.getXmlAttrByName(x.attrib, "v")
                if (a is None): 
                    continue
                val = a[1]
                if (val is None): 
                    continue
                attrs = ("" if Utils.getXmlAttrByName(x.attrib, "a") is None else (Utils.ifNotNull(Utils.getXmlAttrByName(x.attrib, "a")[1], "")))
                if (val == "ДЕВОЧКА"): 
                    pass
                pat = PersonAttrTermin._new3192(val, PersonAttrTerminType.POSITION, lang)
                for ch in attrs: 
                    if (ch == 'p'): 
                        pat.can_has_person_after = 1
                    elif (ch == 'P'): 
                        pat.can_has_person_after = 2
                    elif (ch == 's'): 
                        pat.can_be_same_surname = True
                    elif (ch == 'm'): 
                        pat.gender = MorphGender.MASCULINE
                    elif (ch == 'f'): 
                        pat.gender = MorphGender.FEMINIE
                    elif (ch == 'b'): 
                        pat.is_boss = True
                    elif (ch == 'r'): 
                        pat.is_military_rank = True
                    elif (ch == 'n'): 
                        pat.is_nation = True
                    elif (ch == 'c'): 
                        pat.typ = PersonAttrTerminType.KING
                    elif (ch == 'q'): 
                        pat.typ = PersonAttrTerminType.KING
                    elif (ch == 'k'): 
                        pat.is_kin = True
                    elif (ch == 'a'): 
                        pat.typ2 = PersonAttrTerminType2.IO2
                    elif (ch == '1'): 
                        pat.can_be_independant = True
                    elif (ch == 'w'): 
                        pat.is_profession = True
                    elif (ch == 'd'): 
                        pat.is_post = True
                    elif (ch == '?'): 
                        pat.is_doubt = True
                if (Utils.getXmlAttrByName(x.attrib, "alt") is not None): 
                    val = Utils.getXmlAttrByName(x.attrib, "alt")[1]
                    pat.add_variant(val, False)
                    if (val.find('.') > 0): 
                        pat.add_abridge(val)
                if (len(x) > 0): 
                    for xx in x: 
                        if (Utils.getXmlName(xx) == "alt"): 
                            val = Utils.getXmlInnerText(xx)
                            pat.add_variant(val, False)
                            if (val.find('.') > 0): 
                                pat.add_abridge(val)
                termins.add(pat)
    
    def __init__(self, begin : 'Token', end : 'Token') -> None:
        super().__init__(None, begin, end, None)
        self.typ = PersonAttrTerminType.PREFIX
        self.gender = MorphGender.UNDEFINED
        self.value = None;
        self.age = None;
        self.higher_prop_ref = None;
        self.add_outer_org_as_ref = False
        self.anafor = None;
        self.__m_can_be_independent_property = False
        self.can_be_single_person = False
        self.can_has_person_after = 0
        self.can_be_same_surname = False
        self.is_doubt = False
    
    @property
    def prop_ref(self) -> 'PersonPropertyReferent':
        return Utils.asObjectOrNull(self.referent, PersonPropertyReferent)
    @prop_ref.setter
    def prop_ref(self, value_) -> 'PersonPropertyReferent':
        self.referent = (value_)
        return value_
    
    @property
    def can_be_independent_property(self) -> bool:
        if (self.prop_ref is None): 
            return False
        if (self.morph.number == MorphNumber.PLURAL): 
            return False
        if (self.higher_prop_ref is not None and self.higher_prop_ref.can_be_independent_property): 
            return True
        if (self.can_be_single_person): 
            return True
        if (self.typ != PersonAttrTerminType.POSITION): 
            return False
        if (not self.__m_can_be_independent_property): 
            if (self.prop_ref.kind == PersonPropertyKind.BOSS): 
                return True
            return False
        if (self.prop_ref.find_slot(PersonPropertyReferent.ATTR_REF, None, True) is not None): 
            if (self.prop_ref.name != "член"): 
                return True
        return False
    @can_be_independent_property.setter
    def can_be_independent_property(self, value_) -> bool:
        self.__m_can_be_independent_property = value_
        return value_
    
    def __str__(self) -> str:
        if (self.referent is not None): 
            return super().__str__()
        res = io.StringIO()
        print("{0}: {1}".format(Utils.enumToString(self.typ), Utils.ifNotNull(self.value, "")), end="", file=res, flush=True)
        if (self.prop_ref is not None): 
            print(" Ref: {0}".format(str(self.prop_ref)), end="", file=res, flush=True)
        if (self.gender != MorphGender.UNDEFINED): 
            print("; {0}".format(Utils.enumToString(self.gender)), end="", file=res, flush=True)
        if (self.can_has_person_after >= 0): 
            print("; MayBePersonAfter={0}".format(self.can_has_person_after), end="", file=res, flush=True)
        if (self.can_be_same_surname): 
            print("; CanHasLikeSurname", end="", file=res)
        if (self.__m_can_be_independent_property): 
            print("; CanBeIndependent", end="", file=res)
        if (self.is_doubt): 
            print("; Doubt", end="", file=res)
        if (self.age is not None): 
            print("; Age={0}".format(self.age), end="", file=res, flush=True)
        if (not self.morph.case_.is_undefined): 
            print("; {0}".format(str(self.morph.case_)), end="", file=res, flush=True)
        return Utils.toStringStringIO(res)
    
    def save_to_local_ontology(self) -> None:
        ad = self.data
        if (ad is None or self.prop_ref is None or self.higher_prop_ref is None): 
            super().save_to_local_ontology()
            return
        li = list()
        pr = self
        while pr is not None and pr.prop_ref is not None: 
            li.insert(0, pr)
            pr = pr.higher_prop_ref
        i = 0
        while i < len(li): 
            li[i].data = ad
            li[i].higher_prop_ref = (None)
            li[i].save_to_local_ontology()
            if ((i + 1) < len(li)): 
                li[i + 1].prop_ref.higher = li[i].prop_ref
            i += 1
    
    SPEED_REGIME = False
    
    @staticmethod
    def _prepare_all_data(t0 : 'Token') -> None:
        if (not PersonAttrToken.SPEED_REGIME): 
            return
        ad = PersonAnalyzer._get_data(t0)
        if (ad is None): 
            return
        t = t0
        while t is not None: 
            d = Utils.asObjectOrNull(t.tag, PersonTokenData)
            typ_ = PersonAttrToken.try_attach(t, PersonAttrToken.PersonAttrAttachAttrs.NO)
            if (typ_ is not None): 
                if (d is None): 
                    d = PersonTokenData(t)
                d.attr = typ_
            t = t.next0_
    
    @staticmethod
    def try_attach(t : 'Token', attrs : 'PersonAttrAttachAttrs'=PersonAttrAttachAttrs.NO) -> 'PersonAttrToken':
        if (t is None): 
            return None
        ad = PersonAnalyzer._get_data(t)
        if (ad is None): 
            return None
        if (PersonAttrToken.SPEED_REGIME and ad.aregime and attrs == PersonAttrToken.PersonAttrAttachAttrs.NO): 
            d = Utils.asObjectOrNull(t.tag, PersonTokenData)
            if (d is not None): 
                return d.attr
            return None
        if (ad.level > 4): 
            return None
        ad.level += 1
        res = PersonAttrToken.__try_attach(t, attrs)
        ad.level -= 1
        if (t.is_value("СПОРТСМЕНКА", None)): 
            pass
        if (res is None): 
            if (t.morph.class0_.is_noun): 
                aterr = Utils.asObjectOrNull(t.kit.processor.find_analyzer("GEO"), GeoAnalyzer)
                if (aterr is not None): 
                    rt = aterr.process_citizen(t)
                    if (rt is not None): 
                        res = PersonAttrToken._new3193(rt.begin_token, rt.end_token, rt.morph)
                        res.prop_ref = PersonPropertyReferent()
                        res.prop_ref.add_slot(PersonPropertyReferent.ATTR_NAME, ("громадянин" if t.kit.base_language.is_ua else "гражданин"), True, 0)
                        res.prop_ref.add_slot(PersonPropertyReferent.ATTR_REF, rt.referent, True, 0)
                        res.prop_ref.add_ext_referent(rt)
                        res.typ = PersonAttrTerminType.POSITION
                        if ((res.end_token.next0_ is not None and res.end_token.next0_.is_value("ПО", None) and res.end_token.next0_.next0_ is not None) and res.end_token.next0_.next0_.is_value("ПРОИСХОЖДЕНИЕ", None)): 
                            res.end_token = res.end_token.next0_.next0_
                        return res
            if ((((isinstance(t, TextToken)) and t.term == "АК" and t.next0_ is not None) and t.next0_.is_char('.') and t.next0_.next0_ is not None) and not t.next0_.next0_.chars.is_all_lower): 
                res = PersonAttrToken._new3194(t, t.next0_, PersonAttrTerminType.POSITION)
                res.prop_ref = PersonPropertyReferent._new3195("академик")
                return res
            if ((isinstance(t, TextToken)) and t.next0_ is not None): 
                if (((t.is_value("ВИЦЕ", "ВІЦЕ") or t.is_value("ЭКС", "ЕКС") or t.is_value("ГЕН", None)) or t.is_value("VICE", None) or t.is_value("EX", None)) or t.is_value("DEPUTY", None)): 
                    tt = t.next0_
                    if (tt.is_hiphen or tt.is_char('.')): 
                        tt = tt.next0_
                    res = PersonAttrToken.__try_attach(tt, attrs)
                    if (res is not None and res.prop_ref is not None): 
                        res.begin_token = t
                        if (t.is_value("ГЕН", None)): 
                            res.prop_ref.name = "генеральный {0}".format(res.prop_ref.name)
                        else: 
                            res.prop_ref.name = "{0}-{1}".format(t.term.lower(), res.prop_ref.name)
                        return res
            if (t.is_value("ГВАРДИИ", "ГВАРДІЇ")): 
                res = PersonAttrToken.__try_attach(t.next0_, attrs)
                if (res is not None): 
                    if (res.prop_ref is not None and res.prop_ref.kind == PersonPropertyKind.MILITARYRANK): 
                        res.begin_token = t
                        return res
            tt1 = t
            if (tt1.morph.class0_.is_preposition and tt1.next0_ is not None): 
                tt1 = tt1.next0_
            if ((tt1.next0_ is not None and tt1.is_value("НАЦИОНАЛЬНОСТЬ", "НАЦІОНАЛЬНІСТЬ")) or tt1.is_value("ПРОФЕССИЯ", "ПРОФЕСІЯ") or tt1.is_value("СПЕЦИАЛЬНОСТЬ", "СПЕЦІАЛЬНІСТЬ")): 
                tt1 = tt1.next0_
                if (tt1 is not None): 
                    if (tt1.is_hiphen or tt1.is_char(':')): 
                        tt1 = tt1.next0_
                res = PersonAttrToken.__try_attach(tt1, attrs)
                if (res is not None): 
                    res.begin_token = t
                    return res
            return None
        if (res.typ == PersonAttrTerminType.OTHER and res.age is not None and res.value is None): 
            res1 = PersonAttrToken.__try_attach(res.end_token.next0_, attrs)
            if (res1 is not None): 
                res1.begin_token = res.begin_token
                res1.age = res.age
                res = res1
        if (res.end_token.is_value("ТЕХНИК", None) and (isinstance(res.end_token, TextToken))): 
            if (res.end_token.term != "ТЕХНИК"): 
                return None
        if (res.begin_token.is_value("ГЛАВА", None)): 
            if (isinstance(t.previous, NumberToken)): 
                return None
        elif (res.begin_token.is_value("АДВОКАТ", None)): 
            if (t.previous is not None): 
                if (t.previous.is_value("РЕЕСТР", "РЕЄСТР") or t.previous.is_value("УДОСТОВЕРЕНИЕ", "ПОСВІДЧЕННЯ")): 
                    return None
        mc = res.begin_token.get_morph_class_in_dictionary()
        if (mc.is_adjective): 
            npt = NounPhraseHelper.try_parse(res.begin_token, NounPhraseParseAttr.NO, 0, None)
            if (npt is not None and npt.end_char >= res.end_char): 
                if (PersonAttrToken.M_TERMINS.try_parse(npt.end_token, TerminParseAttr.NO) is None and npt.end_token.chars.is_all_lower): 
                    return None
        if (res.typ == PersonAttrTerminType.PREFIX and ((((((res.value == "ГРАЖДАНИН" or res.value == "ГРАЖДАНКА" or res.value == "УРОЖЕНЕЦ") or res.value == "УРОЖЕНКА" or res.value == "ВЫХОДЕЦ ИЗ") or res.value == "ВИХОДЕЦЬ З" or res.value == "ГРОМАДЯНИН") or res.value == "ГРОМАДЯНКА" or res.value == "УРОДЖЕНЕЦЬ") or res.value == "УРОДЖЕНКА")) and res.end_token.next0_ is not None): 
            tt = res.end_token.next0_
            if (((tt is not None and tt.is_char('(') and tt.next0_ is not None) and tt.next0_.is_value("КА", None) and tt.next0_.next0_ is not None) and tt.next0_.next0_.is_char(')')): 
                res.end_token = tt.next0_.next0_
                tt = res.end_token.next0_
            r = (None if tt is None else tt.get_referent())
            if (r is not None and r.type_name == PersonAttrToken.OBJ_NAME_GEO): 
                res.end_token = tt
                res.prop_ref = PersonPropertyReferent()
                res.prop_ref.add_slot(PersonPropertyReferent.ATTR_NAME, res.value.lower(), True, 0)
                res.prop_ref.add_slot(PersonPropertyReferent.ATTR_REF, r, True, 0)
                res.typ = PersonAttrTerminType.POSITION
                ttt = tt.next0_
                while ttt is not None: 
                    if (not ttt.is_comma_and or ttt.next0_ is None): 
                        break
                    ttt = ttt.next0_
                    r = ttt.get_referent()
                    if (r is None or r.type_name != PersonAttrToken.OBJ_NAME_GEO): 
                        break
                    res.prop_ref.add_slot(PersonPropertyReferent.ATTR_REF, r, False, 0)
                    tt = ttt
                    res.end_token = tt
                    if (ttt.previous.is_and): 
                        break
                    ttt = ttt.next0_
                if (((isinstance(res.end_token.next0_, ReferentToken)) and (res.whitespaces_after_count < 3) and res.end_token.next0_.get_referent() is not None) and res.end_token.next0_.get_referent().type_name == PersonAttrToken.OBJ_NAME_GEO): 
                    if (GeoOwnerHelper.can_be_higher(Utils.asObjectOrNull(r, GeoReferent), Utils.asObjectOrNull(res.end_token.next0_.get_referent(), GeoReferent), None, None)): 
                        res.prop_ref.add_slot(PersonPropertyReferent.ATTR_REF, res.end_token.next0_.get_referent(), False, 0)
                        res.end_token = res.end_token.next0_
            elif ((tt is not None and tt.is_and and tt.next0_ is not None) and tt.next0_.is_value("ЖИТЕЛЬ", None)): 
                aaa = PersonAttrToken.__try_attach(tt.next0_, attrs)
                if (aaa is not None and aaa.prop_ref is not None): 
                    aaa.begin_token = res.begin_token
                    aaa.value = res.value
                    aaa.prop_ref.name = aaa.value.lower()
                    res = aaa
            else: 
                tt2 = tt
                if (tt2.is_comma_and): 
                    tt2 = tt2.next0_
                nex = PersonAttrToken.__try_attach(tt2, attrs)
                if (nex is not None and nex.prop_ref is not None): 
                    for sss in nex.prop_ref.slots: 
                        if (isinstance(sss.value, GeoReferent)): 
                            if (res.prop_ref is None): 
                                res.prop_ref = PersonPropertyReferent()
                            res.prop_ref.add_slot(PersonPropertyReferent.ATTR_NAME, res.value.lower(), False, 0)
                            res.prop_ref.add_slot(sss.type_name, sss.value, False, 0)
                            res.typ = PersonAttrTerminType.POSITION
        if (res.typ == PersonAttrTerminType.KING or res.typ == PersonAttrTerminType.POSITION): 
            if (res.begin_token == res.end_token and res.chars.is_capital_upper and res.whitespaces_after_count == 1): 
                pit = PersonItemToken.try_attach(t, PersonItemToken.ParseAttr.IGNOREATTRS, None)
                if (pit is not None and pit.lastname is not None and pit.lastname.is_lastname_has_std_tail): 
                    rt1 = PersonAnalyzer.process_referent_stat(t.next0_, None)
                    if (rt1 is not None and (isinstance(rt1.referent, PersonReferent))): 
                        pass
                    elif ((((attrs) & (PersonAttrToken.PersonAttrAttachAttrs.INPROCESS))) != (PersonAttrToken.PersonAttrAttachAttrs.NO)): 
                        pass
                    else: 
                        return None
        if (res.prop_ref is None): 
            return res
        if (res.chars.is_latin_letter): 
            tt = res.end_token.next0_
            if (tt is not None and tt.is_hiphen): 
                tt = tt.next0_
            if (tt is not None and tt.is_value("ELECT", None)): 
                res.end_token = tt
        if (not res.begin_token.chars.is_all_lower): 
            pat = PersonItemToken.try_attach(res.begin_token, PersonItemToken.ParseAttr.IGNOREATTRS, None)
            if (pat is not None and pat.lastname is not None): 
                if (pat.lastname.is_in_dictionary or pat.lastname.is_in_ontology): 
                    if (PersonAttrToken.check_kind(res.prop_ref) != PersonPropertyKind.KING): 
                        return None
        s = str(res.prop_ref)
        if (s == "глава книги"): 
            return None
        if (s == "глава" and res.prop_ref.find_slot(PersonPropertyReferent.ATTR_REF, None, True) is None): 
            return None
        if (((s == "королева" or s == "король" or s == "князь")) and res.chars.is_capital_upper): 
            pits = PersonItemToken.try_attach_list(res.end_token.next0_, PersonItemToken.ParseAttr.NO, 10)
            if (pits is not None and len(pits) > 0): 
                if (pits[0].typ == PersonItemToken.ItemType.INITIAL): 
                    return None
                if (pits[0].firstname is not None): 
                    if (len(pits) == 1): 
                        return None
                    if (len(pits) == 2 and pits[1].middlename is not None): 
                        return None
            if (not MiscHelper.can_be_start_of_sentence(t)): 
                return None
        if (s == "друг" or s.startswith("друг ")): 
            if (t.previous is not None): 
                if (t.previous.is_value("ДРУГ", None)): 
                    return None
                if (t.previous.morph.class0_.is_preposition and t.previous.previous is not None and t.previous.previous.is_value("ДРУГ", None)): 
                    return None
            if (t.next0_ is not None): 
                if (t.next0_.is_value("ДРУГ", None)): 
                    return None
                if (t.next0_.morph.class0_.is_preposition and t.next0_.next0_ is not None and t.next0_.next0_.is_value("ДРУГ", None)): 
                    return None
        if (res.chars.is_latin_letter and ((res.is_doubt or s == "senior")) and (res.whitespaces_after_count < 2)): 
            if (res.prop_ref is not None and len(res.prop_ref.slots) == 1): 
                tt2 = res.end_token.next0_
                if (MiscHelper.is_eng_adj_suffix(tt2)): 
                    tt2 = tt2.next0_.next0_
                res2 = PersonAttrToken.__try_attach(tt2, attrs)
                if ((res2 is not None and res2.chars.is_latin_letter and res2.typ == res.typ) and res2.prop_ref is not None): 
                    res2.prop_ref.name = "{0} {1}".format(Utils.ifNotNull(res.prop_ref.name, ""), Utils.ifNotNull(res2.prop_ref.name, "")).strip()
                    res2.begin_token = res.begin_token
                    res = res2
        if (res.prop_ref.name == "министр"): 
            rt1 = res.kit.process_referent("ORGANIZATION", res.end_token.next0_, None)
            if (rt1 is not None and rt1.referent.find_slot("TYPE", "министерство", True) is not None): 
                t1 = rt1.end_token
                if (isinstance(t1.get_referent(), GeoReferent)): 
                    t1 = t1.previous
                if (rt1.begin_char < t1.end_char): 
                    add_str = MiscHelper.get_text_value(rt1.begin_token, t1, GetTextAttr.NO)
                    if (add_str is not None): 
                        res.prop_ref.name = res.prop_ref.name + (" " + add_str.lower())
                        res.end_token = t1
        p = res.prop_ref
        while p is not None: 
            if (p.name is not None and " - " in p.name): 
                p.name = p.name.replace(" - ", "-")
            p = p.higher
        if (res.begin_token.morph.class0_.is_adjective): 
            r = res.kit.process_referent("GEO", res.begin_token, None)
            if (r is not None): 
                res.prop_ref.add_slot(PersonPropertyReferent.ATTR_REF, r.referent, False, 0)
                res.prop_ref.add_ext_referent(r)
                i = res.prop_ref.name.find(' ')
                if (i > 0): 
                    res.prop_ref.name = res.prop_ref.name[i:].strip()
        if (res.prop_ref is not None and res.prop_ref.kind == PersonPropertyKind.KING): 
            t1 = res.end_token.next0_
            if (res.prop_ref.name == "отец"): 
                if (t1 is None or not t1.chars.is_capital_upper): 
                    return None
                if (((res.morph.case_) & t1.morph.case_).is_undefined): 
                    return None
                res.prop_ref.name = "священник"
                return res
            if (t1 is not None and t1.chars.is_capital_upper and (t1.whitespaces_before_count < 3)): 
                adjs = list()
                is_and_ = False
                t2 = None
                tt = t1
                while tt is not None: 
                    if (((tt.is_value("ВСЕЙ", None) or tt.is_value("ВСЕЯ", "ВСІЄЇ"))) and (isinstance(tt.next0_, ReferentToken)) and (isinstance(tt.next0_.get_referent(), GeoReferent))): 
                        adjs.append(MiscHelper.convert_first_char_upper_and_other_lower(MiscHelper.get_text_value(tt, tt.next0_, GetTextAttr.NO)))
                        tt = tt.next0_
                        t2 = tt
                    elif ((isinstance(tt.get_referent(), GeoReferent)) and tt.end_token.morph.class0_.is_adjective): 
                        v = MiscHelper.get_text_value_of_meta_token(Utils.asObjectOrNull(tt, ReferentToken), GetTextAttr.NO)
                        adjs.append(MiscHelper.convert_first_char_upper_and_other_lower(v))
                        t2 = tt
                        tt = t2
                    else: 
                        if (not tt.chars.is_capital_upper): 
                            break
                        pit = PersonItemToken.try_attach(tt, PersonItemToken.ParseAttr.IGNOREATTRS, None)
                        if (pit is None or pit.value is None or pit.firstname is not None): 
                            break
                        if (pit.lastname is None and not pit.value.endswith("КИЙ")): 
                            break
                        v = None
                        if (pit.lastname is None): 
                            v = pit.value
                        else: 
                            for fv in pit.lastname.vars0_: 
                                if (fv.value.endswith("КИЙ")): 
                                    v = fv.value
                                    break
                        if (v is None): 
                            break
                        adjs.append(MiscHelper.convert_first_char_upper_and_other_lower(v))
                        t2 = pit.end_token
                        tt = t2
                    if (tt.next0_ is None): 
                        break
                    tt = tt.next0_
                    if (not tt.is_comma_and): 
                        break
                    is_and_ = tt.is_and
                    tt = tt.next0_
                if (len(adjs) > 1 and not is_and_): 
                    pass
                elif (t2 is not None): 
                    i = 0
                    while i < len(adjs): 
                        if (i > 0): 
                            res.prop_ref.name = "{0}{1}".format(res.prop_ref.name, ("," if (i + 1) < len(adjs) else " и"))
                        res.prop_ref.name = "{0} {1}".format(res.prop_ref.name, adjs[i])
                        i += 1
                    res.end_token = t2
        contains_geo = False
        for ss in res.prop_ref.slots: 
            if (isinstance(ss.value, Referent)): 
                if (ss.value.type_name == PersonAttrToken.OBJ_NAME_GEO): 
                    contains_geo = True
                    break
        if (not contains_geo and (res.end_token.whitespaces_after_count < 2)): 
            if ((isinstance(res.end_token.next0_, ReferentToken)) and res.end_token.next0_.get_referent().type_name == PersonAttrToken.OBJ_NAME_GEO): 
                res.prop_ref.add_slot(PersonPropertyReferent.ATTR_REF, res.end_token.next0_.get_referent(), False, 0)
                res.end_token = res.end_token.next0_
        if (res.end_token.whitespaces_after_count < 2): 
            te = res.end_token.next0_
            if (te is not None and te.is_value("В", None)): 
                te = te.next0_
                if ((isinstance(te, ReferentToken)) and ((te.get_referent().type_name == PersonAttrToken.OBJ_NAME_DATE or te.get_referent().type_name == PersonAttrToken.OBJ_NAME_DATE_RANGE))): 
                    res.end_token = te
            elif (te is not None and te.is_char('(')): 
                te = te.next0_
                if (((isinstance(te, ReferentToken)) and ((te.get_referent().type_name == PersonAttrToken.OBJ_NAME_DATE or te.get_referent().type_name == PersonAttrToken.OBJ_NAME_DATE_RANGE)) and te.next0_ is not None) and te.next0_.is_char(')')): 
                    res.end_token = te.next0_
                elif (isinstance(te, NumberToken)): 
                    rt1 = te.kit.process_referent("DATE", te, None)
                    if (rt1 is not None and rt1.end_token.next0_ is not None and rt1.end_token.next0_.is_char(')')): 
                        res.end_token = rt1.end_token.next0_
        if (res.prop_ref is not None and res.prop_ref.name == "отец"): 
            is_king = False
            tt = res.end_token.next0_
            if ((isinstance(tt, TextToken)) and tt.get_morph_class_in_dictionary().is_proper_name): 
                if (not ((res.morph.case_) & tt.morph.case_).is_undefined): 
                    if (not tt.morph.case_.is_genitive): 
                        is_king = True
            if (is_king): 
                res.prop_ref.name = "священник"
        if (res.can_has_person_after > 0 and res.prop_ref.find_slot(PersonPropertyReferent.ATTR_REF, None, True) is None): 
            npt = NounPhraseHelper.try_parse(res.begin_token, NounPhraseParseAttr.NO, 0, None)
            tt0 = res.begin_token
            have = False
            if ((isinstance(tt0, TextToken)) and tt0.morph.class0_.is_personal_pronoun and ((tt0.is_value("ОН", None) or tt0.is_value("ОНА", None)))): 
                pass
            else: 
                tt0 = tt0.previous
                if ((isinstance(tt0, TextToken)) and tt0.morph.class0_.is_personal_pronoun and ((tt0.is_value("ОН", None) or tt0.is_value("ОНА", None)))): 
                    pass
                elif ((isinstance(tt0, TextToken)) and tt0.morph.class0_.is_pronoun and tt0.is_value("СВОЙ", None)): 
                    pass
                elif ((isinstance(tt0, TextToken)) and ((tt0.is_value("ИМЕТЬ", None) or tt0.is_verb_be))): 
                    have = True
                else: 
                    tt0 = (None)
            if (tt0 is not None): 
                gen = MorphGender.UNDEFINED
                cou = 0
                if (not have): 
                    for wf in tt0.morph.items: 
                        if (wf.class0_.is_personal_pronoun or wf.class0_.is_pronoun): 
                            gen = wf.gender
                            if (((gen)) == MorphGender.NEUTER): 
                                gen = MorphGender.MASCULINE
                            break
                tt = tt0.previous
                first_pass4231 = True
                while True:
                    if first_pass4231: first_pass4231 = False
                    else: tt = tt.previous; cou += 1
                    if (not (tt is not None and (cou < 20))): break
                    pr = Utils.asObjectOrNull(tt.get_referent(), PersonPropertyReferent)
                    if (pr is not None): 
                        if (((tt.morph.gender) & (gen)) == (MorphGender.UNDEFINED)): 
                            continue
                        break
                    p = Utils.asObjectOrNull(tt.get_referent(), PersonReferent)
                    if (p is None): 
                        continue
                    if (have and (cou < 10)): 
                        pass
                    elif (gen == MorphGender.FEMINIE): 
                        if (p.is_male and not p.is_female): 
                            continue
                    elif (gen == MorphGender.MASCULINE): 
                        if (p.is_female and not p.is_male): 
                            continue
                    else: 
                        break
                    res.begin_token = (tt0.next0_ if have else tt0)
                    res.prop_ref.add_slot(PersonPropertyReferent.ATTR_REF, p, False, 0)
                    res.can_be_independent_property = True
                    if (res.morph.number != MorphNumber.PLURAL): 
                        res.can_be_single_person = True
                    npt = NounPhraseHelper.try_parse(tt0, NounPhraseParseAttr.NO, 0, None)
                    if (npt is not None and npt.begin_token != npt.end_token): 
                        res.morph = npt.morph
                    break
            elif (res.whitespaces_after_count == 1): 
                pa = Utils.asObjectOrNull(res.kit.processor.find_analyzer("PERSON"), PersonAnalyzer)
                if (pa is not None): 
                    t1 = res.end_token.next0_
                    pr = PersonAnalyzer._try_attach_person(t1, False, 0, True)
                    if (pr is not None and res.can_has_person_after == 1): 
                        if (pr.begin_token == t1): 
                            if (not pr.morph.case_.is_genitive and not pr.morph.case_.is_undefined): 
                                pr = (None)
                            elif (not pr.morph.case_.is_undefined and not ((res.morph.case_) & pr.morph.case_).is_undefined): 
                                if (PersonAnalyzer._try_attach_person(pr.end_token.next0_, False, 0, True) is not None): 
                                    pass
                                else: 
                                    pr = (None)
                        elif (pr.begin_token.previous == t1): 
                            pr = (None)
                            res.prop_ref.name = "{0} {1}".format(res.prop_ref.name, t1.get_source_text().lower())
                            res.end_token = t1
                        else: 
                            pr = (None)
                    elif (pr is not None and res.can_has_person_after == 2): 
                        pits = PersonItemToken.try_attach_list(t1, PersonItemToken.ParseAttr.NO, 10)
                        if (((pits is not None and len(pits) > 1 and pits[0].firstname is not None) and pits[1].firstname is not None and pr.end_char > pits[0].end_char) and pits[0].morph.case_.is_genitive): 
                            pr = (None)
                            cou = 100
                            tt = t1.previous
                            first_pass4232 = True
                            while True:
                                if first_pass4232: first_pass4232 = False
                                else: tt = tt.previous; cou -= 1
                                if (not (tt is not None and cou > 0)): break
                                p0 = Utils.asObjectOrNull(tt.get_referent(), PersonReferent)
                                if (p0 is None): 
                                    continue
                                for v in pits[0].firstname.vars0_: 
                                    if (p0.find_slot(PersonReferent.ATTR_FIRSTNAME, v.value, True) is not None): 
                                        pr = ReferentToken(p0, t1, pits[0].end_token)
                                        break
                                if (pr is not None): 
                                    break
                        elif (pits is not None and len(pits) == 3 and ((pits[2].middlename is not None or ((pits[1].typ == PersonItemToken.ItemType.INITIAL and pits[2].typ == PersonItemToken.ItemType.INITIAL))))): 
                            tt = pits[2].end_token.next0_
                            if (tt is not None and ((tt.is_hiphen or tt.is_char('(')))): 
                                pits2 = PersonItemToken.try_attach_list(tt.next0_, PersonItemToken.ParseAttr.NO, 10)
                                if (pits2 is not None and len(pits2) > 0): 
                                    pass
                                else: 
                                    pr = (None)
                            else: 
                                pr = (None)
                    if (pr is not None): 
                        res.prop_ref.add_slot(PersonPropertyReferent.ATTR_REF, pr, False, 0)
                        res.end_token = pr.end_token
                        res.can_be_independent_property = True
                        if (res.morph.number != MorphNumber.PLURAL): 
                            res.can_be_single_person = True
        if (res.prop_ref.higher is None and res.prop_ref.kind == PersonPropertyKind.BOSS and res.prop_ref.find_slot(PersonPropertyReferent.ATTR_REF, None, True) is None): 
            tok = PersonAttrToken.M_TERMINS.try_parse(res.begin_token, TerminParseAttr.NO)
            if (tok is not None and tok.end_token == res.end_token): 
                cou = 0
                refs = list()
                tt = tok.begin_token.previous
                first_pass4233 = True
                while True:
                    if first_pass4233: first_pass4233 = False
                    else: tt = tt.previous
                    if (not (tt is not None)): break
                    if (tt.whitespaces_after_count > 15): 
                        break
                    if (tt.is_newline_after): 
                        cou += 10
                    cou += 1
                    if (cou > 1000): 
                        break
                    if (not (isinstance(tt, ReferentToken))): 
                        continue
                    li = tt.get_referents()
                    if (li is None): 
                        continue
                    breaks = False
                    for r in li: 
                        if (((r.type_name == "ORGANIZATION" or r.type_name == "GEO")) and r.parent_referent is None): 
                            if (not r in refs): 
                                if (res.prop_ref.can_has_ref(r)): 
                                    refs.append(r)
                        elif (isinstance(r, PersonPropertyReferent)): 
                            if (r.find_slot(PersonPropertyReferent.ATTR_REF, None, True) is not None): 
                                breaks = True
                        elif (isinstance(r, PersonReferent)): 
                            breaks = True
                    if (len(refs) > 1 or breaks): 
                        break
                if (len(refs) == 1): 
                    res.prop_ref.add_slot(PersonPropertyReferent.ATTR_REF, refs[0], False, 0)
                    res.add_outer_org_as_ref = True
        if (res.chars.is_latin_letter and res.prop_ref is not None and res.prop_ref.find_slot(PersonPropertyReferent.ATTR_REF, None, True) is None): 
            if (res.begin_token.previous is not None and res.begin_token.previous.is_value("S", None)): 
                if (MiscHelper.is_eng_adj_suffix(res.begin_token.previous.previous) and (isinstance(res.begin_token.previous.previous.previous, ReferentToken))): 
                    res.begin_token = res.begin_token.previous.previous.previous
                    res.prop_ref.add_slot(PersonPropertyReferent.ATTR_REF, res.begin_token.get_referent(), False, 0)
        if (res.chars.is_latin_letter and res.prop_ref is not None and (res.whitespaces_after_count < 2)): 
            rnext = PersonAttrToken.try_attach(res.end_token.next0_, PersonAttrToken.PersonAttrAttachAttrs.NO)
            if ((rnext is not None and rnext.chars.is_latin_letter and rnext.prop_ref is not None) and len(rnext.prop_ref.slots) == 1 and rnext.can_has_person_after > 0): 
                res.end_token = rnext.end_token
                res.prop_ref.name = "{0} {1}".format(res.prop_ref.name, rnext.prop_ref.name)
        return res
    
    @staticmethod
    def __try_attach(t : 'Token', attrs : 'PersonAttrAttachAttrs') -> 'PersonAttrToken':
        if (t is None): 
            return None
        if (t.morph.class0_.is_pronoun and (((t.is_value("ЕГО", "ЙОГО") or t.is_value("ЕЕ", "ЇЇ") or t.is_value("HIS", None)) or t.is_value("HER", None)))): 
            res1 = PersonAttrToken.try_attach(t.next0_, attrs)
            if (res1 is not None and res1.prop_ref is not None): 
                k = 0
                tt2 = t.previous
                first_pass4234 = True
                while True:
                    if first_pass4234: first_pass4234 = False
                    else: tt2 = tt2.previous; k += 1
                    if (not (tt2 is not None and (k < 10))): break
                    r = tt2.get_referent()
                    if (r is None): 
                        continue
                    if (r.type_name == PersonAttrToken.OBJ_NAME_ORG or (isinstance(r, PersonReferent))): 
                        ok = False
                        if (t.is_value("ЕЕ", "ЇЇ") or t.is_value("HER", None)): 
                            if (tt2.morph.gender == MorphGender.FEMINIE): 
                                ok = True
                        elif (((tt2.morph.gender) & ((MorphGender.MASCULINE) | (MorphGender.NEUTER))) != (MorphGender.UNDEFINED)): 
                            ok = True
                        if (ok): 
                            res1.prop_ref.add_slot(PersonPropertyReferent.ATTR_REF, r, False, 0)
                            res1.begin_token = t
                            return res1
                        break
            return None
        nta = NumberHelper.try_parse_age(t)
        if (nta is not None): 
            if (nta.morph.class0_.is_adjective or ((t.previous is not None and t.previous.is_comma)) or ((nta.end_token.next0_ is not None and nta.end_token.next0_.is_char_of(",.")))): 
                return PersonAttrToken._new3196(t, nta.end_token, PersonAttrTerminType.OTHER, str(nta.value), nta.morph)
        if (t.is_newline_before): 
            li = MailLine.parse(t, 0, 0)
            if (li is not None and li.typ == MailLine.Types.BESTREGARDS): 
                return PersonAttrToken._new3198(li.begin_token, li.end_token, PersonAttrTerminType.BESTREGARDS, MorphCollection._new3197(MorphCase.NOMINATIVE))
        tt = Utils.asObjectOrNull(t, TextToken)
        if (tt is None): 
            nt = Utils.asObjectOrNull(t, NumberToken)
            if (nt is not None): 
                if (((nt.value == "1" or nt.value == "2" or nt.value == "3")) and nt.morph.class0_.is_adjective): 
                    pat0 = PersonAttrToken.__try_attach(t.next0_, attrs)
                    if (pat0 is not None and pat0.prop_ref is not None): 
                        pat0.begin_token = t
                        for s in pat0.prop_ref.slots: 
                            if (s.type_name == PersonPropertyReferent.ATTR_NAME): 
                                if ("глава" in str(s.value)): 
                                    return None
                                pat0.prop_ref.upload_slot(s, "{0} {1}".format(((("первая" if nt.value == "1" else ("вторая" if nt.value == "2" else "третья"))) if pat0.morph.gender == MorphGender.FEMINIE or t.morph.gender == MorphGender.FEMINIE else (("первый" if nt.value == "1" else ("второй" if nt.value == "2" else "третий")))), s.value))
                        return pat0
            rr = None
            if (t is not None): 
                rr = t.get_referent()
            if (rr is not None and (((isinstance(rr, GeoReferent)) or rr.type_name == "ORGANIZATION"))): 
                ttt = t.next0_
                if (MiscHelper.is_eng_adj_suffix(ttt)): 
                    ttt = ttt.next0_.next0_
                if ((isinstance(ttt, TextToken)) and ttt.morph.language.is_en and (ttt.whitespaces_before_count < 2)): 
                    res0 = PersonAttrToken.__try_attach(ttt, attrs)
                    if (res0 is not None and res0.prop_ref is not None): 
                        res0.begin_token = t
                        res0.prop_ref.add_slot(PersonPropertyReferent.ATTR_REF, t.get_referent(), False, 0)
                        return res0
            if ((isinstance(rr, PersonReferent)) and MiscHelper.is_eng_adj_suffix(t.next0_)): 
                res0 = PersonAttrToken.__try_attach(t.next0_.next0_.next0_, attrs)
                if (res0 is not None and res0.prop_ref is not None and res0.chars.is_latin_letter): 
                    res0.begin_token = t
                    res0.prop_ref.add_slot(PersonPropertyReferent.ATTR_REF, t.get_referent(), False, 0)
                    return res0
            return None
        if (MiscHelper.is_eng_article(tt)): 
            res0 = PersonAttrToken.__try_attach(t.next0_, attrs)
            if (res0 is not None): 
                res0.begin_token = t
                return res0
        if ((tt.term == "Г" or tt.term == "ГР" or tt.term == "М") or tt.term == "Д"): 
            if (tt.next0_ is not None and tt.next0_.is_hiphen and (isinstance(tt.next0_.next0_, TextToken))): 
                pref = tt.term
                tail = tt.next0_.next0_.term
                vars0_ = None
                if (pref == "Г"): 
                    vars0_ = PersonAttrToken.__get_std_forms(tail, "ГОСПОДИН", "ГОСПОЖА")
                elif (pref == "ГР"): 
                    vars0_ = PersonAttrToken.__get_std_forms(tail, "ГРАЖДАНИН", "ГРАЖДАНКА")
                elif (pref == "М"): 
                    vars0_ = PersonAttrToken.__get_std_forms(tail, "МИСТЕР", None)
                elif (pref == "Д"): 
                    if (PersonAttrToken.__find_grade_last(tt.next0_.next0_.next0_, tt) is not None): 
                        pass
                    else: 
                        vars0_ = PersonAttrToken.__get_std_forms(tail, "ДОКТОР", None)
                if (vars0_ is not None): 
                    res = PersonAttrToken._new3194(tt, tt.next0_.next0_, PersonAttrTerminType.PREFIX)
                    for v in vars0_: 
                        res.morph.add_item(v)
                        if (res.value is None): 
                            res.value = v.normal_case
                            res.gender = v.gender
                    return res
        if (tt.term == "ГР" or tt.term == "ГРАЖД"): 
            t1 = tt
            if (tt.next0_ is not None and tt.next0_.is_char('.')): 
                t1 = tt.next0_
            if (isinstance(t1.next0_, NumberToken)): 
                return None
            return PersonAttrToken._new3200(tt, t1, PersonAttrTerminType.PREFIX, ("ГРОМАДЯНИН" if tt.morph.language.is_ua else "ГРАЖДАНИН"))
        npt0 = None
        step = 0
        while step < 2: 
            toks = PersonAttrToken.M_TERMINS.try_parse_all(t, TerminParseAttr.NO)
            if (toks is None and t.is_value("ВРИО", None)): 
                toks = list()
                toks.append(TerminToken._new563(t, t, PersonAttrToken.M_TERMIN_VRIO))
            elif (toks is None and (isinstance(t, TextToken)) and t.morph.language.is_en): 
                str0_ = t.term
                if (str0_.endswith("MAN") or str0_.endswith("PERSON") or str0_.endswith("MIST")): 
                    toks = list()
                    toks.append(TerminToken._new563(t, t, PersonAttrTermin._new3149(str0_, t.morph.language, PersonAttrTerminType.POSITION)))
                elif (str0_ == "MODEL" and (t.whitespaces_after_count < 2)): 
                    rt = PersonAnalyzer.process_referent_stat(t.next0_, None)
                    if (rt is not None and (isinstance(rt.referent, PersonReferent))): 
                        toks = list()
                        toks.append(TerminToken._new563(t, t, PersonAttrTermin._new3149(str0_, t.morph.language, PersonAttrTerminType.POSITION)))
            if ((toks is None and step == 0 and t.chars.is_latin_letter) and (t.whitespaces_after_count < 2)): 
                npt1 = NounPhraseHelper.try_parse(t, NounPhraseParseAttr.NO, 0, None)
                if (npt1 is not None and npt1.begin_token != npt1.end_token): 
                    pits = PersonItemToken.try_attach_list(t, Utils.valToEnum((PersonItemToken.ParseAttr.CANBELATIN) | (PersonItemToken.ParseAttr.IGNOREATTRS), PersonItemToken.ParseAttr), 10)
                    if (pits is not None and len(pits) > 1 and pits[0].firstname is not None): 
                        npt1 = (None)
                    k = 0
                    if (npt1 is not None): 
                        tt2 = npt1.begin_token
                        while tt2 is not None and tt2.end_char <= npt1.end_char: 
                            toks1 = PersonAttrToken.M_TERMINS.try_parse_all(tt2, TerminParseAttr.NO)
                            if (toks1 is not None): 
                                step = 1
                                toks = toks1
                                npt0 = NounPhraseHelper.try_parse(t, NounPhraseParseAttr.NO, toks1[0].end_char, None)
                                if (not toks[0].termin.is_doubt): 
                                    if (toks[0].morph.number == MorphNumber.PLURAL): 
                                        pass
                                    else: 
                                        break
                            k += 1
                            if (k >= 3 and t.chars.is_all_lower): 
                                if (not MiscHelper.is_eng_article(t.previous)): 
                                    break
                            tt2 = tt2.next0_
                elif (((npt1 is None or npt1.end_token == t)) and t.chars.is_capital_upper): 
                    mc = t.get_morph_class_in_dictionary()
                    if ((mc.is_misc or mc.is_preposition or mc.is_conjunction) or mc.is_personal_pronoun or mc.is_pronoun): 
                        pass
                    else: 
                        tt1 = None
                        if ((t.next0_ is not None and t.next0_.is_hiphen and not t.is_whitespace_after) and not t.next0_.is_whitespace_after): 
                            tt1 = t.next0_.next0_
                        elif (npt1 is None): 
                            tt1 = t.next0_
                        toks1 = PersonAttrToken.M_TERMINS.try_parse_all(tt1, TerminParseAttr.NO)
                        if (toks1 is not None and toks1[0].termin.typ == PersonAttrTerminType.POSITION and (tt1.whitespaces_before_count < 2)): 
                            step = 1
                            toks = toks1
            if (toks is not None): 
                for tok in toks: 
                    if (((tok.morph.class0_.is_preposition or tok.morph.contains_attr("к.ф.", None))) and tok.end_token == tok.begin_token): 
                        continue
                    pat = Utils.asObjectOrNull(tok.termin, PersonAttrTermin)
                    if ((isinstance(tok.end_token, TextToken)) and pat.canonic_text.startswith(tok.end_token.term)): 
                        if (tok.length_char < len(pat.canonic_text)): 
                            if (tok.end_token.next0_ is not None and tok.end_token.next0_.is_char('.')): 
                                tok.end_token = tok.end_token.next0_
                    if (pat.typ == PersonAttrTerminType.PREFIX): 
                        if (step == 0 or ((pat.canonic_text != "ГРАЖДАНИН" and pat.canonic_text != "ГРОМАДЯНИН"))): 
                            return PersonAttrToken._new3206(tok.begin_token, tok.end_token, PersonAttrTerminType.PREFIX, pat.canonic_text, tok.morph, pat.gender)
                    if (pat.typ == PersonAttrTerminType.BESTREGARDS): 
                        end = tok.end_token
                        if (end.next0_ is not None and end.next0_.is_char_of(",")): 
                            end = end.next0_
                        return PersonAttrToken._new3198(tok.begin_token, end, PersonAttrTerminType.BESTREGARDS, MorphCollection._new3197(MorphCase.NOMINATIVE))
                    if (pat.typ == PersonAttrTerminType.POSITION or pat.typ == PersonAttrTerminType.PREFIX or pat.typ == PersonAttrTerminType.KING): 
                        if (pat.canonic_text == "ГЛАВА"): 
                            num = ComplexNumToken.try_parse(tok.end_token.next0_, None, True, False)
                            if (num is not None): 
                                return None
                        res = PersonAttrToken.__create_attr_position(tok, attrs)
                        if (res is not None): 
                            if (pat.typ == PersonAttrTerminType.KING): 
                                res.typ = pat.typ
                            if (pat.gender != MorphGender.UNDEFINED and res.gender == MorphGender.UNDEFINED): 
                                res.gender = pat.gender
                            if (pat.can_has_person_after > 0): 
                                if (res.end_token.is_value(pat.canonic_text, None)): 
                                    res.can_has_person_after = pat.can_has_person_after
                                else: 
                                    for ii in range(len(pat.canonic_text) - 1, 0, -1):
                                        if (not str.isalpha(pat.canonic_text[ii])): 
                                            if (res.end_token.is_value(pat.canonic_text[ii + 1:], None)): 
                                                res.can_has_person_after = pat.can_has_person_after
                                            break
                            if (pat.can_be_same_surname): 
                                res.can_be_same_surname = True
                            if (pat.can_be_independant): 
                                res.can_be_independent_property = True
                            if (pat.is_doubt): 
                                res.is_doubt = True
                                if (res.prop_ref is not None and ((res.prop_ref.find_slot(PersonPropertyReferent.ATTR_REF, None, True) is not None))): 
                                    res.is_doubt = False
                            if ((t.end_char < res.begin_char) and res.prop_ref is not None): 
                                tt1 = res.begin_token.previous
                                if (tt1.is_hiphen): 
                                    res.prop_ref.name = "{0} {1}".format(res.prop_ref.name, MiscHelper.get_text_value(t, tt1.previous, GetTextAttr.NO).lower())
                                else: 
                                    res.prop_ref.name = "{0} {1}".format(MiscHelper.get_text_value(t, tt1, GetTextAttr.NO).lower(), res.prop_ref.name)
                                res.begin_token = t
                        if (res is not None): 
                            pit = PersonItemToken.try_attach(t, PersonItemToken.ParseAttr.IGNOREATTRS, None)
                            if (pit is not None and pit.typ == PersonItemToken.ItemType.INITIAL): 
                                ok = False
                                pit = PersonItemToken.try_attach(pit.end_token.next0_, PersonItemToken.ParseAttr.IGNOREATTRS, None)
                                if (pit is not None and pit.typ == PersonItemToken.ItemType.INITIAL): 
                                    pit = PersonItemToken.try_attach(pit.end_token.next0_, PersonItemToken.ParseAttr.IGNOREATTRS, None)
                                    if (pit is not None and pit.typ == PersonItemToken.ItemType.INITIAL): 
                                        ok = True
                                if (not ok): 
                                    if (PersonAttrToken.__try_attach(tok.end_token.next0_, attrs) is not None): 
                                        ok = True
                                if (not ok): 
                                    return None
                            if (npt0 is not None): 
                                ttt1 = (npt0.adjectives[0].begin_token if len(npt0.adjectives) > 0 else npt0.begin_token)
                                if (ttt1.begin_char < res.begin_char): 
                                    res.begin_token = ttt1
                                res.anafor = npt0.anafor
                                empty_adj = None
                                i = 0
                                while i < len(npt0.adjectives): 
                                    j = 0
                                    j = 0
                                    while j < len(PersonAttrToken.M_EMPTY_ADJS): 
                                        if (npt0.adjectives[i].is_value(PersonAttrToken.M_EMPTY_ADJS[j], None)): 
                                            break
                                        j += 1
                                    if (j < len(PersonAttrToken.M_EMPTY_ADJS)): 
                                        empty_adj = PersonAttrToken.M_EMPTY_ADJS[j].lower()
                                        del npt0.adjectives[i]
                                        break
                                    i += 1
                                na0 = npt0.get_normal_case_text(None, MorphNumber.SINGULAR, MorphGender.UNDEFINED, False).lower()
                                na1 = res.prop_ref.name
                                i = 1
                                while i < (len(na0) - 1): 
                                    if (na1.startswith(na0[i:])): 
                                        res.prop_ref.name = "{0} {1}".format(na0[0:0+i].strip(), na1)
                                        break
                                    i += 1
                                if (empty_adj is not None): 
                                    res1 = PersonAttrToken._new3209(res.begin_token, res.end_token, npt0.morph, res)
                                    res1.prop_ref = PersonPropertyReferent()
                                    res1.prop_ref.name = empty_adj
                                    res1.prop_ref.higher = res.prop_ref
                                    res1.can_be_independent_property = res.can_be_independent_property
                                    res1.typ = res.typ
                                    if (res.begin_token != res.end_token): 
                                        res.begin_token = res.begin_token.next0_
                                    res = res1
                            if (res is not None): 
                                res.morph.remove_not_in_dictionary_items()
                            return res
            if (step > 0 or t.chars.is_latin_letter): 
                break
            if (t.morph.class0_.is_adjective or t.chars.is_latin_letter): 
                pass
            elif (t.next0_ is not None and t.next0_.is_hiphen): 
                pass
            else: 
                break
            npt = NounPhraseHelper.try_parse(t, NounPhraseParseAttr.NO, 0, None)
            if (npt is None or npt.end_token == t or npt.internal_noun is not None): 
                break
            if (npt.end_token.is_value("ВИЦЕ", "ВІЦЕ")): 
                break
            t = npt.end_token
            npt0 = npt
            step += 1
        if ((isinstance(t, TextToken)) and (((t.is_value("ВИЦЕ", "ВІЦЕ") or t.is_value("ЭКС", "ЕКС") or t.is_value("VICE", None)) or t.is_value("EX", None) or t.is_value("DEPUTY", None))) and t.next0_ is not None): 
            te = t.next0_
            if (te.is_hiphen): 
                te = te.next0_
            ppp = PersonAttrToken.__try_attach(te, attrs)
            if (ppp is not None): 
                if (t.begin_char < ppp.begin_char): 
                    ppp.begin_token = t
                    if (ppp.prop_ref is not None and ppp.prop_ref.name is not None): 
                        ppp.prop_ref.name = "{0}-{1}".format(t.term.lower(), ppp.prop_ref.name)
                return ppp
            if ((te is not None and te.previous.is_hiphen and not te.is_whitespace_after) and not te.is_whitespace_before): 
                if (BracketHelper.is_bracket(te, False)): 
                    br = BracketHelper.try_parse(te, BracketParseAttr.NO, 100)
                    if (br is not None and (isinstance(te, TextToken))): 
                        ppp = PersonAttrToken._new3193(t, br.end_token, br.end_token.previous.morph)
                        ppp.prop_ref = PersonPropertyReferent()
                        ppp.prop_ref.name = "{0}-{1}".format(t.term, MiscHelper.get_text_value(te.next0_, br.end_token, GetTextAttr.FIRSTNOUNGROUPTONOMINATIVE)).lower()
                        return ppp
        if ((isinstance(t, TextToken)) and t.chars.is_latin_letter): 
            if (t.is_value("STATE", None)): 
                tt1 = t.next0_
                if (MiscHelper.is_eng_adj_suffix(tt1)): 
                    tt1 = tt1.next0_.next0_
                res1 = PersonAttrToken.__try_attach(tt1, attrs)
                if (res1 is not None and res1.prop_ref is not None): 
                    res1.begin_token = t
                    res1.prop_ref.name = "{0} {1}".format(t.term.lower(), res1.prop_ref.name)
                    return res1
        return None
    
    M_EMPTY_ADJS = None
    
    M_STD_FORMS = None
    
    @staticmethod
    def __get_std_forms(tail : str, w1 : str, w2 : str) -> typing.List['MorphWordForm']:
        res = list()
        li1 = None
        li2 = None
        wrapli13215 = RefOutArgWrapper(None)
        inoutres3216 = Utils.tryGetValue(PersonAttrToken.M_STD_FORMS, w1, wrapli13215)
        li1 = wrapli13215.value
        if (not inoutres3216): 
            try: 
                li1 = MorphologyService.get_all_wordforms(w1, None)
                PersonAttrToken.M_STD_FORMS[w1] = li1
            except Exception as ex3211: 
                pass
        for v in li1: 
            if (LanguageHelper.ends_with(v.normal_case, tail)): 
                res.append(v)
        if (w2 is not None): 
            wrapli23213 = RefOutArgWrapper(None)
            inoutres3214 = Utils.tryGetValue(PersonAttrToken.M_STD_FORMS, w2, wrapli23213)
            li2 = wrapli23213.value
            if (not inoutres3214): 
                try: 
                    li2 = MorphologyService.get_all_wordforms(w2, None)
                    PersonAttrToken.M_STD_FORMS[w2] = li2
                except Exception as ex3212: 
                    pass
        if (li2 is not None): 
            for v in li2: 
                if (LanguageHelper.ends_with(v.normal_case, tail)): 
                    res.append(v)
        return (res if len(res) > 0 else None)
    
    @staticmethod
    def __create_attr_position(tok : 'TerminToken', attrs : 'PersonAttrAttachAttrs') -> 'PersonAttrToken':
        from pullenti.ner.person.internal.PersonIdentityToken import PersonIdentityToken
        ty2 = tok.termin.typ2
        if (ty2 == PersonAttrTerminType2.ABBR): 
            pr0 = PersonPropertyReferent()
            pr0.name = tok.termin.canonic_text
            return PersonAttrToken._new3217(tok.begin_token, tok.end_token, pr0, PersonAttrTerminType.POSITION)
        if (ty2 == PersonAttrTerminType2.IO or ty2 == PersonAttrTerminType2.IO2): 
            k = 0
            first_pass4235 = True
            while True:
                if first_pass4235: first_pass4235 = False
                else: k += 1
                if (k > 0): 
                    if (ty2 == PersonAttrTerminType2.IO): 
                        return None
                    if (((tok.morph.number) & (MorphNumber.PLURAL)) != (MorphNumber.UNDEFINED)): 
                        return None
                    break
                tt = tok.end_token.next0_
                if (tt is not None and tt.morph.class0_.is_preposition): 
                    tt = tt.next0_
                res_pat = PersonAttrToken._new3194(tok.begin_token, tok.end_token, PersonAttrTerminType.POSITION)
                res_pat.prop_ref = PersonPropertyReferent()
                if (tt is not None and (isinstance(tt.get_referent(), PersonPropertyReferent))): 
                    res_pat.end_token = tt
                    res_pat.prop_ref.higher = Utils.asObjectOrNull(tt.get_referent(), PersonPropertyReferent)
                else: 
                    aa = attrs
                    if (ty2 == PersonAttrTerminType2.IO2): 
                        aa = (Utils.valToEnum((aa) | (PersonAttrToken.PersonAttrAttachAttrs.AFTERZAMESTITEL), PersonAttrToken.PersonAttrAttachAttrs))
                    pat = PersonAttrToken.try_attach(tt, aa)
                    if (pat is None): 
                        if (not (isinstance(tt, TextToken))): 
                            continue
                        npt = NounPhraseHelper.try_parse(tt, NounPhraseParseAttr.NO, 0, None)
                        if (npt is None or npt.end_token == tok.end_token.next0_): 
                            continue
                        pat = PersonAttrToken.try_attach(npt.end_token, PersonAttrToken.PersonAttrAttachAttrs.NO)
                        if (pat is None or pat.begin_token != tt): 
                            continue
                    if (pat.typ != PersonAttrTerminType.POSITION): 
                        continue
                    res_pat.end_token = pat.end_token
                    res_pat.prop_ref.higher = pat.prop_ref
                    res_pat.higher_prop_ref = pat
                nam = tok.termin.canonic_text
                ts = res_pat.end_token.next0_
                te = None
                first_pass4236 = True
                while True:
                    if first_pass4236: first_pass4236 = False
                    else: ts = ts.next0_
                    if (not (ts is not None)): break
                    if (ts.morph.class0_.is_preposition): 
                        if (ts.is_value("В", None) or ts.is_value("ПО", None)): 
                            if (isinstance(ts.next0_, ReferentToken)): 
                                r = ts.next0_.get_referent()
                                if (r.type_name == PersonAttrToken.OBJ_NAME_GEO or r.type_name == PersonAttrToken.OBJ_NAME_ORG): 
                                    res_pat.prop_ref.add_slot(PersonPropertyReferent.ATTR_REF, r, False, 0)
                                    res_pat.end_token = ts.next0_
                                else: 
                                    te = ts.next0_
                                ts = ts.next0_
                                continue
                            rt11 = ts.kit.process_referent("NAMEDENTITY", ts.next0_, None)
                            if (rt11 is not None): 
                                res_pat.prop_ref.add_slot(PersonPropertyReferent.ATTR_REF, rt11, False, 0)
                                res_pat.end_token = rt11.end_token
                                ts = rt11.end_token
                                continue
                        if (ts.is_value("ПО", None) and ts.next0_ is not None): 
                            nnn = NounPhraseHelper.try_parse(ts.next0_, NounPhraseParseAttr.NO, 0, None)
                            if (nnn is not None): 
                                te = nnn.end_token
                                ts = te
                                if (ts.next0_ is not None and ts.next0_.is_comma_and): 
                                    tt2 = ts.next0_.next0_
                                    while tt2 is not None: 
                                        nnn2 = NounPhraseHelper.try_parse(tt2, NounPhraseParseAttr.NO, 0, None)
                                        if (nnn2 is None): 
                                            break
                                        if (((nnn2.morph.case_) & nnn.morph.case_).is_undefined): 
                                            break
                                        if (tt2.previous.is_and): 
                                            te = nnn2.end_token
                                            ts = te
                                            break
                                        tt2 = nnn2.end_token
                                        if (tt2.next0_ is not None and tt2.next0_.is_comma_and): 
                                            tt2 = tt2.next0_
                                        else: 
                                            break
                                        tt2 = tt2.next0_
                            elif ((isinstance(ts.next0_, TextToken)) and ((not ts.next0_.chars.is_all_lower and not ts.next0_.chars.is_capital_upper))): 
                                te = ts.next0_
                                ts = te
                            else: 
                                break
                            if (ts.next0_ is not None and ts.next0_.is_and and nnn is not None): 
                                nnn2 = NounPhraseHelper.try_parse(ts.next0_.next0_, NounPhraseParseAttr.NO, 0, None)
                                if (nnn2 is not None and not ((nnn2.morph.case_) & nnn.morph.case_).is_undefined): 
                                    te = nnn2.end_token
                                    ts = te
                            continue
                        break
                    if (ts != res_pat.end_token.next0_ and ts.chars.is_all_lower): 
                        nnn = NounPhraseHelper.try_parse(ts, NounPhraseParseAttr.NO, 0, None)
                        if (nnn is None): 
                            break
                        te = nnn.end_token
                        ts = te
                        continue
                    break
                if (te is not None): 
                    s = MiscHelper.get_text_value(res_pat.end_token.next0_, te, GetTextAttr.NO)
                    if (not Utils.isNullOrEmpty(s)): 
                        nam = "{0} {1}".format(nam, s)
                        res_pat.end_token = te
                    if ((res_pat.higher_prop_ref is not None and (te.whitespaces_after_count < 4) and te.next0_.get_referent() is not None) and te.next0_.get_referent().type_name == PersonAttrToken.OBJ_NAME_ORG): 
                        res_pat.end_token = res_pat.higher_prop_ref.end_token = te.next0_
                        res_pat.higher_prop_ref.prop_ref.add_slot(PersonPropertyReferent.ATTR_REF, te.next0_.get_referent(), False, 0)
                wrapnam3219 = RefOutArgWrapper(nam)
                res_pat.begin_token = PersonAttrToken.__analize_vise(res_pat.begin_token, wrapnam3219)
                nam = wrapnam3219.value
                res_pat.prop_ref.name = nam.lower()
                res_pat.morph = tok.morph
                return res_pat
        if (ty2 == PersonAttrTerminType2.ADJ): 
            pat = PersonAttrToken.__try_attach(tok.end_token.next0_, attrs)
            if (pat is None or pat.typ != PersonAttrTerminType.POSITION): 
                return None
            if (tok.begin_char == tok.end_char and not tok.begin_token.morph.class0_.is_undefined): 
                return None
            pat.begin_token = tok.begin_token
            pat.prop_ref.name = "{0} {1}".format(tok.termin.canonic_text.lower(), pat.prop_ref.name)
            pat.morph = tok.morph
            return pat
        if (ty2 == PersonAttrTerminType2.IGNOREDADJ): 
            pat = PersonAttrToken.__try_attach(tok.end_token.next0_, attrs)
            if (pat is None or pat.typ != PersonAttrTerminType.POSITION): 
                return None
            pat.begin_token = tok.begin_token
            pat.morph = tok.morph
            return pat
        if (ty2 == PersonAttrTerminType2.GRADE): 
            gr = PersonAttrToken.__create_attr_grade(tok)
            if (gr is not None): 
                return gr
            if (tok.begin_token.is_value("КАНДИДАТ", None)): 
                tt = tok.end_token.next0_
                if (tt is not None and tt.is_value("В", None)): 
                    tt = tt.next0_
                elif ((tt is not None and tt.is_value("НА", None) and tt.next0_ is not None) and ((tt.next0_.is_value("ПОСТ", None) or tt.next0_.is_value("ДОЛЖНОСТЬ", None)))): 
                    tt = tt.next0_.next0_
                else: 
                    tt = (None)
                if (tt is not None): 
                    pat2 = PersonAttrToken.__try_attach(tt, PersonAttrToken.PersonAttrAttachAttrs.NO)
                    if (pat2 is not None): 
                        res0 = PersonAttrToken._new3194(tok.begin_token, pat2.end_token, PersonAttrTerminType.POSITION)
                        res0.prop_ref = PersonPropertyReferent._new3195("кандидат")
                        res0.prop_ref.higher = pat2.prop_ref
                        res0.higher_prop_ref = pat2
                        res0.morph = tok.morph
                        return res0
            if (not tok.begin_token.is_value("ДОКТОР", None) and not tok.begin_token.is_value("КАНДИДАТ", None)): 
                return None
        name = tok.termin.canonic_text.lower()
        if (name == "русский"): 
            npt = NounPhraseHelper.try_parse(tok.begin_token, NounPhraseParseAttr.NO, 0, None)
            if (npt is not None and npt.end_token != npt.begin_token): 
                return None
        t0 = tok.begin_token
        t1 = tok.end_token
        wrapname3231 = RefOutArgWrapper(name)
        t0 = PersonAttrToken.__analize_vise(t0, wrapname3231)
        name = wrapname3231.value
        pr = PersonPropertyReferent()
        if ((t1.next0_ is not None and t1.next0_.is_hiphen and not t1.is_whitespace_after) and not t1.next0_.is_whitespace_after): 
            if (t1.next0_.next0_.chars.equals(t1.chars) or PersonAttrToken.M_TERMINS.try_parse(t1.next0_.next0_, TerminParseAttr.NO) is not None or ((t1.next0_.next0_.chars.is_all_lower and t1.next0_.next0_.chars.is_cyrillic_letter))): 
                npt = NounPhraseHelper.try_parse(t1, NounPhraseParseAttr.NO, 0, None)
                if (npt is not None and npt.end_token == t1.next0_.next0_): 
                    name = npt.get_normal_case_text(None, MorphNumber.UNDEFINED, MorphGender.UNDEFINED, False).lower()
                    t1 = npt.end_token
        tname0 = t1.next0_
        tname1 = None
        category = None
        npt0 = None
        is_depart = False
        t = t1.next0_
        first_pass4237 = True
        while True:
            if first_pass4237: first_pass4237 = False
            else: t = t.next0_
            if (not (t is not None)): break
            if ((((attrs) & (PersonAttrToken.PersonAttrAttachAttrs.ONLYKEYWORD))) != (PersonAttrToken.PersonAttrAttachAttrs.NO)): 
                break
            if ((((attrs) & (PersonAttrToken.PersonAttrAttachAttrs.AFTERZAMESTITEL))) != (PersonAttrToken.PersonAttrAttachAttrs.NO)): 
                if (t.is_value("ПО", None) or t.is_value("В", None)): 
                    break
            if (t == t1.next0_): 
                if (t.is_value("ИСТЕЦ", "ПОЗИВАЧ") or t.is_value("ОТВЕТЧИК", "ВІДПОВІДАЧ")): 
                    if (t1.is_value("ПРЕДСТАВИТЕЛЬ", "ПРЕДСТАВНИК")): 
                        return None
            if (MiscHelper.check_number_prefix(t) is not None): 
                break
            if (t.is_newline_before): 
                ok = False
                if (t.get_referent() is not None): 
                    if (t.get_referent().type_name == PersonAttrToken.OBJ_NAME_ORG or (isinstance(t.get_referent(), GeoReferent))): 
                        if (pr.find_slot(PersonPropertyReferent.ATTR_REF, None, True) is None): 
                            ok = True
                if (t.newlines_before_count > 1 and not t.chars.is_all_lower): 
                    if (not ok): 
                        break
                    if ((t.newlines_after_count < 3) and tok.begin_token.is_newline_before): 
                        pass
                    else: 
                        break
                if (tok.is_newline_before): 
                    if (PersonAttrToken.M_TERMINS.try_parse(t, TerminParseAttr.NO) is not None): 
                        break
                    else: 
                        ok = True
                if (t0.previous is not None and t0.previous.is_char('(')): 
                    br0 = BracketHelper.try_parse(t0.previous, BracketParseAttr.CANBEMANYLINES, 10)
                    if (br0 is not None and br0.end_char > t.end_char): 
                        ok = True
                if (t.is_and): 
                    ok = True
                if (not ok): 
                    npt00 = NounPhraseHelper.try_parse(t, NounPhraseParseAttr.PARSEPREPOSITION, 0, None)
                    if (npt00 is not None and npt00.end_token.next0_ is not None and not PersonAttrToken.__is_person(t)): 
                        tt1 = npt00.end_token
                        zap = False
                        and0_ = False
                        ttt = tt1.next0_
                        while ttt is not None: 
                            if (not ttt.is_comma_and): 
                                break
                            npt00 = NounPhraseHelper.try_parse(ttt.next0_, NounPhraseParseAttr.NO, 0, None)
                            if (npt00 is None): 
                                break
                            tt1 = npt00.end_token
                            if (ttt.is_char(',')): 
                                zap = True
                            else: 
                                and0_ = True
                                break
                            ttt = npt00.end_token
                            ttt = ttt.next0_
                        if (zap and not and0_): 
                            pass
                        elif (tt1.next0_ is None): 
                            pass
                        else: 
                            if (PersonAttrToken.__is_person(tt1.next0_)): 
                                ok = True
                            elif (isinstance(tt1.next0_.get_referent(), GeoReferent)): 
                                if (PersonAttrToken.__is_person(tt1.next0_.next0_)): 
                                    ok = True
                                else: 
                                    ccc = None
                                    wrapccc3222 = RefOutArgWrapper(None)
                                    ttt = PersonAttrToken.__try_attach_category(tt1.next0_.next0_, wrapccc3222)
                                    ccc = wrapccc3222.value
                                    if (ttt is not None): 
                                        ok = True
                            if (ok): 
                                tname1 = tt1
                                t1 = tname1
                                t = t1
                                continue
                    break
            if (t.is_char('(')): 
                br = BracketHelper.try_parse(t, BracketParseAttr.NO, 100)
                if (br is not None): 
                    t = br.end_token
                    ok = True
                    ttt = br.begin_token
                    while ttt != br.end_token: 
                        if (ttt.chars.is_letter): 
                            if (not ttt.chars.is_all_lower): 
                                ok = False
                                break
                        ttt = ttt.next0_
                    if (not ok): 
                        break
                    continue
                else: 
                    break
            tt2 = PersonAttrToken.__analyze_roman_nums(t)
            if (tt2 is not None): 
                t = tt2
                t1 = t
                if (t.is_value("СОЗЫВ", None) and t.next0_ is not None and t.next0_.is_value("ОТ", None)): 
                    t = t.next0_
                    continue
                break
            pat = None
            if ((((attrs) & (PersonAttrToken.PersonAttrAttachAttrs.ONLYKEYWORD))) == (PersonAttrToken.PersonAttrAttachAttrs.NO)): 
                pat = PersonAttrToken.__try_attach(t, PersonAttrToken.PersonAttrAttachAttrs.ONLYKEYWORD)
            if (pat is not None): 
                if (pat.morph.number == MorphNumber.PLURAL and not pat.morph.case_.is_nominative): 
                    pass
                elif (((isinstance(tok.termin, PersonAttrTermin)) and tok.termin.is_doubt and pat.prop_ref is not None) and len(pat.prop_ref.slots) == 1 and tok.chars.is_latin_letter == pat.chars.is_latin_letter): 
                    t = pat.end_token
                    tname1 = t
                    t1 = tname1
                    continue
                elif ((not tok.morph.case_.is_genitive and (isinstance(tok.termin, PersonAttrTermin)) and tok.termin.can_has_person_after == 1) and pat.morph.case_.is_genitive): 
                    rr = None
                    if (not "IgnorePersons" in t.kit.misc_data): 
                        t.kit.misc_data["IgnorePersons"] = None
                        rr = PersonAnalyzer.process_referent_stat(t, None)
                        if ("IgnorePersons" in t.kit.misc_data): 
                            del t.kit.misc_data["IgnorePersons"]
                    if (rr is not None and rr.morph.case_.is_genitive): 
                        pr.add_ext_referent(rr)
                        pr.add_slot(PersonPropertyReferent.ATTR_REF, rr.referent, False, 0)
                        t = rr.end_token
                        t1 = t
                    else: 
                        t = pat.end_token
                        tname1 = t
                        t1 = tname1
                    continue
                elif (t.is_value("ГР", None) and (isinstance(pat.end_token.next0_, TextToken)) and not pat.end_token.next0_.chars.is_all_lower): 
                    ppp = PersonAnalyzer.process_referent_stat(pat.end_token.next0_.next0_, None)
                    if (ppp is not None): 
                        t = pat.end_token
                        tname1 = t
                        t1 = tname1
                        continue
                    break
                elif (((not tok.morph.case_.is_genitive and (isinstance(tok.termin, PersonAttrTermin)) and tok.termin.is_kin) and pat.morph.case_.is_genitive and pat.prop_ref is not None) and pat.prop_ref.kind == PersonPropertyKind.KIN): 
                    t = pat.end_token
                    tname1 = t
                    t1 = tname1
                    continue
                else: 
                    break
            te = t
            if (te.next0_ is not None and te.is_char_of(",в") and (((attrs) & (PersonAttrToken.PersonAttrAttachAttrs.AFTERZAMESTITEL))) == (PersonAttrToken.PersonAttrAttachAttrs.NO)): 
                te = te.next0_
                if (te.is_value("ОРГАНИЗАЦИЯ", None) and (isinstance(te.next0_, ReferentToken)) and te.next0_.get_referent().type_name == PersonAttrToken.OBJ_NAME_ORG): 
                    te = te.next0_
            elif (te.next0_ is not None and te.morph.class0_.is_preposition): 
                if ((((attrs) & (PersonAttrToken.PersonAttrAttachAttrs.AFTERZAMESTITEL))) == (PersonAttrToken.PersonAttrAttachAttrs.AFTERZAMESTITEL)): 
                    break
                if (((te.is_value("ИЗ", None) or te.is_value("ПРИ", None) or te.is_value("ПО", None)) or te.is_value("НА", None) or te.is_value("ОТ", None)) or te.is_value("OF", None)): 
                    te = te.next0_
            elif ((te.is_hiphen and te.next0_ is not None and not te.is_whitespace_before) and not te.is_whitespace_after and te.previous.chars.equals(te.next0_.chars)): 
                continue
            elif (te.is_value("REPRESENT", None) and (isinstance(te.next0_, ReferentToken))): 
                te = te.next0_
            r = te.get_referent()
            r1 = None
            if ((te.chars.is_latin_letter and te.length_char > 1 and not t0.chars.is_latin_letter) and not te.chars.is_all_lower): 
                if (r is None or r.type_name != PersonAttrToken.OBJ_NAME_ORG): 
                    wrapcategory3223 = RefOutArgWrapper(None)
                    tt = PersonAttrToken.__try_attach_category(t, wrapcategory3223)
                    category = wrapcategory3223.value
                    if (tt is not None and name is not None): 
                        t1 = tt
                        t = t1
                        continue
                    while te is not None: 
                        if (te.chars.is_letter): 
                            if (not te.chars.is_latin_letter): 
                                break
                            t = te
                            tname1 = t
                            t1 = tname1
                        te = te.next0_
                    continue
            if (r is not None): 
                if ((r.type_name == PersonAttrToken.OBJ_NAME_GEO and te.previous is not None and te.previous.is_value("ДЕЛО", "СПРАВІ")) and te.previous.previous is not None and te.previous.previous.is_value("ПО", None)): 
                    t = te
                    tname1 = t
                    t1 = tname1
                    continue
                if (r.type_name == PersonAttrToken.OBJ_NAME_GEO and tok.termin.typ == PersonAttrTerminType.KING and te.end_token.morph.class0_.is_adjective): 
                    break
                if ((r.type_name == PersonAttrToken.OBJ_NAME_GEO or r.type_name == PersonAttrToken.OBJ_NAME_ADDR or r.type_name == "DATERANGE") or r.type_name == PersonAttrToken.OBJ_NAME_ORG or r.type_name == PersonAttrToken.OBJ_NAME_TRANSPORT): 
                    if (t0.previous is not None and t0.previous.is_value("ОТ", None) and t.is_newline_before): 
                        break
                    t1 = te
                    pr.add_slot(PersonPropertyReferent.ATTR_REF, r, False, 0)
                    posol = ((r.type_name == PersonAttrToken.OBJ_NAME_GEO or r.type_name == PersonAttrToken.OBJ_NAME_ORG)) and LanguageHelper.ends_with_ex(name, "посол", "представитель", "консул", "представник")
                    if (posol): 
                        t = t1
                        continue
                    if ((((r.type_name == PersonAttrToken.OBJ_NAME_GEO and t1.next0_ is not None and t1.next0_.morph.class0_.is_preposition) and t1.next0_.next0_ is not None and not t1.next0_.is_value("О", None)) and not t1.next0_.is_value("ОБ", None) and (((attrs) & (PersonAttrToken.PersonAttrAttachAttrs.AFTERZAMESTITEL))) == (PersonAttrToken.PersonAttrAttachAttrs.NO)) and not tok.termin.is_boss): 
                        r1 = t1.next0_.next0_.get_referent()
                        if ((r1) is not None): 
                            if (r1.type_name == PersonAttrToken.OBJ_NAME_ORG): 
                                pr.add_slot(PersonPropertyReferent.ATTR_REF, r1, False, 0)
                                t1 = t1.next0_.next0_
                                t = t1
                    if (r.type_name == PersonAttrToken.OBJ_NAME_ORG): 
                        t = te.next0_
                        first_pass4238 = True
                        while True:
                            if first_pass4238: first_pass4238 = False
                            else: t = t.next0_
                            if (not (t is not None)): break
                            if (((isinstance(t, TextToken)) and t.length_char >= 2 and t.chars.is_all_upper) and (t.whitespaces_before_count < 2)): 
                                t1 = t
                                continue
                            if (not t.is_comma_and or not (isinstance(t.next0_, ReferentToken))): 
                                break
                            r = t.next0_.get_referent()
                            if (r is None): 
                                break
                            if (r.type_name != PersonAttrToken.OBJ_NAME_ORG): 
                                break
                            pr.add_slot(PersonPropertyReferent.ATTR_REF, r, False, 0)
                            t = t.next0_
                            t1 = t
                            if (t.previous.is_and): 
                                t = t.next0_
                                break
                        first_pass4239 = True
                        while True:
                            if first_pass4239: first_pass4239 = False
                            else: t = t.next0_
                            if (not (t is not None)): break
                            if (t.is_newline_before): 
                                break
                            tt2 = PersonAttrToken.__analyze_roman_nums(t)
                            if (tt2 is not None): 
                                t = tt2
                                t1 = t
                                if (t.is_value("СОЗЫВ", None) and t.next0_ is not None and t.next0_.is_value("ОТ", None)): 
                                    t = t.next0_
                                else: 
                                    break
                            if (t.is_value("В", None) or t.is_value("ОТ", None) or t.is_and): 
                                continue
                            if (t.morph.language.is_ua): 
                                if (t.is_value("ВІД", None)): 
                                    continue
                            if (((isinstance(t, TextToken)) and t.chars.is_letter and not t.chars.is_all_lower) and t.previous.is_value("ОТ", "ВІД")): 
                                tname0 = t.previous
                                t1 = t
                                tname1 = t1
                                continue
                            if ((isinstance(t, TextToken)) and BracketHelper.can_be_start_of_sequence(t, False, False) and t.previous.is_value("ОТ", "ВІД")): 
                                br = BracketHelper.try_parse(t, BracketParseAttr.NO, 100)
                                if (br is not None and (br.length_char < 100)): 
                                    tname0 = t.previous
                                    t = br.end_token
                                    t1 = t
                                    tname1 = t1
                                    continue
                            if (((isinstance(t, TextToken)) and t.length_char > 2 and t.previous.is_value("В", None)) and tname1 is None and t.next0_ is not None): 
                                rt = PersonAnalyzer.process_referent_stat(t.next0_, None)
                                if (rt is not None or (isinstance(t.next0_.get_referent(), PersonReferent))): 
                                    tname0 = t.previous
                                    t1 = t
                                    tname1 = t1
                                    continue
                            r = t.get_referent()
                            if (r is None): 
                                break
                            if (r.type_name != PersonAttrToken.OBJ_NAME_GEO): 
                                if (r.type_name == PersonAttrToken.OBJ_NAME_ORG and t.previous is not None and ((t.previous.is_value("ОТ", None) or t.previous.is_value("ВІД", None)))): 
                                    pass
                                else: 
                                    break
                            pr.add_slot(PersonPropertyReferent.ATTR_REF, r, False, 0)
                            t1 = t
                if ((t1.next0_ is not None and (t1.whitespaces_after_count < 2) and t1.next0_.chars.is_latin_letter) and not t1.next0_.chars.is_all_lower and MiscHelper.check_number_prefix(t1.next0_) is None): 
                    t = t1.next0_
                    while t is not None: 
                        if (not (isinstance(t, TextToken))): 
                            break
                        if (not t.chars.is_letter): 
                            break
                        if (not t.chars.is_latin_letter): 
                            break
                        if (t.kit.base_language.is_en): 
                            break
                        ttt = PersonAttrToken.__analyze_roman_nums(t)
                        if (ttt is not None): 
                            t = ttt
                        tname1 = t
                        t1 = tname1
                        t = t.next0_
                t = t1
                if (((tname0 == t and tname1 is None and t.next0_ is not None) and (((attrs) & (PersonAttrToken.PersonAttrAttachAttrs.AFTERZAMESTITEL))) == (PersonAttrToken.PersonAttrAttachAttrs.NO) and name != "президент") and t.next0_.is_value("ПО", None)): 
                    tname0 = t.next0_
                    continue
                break
            if (category is None): 
                wrapcategory3224 = RefOutArgWrapper(None)
                tt = PersonAttrToken.__try_attach_category(t, wrapcategory3224)
                category = wrapcategory3224.value
                if (tt is not None and name is not None): 
                    t1 = tt
                    t = t1
                    continue
            if (name == "премьер"): 
                break
            if (isinstance(t, TextToken)): 
                if (t.is_value("ИМЕНИ", "ІМЕНІ")): 
                    break
            if (not t.chars.is_all_lower): 
                pit = PersonItemToken.try_attach(t, Utils.valToEnum((PersonItemToken.ParseAttr.CANBELATIN) | (PersonItemToken.ParseAttr.IGNOREATTRS), PersonItemToken.ParseAttr), None)
                if (pit is not None): 
                    if (pit.referent is not None): 
                        break
                    if (pit.lastname is not None and ((pit.lastname.is_in_dictionary or pit.lastname.is_in_ontology))): 
                        break
                    if (pit.firstname is not None and pit.firstname.is_in_dictionary): 
                        break
                    if (tok.termin.typ == PersonAttrTerminType.KING): 
                        if (pit.lastname is not None or pit.value is None): 
                            break
                        if (pit.value.endswith("КИЙ")): 
                            break
                    pits = PersonItemToken.try_attach_list(t, Utils.valToEnum((PersonItemToken.ParseAttr.NO) | (PersonItemToken.ParseAttr.IGNOREATTRS), PersonItemToken.ParseAttr), 6)
                    if (pits is not None and len(pits) > 0): 
                        if (len(pits) == 2): 
                            if (pits[1].lastname is not None and pits[1].lastname.is_in_dictionary): 
                                break
                            if (pits[1].typ == PersonItemToken.ItemType.INITIAL and pits[0].lastname is not None): 
                                break
                        if (len(pits) == 3): 
                            if (pits[2].lastname is not None): 
                                if (pits[1].middlename is not None): 
                                    break
                                if (pits[0].firstname is not None and pits[0].firstname.is_in_dictionary): 
                                    break
                            if (pits[1].typ == PersonItemToken.ItemType.INITIAL and pits[2].typ == PersonItemToken.ItemType.INITIAL and pits[0].lastname is not None): 
                                break
                        if (pits[0].typ == PersonItemToken.ItemType.INITIAL): 
                            break
                        if (tok.termin.typ == PersonAttrTerminType.KING): 
                            if (pits[0].morph.case_.is_undefined and not pits[0].morph.case_.is_genitive): 
                                break
                            if (len(pits) == 1): 
                                mc1 = pits[0].begin_token.get_morph_class_in_dictionary()
                                if (mc1.is_undefined): 
                                    break
            test_person = False
            if (not t.chars.is_all_lower): 
                if ("TestAttr" in t.kit.misc_data): 
                    pass
                else: 
                    pits = PersonItemToken.try_attach_list(t, PersonItemToken.ParseAttr.IGNOREATTRS, 10)
                    if (pits is not None and len(pits) > 1): 
                        nnn = NounPhraseHelper.try_parse(t, NounPhraseParseAttr.NO, 0, None)
                        iii = 1
                        if (nnn is not None and len(nnn.adjectives) > 0): 
                            iii += len(nnn.adjectives)
                        test_person = True
                        t.kit.misc_data["TestAttr"] = None
                        li = PersonIdentityToken.try_attach(pits, 0, MorphBaseInfo._new3225(MorphCase.ALL_CASES), None, False, False)
                        del t.kit.misc_data["TestAttr"]
                        if (len(li) > 0 and li[0].coef > 1): 
                            t.kit.misc_data["TestAttr"] = None
                            li1 = PersonIdentityToken.try_attach(pits, iii, MorphBaseInfo._new3225(MorphCase.ALL_CASES), None, False, False)
                            del t.kit.misc_data["TestAttr"]
                            if (len(li1) == 0): 
                                break
                            if (li1[0].coef <= li[0].coef): 
                                break
                        else: 
                            t.kit.misc_data["TestAttr"] = None
                            li1 = PersonIdentityToken.try_attach(pits, 1, MorphBaseInfo._new3225(MorphCase.ALL_CASES), None, False, False)
                            del t.kit.misc_data["TestAttr"]
                            if (len(li1) > 0 and li1[0].coef >= 1 and li1[0].begin_token == t): 
                                continue
            if (BracketHelper.can_be_start_of_sequence(t, True, False)): 
                br = BracketHelper.try_parse(t, BracketParseAttr.NO, 100)
                if ((br is not None and t.next0_.get_referent() is not None and t.next0_.get_referent().type_name == PersonAttrToken.OBJ_NAME_ORG) and t.next0_.next0_ == br.end_token): 
                    pr.add_slot(PersonPropertyReferent.ATTR_REF, t.next0_.get_referent(), False, 0)
                    t1 = br.end_token
                    break
                elif (br is not None and (br.length_char < 40)): 
                    tname1 = br.end_token
                    t1 = tname1
                    t = t1
                    continue
            if ((isinstance(t, NumberToken)) and t.previous.is_value("ГЛАВА", None)): 
                break
            npt = NounPhraseHelper.try_parse(t, NounPhraseParseAttr.NO, 0, None)
            if ((npt is None and (isinstance(t, NumberToken)) and (t.whitespaces_after_count < 3)) and (t.whitespaces_before_count < 3)): 
                npt00 = NounPhraseHelper.try_parse(t.next0_, NounPhraseParseAttr.NO, 0, None)
                if (npt00 is not None): 
                    if (npt00.end_token.is_value("ОРДЕН", None) or npt00.end_token.is_value("МЕДАЛЬ", None)): 
                        npt = npt00
            test = False
            if (npt is not None): 
                if (PersonAttrToken.__exists_in_doctionary(npt.end_token) and (((((npt.morph.case_.is_genitive or npt.morph.case_.is_instrumental or npt.end_token.is_value("НАПРАВЛЕНИЕ", None)) or npt.end_token.is_value("ОТДЕЛ", None) or npt.end_token.is_value("ОТДЕЛЕНИЕ", None)) or npt.end_token.is_value("ДЕПАРТАМЕНТ", None) or npt.end_token.is_value("СЛУЖБА", None)) or npt.end_token.is_value("ПОДРАЗДЕЛЕНИЕ", None) or npt.end_token.is_value("УПРАВЛЕНИЕ", None)))): 
                    test = True
                    is_depart = True
                elif (npt.begin_token == npt.end_token and t.length_char > 1 and ((t.chars.is_all_upper or t.chars.is_last_lower))): 
                    test = True
            elif (t.chars.is_all_upper or t.chars.is_last_lower): 
                test = True
            if (test): 
                rto = t.kit.process_referent("ORGANIZATION", t, None)
                if (rto is not None): 
                    str0_ = str(rto.referent).upper()
                    if (str0_.startswith("ГОСУДАРСТВЕННАЯ ГРАЖДАНСКАЯ СЛУЖБА")): 
                        rto = (None)
                if (rto is not None and rto.end_char >= t.end_char and rto.begin_char == t.begin_char): 
                    pr.add_slot(PersonPropertyReferent.ATTR_REF, rto.referent, False, 0)
                    pr.add_ext_referent(rto)
                    t1 = rto.end_token
                    t = t1
                    if ((((attrs) & (PersonAttrToken.PersonAttrAttachAttrs.AFTERZAMESTITEL))) != (PersonAttrToken.PersonAttrAttachAttrs.NO)): 
                        break
                    npt0 = npt
                    if (t.next0_ is not None and t.next0_.is_and): 
                        rto2 = t.kit.process_referent("ORGANIZATION", t.next0_.next0_, None)
                        if (rto2 is not None and rto2.begin_char == t.next0_.next0_.begin_char): 
                            pr.add_slot(PersonPropertyReferent.ATTR_REF, rto2.referent, False, 0)
                            pr.add_ext_referent(rto2)
                            t1 = rto2.end_token
                            t = t1
                    continue
                rto = t.kit.process_referent("NAMEDENTITY", t, None)
                if (rto is not None and rto.morph.case_.is_genitive): 
                    pr.add_slot(PersonPropertyReferent.ATTR_REF, rto.referent, False, 0)
                    pr.add_ext_referent(rto)
                    t1 = rto.end_token
                    t = t1
                    continue
                if (npt is not None): 
                    tname1 = npt.end_token
                    t1 = tname1
                    t = t1
                    npt0 = npt
                    continue
                if (((is_depart and t.chars.is_all_upper and t.length_char > 1) and (t.length_char < 6) and not t.previous.chars.is_all_upper) and t.get_morph_class_in_dictionary().is_undefined): 
                    tname1 = t
                    t1 = tname1
                    tt = t.next0_
                    while tt is not None: 
                        if (not tt.is_comma_and or tt.next0_ is None): 
                            break
                        tt = tt.next0_
                        if (tt.chars.is_all_upper and tt.length_char > 1 and (tt.length_char < 6)): 
                            pass
                        else: 
                            break
                        t = tt
                        tname1 = t
                        t1 = tname1
                        if (tt.previous.is_and): 
                            break
                        tt = tt.next0_
                    continue
            if (t.morph.class0_.is_preposition): 
                npt = NounPhraseHelper.try_parse(t.next0_, NounPhraseParseAttr.NO, 0, None)
                if (npt is None and t.next0_ is not None and t.next0_.morph.class0_.is_adverb): 
                    npt = NounPhraseHelper.try_parse(t.next0_.next0_, NounPhraseParseAttr.NO, 0, None)
                if (npt is not None and PersonAttrToken.__exists_in_doctionary(npt.end_token)): 
                    if (BracketHelper.can_be_start_of_sequence(npt.end_token.next0_, True, False)): 
                        if (((t.is_value("ПО", "ЗА") and npt.end_token.is_value("СПЕЦИАЛЬНОСТЬ", "ФАХОМ"))) or ((t.is_value("С", "ЗІ") and npt.end_token.is_value("СПЕЦИАЛИЗАЦИЯ", "СПЕЦІАЛІЗАЦІЯ")))): 
                            br = BracketHelper.try_parse(npt.end_token.next0_, BracketParseAttr.NO, 100)
                            if (br is not None): 
                                t1 = br.end_token
                                t = t1
                                continue
                    ok = False
                    if ((t.is_value("ПО", None) and npt.morph.case_.is_dative and not npt.noun.is_value("ИМЯ", "ІМЯ")) and not npt.noun.is_value("ПРОЗВИЩЕ", "ПРІЗВИСЬКО") and not npt.noun.is_value("ПРОЗВАНИЕ", "ПРОЗВАННЯ")): 
                        ok = True
                        if (npt.noun.is_value("РАБОТА", "РОБОТА") or npt.noun.is_value("ПОДДЕРЖКА", "ПІДТРИМКА") or npt.noun.is_value("СОПРОВОЖДЕНИЕ", "СУПРОВІД")): 
                            npt2 = NounPhraseHelper.try_parse(npt.end_token.next0_, NounPhraseParseAttr.PARSEPREPOSITION, 0, None)
                            if (npt2 is not None): 
                                npt = npt2
                    elif (npt.noun.is_value("ОТСТАВКА", None) or npt.noun.is_value("ВІДСТАВКА", None)): 
                        ok = True
                    elif (name == "кандидат" and t.is_value("В", None)): 
                        ok = True
                    if (ok): 
                        tname1 = npt.end_token
                        t1 = tname1
                        t = t1
                        npt0 = npt
                        continue
                if (t.is_value("OF", None)): 
                    continue
            elif (t.is_and and npt0 is not None): 
                npt = NounPhraseHelper.try_parse(t.next0_, NounPhraseParseAttr.NO, 0, None)
                if (npt is not None and not ((npt.morph.class0_) & npt0.morph.class0_).is_undefined): 
                    if (npt0.chars.equals(npt.chars)): 
                        tname1 = npt.end_token
                        t1 = tname1
                        t = t1
                        npt0 = (None)
                        continue
                if (((npt is None and (isinstance(t.next0_, TextToken)) and t.next0_.chars.is_all_upper) and t.next0_.length_char >= 2 and t.previous is not None) and t.previous.chars.equals(t.next0_.chars)): 
                    tname1 = t.next0_
                    t1 = tname1
                    t = t1
                    npt0 = (None)
                    continue
            elif (t.is_comma_and and ((not t.is_newline_after or tok.is_newline_before)) and npt0 is not None): 
                npt = NounPhraseHelper.try_parse(t.next0_, NounPhraseParseAttr.NO, 0, None)
                if (npt is not None and not ((npt.morph.class0_) & npt0.morph.class0_).is_undefined): 
                    if (npt0.chars.equals(npt.chars) and npt.end_token.next0_ is not None and npt.end_token.next0_.is_and): 
                        npt1 = NounPhraseHelper.try_parse(npt.end_token.next0_.next0_, NounPhraseParseAttr.NO, 0, None)
                        if (npt1 is not None and not ((npt1.morph.class0_) & npt.morph.class0_ & npt0.morph.class0_).is_undefined): 
                            if (npt0.chars.equals(npt1.chars)): 
                                tname1 = npt1.end_token
                                t1 = tname1
                                t = t1
                                npt0 = (None)
                                continue
            elif (t.morph.class0_.is_adjective and BracketHelper.can_be_start_of_sequence(t.next0_, True, False)): 
                br = BracketHelper.try_parse(t.next0_, BracketParseAttr.NO, 100)
                if (br is not None and (br.length_char < 100)): 
                    tname1 = br.end_token
                    t1 = tname1
                    t = t1
                    npt0 = (None)
                    continue
            if (t.chars.is_latin_letter and t.previous.chars.is_cyrillic_letter): 
                while t is not None: 
                    if (not t.chars.is_latin_letter or t.is_newline_before): 
                        break
                    else: 
                        tname1 = t
                        t1 = tname1
                    t = t.next0_
                break
            if (((t.chars.is_all_upper or ((not t.chars.is_all_lower and not t.chars.is_capital_upper)))) and t.length_char > 1 and not t0.chars.is_all_upper): 
                tname1 = t
                t1 = tname1
                continue
            if ((not t.chars.is_all_lower and not t.chars.is_all_upper and not t.chars.is_capital_upper) and t.length_char > 2 and not t0.chars.is_all_upper): 
                tname1 = t
                t1 = tname1
                continue
            if (((t.chars.is_letter and (isinstance(t.next0_, ReferentToken)) and (isinstance(t.next0_.get_referent(), PersonReferent))) and not t.morph.class0_.is_preposition and not t.morph.class0_.is_conjunction) and not t.morph.class0_.is_verb): 
                tname1 = t
                t1 = tname1
                break
            if (isinstance(t, NumberToken)): 
                if (t.begin_token.is_value("МИЛЛИОНОВ", None) or t.begin_token.is_value("МІЛЬЙОНІВ", None)): 
                    tname1 = t
                    t1 = tname1
                    break
            if (test_person): 
                if (t.next0_ is None): 
                    break
                te = t.next0_
                if (((te.is_char_of(",в") or te.is_value("ИЗ", None))) and te.next0_ is not None): 
                    te = te.next0_
                r = te.get_referent()
                if ((r) is not None): 
                    if (r.type_name == PersonAttrToken.OBJ_NAME_GEO or r.type_name == PersonAttrToken.OBJ_NAME_ORG or r.type_name == PersonAttrToken.OBJ_NAME_TRANSPORT): 
                        tname1 = t
                        t1 = tname1
                        continue
                break
            if (t.morph.language.is_en): 
                break
            if (t.morph.class0_.is_noun and t.get_morph_class_in_dictionary().is_undefined and (t.whitespaces_before_count < 2)): 
                tname1 = t
                t1 = tname1
                continue
            if (t.morph.class0_.is_pronoun): 
                continue
            if ((t.is_hiphen and tname1 == t.previous and not t.is_whitespace_before) and not t.is_whitespace_after and (isinstance(t.next0_, TextToken))): 
                t = t.next0_
                tname1 = t
                t1 = tname1
                continue
            break
        if (tname1 is not None): 
            if (pr.find_slot(PersonPropertyReferent.ATTR_REF, None, True) is None and ((((((tname1.is_value("КОМПАНИЯ", "КОМПАНІЯ") or tname1.is_value("ФИРМА", "ФІРМА") or tname1.is_value("ГРУППИРОВКА", "УГРУПОВАННЯ")) or tname1.is_value("ПРЕДПРИЯТИЕ", "ПІДПРИЄМСТВО") or tname1.is_value("ПРЕЗИДИУМ", "ПРЕЗИДІЯ")) or tname1.is_value("ЧАСТЬ", "ЧАСТИНА") or tname1.is_value("ФЕДЕРАЦИЯ", "ФЕДЕРАЦІЯ")) or tname1.is_value("ВЕДОМСТВО", "ВІДОМСТВО") or tname1.is_value("БАНК", None)) or tname1.is_value("КОРПОРАЦИЯ", "КОРПОРАЦІЯ")))): 
                if (tname1 == tname0 or ((tname0.is_value("ЭТОТ", "ЦЕЙ") and tname0.next0_ == tname1))): 
                    org0_ = None
                    cou = 0
                    tt0 = t0.previous
                    first_pass4240 = True
                    while True:
                        if first_pass4240: first_pass4240 = False
                        else: tt0 = tt0.previous
                        if (not (tt0 is not None)): break
                        if (tt0.is_newline_after): 
                            cou += 10
                        cou += 1
                        if (cou > 500): 
                            break
                        rs0 = tt0.get_referents()
                        if (rs0 is None): 
                            continue
                        has_org = False
                        for r0 in rs0: 
                            if (r0.type_name == PersonAttrToken.OBJ_NAME_ORG): 
                                has_org = True
                                if (tname1.is_value("БАНК", None)): 
                                    if (r0.find_slot("TYPE", "банк", True) is None): 
                                        continue
                                if (tname1.is_value("ЧАСТЬ", "ЧАСТИНА")): 
                                    ok1 = False
                                    for s in r0.slots: 
                                        if (s.type_name == "TYPE"): 
                                            if (s.value.endswith("часть") or s.value.endswith("частина")): 
                                                ok1 = True
                                    if (not ok1): 
                                        continue
                                org0_ = r0
                                break
                        if (org0_ is not None or has_org): 
                            break
                    if (org0_ is not None): 
                        pr.add_slot(PersonPropertyReferent.ATTR_REF, org0_, False, 0)
                        tname1 = (None)
        if (tname1 is not None): 
            s = MiscHelper.get_text_value(tname0, tname1, GetTextAttr.NO)
            if (s is not None): 
                name = "{0} {1}".format(name, s.lower())
        if (category is not None): 
            name = "{0} {1}".format(name, category)
        else: 
            wrapcategory3228 = RefOutArgWrapper(None)
            tt = PersonAttrToken.__try_attach_category(t1.next0_, wrapcategory3228)
            category = wrapcategory3228.value
            if (tt is not None): 
                name = "{0} {1}".format(name, category)
                t1 = tt
        pr.name = name
        res = PersonAttrToken._new3229(t0, t1, PersonAttrTerminType.POSITION, pr, tok.morph)
        res.can_be_independent_property = tok.termin.can_be_unique_identifier
        i = name.find("заместитель ")
        if (i < 0): 
            i = name.find("заступник ")
        if (i >= 0): 
            i += 11
            res1 = PersonAttrToken._new3198(t0, t1, PersonAttrTerminType.POSITION, tok.morph)
            res1.prop_ref = PersonPropertyReferent()
            res1.prop_ref.name = name[0:0+i]
            res1.prop_ref.higher = res.prop_ref
            res1.higher_prop_ref = res
            res.prop_ref.name = name[i + 1:]
            return res1
        return res
    
    @staticmethod
    def __exists_in_doctionary(t : 'Token') -> bool:
        tt = Utils.asObjectOrNull(t, TextToken)
        if (tt is None): 
            return False
        for wf in tt.morph.items: 
            if (wf.is_in_dictionary): 
                return True
        return False
    
    @staticmethod
    def __is_person(t : 'Token') -> bool:
        if (t is None): 
            return False
        if (isinstance(t, ReferentToken)): 
            return isinstance(t.get_referent(), PersonReferent)
        if (not t.chars.is_letter or t.chars.is_all_lower): 
            return False
        rt00 = PersonAnalyzer.process_referent_stat(t, None)
        return rt00 is not None and (isinstance(rt00.referent, PersonReferent))
    
    @staticmethod
    def __analyze_roman_nums(t : 'Token') -> 'Token':
        tt2 = t
        if (tt2.is_value("В", None) and tt2.next0_ is not None): 
            tt2 = tt2.next0_
        lat = NumberHelper.try_parse_roman(tt2)
        if (lat is None): 
            return None
        tt2 = lat.end_token
        if (tt2.next0_ is not None and tt2.next0_.is_hiphen): 
            lat2 = NumberHelper.try_parse_roman(tt2.next0_.next0_)
            if (lat2 is not None): 
                tt2 = lat2.end_token
        elif (tt2.next0_ is not None and tt2.next0_.is_comma_and): 
            lat2 = NumberHelper.try_parse_roman(tt2.next0_.next0_)
            if (lat2 is not None): 
                tt2 = lat2.end_token
                tt = tt2.next0_
                while tt is not None: 
                    if (not tt.is_comma_and and not tt.is_hiphen): 
                        break
                    lat2 = NumberHelper.try_parse_roman(tt.next0_)
                    if (lat2 is None): 
                        break
                    tt2 = lat2.end_token
                    if (tt.is_and): 
                        break
                    tt = tt2
                    tt = tt.next0_
        if (tt2.next0_ is not None and ((tt2.next0_.is_value("ВЕК", None) or tt2.next0_.is_value("СТОЛЕТИЕ", None) or tt2.next0_.is_value("СОЗЫВ", None)))): 
            return tt2.next0_
        if (tt2.next0_ is not None and tt2.next0_.is_value("В", None)): 
            tt2 = tt2.next0_
            if (tt2.next0_ is not None and tt2.next0_.is_char('.')): 
                tt2 = tt2.next0_
            return tt2
        return None
    
    @staticmethod
    def __analize_vise(t0 : 'Token', name : str) -> 'Token':
        if (t0 is None): 
            return None
        if (t0.previous is not None and t0.previous.is_hiphen and (isinstance(t0.previous.previous, TextToken))): 
            if (t0.previous.previous.is_value("ВИЦЕ", "ВІЦЕ")): 
                t0 = t0.previous.previous
                name.value = (((("віце-" if t0.kit.base_language.is_ua else "вице-"))) + name.value)
            if (t0.previous is not None and t0.previous.previous is not None): 
                if (t0.previous.previous.is_value("ЭКС", "ЕКС")): 
                    t0 = t0.previous.previous
                    name.value = (((("екс-" if t0.kit.base_language.is_ua else "экс-"))) + name.value)
                elif (t0.previous.previous.chars.equals(t0.chars) and not t0.is_whitespace_before and not t0.previous.is_whitespace_before): 
                    npt00 = NounPhraseHelper.try_parse(t0.previous.previous, NounPhraseParseAttr.NO, 0, None)
                    if (npt00 is not None): 
                        name.value = npt00.get_normal_case_text(None, MorphNumber.UNDEFINED, MorphGender.UNDEFINED, False).lower()
                        t0 = t0.previous.previous
        return t0
    
    @staticmethod
    def __try_attach_category(t : 'Token', cat : str) -> 'Token':
        cat.value = (None)
        if (t is None or t.next0_ is None): 
            return None
        tt = None
        num = -1
        if (isinstance(t, NumberToken)): 
            if (t.int_value is None): 
                return None
            num = t.int_value
            tt = t
        else: 
            npt = NumberHelper.try_parse_roman(t)
            if (npt is not None and npt.int_value is not None): 
                num = npt.int_value
                tt = npt.end_token
        if ((num < 0) and ((t.is_value("ВЫСШИЙ", None) or t.is_value("ВЫСШ", None) or t.is_value("ВИЩИЙ", None)))): 
            num = 0
            tt = t
            if (tt.next0_ is not None and tt.next0_.is_char('.')): 
                tt = tt.next0_
        if (tt is None or tt.next0_ is None or (num < 0)): 
            return None
        tt = tt.next0_
        if (tt.is_value("КАТЕГОРИЯ", None) or tt.is_value("КАТЕГОРІЯ", None) or tt.is_value("КАТ", None)): 
            if (tt.next0_ is not None and tt.next0_.is_char('.')): 
                tt = tt.next0_
            if (num == 0): 
                cat.value = ("вищої категорії" if tt.kit.base_language.is_ua else "высшей категории")
            else: 
                cat.value = ("{0} категорії".format(num) if tt.kit.base_language.is_ua else "{0} категории".format(num))
            return tt
        if (tt.is_value("РАЗРЯД", None) or tt.is_value("РОЗРЯД", None)): 
            if (num == 0): 
                cat.value = ("вищого розряду" if tt.kit.base_language.is_ua else "высшего разряда")
            else: 
                cat.value = ("{0} розряду".format(num) if tt.kit.base_language.is_ua else "{0} разряда".format(num))
            return tt
        if (tt.is_value("КЛАСС", None) or tt.is_value("КЛАС", None)): 
            if (num == 0): 
                cat.value = ("вищого класу" if tt.kit.base_language.is_ua else "высшего класса")
            else: 
                cat.value = ("{0} класу".format(num) if tt.kit.base_language.is_ua else "{0} класса".format(num))
            return tt
        if (tt.is_value("РАНГ", None)): 
            if (num == 0): 
                return None
            else: 
                cat.value = "{0} ранга".format(num)
            return tt
        if (tt.is_value("СОЗЫВ", None) or tt.is_value("СКЛИКАННЯ", None)): 
            if (num == 0): 
                return None
            else: 
                cat.value = ("{0} скликання".format(num) if tt.kit.base_language.is_ua else "{0} созыва".format(num))
            return tt
        return None
    
    OBJ_NAME_GEO = "GEO"
    
    OBJ_NAME_ADDR = "ADDRESS"
    
    OBJ_NAME_ORG = "ORGANIZATION"
    
    OBJ_NAME_TRANSPORT = "TRANSPORT"
    
    OBJ_NAME_DATE = "DATE"
    
    OBJ_NAME_DATE_RANGE = "DATERANGE"
    
    @staticmethod
    def __create_attr_grade(tok : 'TerminToken') -> 'PersonAttrToken':
        t1 = PersonAttrToken.__find_grade_last(tok.end_token.next0_, tok.begin_token)
        if (t1 is None): 
            return None
        pr = PersonPropertyReferent()
        ss = Utils.asObjectOrNull(t1.tag, str)
        if (ss is None): 
            ss = "наук"
        pr.name = "{0} {1}".format(tok.termin.canonic_text.lower(), ss)
        return PersonAttrToken._new3232(tok.begin_token, t1, PersonAttrTerminType.POSITION, pr, tok.morph, False)
    
    @staticmethod
    def __find_grade_last(t : 'Token', t0 : 'Token') -> 'Token':
        i = 0
        te = PersonAttrToken.M_TERMINS_GRADE.try_parse(t, TerminParseAttr.NO)
        if (te is not None): 
            te.end_token.tag = (te.termin.canonic_text.lower())
            return te.end_token
        tt = t
        t1 = None
        while t is not None: 
            if (t.is_value("НАУК", None)): 
                if (tt.next0_ == t and tt.get_morph_class_in_dictionary().is_adjective): 
                    t.tag = (MiscHelper.get_text_value(tt, t, GetTextAttr.NO).lower())
                t1 = t
                i += 1
                break
            if (t.is_value("Н", None)): 
                if (t0.length_char > 1 or not t0.chars.equals(t.chars)): 
                    return None
                if ((t.next0_ is not None and t.next0_.is_hiphen and t.next0_.next0_ is not None) and t.next0_.next0_.is_value("К", None)): 
                    t1 = t.next0_.next0_
                    break
                if (t.next0_ is not None and t.next0_.is_char('.')): 
                    t1 = t.next0_
                    break
            if (not t.chars.is_all_lower and t0.chars.is_all_lower): 
                break
            i += 1
            if (i > 2): 
                break
            if (t.next0_ is not None and t.next0_.is_char('.')): 
                t = t.next0_
            if (t.next0_ is not None and t.next0_.is_hiphen): 
                t = t.next0_
            t = t.next0_
        if (t1 is None or i == 0): 
            return None
        return t1
    
    @staticmethod
    def check_kind(pr : 'PersonPropertyReferent') -> 'PersonPropertyKind':
        if (pr is None): 
            return PersonPropertyKind.UNDEFINED
        n = pr.get_string_value(PersonPropertyReferent.ATTR_NAME)
        if (n is None): 
            return PersonPropertyKind.UNDEFINED
        n = n.upper()
        for nn in Utils.splitString(n, ' ' + '-', False): 
            li = PersonAttrToken.M_TERMINS.find_termins_by_string(nn, MorphLang.RU)
            if (li is None or len(li) == 0): 
                li = PersonAttrToken.M_TERMINS.find_termins_by_string(n, MorphLang.UA)
            if (li is not None and len(li) > 0): 
                pat = Utils.asObjectOrNull(li[0], PersonAttrTermin)
                if (pat.is_boss): 
                    return PersonPropertyKind.BOSS
                if (pat.is_kin): 
                    return PersonPropertyKind.KIN
                if (pat.typ == PersonAttrTerminType.KING): 
                    if (n != "ДОН"): 
                        return PersonPropertyKind.KING
                if (pat.is_military_rank): 
                    if (nn == "ВИЦЕ"): 
                        continue
                    if (nn == "КАПИТАН" or nn == "CAPTAIN" or nn == "КАПІТАН"): 
                        org0_ = Utils.asObjectOrNull(pr.get_slot_value(PersonPropertyReferent.ATTR_REF), Referent)
                        if (org0_ is not None and org0_.type_name == "ORGANIZATION"): 
                            continue
                    return PersonPropertyKind.MILITARYRANK
                if (pat.is_nation): 
                    return PersonPropertyKind.NATIONALITY
        return PersonPropertyKind.UNDEFINED
    
    @staticmethod
    def try_attach_word(t : 'Token', ignore_io : bool=False) -> 'TerminToken':
        tok = PersonAttrToken.M_TERMINS.try_parse(t, TerminParseAttr.NO)
        if ((tok is not None and tok.begin_token == tok.end_token and t.length_char == 1) and t.is_value("Д", None)): 
            if (BracketHelper.is_bracket(t.next0_, True) and not t.is_whitespace_after): 
                return None
        if (tok is not None and tok.termin.canonic_text == "ГРАФ"): 
            tok.morph = MorphCollection(t.morph)
            tok.morph.remove_items(MorphGender.MASCULINE, False)
        if (tok is not None and ignore_io): 
            pat = Utils.asObjectOrNull(tok.termin, PersonAttrTermin)
            if (pat.typ2 != PersonAttrTerminType2.UNDEFINED and pat.typ2 != PersonAttrTerminType2.GRADE): 
                return None
        return tok
    
    @staticmethod
    def try_attach_position_word(t : 'Token') -> 'TerminToken':
        tok = PersonAttrToken.M_TERMINS.try_parse(t, TerminParseAttr.NO)
        if (tok is None): 
            return None
        pat = Utils.asObjectOrNull(tok.termin, PersonAttrTermin)
        if (pat is None): 
            return None
        if (pat.typ != PersonAttrTerminType.POSITION): 
            return None
        if (pat.typ2 != PersonAttrTerminType2.IO2 and pat.typ2 != PersonAttrTerminType2.UNDEFINED): 
            return None
        return tok
    
    @staticmethod
    def _new3193(_arg1 : 'Token', _arg2 : 'Token', _arg3 : 'MorphCollection') -> 'PersonAttrToken':
        res = PersonAttrToken(_arg1, _arg2)
        res.morph = _arg3
        return res
    
    @staticmethod
    def _new3194(_arg1 : 'Token', _arg2 : 'Token', _arg3 : 'PersonAttrTerminType') -> 'PersonAttrToken':
        res = PersonAttrToken(_arg1, _arg2)
        res.typ = _arg3
        return res
    
    @staticmethod
    def _new3196(_arg1 : 'Token', _arg2 : 'Token', _arg3 : 'PersonAttrTerminType', _arg4 : str, _arg5 : 'MorphCollection') -> 'PersonAttrToken':
        res = PersonAttrToken(_arg1, _arg2)
        res.typ = _arg3
        res.age = _arg4
        res.morph = _arg5
        return res
    
    @staticmethod
    def _new3198(_arg1 : 'Token', _arg2 : 'Token', _arg3 : 'PersonAttrTerminType', _arg4 : 'MorphCollection') -> 'PersonAttrToken':
        res = PersonAttrToken(_arg1, _arg2)
        res.typ = _arg3
        res.morph = _arg4
        return res
    
    @staticmethod
    def _new3200(_arg1 : 'Token', _arg2 : 'Token', _arg3 : 'PersonAttrTerminType', _arg4 : str) -> 'PersonAttrToken':
        res = PersonAttrToken(_arg1, _arg2)
        res.typ = _arg3
        res.value = _arg4
        return res
    
    @staticmethod
    def _new3206(_arg1 : 'Token', _arg2 : 'Token', _arg3 : 'PersonAttrTerminType', _arg4 : str, _arg5 : 'MorphCollection', _arg6 : 'MorphGender') -> 'PersonAttrToken':
        res = PersonAttrToken(_arg1, _arg2)
        res.typ = _arg3
        res.value = _arg4
        res.morph = _arg5
        res.gender = _arg6
        return res
    
    @staticmethod
    def _new3209(_arg1 : 'Token', _arg2 : 'Token', _arg3 : 'MorphCollection', _arg4 : 'PersonAttrToken') -> 'PersonAttrToken':
        res = PersonAttrToken(_arg1, _arg2)
        res.morph = _arg3
        res.higher_prop_ref = _arg4
        return res
    
    @staticmethod
    def _new3217(_arg1 : 'Token', _arg2 : 'Token', _arg3 : 'PersonPropertyReferent', _arg4 : 'PersonAttrTerminType') -> 'PersonAttrToken':
        res = PersonAttrToken(_arg1, _arg2)
        res.prop_ref = _arg3
        res.typ = _arg4
        return res
    
    @staticmethod
    def _new3229(_arg1 : 'Token', _arg2 : 'Token', _arg3 : 'PersonAttrTerminType', _arg4 : 'PersonPropertyReferent', _arg5 : 'MorphCollection') -> 'PersonAttrToken':
        res = PersonAttrToken(_arg1, _arg2)
        res.typ = _arg3
        res.prop_ref = _arg4
        res.morph = _arg5
        return res
    
    @staticmethod
    def _new3232(_arg1 : 'Token', _arg2 : 'Token', _arg3 : 'PersonAttrTerminType', _arg4 : 'PersonPropertyReferent', _arg5 : 'MorphCollection', _arg6 : bool) -> 'PersonAttrToken':
        res = PersonAttrToken(_arg1, _arg2)
        res.typ = _arg3
        res.prop_ref = _arg4
        res.morph = _arg5
        res.can_be_independent_property = _arg6
        return res
    
    # static constructor for class PersonAttrToken
    @staticmethod
    def _static_ctor():
        PersonAttrToken.M_EMPTY_ADJS = ["УСПЕШНЫЙ", "ИЗВЕСТНЫЙ", "ЗНАМЕНИТЫЙ", "ИЗВЕСТНЕЙШИЙ", "ПОПУЛЯРНЫЙ", "ГЕНИАЛЬНЫЙ", "ТАЛАНТЛИВЫЙ", "МОЛОДОЙ", "УСПІШНИЙ", "ВІДОМИЙ", "ЗНАМЕНИТИЙ", "ВІДОМИЙ", "ПОПУЛЯРНИЙ", "ГЕНІАЛЬНИЙ", "ТАЛАНОВИТИЙ", "МОЛОДИЙ"]
        PersonAttrToken.M_STD_FORMS = dict()

PersonAttrToken._static_ctor()