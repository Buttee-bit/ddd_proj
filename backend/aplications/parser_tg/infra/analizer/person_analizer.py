from dataclasses import dataclass


from backend.aplications.parser_tg.infra.analizer.base import BaseAnalazer
from backend.pullenti.ner.person import PersonAnalyzer
from backend.pullenti.ner.ProcessorService import ProcessorService
from backend.pullenti.ner.person.PersonAnalyzer import PersonAnalyzer
from backend.pullenti.morph.MorphLang import MorphLang
from backend.pullenti.ner.AnalysisResult import AnalysisResult


@dataclass(frozen=True)
class PersonAnalizer(BaseAnalazer):


    def get_result(self, text) -> AnalysisResult:
        LANGUAGE = MorphLang.UA
        ProcessorService.initialize(LANGUAGE)
        PersonAnalyzer.initialize()
        processor = ProcessorService.create_processor()
        return self._get_service.process_on_server(
            address_=self.address_, proc=processor, text=text, lang=LANGUAGE
        )
