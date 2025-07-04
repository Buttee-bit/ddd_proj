﻿# SDK Pullenti Lingvo, version 4.30, june 2025. Copyright (c) 2013-2025, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

import typing
from pullenti.unisharp.Utils import Utils
from pullenti.unisharp.Streams import Stream

from pullenti.morph.MorphGender import MorphGender
from pullenti.ner.core.internal.SerializerHelper import SerializerHelper
from pullenti.morph.CharsInfo import CharsInfo
from pullenti.morph.MorphNumber import MorphNumber
from pullenti.morph.LanguageHelper import LanguageHelper
from pullenti.ner.MorphCollection import MorphCollection

class Token:
    """ Базовый класс для всех токенов. Наследные классы - TextToken (конечная словоформа) и MetaToken (связный фрагмент других токенов).
    
    Токен
    """
    
    def __init__(self, kit_ : 'AnalysisKit', begin : int, end : int) -> None:
        self.kit = None;
        self.__m_begin_char = 0
        self.__m_end_char = 0
        self.tag = None;
        self._m_previous = None;
        self._m_next = None;
        self.__m_morph = None;
        self.chars = None;
        self.__m_attrs = 0
        self.kit = kit_
        self.__m_begin_char = begin
        self.__m_end_char = end
    
    @property
    def begin_char(self) -> int:
        """ Позиция в тексте начального символа
        
        """
        return self.__m_begin_char
    
    @property
    def end_char(self) -> int:
        """ Позиция в тексте конечного символа
        
        """
        return self.__m_end_char
    
    @property
    def length_char(self) -> int:
        """ Длина в текстовых символах """
        return (self.end_char - self.begin_char) + 1
    
    @property
    def is_ignored(self) -> bool:
        """ Игнорировать токен при обработке """
        if (self.kit.sofa.ignored_end_char > 0): 
            if (self.begin_char >= self.kit.sofa.ignored_begin_char and self.end_char <= self.kit.sofa.ignored_end_char): 
                return True
        return False
    
    @property
    def previous(self) -> 'Token':
        """ Предыдущий токен в цепочке токенов
        
        """
        return self._m_previous
    @previous.setter
    def previous(self, value) -> 'Token':
        self._m_previous = value
        if (value is not None): 
            value._m_next = self
        self.__m_attrs = (0)
        return value
    
    @property
    def next0_(self) -> 'Token':
        """ Следующий токен в цепочке токенов
        
        """
        return self._m_next
    @next0_.setter
    def next0_(self, value) -> 'Token':
        self._m_next = value
        if (value is not None): 
            value._m_previous = self
        else: 
            pass
        self.__m_attrs = (0)
        return value
    
    @property
    def morph(self) -> 'MorphCollection':
        """ Морфологическая информация
        
        """
        if (self.__m_morph is None): 
            self.__m_morph = MorphCollection()
        return self.__m_morph
    @morph.setter
    def morph(self, value) -> 'MorphCollection':
        self.__m_morph = value
        return value
    
    def __str__(self) -> str:
        end = self.end_char
        err = False
        if (end >= len(self.kit.sofa.text)): 
            end = (len(self.kit.sofa.text) - 1)
            err = True
        if (self.begin_char > end): 
            return "?"
        res = self.kit.sofa.text[self.begin_char:self.begin_char+(end + 1) - self.begin_char]
        if (err): 
            res = "{0} (ERROR: EndChar={0} > TextLength={1})".format(res, self.end_char, len(self.kit.sofa.text))
        return res
    
    def __get_attr(self, i : int) -> bool:
        ch = '\x00'
        if ((((self.__m_attrs) & 1)) == 0): 
            self.__m_attrs = (1)
            if (self._m_previous is None): 
                self._set_attr(1, True)
                self._set_attr(3, True)
            else: 
                j = self._m_previous.end_char + 1
                while (j < self.begin_char) and (j < len(self.kit.sofa.text)): 
                    ch = self.kit.sofa.text[j]
                    if (Utils.isWhitespace((ch))): 
                        self._set_attr(1, True)
                        if (((ord(ch)) == 0xD or (ord(ch)) == 0xA or ch == '\f') or (ord(ch)) == 0x2028): 
                            self._set_attr(3, True)
                    j += 1
            if (self._m_next is None): 
                self._set_attr(2, True)
                self._set_attr(4, True)
            else: 
                j = self.end_char + 1
                while (j < self._m_next.begin_char) and (j < len(self.kit.sofa.text)): 
                    ch = self.kit.sofa.text[j]
                    if (Utils.isWhitespace(ch)): 
                        self._set_attr(2, True)
                        if (((ord(ch)) == 0xD or (ord(ch)) == 0xA or ch == '\f') or (ord(ch)) == 0x2028): 
                            self._set_attr(4, True)
                    j += 1
        return (((((self.__m_attrs) >> i)) & 1)) != 0
    
    def _set_attr(self, i : int, val : bool) -> None:
        if (val): 
            self.__m_attrs |= ((1 << i))
        else: 
            self.__m_attrs &= (~ ((1 << i)))
    
    @property
    def is_whitespace_before(self) -> bool:
        """ Наличие пробельных символов перед """
        return self.__get_attr(1)
    @is_whitespace_before.setter
    def is_whitespace_before(self, value) -> bool:
        self._set_attr(1, value)
        return value
    
    @property
    def is_whitespace_after(self) -> bool:
        """ Наличие пробельных символов после """
        return self.__get_attr(2)
    @is_whitespace_after.setter
    def is_whitespace_after(self, value) -> bool:
        self._set_attr(2, value)
        return value
    
    @property
    def is_newline_before(self) -> bool:
        """ Элемент начинается с новой строки.
        Для 1-го элемента всегда true. """
        return self.__get_attr(3)
    @is_newline_before.setter
    def is_newline_before(self, value) -> bool:
        self._set_attr(3, value)
        return value
    
    @property
    def is_newline_after(self) -> bool:
        """ Элемент заканчивает строку.
        Для последнего элемента всегда true. """
        return self.__get_attr(4)
    @is_newline_after.setter
    def is_newline_after(self, value) -> bool:
        self._set_attr(4, value)
        return value
    
    @property
    def inner_bool(self) -> bool:
        # Это используется внутренним образом
        return self.__get_attr(5)
    @inner_bool.setter
    def inner_bool(self, value) -> bool:
        self._set_attr(5, value)
        return value
    
    @property
    def not_noun_phrase(self) -> bool:
        # Это используется внутренним образом
        # (признак того, что здесь не начинается именная группа, чтобы повторно не пытаться выделять)
        return self.__get_attr(6)
    @not_noun_phrase.setter
    def not_noun_phrase(self, value) -> bool:
        self._set_attr(6, value)
        return value
    
    @property
    def whitespaces_before_count(self) -> int:
        """ Количество пробелов перед, переход на новую строку = 10, табуляция = 5 """
        if (self.previous is None): 
            return 100
        if ((self.previous.end_char + 1) == self.begin_char): 
            return 0
        return self.__calc_whitespaces(self.previous.end_char + 1, self.begin_char - 1)
    
    @property
    def newlines_before_count(self) -> int:
        """ Количество переходов на новую строку перед """
        ch0 = chr(0)
        res = 0
        txt = self.kit.sofa.text
        p = self.begin_char - 1
        while p >= 0 and (p < len(txt)): 
            ch = txt[p]
            if ((ord(ch)) == 0xA or (ord(ch)) == 0x2028): 
                res += 1
            elif ((ord(ch)) == 0xD and (ord(ch0)) != 0xA): 
                res += 1
            elif (ch == '\f'): 
                res += 10
            elif (not Utils.isWhitespace(ch)): 
                break
            ch0 = ch
            p -= 1
        return res
    
    @property
    def newlines_after_count(self) -> int:
        """ Количество переходов на новую строку перед """
        ch0 = chr(0)
        res = 0
        txt = self.kit.sofa.text
        p = self.end_char + 1
        while p < len(txt): 
            ch = txt[p]
            if ((ord(ch)) == 0xD or (ord(ch)) == 0x2028): 
                res += 1
            elif ((ord(ch)) == 0xA and (ord(ch0)) != 0xD): 
                res += 1
            elif (ch == '\f'): 
                res += 10
            elif (not Utils.isWhitespace(ch)): 
                break
            ch0 = ch
            p += 1
        return res
    
    @property
    def whitespaces_after_count(self) -> int:
        """ Количество пробелов перед, переход на новую строку = 10, табуляция = 5 """
        if (self.next0_ is None): 
            return 100
        if ((self.end_char + 1) == self.next0_.begin_char): 
            return 0
        return self.__calc_whitespaces(self.end_char + 1, self.next0_.begin_char - 1)
    
    def __calc_whitespaces(self, p0 : int, p1 : int) -> int:
        if ((p0 < 0) or p0 > p1 or p1 >= len(self.kit.sofa.text)): 
            return -1
        res = 0
        i = p0
        while i <= p1: 
            ch = self.kit.get_text_character(i)
            if (ch == '\r' or ch == '\n' or (ord(ch)) == 0x2028): 
                res += 10
                ch1 = self.kit.get_text_character(i + 1)
                if (ch != ch1 and ((ch1 == '\r' or ch1 == '\n'))): 
                    i += 1
            elif (ch == '\t'): 
                res += 5
            elif (ch == '\u0007'): 
                res += 100
            elif (ch == '\f'): 
                res += 100
            else: 
                res += 1
            i += 1
        return res
    
    @property
    def is_hiphen(self) -> bool:
        """ Это символ переноса """
        if (self.begin_char >= len(self.kit.sofa.text)): 
            return False
        ch = self.kit.sofa.text[self.begin_char]
        return LanguageHelper.is_hiphen(ch)
    
    @property
    def is_table_control_char(self) -> bool:
        """ Это спец-символы для табличных элементов (7h, 1Eh, 1Fh) """
        if (self.begin_char >= len(self.kit.sofa.text)): 
            return False
        ch = self.kit.sofa.text[self.begin_char]
        return (ord(ch)) == 7 or (ord(ch)) == 0x1F or (ord(ch)) == 0x1E
    
    @property
    def is_and(self) -> bool:
        """ Это соединительный союз И (на всех языках) """
        return False
    
    @property
    def is_or(self) -> bool:
        """ Это соединительный союз ИЛИ (на всех языках) """
        return False
    
    @property
    def is_comma(self) -> bool:
        """ Это запятая """
        return self.is_char(',')
    
    @property
    def is_comma_and(self) -> bool:
        """ Это запятая или союз И """
        return self.is_comma or self.is_and
    
    def is_char(self, ch : 'char') -> bool:
        """ Токен состоит из конкретного символа
        
        Args:
            ch('char'): проверяемый символ
        
        """
        if (self.begin_char != self.end_char): 
            return False
        if (self.begin_char >= len(self.kit.sofa.text)): 
            return False
        if (ch == '-'): 
            if (self.is_hiphen): 
                return True
        return self.kit.sofa.text[self.begin_char] == ch
    
    def is_char_of(self, chars_ : str) -> bool:
        """ Токен состоит из одного символа, который есть в указанной строке
        
        Args:
            chars_(str): строка возможных символов
        
        """
        if (self.begin_char != self.end_char): 
            return False
        if (self.begin_char >= len(self.kit.sofa.text)): 
            return False
        if (chars_.find(self.kit.sofa.text[self.begin_char]) >= 0): 
            return True
        if (chars_.find('-') >= 0): 
            if (self.is_hiphen): 
                return True
        return False
    
    def is_value(self, term : str, termua : str=None) -> bool:
        """ Проверка конкретного значения слова (с учётом морф.вариантов)
        
        Args:
            term(str): слово (проверяется значение TextToken.Term и все морфварианты)
            termua(str): слово для проверки на украинском языке
        
        Returns:
            bool: да-нет
        """
        return False
    
    def is_value2(self, term : str, next_term : str) -> bool:
        """ Проверка двух подряд идущих слов (с учётом морф.вариантов)
        
        Args:
            term(str): слово (проверяется значение TextToken.Term и все морфварианты)
            next_term(str): слово в следующем токене
        
        Returns:
            bool: да или нет
        """
        if (self.next0_ is None): 
            return False
        if (not self.is_value(term, None)): 
            return False
        return self.next0_.is_value(next_term, None)
    
    def is_value3(self, term1 : str, term2 : str, term3 : str) -> bool:
        """ Проверка трёх подряд идущих слова (с учётом морф.вариантов)
        
        Args:
            term1(str): первое слово
            term2(str): слово в след. токене
            term3(str): слово в третьем токене
        
        Returns:
            bool: да или нет
        """
        if (self.next0_ is None or self.next0_.next0_ is None): 
            return False
        if (not self.is_value(term1, None)): 
            return False
        if (not self.next0_.is_value(term2, None)): 
            return False
        return self.next0_.next0_.is_value(term3, None)
    
    @property
    def is_letters(self) -> bool:
        """ Признак того, что это буквенный текстовой токен (TextToken) """
        return False
    
    def get_referent(self) -> 'Referent':
        """ Получить ссылку на сущность (не null только для ReferentToken)
        
        """
        return None
    
    def get_referents(self) -> typing.List['Referent']:
        """ Получить список ссылок на все сущности, скрывающиеся под элементом.
        Дело в том, что одни сущности могут накрывать другие (например, адрес накроет город).
        
        """
        return None
    
    def get_normal_case_text(self, mc : 'MorphClass'=None, num : 'MorphNumber'=MorphNumber.UNDEFINED, gender : 'MorphGender'=MorphGender.UNDEFINED, keep_chars : bool=False) -> str:
        """ Получить связанный с токеном текст в именительном падеже
        
        Args:
            mc(MorphClass): желательная часть речи
            num(MorphNumber): желательное число
            gender(MorphGender): желательный пол
            keep_chars(bool): сохранять регистр символов (по умолчанию, всё в верхний)
        
        Returns:
            str: строка текста
        """
        return str(self)
    
    def get_source_text(self) -> str:
        """ Получить фрагмент исходного текста, связанный с токеном
        
        Returns:
            str: фрагмент исходного текста
        """
        len0_ = (self.end_char + 1) - self.begin_char
        if ((len0_ < 1) or (self.begin_char < 0)): 
            return None
        if ((self.begin_char + len0_) > len(self.kit.sofa.text)): 
            return None
        return self.kit.sofa.text[self.begin_char:self.begin_char+len0_]
    
    def get_morph_class_in_dictionary(self) -> 'MorphClass':
        """ Проверка, что слово есть в словаре соответствующего языка
        
        Returns:
            MorphClass: части речи, если не из словаря, то IsUndefined
        """
        return self.morph.class0_
    
    def _serialize(self, stream : Stream) -> None:
        SerializerHelper.serialize_int(stream, self.begin_char)
        SerializerHelper.serialize_int(stream, self.end_char)
        SerializerHelper.serialize_int(stream, self.__m_attrs)
        SerializerHelper.serialize_int(stream, self.chars.value)
        if (self.__m_morph is None): 
            self.__m_morph = MorphCollection()
        self.__m_morph._serialize(stream)
    
    def _deserialize(self, stream : Stream, kit_ : 'AnalysisKit', vers : int) -> None:
        self.kit = kit_
        self.__m_begin_char = SerializerHelper.deserialize_int(stream)
        self.__m_end_char = SerializerHelper.deserialize_int(stream)
        self.__m_attrs = (SerializerHelper.deserialize_int(stream))
        self.chars = CharsInfo._new3322(SerializerHelper.deserialize_int(stream))
        self.__m_morph = MorphCollection()
        self.__m_morph._deserialize(stream)