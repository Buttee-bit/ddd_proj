from dataclasses import dataclass, field
import logging
from typing import ClassVar, Dict

from app.domain.entity.ner.entity import Ner
from app.infra.repositoryes.ners.factory.creators import BaseNerCreator, OrganizationNerCreator, PeopleNerCreator


@dataclass
class NerFactory:

    _creators: ClassVar[Dict[str, BaseNerCreator]] = {}

    @classmethod
    async def create_ner(cls, data: Dict) -> Ner:
        ner_type = data.get('type')
        if not ner_type:
            ...
        try:
            creator = cls._creators.get(ner_type)
            if not creator:
                ...
            ner = await creator.create_ner(data)
            return ner

        except Exception as e:
            ...

    @classmethod
    def register_creator(cls, ner_type: str, creator: BaseNerCreator):
        cls._creators[ner_type] = creator