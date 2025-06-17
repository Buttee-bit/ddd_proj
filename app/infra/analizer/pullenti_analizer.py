from dataclasses import dataclass
from app.infra.analizer.base import BaseAnalazer
from backend.pullenti.ner.ServerService import ServerService
from backend.pullenti.ner.person.PersonAnalyzer import PersonAnalyzer
from backend.pullenti.ner.address.AddressAnalyzer import AddressAnalyzer
from backend.pullenti.ner.geo.GeoAnalyzer import GeoAnalyzer
from backend.pullenti.ner.geo.GeoReferent import GeoReferent
from backend.pullenti.ner.org.OrganizationAnalyzer import OrganizationAnalyzer
from backend.pullenti.ner.date.DateAnalyzer import DateAnalyzer

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