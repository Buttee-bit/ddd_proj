﻿# SDK Pullenti Lingvo, version 4.30, june 2025. Copyright (c) 2013-2025, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

import io
import typing
from pullenti.unisharp.Utils import Utils
from pullenti.unisharp.Misc import RefOutArgWrapper

from pullenti.ner.core.internal.ResourceHelper2 import ResourceHelper2

class PhoneHelper:
    
    class PhoneNode:
        
        def __init__(self) -> None:
            self.pref = None;
            self.children = dict()
            self.countries = None;
        
        def __str__(self) -> str:
            if (self.countries is None): 
                return self.pref
            res = Utils.newStringIO(self.pref)
            for c in self.countries: 
                print(" {0}".format(c), end="", file=res, flush=True)
            return Utils.toStringStringIO(res)
    
    @staticmethod
    def initialize() -> None:
        if (PhoneHelper.M_PHONE_ROOT is not None): 
            return
        PhoneHelper.M_PHONE_ROOT = PhoneHelper.PhoneNode()
        PhoneHelper.M_ALL_COUNTRY_CODES = dict()
        str0_ = ResourceHelper2.get_string("CountryPhoneCodes.txt")
        if (str0_ is None): 
            raise Utils.newException("Can't file resource file {0} in Organization analyzer".format("CountryPhoneCodes.txt"), None)
        for line0 in Utils.splitString(str0_, '\n', False): 
            line = line0.strip()
            if (Utils.isNullOrEmpty(line)): 
                continue
            if (len(line) < 2): 
                continue
            country = line[0:0+2]
            cod = line[2:].strip()
            if (len(cod) < 1): 
                continue
            if (not country in PhoneHelper.M_ALL_COUNTRY_CODES): 
                PhoneHelper.M_ALL_COUNTRY_CODES[country] = cod
            tn = PhoneHelper.M_PHONE_ROOT
            i = 0
            while i < len(cod): 
                dig = cod[i]
                nn = None
                wrapnn3389 = RefOutArgWrapper(None)
                inoutres3390 = Utils.tryGetValue(tn.children, dig, wrapnn3389)
                nn = wrapnn3389.value
                if (not inoutres3390): 
                    nn = PhoneHelper.PhoneNode()
                    nn.pref = cod[0:0+i + 1]
                    tn.children[dig] = nn
                tn = nn
                i += 1
            if (tn.countries is None): 
                tn.countries = list()
            tn.countries.append(country)
    
    M_ALL_COUNTRY_CODES = None
    
    @staticmethod
    def get_all_country_codes() -> typing.List[tuple]:
        return PhoneHelper.M_ALL_COUNTRY_CODES
    
    M_PHONE_ROOT = None
    
    @staticmethod
    def get_country_prefix(full_number : str) -> str:
        if (full_number is None): 
            return None
        nod = PhoneHelper.M_PHONE_ROOT
        max_ind = -1
        i = 0
        while i < len(full_number): 
            dig = full_number[i]
            nn = None
            wrapnn3391 = RefOutArgWrapper(None)
            inoutres3392 = Utils.tryGetValue(nod.children, dig, wrapnn3391)
            nn = wrapnn3391.value
            if (not inoutres3392): 
                break
            if (nn.countries is not None and len(nn.countries) > 0): 
                max_ind = i
            nod = nn
            i += 1
        if (max_ind < 0): 
            return None
        else: 
            return full_number[0:0+max_ind + 1]