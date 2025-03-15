from abc import abstractmethod
from dataclasses import dataclass
from backend.pullenti.ner.ServerService import ServerService
from pullenti.morph.MorphLang import MorphLang
from pullenti.ner.ProcessorService import ProcessorService
from pullenti.ner.Analyzer import Analyzer
from pullenti.ner.AnalysisResult import AnalysisResult


@dataclass(frozen=True)
class BaseAnalazer:
    address_: str

    @property
    def _get_service(self) -> ServerService:
        return ServerService

    @abstractmethod
    def get_result(self, text:str) -> AnalysisResult:
        ...