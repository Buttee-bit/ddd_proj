﻿# SDK Pullenti Lingvo, version 4.30, june 2025. Copyright (c) 2013-2025, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

import typing
from pullenti.unisharp.Utils import Utils

from pullenti.ner.core.Termin import Termin
from pullenti.ner.decree.DecreeReferent import DecreeReferent
from pullenti.ner.decree.internal.DecreeToken import DecreeToken
from pullenti.ner.instrument.InstrumentKind import InstrumentKind
from pullenti.ner.decree.DecreeKind import DecreeKind
from pullenti.ner.ProcessorService import ProcessorService
from pullenti.ner.Analyzer import Analyzer
from pullenti.ner.instrument.internal.InstrumentArtefactMeta import InstrumentArtefactMeta
from pullenti.ner.instrument.internal.InstrToken import InstrToken
from pullenti.ner.instrument.InstrumentBlockReferent import InstrumentBlockReferent
from pullenti.ner.core.internal.PullentiNerCoreInternalResourceHelper import PullentiNerCoreInternalResourceHelper
from pullenti.ner.instrument.internal.MetaInstrumentBlock import MetaInstrumentBlock
from pullenti.ner.instrument.internal.InstrumentParticipantMeta import InstrumentParticipantMeta
from pullenti.ner.instrument.InstrumentArtefactReferent import InstrumentArtefactReferent
from pullenti.ner.instrument.InstrumentReferent import InstrumentReferent
from pullenti.ner.instrument.internal.MetaInstrument import MetaInstrument
from pullenti.ner.instrument.InstrumentParticipantReferent import InstrumentParticipantReferent

class InstrumentAnalyzer(Analyzer):
    """ Анализатор структуры нормативных актов и договоров: восстановление иерархической структуры фрагментов,
    выделение фигурантов (для договоров и судебных документов), артефактов.
    Специфический анализатор, то есть нужно явно создавать процессор через функцию CreateSpecificProcessor,
    указав имя анализатора. """
    
    @property
    def name(self) -> str:
        return InstrumentAnalyzer.ANALYZER_NAME
    
    ANALYZER_NAME = "INSTRUMENT"
    """ Имя анализатора ("INSTRUMENT") """
    
    @property
    def caption(self) -> str:
        return "Структура нормативно-правовых документов (НПА)"
    
    @property
    def description(self) -> str:
        return "Разбор структуры НПА на разделы и подразделы"
    
    def clone(self) -> 'Analyzer':
        return InstrumentAnalyzer()
    
    @property
    def is_specific(self) -> bool:
        """ Этот анализатор является специфическим (IsSpecific = true) """
        return True
    
    @property
    def progress_weight(self) -> int:
        return 1
    
    @property
    def type_system(self) -> typing.List['ReferentClass']:
        return [MetaInstrument.GLOBAL_META, MetaInstrumentBlock.GLOBAL_META, InstrumentParticipantMeta.GLOBAL_META, InstrumentArtefactMeta.GLOBAL_META]
    
    @property
    def images(self) -> typing.List[tuple]:
        res = dict()
        res[MetaInstrument.DOC_IMAGE_ID] = PullentiNerCoreInternalResourceHelper.get_bytes("decree.png")
        res[MetaInstrumentBlock.PART_IMAGE_ID] = PullentiNerCoreInternalResourceHelper.get_bytes("part.png")
        res[InstrumentParticipantMeta.IMAGE_ID] = PullentiNerCoreInternalResourceHelper.get_bytes("participant.png")
        res[InstrumentArtefactMeta.IMAGE_ID] = PullentiNerCoreInternalResourceHelper.get_bytes("artefact.png")
        return res
    
    def create_referent(self, type0_ : str) -> 'Referent':
        if (type0_ == InstrumentReferent.OBJ_TYPENAME): 
            return InstrumentReferent()
        if (type0_ == InstrumentBlockReferent.OBJ_TYPENAME): 
            return InstrumentBlockReferent()
        if (type0_ == InstrumentParticipantReferent.OBJ_TYPENAME): 
            return InstrumentParticipantReferent()
        if (type0_ == InstrumentArtefactReferent.OBJ_TYPENAME): 
            return InstrumentArtefactReferent()
        return None
    
    def process(self, kit : 'AnalysisKit') -> None:
        from pullenti.ner.instrument.internal.FragToken import FragToken
        aa = kit.processor.find_analyzer("DOCUMENT")
        if (aa is None): 
            for a in ProcessorService.get_analyzers(): 
                if (a.name == "DOCUMENT"): 
                    aa = a
                    break
        dfr = None
        need_test_new_doc = True
        if (aa is not None): 
            rt = aa.process_referent(kit.first_token, "TEST")
            if (rt is None): 
                dfr = FragToken.create_document(kit.first_token, 0, InstrumentKind.UNDEFINED)
        else: 
            dfr = FragToken.create_document(kit.first_token, 0, InstrumentKind.UNDEFINED)
        if (dfr is not None and dfr._m_doc is not None): 
            ki = DecreeToken.get_kind(dfr._m_doc.typ, None)
            if ((((ki == DecreeKind.CONTRACT or ki == DecreeKind.KODEX or ki == DecreeKind.KONVENTION) or ki == DecreeKind.LAW or ki == DecreeKind.STANDARD) or ki == DecreeKind.ORDER or ki == DecreeKind.PUBLISHER) or ki == DecreeKind.USTAV): 
                need_test_new_doc = False
            elif (DecreeToken.is_justice(dfr._m_doc.typ)): 
                need_test_new_doc = False
            elif (dfr._m_doc.typ == "ИЗМЕНЕНИЕ" or dfr._m_doc.typ == "ИЗМЕНЕНИЯ" or dfr._m_doc.typ == "ПОЛОЖЕНИЕ"): 
                need_test_new_doc = False
            elif (len(dfr.children) > 0 and dfr.children[0].kind == InstrumentKind.HEAD): 
                for ch in dfr.children[0].children: 
                    if (ch.kind == InstrumentKind.APPROVED and ch.referents is not None): 
                        for r in ch.referents: 
                            if (r.type_name == "DECREE"): 
                                ki = r.kind
                                if (((ki == DecreeKind.CONTRACT or ki == DecreeKind.KODEX or ki == DecreeKind.KONVENTION) or ki == DecreeKind.LAW or ki == DecreeKind.ORDER) or ki == DecreeKind.PUBLISHER or ki == DecreeKind.USTAV): 
                                    need_test_new_doc = False
        if (need_test_new_doc): 
            if (aa is not None): 
                rt = aa.process_referent(kit.first_token, "INSTRUMENT")
                if (rt is not None): 
                    return
        if (dfr is None): 
            return
        ad = kit.get_analyzer_data(self)
        res = dfr.create_referent(ad)
    
    __m_inited = None
    
    @staticmethod
    def initialize() -> None:
        from pullenti.ner.instrument.internal.ParticipantToken import ParticipantToken
        if (InstrumentAnalyzer.__m_inited): 
            return
        InstrumentAnalyzer.__m_inited = True
        InstrumentArtefactMeta.initialize()
        MetaInstrumentBlock.initialize()
        MetaInstrument.initialize()
        InstrumentParticipantMeta.initialize()
        try: 
            Termin.ASSIGN_ALL_TEXTS_AS_NORMAL = True
            InstrToken.initialize()
            ParticipantToken.initialize()
            Termin.ASSIGN_ALL_TEXTS_AS_NORMAL = False
        except Exception as ex: 
            raise Utils.newException(ex.__str__(), ex)
        ProcessorService.register_analyzer(InstrumentAnalyzer())