# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru


from backend.pullenti.ner.metadata.ReferentClass import ReferentClass

class MetaLetter(ReferentClass):
    
    @staticmethod
    def initialize() -> None:
        from backend.pullenti.ner.mail.MailReferent import MailReferent
        MetaLetter._global_meta = MetaLetter()
        MetaLetter._global_meta.add_feature(MailReferent.ATTR_KIND, "Тип блока", 1, 1)
        MetaLetter._global_meta.add_feature(MailReferent.ATTR_TEXT, "Текст блока", 1, 1)
        MetaLetter._global_meta.add_feature(MailReferent.ATTR_REF, "Ссылка на объект", 0, 0)
    
    @property
    def name(self) -> str:
        from backend.pullenti.ner.mail.MailReferent import MailReferent
        return MailReferent.OBJ_TYPENAME
    
    @property
    def caption(self) -> str:
        return "Блок письма"
    
    IMAGE_ID = "letter"
    
    def get_image_id(self, obj : 'Referent'=None) -> str:
        return MetaLetter.IMAGE_ID
    
    _global_meta = None