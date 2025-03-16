# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru


class MorphRuleVariantRef:
    
    def __init__(self, rid : int, vid : int, co : int) -> None:
        self.rule_id = 0
        self.variant_id = 0
        self.coef = 0
        self.rule_id = rid
        self.variant_id = vid
        self.coef = co
    
    def __str__(self) -> str:
        return "{0} {1}".format(self.rule_id, self.variant_id)