﻿# SDK Pullenti Lingvo, version 4.30, june 2025. Copyright (c) 2013-2025, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

import typing
import io
from pullenti.unisharp.Utils import Utils

from pullenti.ner.geo.GeoReferent import GeoReferent
from pullenti.ner.address.AddressDetailType import AddressDetailType
from pullenti.ner.core.ReferentsEqualType import ReferentsEqualType
from pullenti.ner.address.StreetReferent import StreetReferent
from pullenti.ner.metadata.ReferentClass import ReferentClass
from pullenti.ner.address.AddressBuildingType import AddressBuildingType
from pullenti.ner.address.AddressHouseType import AddressHouseType
from pullenti.ner.address.internal.MetaAddress import MetaAddress
from pullenti.ner.Referent import Referent

class AddressReferent(Referent):
    """ Сущность, представляющая адрес
    
    """
    
    def __init__(self) -> None:
        super().__init__(AddressReferent.OBJ_TYPENAME)
        self.instance_of = MetaAddress._global_meta
    
    OBJ_TYPENAME = "ADDRESS"
    """ Имя типа сущности TypeName ("ADDRESS") """
    
    ATTR_STREET = "STREET"
    """ Имя атрибута - улица """
    
    ATTR_HOUSE = "HOUSE"
    """ Имя атрибута - дом """
    
    ATTR_HOUSEORPLOT = "HOUSEORPLOT"
    """ Имя атрибута - дом или участок (в тексте не указан) """
    
    ATTR_HOUSETYPE = "HOUSETYPE"
    """ Имя атрибута - тип дома """
    
    ATTR_CORPUS = "CORPUS"
    """ Имя атрибута - корпус """
    
    ATTR_BUILDING = "BUILDING"
    """ Имя атрибута - строение """
    
    ATTR_BUILDINGTYPE = "BUILDINGTYPE"
    """ Имя атрибута - тип строения """
    
    ATTR_CORPUSORFLAT = "CORPUSORFLAT"
    """ Имя атрибута - корпус или квартира (когда неясно) """
    
    ATTR_PORCH = "PORCH"
    """ Имя атрибута - подъезд """
    
    ATTR_FLOOR = "FLOOR"
    """ Имя атрибута - этаж """
    
    ATTR_OFFICE = "OFFICE"
    """ Имя атрибута - офис """
    
    ATTR_SPACE = "SPACE"
    """ Имя атрибута - помещение """
    
    ATTR_SPACETYPE = "SPACETYPE"
    """ Имя атрибута - тип помещения """
    
    ATTR_FLAT = "FLAT"
    """ Имя атрибута - квартира """
    
    ATTR_ROOM = "ROOM"
    """ Имя атрибута - комната """
    
    ATTR_CARPLACE = "CARPLACE"
    """ Имя атрибута - машиноместо """
    
    ATTR_PAVILION = "PAVILION"
    """ Имя атрибута - павильон """
    
    ATTR_KILOMETER = "KILOMETER"
    """ Имя атрибута - километр """
    
    ATTR_PLOT = "PLOT"
    """ Имя атрибута - участок """
    
    ATTR_FIELD = "FIELD"
    """ Имя атрибута - поле """
    
    ATTR_BLOCK = "BLOCK"
    """ Имя атрибута - блок (ряд) """
    
    ATTR_BOX = "BOX"
    """ Имя атрибута - бокс (гараж) """
    
    ATTR_PART = "PART"
    """ Имя атрибута - часть (дома) """
    
    ATTR_GENPLAN = "GENPLAN"
    """ Имя атрибута - номер генплана """
    
    ATTR_WELL = "WELL"
    """ Имя атрибута - скважина """
    
    ATTR_GEO = "GEO"
    """ Имя атрибута - географический объект (ближайший в иерархии) """
    
    ATTR_ZIP = "ZIP"
    """ Имя атрибута - почтовый индекс """
    
    ATTR_POSTOFFICEBOX = "POSTOFFICEBOX"
    """ Имя атрибута - почтовый ящик """
    
    ATTR_DELIVERYAREA = "TARGETPLOT"
    """ Имя атрибута - доставочный участок """
    
    ATTR_CSP = "CSP"
    """ Имя атрибута - ГСП """
    
    ATTR_METRO = "METRO"
    """ Имя атрибута - станция метро """
    
    ATTR_DETAIL = "DETAIL"
    """ Имя атрибута - дополнительная информация (AddressDetailType) """
    
    ATTR_DETAILPARAM = "DETAILPARAM"
    """ Имя атрибута - параметр дополнительной информации """
    
    ATTR_DETAILREF = "DETAILREF"
    """ Ссылка на объект, связанный с дополнительной информацией """
    
    ATTR_MISC = "MISC"
    """ Имя атрибута - разное """
    
    @property
    def streets(self) -> typing.List['Referent']:
        """ Улица (кстати, их может быть несколько) """
        res = list()
        for s in self.slots: 
            if (s.type_name == AddressReferent.ATTR_STREET and (isinstance(s.value, Referent))): 
                res.append(Utils.asObjectOrNull(s.value, Referent))
        return res
    
    @property
    def house(self) -> str:
        """ Дом """
        return self.get_string_value(AddressReferent.ATTR_HOUSE)
    @house.setter
    def house(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_HOUSE, value, True, 0)
        return value
    
    @property
    def house_type(self) -> 'AddressHouseType':
        """ Тип дома """
        str0_ = self.get_string_value(AddressReferent.ATTR_HOUSETYPE)
        if (Utils.isNullOrEmpty(str0_)): 
            return AddressHouseType.HOUSE
        try: 
            return Utils.valToEnum(str0_, AddressHouseType)
        except Exception as ex455: 
            return AddressHouseType.HOUSE
    @house_type.setter
    def house_type(self, value) -> 'AddressHouseType':
        self.add_slot(AddressReferent.ATTR_HOUSETYPE, Utils.enumToString(value).upper(), True, 0)
        return value
    
    @property
    def building(self) -> str:
        """ Строение """
        return self.get_string_value(AddressReferent.ATTR_BUILDING)
    @building.setter
    def building(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_BUILDING, value, True, 0)
        return value
    
    @property
    def building_type(self) -> 'AddressBuildingType':
        """ Тип строения """
        str0_ = self.get_string_value(AddressReferent.ATTR_BUILDINGTYPE)
        if (Utils.isNullOrEmpty(str0_)): 
            return AddressBuildingType.BUILDING
        try: 
            return Utils.valToEnum(str0_, AddressBuildingType)
        except Exception as ex456: 
            return AddressBuildingType.BUILDING
    @building_type.setter
    def building_type(self, value) -> 'AddressBuildingType':
        self.add_slot(AddressReferent.ATTR_BUILDINGTYPE, Utils.enumToString(value).upper(), True, 0)
        return value
    
    @property
    def corpus(self) -> str:
        """ Корпус """
        return self.get_string_value(AddressReferent.ATTR_CORPUS)
    @corpus.setter
    def corpus(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_CORPUS, value, True, 0)
        return value
    
    @property
    def corpus_or_flat(self) -> str:
        """ Корпус или квартира """
        return self.get_string_value(AddressReferent.ATTR_CORPUSORFLAT)
    @corpus_or_flat.setter
    def corpus_or_flat(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_CORPUSORFLAT, value, True, 0)
        return value
    
    @property
    def floor0_(self) -> str:
        """ Этаж """
        return self.get_string_value(AddressReferent.ATTR_FLOOR)
    @floor0_.setter
    def floor0_(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_FLOOR, value, True, 0)
        return value
    
    @property
    def potch(self) -> str:
        """ Подъезд """
        return self.get_string_value(AddressReferent.ATTR_PORCH)
    @potch.setter
    def potch(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_PORCH, value, True, 0)
        return value
    
    @property
    def flat(self) -> str:
        """ Квартира """
        return self.get_string_value(AddressReferent.ATTR_FLAT)
    @flat.setter
    def flat(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_FLAT, value, True, 0)
        return value
    
    @property
    def pavilion(self) -> str:
        """ Павильон """
        return self.get_string_value(AddressReferent.ATTR_PAVILION)
    @pavilion.setter
    def pavilion(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_PAVILION, value, True, 0)
        return value
    
    @property
    def office(self) -> str:
        """ Номер офиса """
        return self.get_string_value(AddressReferent.ATTR_OFFICE)
    @office.setter
    def office(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_OFFICE, value, True, 0)
        return value
    
    @property
    def room(self) -> str:
        """ Номер комнаты """
        return self.get_string_value(AddressReferent.ATTR_ROOM)
    @room.setter
    def room(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_ROOM, value, True, 0)
        return value
    
    @property
    def plot(self) -> str:
        """ Номер участка """
        return self.get_string_value(AddressReferent.ATTR_PLOT)
    @plot.setter
    def plot(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_PLOT, value, True, 0)
        return value
    
    @property
    def house_or_plot(self) -> str:
        """ Номер дома или участка (в тексте не указано) """
        return self.get_string_value(AddressReferent.ATTR_HOUSEORPLOT)
    @house_or_plot.setter
    def house_or_plot(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_HOUSEORPLOT, value, True, 0)
        return value
    
    @property
    def field(self) -> str:
        """ Номер поля """
        return self.get_string_value(AddressReferent.ATTR_FIELD)
    @field.setter
    def field(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_FIELD, value, True, 0)
        return value
    
    @property
    def genplan(self) -> str:
        """ Генплан """
        return self.get_string_value(AddressReferent.ATTR_GENPLAN)
    @genplan.setter
    def genplan(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_GENPLAN, value, True, 0)
        return value
    
    @property
    def block(self) -> str:
        """ Блок (ряд) """
        return self.get_string_value(AddressReferent.ATTR_BLOCK)
    @block.setter
    def block(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_BLOCK, value, True, 0)
        return value
    
    @property
    def box(self) -> str:
        """ Бокс (гараж) """
        return self.get_string_value(AddressReferent.ATTR_BOX)
    @box.setter
    def box(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_BOX, value, True, 0)
        return value
    
    @property
    def well(self) -> str:
        """ Скважина (месторождений) """
        return self.get_string_value(AddressReferent.ATTR_WELL)
    @well.setter
    def well(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_WELL, value, True, 0)
        return value
    
    @property
    def carplace(self) -> str:
        """ Машиноместо """
        return self.get_string_value(AddressReferent.ATTR_CARPLACE)
    @carplace.setter
    def carplace(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_CARPLACE, value, True, 0)
        return value
    
    @property
    def part(self) -> str:
        """ Часть (дома) """
        return self.get_string_value(AddressReferent.ATTR_PART)
    @part.setter
    def part(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_PART, value, True, 0)
        return value
    
    @property
    def space(self) -> str:
        """ Помещение """
        return self.get_string_value(AddressReferent.ATTR_SPACE)
    @space.setter
    def space(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_SPACE, value, True, 0)
        return value
    
    @property
    def space_type(self) -> str:
        """ Тип помещения """
        return self.get_string_value(AddressReferent.ATTR_SPACETYPE)
    @space_type.setter
    def space_type(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_SPACETYPE, value, True, 0)
        return value
    
    @property
    def metro(self) -> str:
        """ Станция метро """
        return self.get_string_value(AddressReferent.ATTR_METRO)
    @metro.setter
    def metro(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_METRO, value, True, 0)
        return value
    
    @property
    def kilometer(self) -> str:
        """ Километр """
        return self.get_string_value(AddressReferent.ATTR_KILOMETER)
    @kilometer.setter
    def kilometer(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_KILOMETER, value, True, 0)
        return value
    
    @property
    def zip0_(self) -> str:
        """ Почтовый индекс """
        return self.get_string_value(AddressReferent.ATTR_ZIP)
    @zip0_.setter
    def zip0_(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_ZIP, value, True, 0)
        return value
    
    @property
    def post_office_box(self) -> str:
        """ Почтовый ящик """
        return self.get_string_value(AddressReferent.ATTR_POSTOFFICEBOX)
    @post_office_box.setter
    def post_office_box(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_POSTOFFICEBOX, value, True, 0)
        return value
    
    @property
    def delivery_area(self) -> str:
        """ Доставочный участок """
        return self.get_string_value(AddressReferent.ATTR_DELIVERYAREA)
    @delivery_area.setter
    def delivery_area(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_DELIVERYAREA, value, True, 0)
        return value
    
    @property
    def csp(self) -> str:
        """ ГСП (абонент городской служебной почты) """
        return self.get_string_value(AddressReferent.ATTR_CSP)
    @csp.setter
    def csp(self, value) -> str:
        self.add_slot(AddressReferent.ATTR_CSP, value, True, 0)
        return value
    
    @property
    def geos(self) -> typing.List['GeoReferent']:
        """ Ссылки на географические объекты (самого нижнего уровня) """
        res = list()
        for a in self.slots: 
            if (a.type_name == AddressReferent.ATTR_GEO and (isinstance(a.value, GeoReferent))): 
                res.append(Utils.asObjectOrNull(a.value, GeoReferent))
            elif (a.type_name == AddressReferent.ATTR_STREET and (isinstance(a.value, Referent))): 
                for s in a.value.slots: 
                    if (isinstance(s.value, GeoReferent)): 
                        res.append(Utils.asObjectOrNull(s.value, GeoReferent))
        i = len(res) - 1
        while i > 0: 
            for j in range(i - 1, -1, -1):
                if (AddressReferent.__is_higher(res[i], res[j])): 
                    del res[i]
                    break
                elif (AddressReferent.__is_higher(res[j], res[i])): 
                    del res[j]
                    i -= 1
            i -= 1
        return res
    
    @staticmethod
    def __is_higher(ghi : 'GeoReferent', glo : 'GeoReferent') -> bool:
        i = 0
        while glo is not None and (i < 10): 
            if (glo.can_be_equals(ghi, ReferentsEqualType.WITHINONETEXT)): 
                return True
            glo = glo.higher; i += 1
        return False
    
    @property
    def parent_referent(self) -> 'Referent':
        sr = Utils.asObjectOrNull(self.get_slot_value(AddressReferent.ATTR_STREET), Referent)
        if (sr is not None): 
            return sr
        geos_ = self.geos
        for g in geos_: 
            if (g.is_city): 
                return g
        for g in geos_: 
            if (g.is_region and not g.is_state): 
                return g
        if (len(geos_) > 0): 
            return geos_[0]
        return None
    
    def add_referent(self, r : 'Referent') -> None:
        from pullenti.ner.geo.internal.GeoOwnerHelper import GeoOwnerHelper
        if (r is None): 
            return
        geo = Utils.asObjectOrNull(r, GeoReferent)
        if (geo is not None): 
            for s in self.slots: 
                if (s.type_name == AddressReferent.ATTR_GEO): 
                    geo0 = Utils.asObjectOrNull(s.value, GeoReferent)
                    if (geo0 is None): 
                        continue
                    if (GeoOwnerHelper.can_be_higher(geo0, geo, None, None)): 
                        if (geo.higher == geo0 or geo.is_city): 
                            self.upload_slot(s, geo)
                            return
                    if (GeoOwnerHelper.can_be_higher(geo, geo0, None, None)): 
                        return
            self.add_slot(AddressReferent.ATTR_GEO, r, False, 0)
        elif ((isinstance(r, StreetReferent)) or r.type_name == "ORGANIZATION"): 
            self.add_slot(AddressReferent.ATTR_STREET, r, False, 0)
    
    @property
    def detail(self) -> 'AddressDetailType':
        """ Дополнительная детализация места (пересечение, около ...) """
        s = self.get_string_value(AddressReferent.ATTR_DETAIL)
        if (s is None): 
            return AddressDetailType.UNDEFINED
        try: 
            return Utils.valToEnum(s, AddressDetailType)
        except Exception as ex457: 
            pass
        return AddressDetailType.UNDEFINED
    @detail.setter
    def detail(self, value) -> 'AddressDetailType':
        if (value != AddressDetailType.UNDEFINED): 
            self.add_slot(AddressReferent.ATTR_DETAIL, Utils.enumToString(value).upper(), True, 0)
        return value
    
    def to_string_ex(self, short_variant : bool, lang : 'MorphLang'=None, lev : int=0) -> str:
        res = io.StringIO()
        strs = self.streets
        if (len(strs) == 0): 
            if (self.metro is not None): 
                if (res.tell() > 0): 
                    print(' ', end="", file=res)
                print(Utils.ifNotNull(self.metro, ""), end="", file=res)
        else: 
            if (res.tell() > 0): 
                print(' ', end="", file=res)
            i = 0
            while i < len(strs): 
                if (i > 0): 
                    print(", ", end="", file=res)
                print(strs[i].to_string_ex(True, lang, 0), end="", file=res)
                i += 1
        self.__out_house(res)
        for g in self.geos: 
            if (res.tell() > 0 and Utils.getCharAtStringIO(res, res.tell() - 1) == ' '): 
                Utils.setLengthStringIO(res, res.tell() - 1)
            if (res.tell() > 0 and Utils.getCharAtStringIO(res, res.tell() - 1) == ']'): 
                pass
            elif (res.tell() > 0): 
                print(';', end="", file=res)
            print(" {0}".format(g.to_string_ex(True, lang, lev + 1)), end="", file=res, flush=True)
        if (self.zip0_ is not None): 
            print("; {0}".format(self.zip0_), end="", file=res, flush=True)
        str0_ = self.get_string_value(AddressReferent.ATTR_DETAIL)
        if (str0_ is not None): 
            str0_ = (Utils.asObjectOrNull(MetaAddress._global_meta.detail_feature.convert_inner_value_to_outer_value(str0_, lang), str))
        if (str0_ is not None): 
            print(" [{0}".format(str0_.lower()), end="", file=res, flush=True)
            str0_ = self.get_string_value(AddressReferent.ATTR_DETAILPARAM)
            if ((str0_) is not None): 
                print(", {0}".format(str0_), end="", file=res, flush=True)
            if (not short_variant): 
                dd = Utils.asObjectOrNull(self.get_slot_value(AddressReferent.ATTR_DETAILREF), Referent)
                if (dd is not None): 
                    print(", {0}".format(dd.to_string_ex(True, lang, lev + 1)), end="", file=res, flush=True)
            print(']', end="", file=res)
        else: 
            dd = Utils.asObjectOrNull(self.get_slot_value(AddressReferent.ATTR_DETAILREF), Referent)
            if (dd is not None): 
                print(" [{0}]".format(dd.to_string_ex(True, lang, lev + 1)), end="", file=res, flush=True)
        return Utils.toStringStringIO(res).strip()
    
    def __out_house(self, res : io.StringIO) -> None:
        if (self.kilometer is not None): 
            print(" {0}км.".format(self.kilometer), end="", file=res, flush=True)
        if (self.field is not None): 
            print(" поле {0}".format(self.field), end="", file=res, flush=True)
        if (self.genplan is not None): 
            print(" ГП-{0}".format(self.genplan), end="", file=res, flush=True)
        if (self.house is not None): 
            ty = self.house_type
            if (ty == AddressHouseType.ESTATE): 
                print(" влад.", end="", file=res)
            elif (ty == AddressHouseType.HOUSEESTATE): 
                print(" домовл.", end="", file=res)
            elif (ty == AddressHouseType.UNFINISHED): 
                print(" ОНС ", end="", file=res)
            elif (ty == AddressHouseType.SPECIAL): 
                print(' ', end="", file=res)
            else: 
                print(" д.", end="", file=res)
            print((("Б/Н" if self.house == "0" else self.house)), end="", file=res)
        elif (self.house_or_plot is not None): 
            print(" {0}".format(("Б/Н" if self.house_or_plot == "0" else self.house_or_plot)), end="", file=res, flush=True)
        if (self.corpus is not None): 
            print(" корп.{0}".format((("Б/Н" if self.corpus == "0" else self.corpus))), end="", file=res, flush=True)
        if (self.building is not None): 
            ty = self.building_type
            if (ty == AddressBuildingType.CONSTRUCTION): 
                print(" сооруж.", end="", file=res)
            elif (ty == AddressBuildingType.LITER): 
                print(" лит.", end="", file=res)
            else: 
                print(" стр.", end="", file=res)
            print((("Б/Н" if self.building == "0" else self.building)), end="", file=res)
        if (self.part is not None): 
            print(" часть {0}".format(self.part), end="", file=res, flush=True)
        if (self.potch is not None): 
            print(" под.{0}".format(self.potch), end="", file=res, flush=True)
        if (self.floor0_ is not None): 
            print(" эт.{0}".format(self.floor0_), end="", file=res, flush=True)
        if (self.flat is not None): 
            print(" кв.{0}".format(("Б/Н" if self.flat == "0" else self.flat)), end="", file=res, flush=True)
        if (self.block is not None): 
            print(" блок {0}".format(self.block), end="", file=res, flush=True)
        if (self.corpus_or_flat is not None): 
            print(" корп.(кв.?){0}".format(self.corpus_or_flat), end="", file=res, flush=True)
        if (self.box is not None): 
            print(" гараж {0}".format(("Б/Н" if self.box == "0" else self.box)), end="", file=res, flush=True)
        if (self.well is not None): 
            print(" скважина {0}".format(("Б/Н" if self.well == "0" else self.well)), end="", file=res, flush=True)
        if (self.space is not None or self.space_type is not None): 
            print(" помещ.".format(), end="", file=res, flush=True)
            if (self.space_type is not None and ((self.space is None or self.space == "0"))): 
                print(" {0}".format(self.space_type), end="", file=res, flush=True)
            else: 
                print(("Б/Н" if self.space == "0" else self.space), end="", file=res)
                if (self.space_type is not None): 
                    print(" ({0})".format(self.space_type), end="", file=res, flush=True)
        if (self.carplace is not None): 
            print(" маш.место {0}".format(("Б/Н" if self.carplace == "0" else self.carplace)), end="", file=res, flush=True)
        if (self.room is not None): 
            print(" ком.{0}".format(("Б/Н" if self.room == "0" else self.room)), end="", file=res, flush=True)
        if (self.office is not None): 
            print(" оф.{0}".format(self.office), end="", file=res, flush=True)
        if (self.pavilion is not None): 
            print(" пав.{0}".format(self.pavilion), end="", file=res, flush=True)
        if (self.plot is not None): 
            print(" уч.{0}".format(self.plot), end="", file=res, flush=True)
        if (self.post_office_box is not None): 
            print(" а\\я{0}".format(self.post_office_box), end="", file=res, flush=True)
        if (self.delivery_area is not None): 
            print(" дост.участок {0}".format(self.delivery_area), end="", file=res, flush=True)
        if (self.csp is not None): 
            print(" ГСП-{0}".format(self.csp), end="", file=res, flush=True)
    
    def to_string_classic(self) -> str:
        """ Вывод адреса в каноническом виде (сначала индекс, потом страна, город, улица и т.д.)
        
        """
        geos_ = list()
        geo = None
        street = Utils.asObjectOrNull(self.get_slot_value(AddressReferent.ATTR_STREET), StreetReferent)
        if (street is not None): 
            geo = (Utils.asObjectOrNull(street.get_slot_value(StreetReferent.ATTR_GEO), GeoReferent))
        if (geo is None): 
            geo = (Utils.asObjectOrNull(self.get_slot_value(AddressReferent.ATTR_GEO), GeoReferent))
        if (geo is not None): 
            for i in range(10):
                if (not geo in geos_): 
                    geos_.insert(0, geo)
                geo = geo.higher
                if (geo is None): 
                    break
        if (len(geos_) == 0): 
            return str(self)
        res = io.StringIO()
        if (self.zip0_ is not None): 
            print("{0}, ".format(self.zip0_), end="", file=res, flush=True)
        for g in geos_: 
            hi = g.higher
            g.higher = None
            print("{0}, ".format(str(g)), end="", file=res, flush=True)
            g.higher = hi
        if (street is not None): 
            print(street.to_string_ex(True, None, 0), end="", file=res)
        elif (res.tell() > 1): 
            if (Utils.getCharAtStringIO(res, res.tell() - 1) == ' '): 
                Utils.setLengthStringIO(res, res.tell() - 1)
            if (Utils.getCharAtStringIO(res, res.tell() - 1) == ','): 
                Utils.setLengthStringIO(res, res.tell() - 1)
        tmp2 = io.StringIO()
        self.__out_house(tmp2)
        if (tmp2.tell() > 0): 
            print(", {0}".format(Utils.toStringStringIO(tmp2)), end="", file=res, flush=True)
        return Utils.toStringStringIO(res)
    
    def can_be_equals(self, obj : 'Referent', typ : 'ReferentsEqualType'=ReferentsEqualType.WITHINONETEXT) -> bool:
        addr = Utils.asObjectOrNull(obj, AddressReferent)
        if (addr is None): 
            return False
        strs1 = self.streets
        strs2 = addr.streets
        if (len(strs1) > 0 or len(strs2) > 0): 
            ok = False
            for s in strs1: 
                for ss in strs2: 
                    if (ss.can_be_equals(s, typ)): 
                        ok = True
                        break
            if (not ok): 
                return False
        if (addr.house is not None or self.house is not None): 
            if (addr.house != self.house): 
                return False
        if (addr.house_or_plot is not None or self.house_or_plot is not None): 
            if (addr.house_or_plot != self.house_or_plot): 
                return False
        if (addr.building is not None or self.building is not None): 
            if (addr.building != self.building): 
                return False
        if (addr.plot is not None or self.plot is not None): 
            if (addr.plot != self.plot): 
                return False
        if (addr.part is not None or self.part is not None): 
            if (addr.part != self.part): 
                return False
        if (addr.field is not None or self.field is not None): 
            if (addr.field != self.field): 
                return False
        if (addr.genplan is not None and self.genplan is not None): 
            if (addr.genplan != self.genplan): 
                return False
        if (addr.box is not None or self.box is not None): 
            if (addr.box != self.box): 
                return False
        if (addr.well is not None or self.well is not None): 
            if (addr.well != self.well): 
                return False
        if (addr.carplace is not None or self.carplace is not None): 
            if (addr.carplace != self.carplace): 
                return False
        if (addr.space is not None or self.space is not None): 
            if (addr.space != self.space): 
                return False
        if (addr.space_type is not None or self.space_type is not None): 
            if (addr.space_type != self.space_type): 
                return False
        if (addr.block is not None or self.block is not None): 
            if (addr.block != self.block): 
                return False
        if (addr.corpus is not None or self.corpus is not None): 
            if (addr.corpus != self.corpus): 
                if (addr.corpus is not None and addr.corpus == self.corpus_or_flat): 
                    pass
                elif (self.corpus is not None and addr.corpus_or_flat == self.corpus): 
                    pass
                else: 
                    return False
        if (addr.flat is not None or self.flat is not None): 
            if (addr.flat != self.flat): 
                if (addr.flat is not None and addr.flat == self.corpus_or_flat): 
                    pass
                elif (self.flat is not None and addr.corpus_or_flat == self.flat): 
                    pass
                else: 
                    return False
        if (addr.corpus_or_flat is not None or self.corpus_or_flat is not None): 
            if (self.corpus_or_flat is not None and addr.corpus_or_flat is not None): 
                if (self.corpus_or_flat != addr.corpus_or_flat): 
                    return False
            elif (self.corpus_or_flat is None): 
                if (self.corpus is None and self.flat is None): 
                    return False
            elif (addr.corpus_or_flat is None): 
                if (addr.corpus is None and addr.flat is None): 
                    return False
        if (addr.pavilion is not None or self.pavilion is not None): 
            if (addr.pavilion != self.pavilion): 
                return False
        if (addr.office is not None or self.office is not None): 
            if (addr.office != self.office): 
                return False
        if (addr.room is not None or self.room is not None): 
            if (addr.room != self.room): 
                return False
        if (addr.potch is not None or self.potch is not None): 
            if (addr.potch != self.potch): 
                return False
        if (addr.floor0_ is not None or self.floor0_ is not None): 
            if (addr.floor0_ != self.floor0_): 
                return False
        if (addr.post_office_box is not None or self.post_office_box is not None): 
            if (addr.post_office_box != self.post_office_box): 
                return False
        if (addr.delivery_area is not None or self.delivery_area is not None): 
            if (addr.delivery_area != self.delivery_area): 
                return False
        if (addr.csp is not None and self.csp is not None): 
            if (addr.csp != self.csp): 
                return False
        geos1 = self.geos
        geos2 = addr.geos
        if (len(geos1) > 0 and len(geos2) > 0): 
            ok = False
            for g1 in geos1: 
                for g2 in geos2: 
                    if (g1.can_be_equals(g2, typ)): 
                        ok = True
                        break
            if (not ok): 
                return False
        return True
    
    def merge_slots(self, obj : 'Referent', merge_statistic : bool=True) -> None:
        super().merge_slots(obj, merge_statistic)
        if (self.corpus_or_flat is not None): 
            if (self.flat == self.corpus_or_flat): 
                self.corpus_or_flat = None
            elif (self.corpus == self.corpus_or_flat): 
                self.corpus_or_flat = None
        self._correct()
    
    def _correct(self) -> None:
        from pullenti.ner.geo.internal.GeoOwnerHelper import GeoOwnerHelper
        geos_ = list()
        for a in self.slots: 
            if (a.type_name == AddressReferent.ATTR_GEO and (isinstance(a.value, GeoReferent))): 
                geos_.append(Utils.asObjectOrNull(a.value, GeoReferent))
            elif (a.type_name == AddressReferent.ATTR_STREET and (isinstance(a.value, Referent))): 
                for s in a.value.slots: 
                    if (isinstance(s.value, GeoReferent)): 
                        geos_.append(Utils.asObjectOrNull(s.value, GeoReferent))
        i = len(geos_) - 1
        while i > 0: 
            for j in range(i - 1, -1, -1):
                if (AddressReferent.__is_higher(geos_[i], geos_[j])): 
                    s = self.find_slot(AddressReferent.ATTR_GEO, geos_[i], True)
                    if (s is not None): 
                        self.slots.remove(s)
                    del geos_[i]
                    break
                elif (AddressReferent.__is_higher(geos_[j], geos_[i])): 
                    s = self.find_slot(AddressReferent.ATTR_GEO, geos_[j], True)
                    if (s is not None): 
                        self.slots.remove(s)
                    del geos_[j]
                    i -= 1
            i -= 1
        if (len(geos_) == 2): 
            reg = None
            cit = None
            if (geos_[0].is_city and geos_[1].is_region): 
                cit = geos_[0]
                reg = geos_[1]
            elif (geos_[1].is_city and geos_[0].is_region): 
                cit = geos_[1]
                reg = geos_[0]
            if (cit is not None and cit.higher is None and GeoOwnerHelper.can_be_higher(reg, cit, None, None)): 
                cit.higher = reg
                ss = self.find_slot(AddressReferent.ATTR_GEO, reg, True)
                if (ss is not None): 
                    self.slots.remove(ss)
                geos_ = self.geos
            else: 
                stat = None
                geo = None
                if (geos_[0].is_state and not geos_[1].is_state): 
                    stat = geos_[0]
                    geo = geos_[1]
                elif (geos_[1].is_state and not geos_[0].is_state): 
                    stat = geos_[1]
                    geo = geos_[0]
                if (stat is not None): 
                    geo = geo.top_higher
                    if (geo.higher is None): 
                        geo.higher = stat
                        s = self.find_slot(AddressReferent.ATTR_GEO, stat, True)
                        if (s is not None): 
                            self.slots.remove(s)