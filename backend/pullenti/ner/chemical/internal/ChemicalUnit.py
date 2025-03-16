# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru


class ChemicalUnit:
    
    def __init__(self, mnem_ : str, nam : str, lat : str=None) -> None:
        self.name_cyr = None;
        self.name_lat = None;
        self.mnem = None;
        self.mnem = mnem_
        self.name_cyr = nam
        self.name_lat = lat
    
    def __str__(self) -> str:
        return "{0} ({1})".format(self.mnem, self.name_cyr)