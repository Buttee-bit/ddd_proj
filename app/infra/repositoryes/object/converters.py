import logging
from typing import Iterable
from app.domain.entity.ner.entity import Ner
from app.domain.entity.ner.person import NerPeople
from app.domain.entity.object.object import ObjectDomain




def convert_document_to_Main_Object(document:dict) -> ObjectDomain:
    return ObjectDomain(
        oid=document['oid'],
        main_name=document['main_name'],
        created_at=document['created_at'],
    )