from dataclasses import dataclass
import logging
from app.infra.analizer.base import BaseAnalazer
from pullenti.ner.Processor import Processor
from pullenti.ner.ServerService import ServerService
from pullenti.ner.person.PersonAnalyzer import PersonAnalyzer
from pullenti.ner.address.AddressAnalyzer import AddressAnalyzer
from pullenti.ner.geo.GeoAnalyzer import GeoAnalyzer
from pullenti.ner.geo.GeoReferent import GeoReferent
from pullenti.ner.org.OrganizationAnalyzer import OrganizationAnalyzer
from pullenti.ner.date.DateAnalyzer import DateAnalyzer
from pullenti.ner.ProcessorService import ProcessorService
from pullenti.Sdk import Sdk
@dataclass
class PullentiAnalizer(BaseAnalazer):

    def __post_init__(self):
        self.processor = Sdk.initialize_all()
        # self.processor.initialize()
        # a = self.processor.get_analyzers()
        # logging.warning(f'a: {a}')
        # logging.warning(f'self.processor: {type(self.processor)}')
        # self.processor.add_analyzer(PersonAnalyzer)
        # DateAnalyzer.initialize()
        # PersonAnalyzer.initialize()
        # AddressAnalyzer.initialize()
        # GeoAnalyzer.initialize()
        # OrganizationAnalyzer.initialize()

    async def get_result(self, text: str):
        result = ServerService.process_on_server(address_=self.address_, text=text, proc=self.processor)
        return result