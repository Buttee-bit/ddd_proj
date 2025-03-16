# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru


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