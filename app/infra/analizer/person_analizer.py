from dataclasses import dataclass


from app.infra.analizer.base import BaseAnalazer
from backend.pullenti.ner.person import PersonAnalyzer
from backend.pullenti.ner.ProcessorService import ProcessorService
from backend.pullenti.ner.person.PersonAnalyzer import PersonAnalyzer
from backend.pullenti.morph.MorphLang import MorphLang
from backend.pullenti.ner.AnalysisResult import AnalysisResult
from backend.pullenti.ner.ServerService import ServerService


@dataclass(frozen=True)
class PersonAnalizer(BaseAnalazer):


    def get_result(self, text) -> AnalysisResult:
        LANGUAGE = MorphLang.UA
        ProcessorService.initialize(LANGUAGE)
        PersonAnalyzer.initialize()
        processor = ProcessorService.create_processor()
        return self.process_on_server(
            address_=self.address_, proc=processor, text=text, lang=LANGUAGE
        )
