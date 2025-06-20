import logging
from typing import Iterable
from app.domain.entity.ner.entity import Ner
from app.domain.entity.ner.person import NerPeople



def convert_docuemnt_to_ners_people(document:dict) -> Iterable[NerPeople]:
    ...

def convert_ner_to_document(data:Ner) -> dict:
    return {
        'oid': data.oid,
        'created_at': data.created_at,
        'value': data.value,
        'type': data.type,
        'props': data.props,
        # 'id_news': data.id_news,
    }



def convert_document_to_ner(document:dict) -> Ner:
    return Ner(
        oid=document['oid'],
        created_at=document['created_at'],
        props=document['props'],
        type=document['type'],
        value=document['value'],
        # id_news=document['id_news'],
    )