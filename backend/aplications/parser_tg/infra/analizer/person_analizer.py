from dataclasses import dataclass


from backend.aplications.parser_tg.infra.analizer.base import BaseAnalazer
from backend.pullenti.ner.person import PersonAnalyzer
from pullenti.ner.ProcessorService import ProcessorService
from pullenti.ner.person.PersonAnalyzer import PersonAnalyzer
from pullenti.morph.MorphLang import MorphLang
from pullenti.ner.AnalysisResult import AnalysisResult


@dataclass
class PersonAnalizer(BaseAnalazer):

    def get_result(self, text) -> AnalysisResult:
        LANGUAGE = MorphLang.UA
        ProcessorService.initialize(LANGUAGE)
        PersonAnalyzer.initialize()
        processor = ProcessorService.create_processor()
        return self._get_service.process_on_server(
            address_=self.address_, proc=processor, text=text, lang=LANGUAGE
        )
