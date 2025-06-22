from dataclasses import dataclass
from app.domain.entity.base import BaseEntity

# TODO не использую нафиг с пляжа
@dataclass
class NerPeople(BaseEntity):
    value: str
    props:list[str]
    index: list[list[int]]