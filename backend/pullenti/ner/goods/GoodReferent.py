# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru

import typing
import io
from backend.pullenti.unisharp.Utils import Utils

from backend.pullenti.ner.core.ReferentsEqualType import ReferentsEqualType
from backend.pullenti.ner.core.IntOntologyItem import IntOntologyItem
from backend.pullenti.ner.core.Termin import Termin
from backend.pullenti.ner.metadata.ReferentClass import ReferentClass
from backend.pullenti.ner.goods.internal.GoodMeta import GoodMeta
from backend.pullenti.ner.Referent import Referent
from backend.pullenti.ner.goods.GoodAttributeReferent import GoodAttributeReferent

class GoodReferent(Referent):
    """ Товар
    
    """
    
    def __init__(self) -> None:
        super().__init__(GoodReferent.OBJ_TYPENAME)
        self.instance_of = GoodMeta.GLOBAL_META
    
    OBJ_TYPENAME = "GOOD"
    """ Имя типа сущности TypeName ("GOOD") """
    
    ATTR_ATTR = "ATTR"
    """ Имя атрибута - атрибут (характеристика) товара (GoodAttributeReferent) """
    
    @property
    def attrs(self) -> typing.List['GoodAttributeReferent']:
        """ Атрибуты товара (список GoodAttributeReferent) """
        res = list()
        for s in self.slots: 
            if (isinstance(s.value, GoodAttributeReferent)): 
                res.append(Utils.asObjectOrNull(s.value, GoodAttributeReferent))
        return res
    
    def to_string_ex(self, short_variant : bool, lang : 'MorphLang'=None, lev : int=0) -> str:
        res = io.StringIO()
        for a in self.attrs: 
            print("{0} ".format(a.to_string_ex(True, lang, lev)), end="", file=res, flush=True)
        return Utils.toStringStringIO(res).strip()
    
    def can_be_equals(self, obj : 'Referent', typ : 'ReferentsEqualType'=ReferentsEqualType.WITHINONETEXT) -> bool:
        return self == obj
    
    def create_ontology_item(self) -> 'IntOntologyItem':
        re = IntOntologyItem(self)
        for s in self.slots: 
            if (s.type_name == GoodReferent.ATTR_ATTR): 
                re.termins.append(Termin(str(s.value)))
        return re