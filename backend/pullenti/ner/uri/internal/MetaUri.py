# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru

from backend.pullenti.unisharp.Utils import Utils

from backend.pullenti.ner.metadata.ReferentClass import ReferentClass

class MetaUri(ReferentClass):
    
    @staticmethod
    def initialize() -> None:
        from backend.pullenti.ner.uri.UriReferent import UriReferent
        MetaUri._global_meta = MetaUri()
        MetaUri._global_meta.add_feature(UriReferent.ATTR_VALUE, "Значение", 0, 1)
        MetaUri._global_meta.add_feature(UriReferent.ATTR_SCHEME, "Схема", 0, 1)
        MetaUri._global_meta.add_feature(UriReferent.ATTR_DETAIL, "Детализация", 0, 1)
    
    @property
    def name(self) -> str:
        from backend.pullenti.ner.uri.UriReferent import UriReferent
        return UriReferent.OBJ_TYPENAME
    
    @property
    def caption(self) -> str:
        return "URI"
    
    MAIL_IMAGE_ID = "mail"
    
    URI_IMAGE_ID = "uri"
    
    def get_image_id(self, obj : 'Referent'=None) -> str:
        from backend.pullenti.ner.uri.UriReferent import UriReferent
        web = Utils.asObjectOrNull(obj, UriReferent)
        if (web is not None and web.scheme == "mailto"): 
            return MetaUri.MAIL_IMAGE_ID
        else: 
            return MetaUri.URI_IMAGE_ID
    
    _global_meta = None