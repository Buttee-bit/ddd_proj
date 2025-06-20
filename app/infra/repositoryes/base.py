from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Iterable, Tuple
from motor.core import AgnosticClient

from app.domain.entity.ner.person import NerPeople
from app.domain.entity.news.news import News
from app.domain.entity.channel.channel import Channel
from app.logic.queries.base import BaseQuery




@dataclass
class BaseMongoDBRepository(ABC):
    mongo_db_client: AgnosticClient
    mongo_db_db_name: str
    mongo_db_collection_name: str

    @property
    def _collection(self):
        return self.mongo_db_client[self.mongo_db_db_name][
            self.mongo_db_collection_name
        ]
