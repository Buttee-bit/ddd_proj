# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru


from backend.pullenti.ner.metadata.ReferentClass import ReferentClass

class MetaChemical(ReferentClass):
    
    @staticmethod
    def initialize() -> None:
        from backend.pullenti.ner.chemical.ChemicalFormulaReferent import ChemicalFormulaReferent
        MetaChemical.GLOBAL_META = MetaChemical()
        MetaChemical.GLOBAL_META.add_feature(ChemicalFormulaReferent.ATTR_VALUE, "Формула", 0, 1)
        MetaChemical.GLOBAL_META.add_feature(ChemicalFormulaReferent.ATTR_NAME, "Текстовое определение", 0, 0)
    
    TYPES = None
    
    @property
    def name(self) -> str:
        from backend.pullenti.ner.chemical.ChemicalFormulaReferent import ChemicalFormulaReferent
        return ChemicalFormulaReferent.OBJ_TYPENAME
    
    @property
    def caption(self) -> str:
        return "Химическая формула"
    
    IMAGE_ID = "chemical"
    
    def get_image_id(self, obj : 'Referent'=None) -> str:
        return MetaChemical.IMAGE_ID
    
    GLOBAL_META = None