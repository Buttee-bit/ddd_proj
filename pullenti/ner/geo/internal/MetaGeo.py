﻿# SDK Pullenti Lingvo, version 4.30, june 2025. Copyright (c) 2013-2025, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

from pullenti.unisharp.Utils import Utils

from pullenti.ner.metadata.ReferentClass import ReferentClass

class MetaGeo(ReferentClass):
    
    @staticmethod
    def initialize() -> None:
        from pullenti.ner.geo.GeoReferent import GeoReferent
        MetaGeo._global_meta = MetaGeo()
        MetaGeo._global_meta.add_feature(GeoReferent.ATTR_NAME, "Наименование", 1, 0)
        MetaGeo._global_meta.add_feature(GeoReferent.ATTR_TYPE, "Тип", 1, 0)
        MetaGeo._global_meta.add_feature(GeoReferent.ATTR_ALPHA2, "Код страны", 0, 1)
        MetaGeo._global_meta.add_feature(GeoReferent.ATTR_HIGHER, "Вышестоящий объект", 0, 1)
        MetaGeo._global_meta.add_feature(GeoReferent.ATTR_REF, "Ссылка на объект", 0, 1)
        MetaGeo._global_meta.add_feature(GeoReferent.ATTR_MISC, "Дополнительно", 0, 0)
    
    @property
    def name(self) -> str:
        from pullenti.ner.geo.GeoReferent import GeoReferent
        return GeoReferent.OBJ_TYPENAME
    
    @property
    def caption(self) -> str:
        return "Территориальное образование"
    
    COUNTRY_CITY_IMAGE_ID = "countrycity"
    
    COUNTRY_IMAGE_ID = "country"
    
    CITY_IMAGE_ID = "city"
    
    DISTRICT_IMAGE_ID = "district"
    
    REGION_IMAGE_ID = "region"
    
    UNION_IMAGE_ID = "union"
    
    def get_image_id(self, obj : 'Referent'=None) -> str:
        from pullenti.ner.geo.GeoReferent import GeoReferent
        ter = Utils.asObjectOrNull(obj, GeoReferent)
        if (ter is not None): 
            if (ter.is_union): 
                return MetaGeo.UNION_IMAGE_ID
            if (ter.is_city and ((ter.is_state or ter.is_region))): 
                return MetaGeo.COUNTRY_CITY_IMAGE_ID
            if (ter.is_state): 
                return MetaGeo.COUNTRY_IMAGE_ID
            if (ter.is_city): 
                return MetaGeo.CITY_IMAGE_ID
            if (ter.is_region and ter.higher is not None and ter.higher.is_city): 
                return MetaGeo.DISTRICT_IMAGE_ID
        return MetaGeo.REGION_IMAGE_ID
    
    _global_meta = None