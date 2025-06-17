from typing import Iterable
from app.domain.entity.ner.person import NerPeople



def convert_docuemnt_to_ners_people(document:dict) -> Iterable[NerPeople]:
    ...


def convert_ner_people_to_document(list_ner:list[NerPeople]) -> dict:
    return [
        {
            "value": ner.value,
            "props": ner.props,
            "index": ner.index
        } for ner in list_ner
    ]


def convert_one_ner_to_document(ner:NerPeople) -> dict:
    return {
        "value": ner.value,
        "props": ner.props,
    }