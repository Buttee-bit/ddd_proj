from dataclasses import dataclass, field

from app.domain.entity.base import BaseEntity
from app.domain.entity.ner.entity import Ner


@dataclass
class Object(BaseEntity):
    name: str
    id_ners: list[str] = field(kw_only=True)
    coords: list[float] = field(kw_only=True)
    id_news: list[str] = field(kw_only=True)
    childrens: list['Object'] = field(kw_only=True)
    parents: list['Object'] = field(kw_only=True)

