﻿# SDK Pullenti Lingvo, version 4.30, june 2025. Copyright (c) 2013-2025, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru


from pullenti.ner.metadata.ReferentClass import ReferentClass

class MetaDenom(ReferentClass):
    
    @staticmethod
    def initialize() -> None:
        from pullenti.ner.denomination.DenominationReferent import DenominationReferent
        MetaDenom._global_meta = MetaDenom()
        MetaDenom._global_meta.add_feature(DenominationReferent.ATTR_VALUE, "Значение", 0, 1)
    
    @property
    def name(self) -> str:
        from pullenti.ner.denomination.DenominationReferent import DenominationReferent
        return DenominationReferent.OBJ_TYPENAME
    
    @property
    def caption(self) -> str:
        return "Обозначение"
    
    DENOM_IMAGE_ID = "denom"
    
    def get_image_id(self, obj : 'Referent'=None) -> str:
        return MetaDenom.DENOM_IMAGE_ID
    
    _global_meta = None