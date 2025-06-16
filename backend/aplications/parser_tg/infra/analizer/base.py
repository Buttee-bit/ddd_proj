from abc import abstractmethod
from dataclasses import dataclass
from backend.pullenti.ner.ServerService import ServerService
from backend.pullenti.ner.AnalysisResult import AnalysisResult


@dataclass(frozen=True)
class BaseAnalazer:
    address_: str

    @abstractmethod
    def get_result(self, text:str):
        ...