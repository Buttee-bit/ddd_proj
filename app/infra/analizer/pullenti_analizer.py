from dataclasses import dataclass
from app.infra.analizer.base import BaseAnalazer
from pullenti.ner.ServerService import ServerService
from pullenti.ner.person.PersonAnalyzer import PersonAnalyzer
from pullenti.ner.address.AddressAnalyzer import AddressAnalyzer
from pullenti.ner.geo.GeoAnalyzer import GeoAnalyzer
from pullenti.ner.geo.GeoReferent import GeoReferent
from pullenti.ner.org.OrganizationAnalyzer import OrganizationAnalyzer
from pullenti.ner.date.DateAnalyzer import DateAnalyzer

@dataclass(frozen=True)
class PullentiAnalizer(BaseAnalazer):

    def __post_init__(self):
        DateAnalyzer.initialize()
        PersonAnalyzer.initialize()
        AddressAnalyzer.initialize()
        GeoAnalyzer.initialize()
        OrganizationAnalyzer.initialize()

    async def get_result(self, text: str):
        result = ServerService.process_on_server(address_=self.address_, text=text)
        return result