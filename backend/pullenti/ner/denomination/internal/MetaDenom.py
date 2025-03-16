# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru


from backend.pullenti.ner.metadata.ReferentClass import ReferentClass

class MetaDenom(ReferentClass):
    
    @staticmethod
    def initialize() -> None:
        from backend.pullenti.ner.denomination.DenominationReferent import DenominationReferent
        MetaDenom._global_meta = MetaDenom()
        MetaDenom._global_meta.add_feature(DenominationReferent.ATTR_VALUE, "Значение", 0, 1)
    
    @property
    def name(self) -> str:
        from backend.pullenti.ner.denomination.DenominationReferent import DenominationReferent
        return DenominationReferent.OBJ_TYPENAME
    
    @property
    def caption(self) -> str:
        return "Обозначение"
    
    DENOM_IMAGE_ID = "denom"
    
    def get_image_id(self, obj : 'Referent'=None) -> str:
        return MetaDenom.DENOM_IMAGE_ID
    
    _global_meta = None