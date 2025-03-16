# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru

from backend.pullenti.unisharp.Utils import Utils
from backend.pullenti.unisharp.Streams import Stream

class backend.pullentiNerBankInternalResourceHelper:
    """ Это для поддержки получения встроенных ресурсов """
    
    @staticmethod
    def get_bytes(name : str) -> bytearray:
        """ Получить встроенный ресурс
        
        Args:
            name(str): имя, на который оканчивается ресурс
        
        """
        
        names = Utils.getResourcesNames('backend.pullenti.ner.bank.properties', '.png;.txt;.csv')
        for n in names: 
            if (Utils.endsWithString(n, name, True)): 
                if (len(name) < len(n)): 
                    if (n[len(n) - len(name) - 1] != '.'): 
                        continue
                try: 
                    inf = Utils.getResourceInfo('backend.pullenti.ner.bank.properties', n)
                    if (inf is None): 
                        continue
                    with Utils.getResourceStream('backend.pullenti.ner.bank.properties', n) as stream: 
                        buf = Utils.newArrayOfBytes(stream.length, 0)
                        stream.read(buf, 0, len(buf))
                        return buf
                except Exception as ex: 
                    pass
        return None
    
    @staticmethod
    def get_string(name : str) -> str:
        arr = backend.pullentiNerBankInternalResourceHelper.get_bytes(name)
        if (arr is None): 
            return None
        if ((len(arr) > 3 and arr[0] == (0xEF) and arr[1] == (0xBB)) and arr[2] == (0xBF)): 
            return arr[3:3+len(arr) - 3].decode("UTF-8", 'ignore')
        else: 
            return arr.decode("UTF-8", 'ignore')