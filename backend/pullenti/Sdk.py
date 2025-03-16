# SDK backend.pullenti Lingvo, version 4.28, february 2025. Copyright (c) 2013-2025, backend.pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from backend.pullenti C# project.
# The latest version of the code is available on the site www.backend.pullenti.ru


from backend.pullenti.ner.ProcessorService import ProcessorService
from backend.pullenti.ner.decree.DecreeAnalyzer import DecreeAnalyzer
from backend.pullenti.ner.transport.TransportAnalyzer import TransportAnalyzer
from backend.pullenti.ner.instrument.InstrumentAnalyzer import InstrumentAnalyzer
from backend.pullenti.ner.person.PersonAnalyzer import PersonAnalyzer
from backend.pullenti.ner.mail.MailAnalyzer import MailAnalyzer
from backend.pullenti.ner.geo.GeoAnalyzer import GeoAnalyzer
from backend.pullenti.ner.titlepage.TitlePageAnalyzer import TitlePageAnalyzer
from backend.pullenti.ner.weapon.WeaponAnalyzer import WeaponAnalyzer
from backend.pullenti.semantic.SemanticService import SemanticService
from backend.pullenti.morph.MorphLang import MorphLang
from backend.pullenti.ner.named.NamedEntityAnalyzer import NamedEntityAnalyzer
from backend.pullenti.ner.booklink.BookLinkAnalyzer import BookLinkAnalyzer
from backend.pullenti.ner.goods.GoodsAnalyzer import GoodsAnalyzer
from backend.pullenti.ner.date.DateAnalyzer import DateAnalyzer
from backend.pullenti.ner.uri.UriAnalyzer import UriAnalyzer
from backend.pullenti.ner.keyword.KeywordAnalyzer import KeywordAnalyzer
from backend.pullenti.ner.money.MoneyAnalyzer import MoneyAnalyzer
from backend.pullenti.ner.phone.PhoneAnalyzer import PhoneAnalyzer
from backend.pullenti.ner.definition.DefinitionAnalyzer import DefinitionAnalyzer
from backend.pullenti.ner.address.AddressAnalyzer import AddressAnalyzer
from backend.pullenti.ner.org.OrganizationAnalyzer import OrganizationAnalyzer
from backend.pullenti.ner.bank.BankAnalyzer import BankAnalyzer
from backend.pullenti.ner.denomination.DenominationAnalyzer import DenominationAnalyzer
from backend.pullenti.ner.measure.MeasureAnalyzer import MeasureAnalyzer

class Sdk:
    """ Инициализация SDK backend.pullenti
    
    """
    
    @staticmethod
    def get_version() -> str:
        """ Версия SDK backend.pullenti """
        return ProcessorService.get_version()
    
    @staticmethod
    def get_version_date() -> str:
        """ Дата выпуска версии SDK """
        return ProcessorService.get_version_date()
    
    @staticmethod
    def initialize_all() -> None:
        """ Инициализация всего SDK и на всех поддержанных языках.
        Вызывать в самом начале работы. Инициализируется морфология (MorphologyService),
        служба процессоров (ProcessorService), все доступные анализаторы сущностей и
        семантический анализ (SemanticService). Так что больше ничего инициализировать не нужно.
        Полная инициализация
        """
        Sdk.initialize((MorphLang.RU) | MorphLang.UA | MorphLang.EN)
    
    @staticmethod
    def initialize(lang : 'MorphLang'=None) -> None:
        """ Инициализация SDK.
        Вызывать в самом начале работы. Инициализируется морфология (MorphologyService),
        служба процессоров (ProcessorService), все доступные анализаторы сущностей и
        семантический анализ (SemanticService). Так что больше ничего инициализировать не нужно.
        
        Args:
            lang(MorphLang): по умолчанию, русский и английский
        Инициализация конкретных языков
        """
        # сначала инициализация всего сервиса
        ProcessorService.initialize(lang)
        # а затем конкретные анализаторы (какие нужно, в данном случае - все)
        MoneyAnalyzer.initialize()
        UriAnalyzer.initialize()
        PhoneAnalyzer.initialize()
        DateAnalyzer.initialize()
        KeywordAnalyzer.initialize()
        DefinitionAnalyzer.initialize()
        DenominationAnalyzer.initialize()
        MeasureAnalyzer.initialize()
        BankAnalyzer.initialize()
        GeoAnalyzer.initialize()
        AddressAnalyzer.initialize()
        OrganizationAnalyzer.initialize()
        PersonAnalyzer.initialize()
        MailAnalyzer.initialize()
        TransportAnalyzer.initialize()
        DecreeAnalyzer.initialize()
        InstrumentAnalyzer.initialize()
        TitlePageAnalyzer.initialize()
        BookLinkAnalyzer.initialize()
        GoodsAnalyzer.initialize()
        NamedEntityAnalyzer.initialize()
        WeaponAnalyzer.initialize()
        # ещё инициализируем семантическую обработки (в принципе, она не используется для задачи NER)
        SemanticService.initialize()