import logging
from typing import Iterable
from backend.aplications.parser_tg.domain.entity.ner.person import NerPeople
from backend.pullenti.ner.AnalysisResult import AnalysisResult
from backend.pullenti.ner.Referent import Referent
from backend.pullenti.ner.Slot import Slot


def convert_analysis_result_to_ners(result: AnalysisResult) -> Iterable[NerPeople]:
    list_ner = []
    for entity in result.entities:
        entity: Referent
        if entity.type_name == "PERSON":
            ner = NerPeople(
                value=entity.get_compare_strings()[0],
                props=[str(value.value) for value in entity.slots],
                index=[(i.begin_char, i.end_char) for i in entity.occurrence],
            )
            logging.warning(f'ner: {ner}')
            list_ner.append(ner)
    return list_ner