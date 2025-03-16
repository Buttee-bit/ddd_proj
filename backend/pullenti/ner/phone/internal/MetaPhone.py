# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru


from backend.pullenti.ner.metadata.ReferentClass import ReferentClass
from backend.pullenti.ner.Referent import Referent

class MetaPhone(ReferentClass):
    
    @staticmethod
    def initialize() -> None:
        from backend.pullenti.ner.phone.PhoneReferent import PhoneReferent
        MetaPhone._global_meta = MetaPhone()
        MetaPhone._global_meta.add_feature(PhoneReferent.ATTR_NUNBER, "Номер", 1, 1)
        MetaPhone._global_meta.add_feature(PhoneReferent.ATTR_ADDNUMBER, "Добавочный номер", 0, 1)
        MetaPhone._global_meta.add_feature(PhoneReferent.ATTR_COUNTRYCODE, "Код страны", 0, 1)
        MetaPhone._global_meta.add_feature(Referent.ATTR_GENERAL, "Обобщающий номер", 0, 1)
        MetaPhone._global_meta.add_feature(PhoneReferent.ATTR_KIND, "Тип", 0, 1)
    
    @property
    def name(self) -> str:
        from backend.pullenti.ner.phone.PhoneReferent import PhoneReferent
        return PhoneReferent.OBJ_TYPENAME
    
    @property
    def caption(self) -> str:
        return "Телефонный номер"
    
    PHONE_IMAGE_ID = "phone"
    
    def get_image_id(self, obj : 'Referent'=None) -> str:
        return MetaPhone.PHONE_IMAGE_ID
    
    _global_meta = None