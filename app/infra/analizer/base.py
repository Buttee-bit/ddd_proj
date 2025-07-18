from abc import abstractmethod
from dataclasses import dataclass
# from backend.pullenti.ner.ServerService import ServerService
# from backend.pullenti.ner.AnalysisResult import AnalysisResult


@dataclass
class BaseAnalazer:
    address_: str

    @abstractmethod
    async def get_result(self, text:str):
        ...