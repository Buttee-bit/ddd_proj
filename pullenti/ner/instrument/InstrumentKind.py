# SDK Pullenti Lingvo, version 4.30, june 2025. Copyright (c) 2013-2025, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

from enum import IntEnum

class InstrumentKind(IntEnum):
    """ Классы фрагментов документа """
    UNDEFINED = 0
    """ Неизвестно """
    DOCUMENT = 1
    """ Корневой документ """
    INTERNALDOCUMENT = 2
    """ Внутренний документ (например, который утверждается) """
    HEAD = 3
    """ Заголовочная часть """
    CONTENT = 4
    """ Элемент с основным содержимым """
    TAIL = 5
    """ Хвостовая часть """
    APPENDIX = 6
    """ Приложение """
    DOCPART = 7
    """ Часть документа (деление самого верхнего уровня) """
    SECTION = 8
    """ Раздел """
    SUBSECTION = 9
    """ Подраздел """
    CHAPTER = 10
    """ Глава """
    PARAGRAPH = 11
    """ Параграф """
    SUBPARAGRAPH = 12
    """ Подпараграф """
    CLAUSE = 13
    """ Статья """
    CLAUSEPART = 14
    """ Часть статьи """
    ITEM = 15
    """ Пункт """
    SUBITEM = 16
    """ Подпункт """
    INDENTION = 17
    """ Абзац """
    FOOTNOTE = 18
    """ Сноска """
    LISTITEM = 19
    """ Элемент списка """
    LISTHEAD = 20
    """ Заголовок списка (первый абзац перед перечислением) """
    PREAMBLE = 21
    """ Преамбула """
    INDEX = 22
    """ Оглавление """
    INDEXITEM = 23
    """ Элемент оглавления """
    NOTICE = 24
    """ Примечание """
    NUMBER = 25
    """ Номер """
    CASENUMBER = 26
    """ Номер дела (для судебных документов) """
    CASEINFO = 27
    """ Дополнительная информация (для судебных документов) """
    NAME = 28
    """ Наименование """
    TYP = 29
    """ Тип """
    SIGNER = 30
    """ Подписант """
    ORGANIZATION = 31
    """ Организация """
    PLACE = 32
    """ Место """
    DATE = 33
    """ Дата-время """
    CONTACT = 34
    """ Контактные данные """
    INITIATOR = 35
    """ Инициатор """
    DIRECTIVE = 36
    """ Директива """
    EDITIONS = 37
    """ Редакции """
    APPROVED = 38
    """ Одобрен, утвержден """
    DOCREFERENCE = 39
    """ Ссылка на документ """
    KEYWORD = 40
    """ Ключевое слово (типа Приложение и т.п.) """
    COMMENT = 41
    """ Комментарий """
    CITATION = 42
    """ Цитата """
    QUESTION = 43
    """ Вопрос """
    ANSWER = 44
    """ Ответ """
    TABLE = 45
    """ Таблица """
    TABLEROW = 46
    """ Строка таблицы """
    TABLECELL = 47
    """ Ячейка таблицы """
    IGNORED = 48
    """ Для внутреннего использования """
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)