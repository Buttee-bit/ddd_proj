from dataclasses import dataclass
from abc import ABC
import logging
from typing import Dict

from app.domain.entity.ner.entity import Ner
from app.infra.repositoryes.ners.base import BaseNerRepository


@dataclass
class BaseNerCreator(ABC):
    ner_repository: BaseNerRepository

    async def create_ner(data: dict) -> Ner: ...


@dataclass
class PeopleNerCreator(BaseNerCreator):

    async def create_ner(self, data: dict) -> Ner:

        ner = await self.ner_repository.get_one_ner_by_value(value=data["value"])
        logging.warning(f'ner: {ner}')
        if ner:
            if ner.props != data["props"]:
                ner.update_props_ner(data=data)
                await self.ner_repository.update_ner_info(ner=ner)
        else:
            ner = Ner.create_ner(data=data)
            logging.warning(f'ner: {ner}')
            await self.ner_repository.add_ner(ner=ner)
        return ner


@dataclass
class OrganizationNerCreator(PeopleNerCreator):

    async def create_ner(self, data: dict) -> Ner:
        return await super().create_ner(data=data)
