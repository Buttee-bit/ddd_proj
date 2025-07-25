﻿# SDK Pullenti Lingvo, version 4.30, june 2025. Copyright (c) 2013-2025, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru


from pullenti.ner.MetaToken import MetaToken

class TableRowToken(MetaToken):
    # Токен - строка таблицы из текста
    
    def __init__(self, b : 'Token', e0_ : 'Token') -> None:
        super().__init__(b, e0_, None)
        self.cells = list()
        self._eor = False
        self._last_row = False
    
    def __str__(self) -> str:
        return "ROW ({0} cells) : {1}".format(len(self.cells), self.get_source_text())