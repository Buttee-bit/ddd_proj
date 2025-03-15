from dataclasses import dataclass
from backend.aplications.parser_tg.domain.entity.base import BaseEntity


@dataclass
class NerPeople(BaseEntity):
    value: str
    props:list[str]
    index: list[list[int]]