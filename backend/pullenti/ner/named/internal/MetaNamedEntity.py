# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru

from backend.pullenti.unisharp.Utils import Utils

from backend.pullenti.ner.metadata.ReferentClass import ReferentClass

class MetaNamedEntity(ReferentClass):
    
    @staticmethod
    def initialize() -> None:
        from backend.pullenti.ner.named.NamedEntityReferent import NamedEntityReferent
        MetaNamedEntity.GLOBAL_META = MetaNamedEntity()
        MetaNamedEntity.GLOBAL_META.add_feature(NamedEntityReferent.ATTR_KIND, "Класс", 1, 1)
        MetaNamedEntity.GLOBAL_META.add_feature(NamedEntityReferent.ATTR_TYPE, "Тип", 0, 0)
        MetaNamedEntity.GLOBAL_META.add_feature(NamedEntityReferent.ATTR_NAME, "Наименование", 0, 0)
        MetaNamedEntity.GLOBAL_META.add_feature(NamedEntityReferent.ATTR_REF, "Ссылка", 0, 1)
    
    @property
    def name(self) -> str:
        from backend.pullenti.ner.named.NamedEntityReferent import NamedEntityReferent
        return NamedEntityReferent.OBJ_TYPENAME
    
    @property
    def caption(self) -> str:
        return "Именованная сущность"
    
    IMAGE_ID = "monument"
    
    def get_image_id(self, obj : 'Referent'=None) -> str:
        from backend.pullenti.ner.named.NamedEntityReferent import NamedEntityReferent
        if (isinstance(obj, NamedEntityReferent)): 
            return Utils.enumToString(obj.kind)
        return MetaNamedEntity.IMAGE_ID
    
    GLOBAL_META = None