import logging
from typing import Iterable
from pullenti.ner.AnalysisResult import AnalysisResult
from pullenti.ner.Referent import Referent
from pullenti.ner.Slot import Slot


def convert_analysis_result(result: AnalysisResult) -> Iterable[dict]:
    for entity in result.entities:
        data = {}
        data['value'] = entity.to_string_ex(short_variant=False)
        data['type'] = entity.type_name
        entity: Referent
        slots_entity = entity.slots
        for slot in slots_entity:
            slot: Slot
            props = slot.convert_value_to_string(lang=result.base_language)
            data['props'] = props
        yield data
