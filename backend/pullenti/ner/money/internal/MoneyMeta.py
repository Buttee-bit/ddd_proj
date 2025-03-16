# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru

from backend.pullenti.unisharp.Utils import Utils

from backend.pullenti.ner.metadata.ReferentClass import ReferentClass

class MoneyMeta(ReferentClass):
    
    @staticmethod
    def initialize() -> None:
        from backend.pullenti.ner.money.MoneyReferent import MoneyReferent
        MoneyMeta.GLOBAL_META = MoneyMeta()
        MoneyMeta.GLOBAL_META.add_feature(MoneyReferent.ATTR_CURRENCY, "Валюта", 1, 1)
        MoneyMeta.GLOBAL_META.add_feature(MoneyReferent.ATTR_VALUE, "Значение", 1, 1)
        MoneyMeta.GLOBAL_META.add_feature(MoneyReferent.ATTR_REST, "Остаток (100)", 0, 1)
        MoneyMeta.GLOBAL_META.add_feature(MoneyReferent.ATTR_ALTVALUE, "Другое значение", 1, 1)
        MoneyMeta.GLOBAL_META.add_feature(MoneyReferent.ATTR_ALTREST, "Другой остаток (100)", 0, 1)
    
    @property
    def name(self) -> str:
        from backend.pullenti.ner.money.MoneyReferent import MoneyReferent
        return MoneyReferent.OBJ_TYPENAME
    
    @property
    def caption(self) -> str:
        return "Денежная сумма"
    
    IMAGE_ID = "sum"
    
    IMAGE2ID = "sumerr"
    
    def get_image_id(self, obj : 'Referent'=None) -> str:
        from backend.pullenti.ner.money.MoneyReferent import MoneyReferent
        m = Utils.asObjectOrNull(obj, MoneyReferent)
        if (m is not None): 
            if (m.alt_value is not None or m.alt_rest is not None): 
                return MoneyMeta.IMAGE2ID
        return MoneyMeta.IMAGE_ID
    
    GLOBAL_META = None