﻿# SDK Pullenti Lingvo, version 4.30, june 2025. Copyright (c) 2013-2025, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru


from pullenti.ner.metadata.ReferentClass import ReferentClass

class MetaBookLink(ReferentClass):
    
    @staticmethod
    def initialize() -> None:
        from pullenti.ner.booklink.BookLinkReferent import BookLinkReferent
        MetaBookLink._global_meta = MetaBookLink()
        MetaBookLink._global_meta.add_feature(BookLinkReferent.ATTR_AUTHOR, "Автор", 0, 0)
        MetaBookLink._global_meta.add_feature(BookLinkReferent.ATTR_NAME, "Наименование", 1, 1)
        MetaBookLink._global_meta.add_feature(BookLinkReferent.ATTR_TYPE, "Тип", 0, 1)
        MetaBookLink._global_meta.add_feature(BookLinkReferent.ATTR_YEAR, "Год", 0, 1)
        MetaBookLink._global_meta.add_feature(BookLinkReferent.ATTR_GEO, "География", 0, 1)
        MetaBookLink._global_meta.add_feature(BookLinkReferent.ATTR_LANG, "Язык", 0, 1)
        MetaBookLink._global_meta.add_feature(BookLinkReferent.ATTR_URL, "URL", 0, 0)
        MetaBookLink._global_meta.add_feature(BookLinkReferent.ATTR_MISC, "Разное", 0, 0)
    
    @property
    def name(self) -> str:
        from pullenti.ner.booklink.BookLinkReferent import BookLinkReferent
        return BookLinkReferent.OBJ_TYPENAME
    
    @property
    def caption(self) -> str:
        return "Ссылка на внешний источник"
    
    IMAGE_ID = "booklink"
    
    def get_image_id(self, obj : 'Referent'=None) -> str:
        return MetaBookLink.IMAGE_ID
    
    _global_meta = None