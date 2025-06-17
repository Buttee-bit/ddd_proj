import logging
from typing import Iterable
from app.domain.entity.ner.person import NerPeople
from pullenti.ner.AnalysisResult import AnalysisResult
from pullenti.ner.Referent import Referent
from pullenti.ner.Slot import Slot


def convert_analysis_result_to_ners(result: AnalysisResult) -> Iterable[NerPeople]:
    list_ner = []
    for entity in result.entities:
        entity: Referent
        if entity.type_name == "PERSON":
            value = entity
            for slot in entity.slots:
                slot: Slot
                props = entity.get_string_values(attr_name="ATTRIBUTE")
                logging.warning(f'props: {props}')
            ner = NerPeople(
                value=value.__str__(),
                props=props,
                index=[(i.begin_char, i.end_char) for i in entity.occurrence],
            )
    return list_ner