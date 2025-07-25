﻿# SDK Pullenti Lingvo, version 4.30, june 2025. Copyright (c) 2013-2025, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru


class ISemanticOnto:
    """ Интерфейс внешней дополнительной онтологии
    (для улучшения качества семантичсекой обработки)
    Внешняя онтология
    """
    
    def check_link(self, master : str, slave : str) -> bool:
        """ Проверка, что в онтологии слова master и slave образуют устойчивую пару
        
        Args:
            master(str): 
            slave(str): 
        
        """
        return None