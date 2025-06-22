from dataclasses import dataclass, field

from app.domain.entity.base import BaseEntity
from app.domain.entity.ner.entity import Ner
from app.domain.entity.news.news import News


@dataclass
class ObjectDomain(BaseEntity):
    main_name: str
    variant_name: list[str] = field(default_factory=list, kw_only=True)
    ners: list[Ner] = field(default_factory=list, kw_only=True)
    coords: list[float] = field(default_factory=list, kw_only=True)
    news: list[News] = field(default_factory=list, kw_only=True)
    childrens: list["ObjectDomain"] = field(default_factory=list, kw_only=True)
    parents: list["ObjectDomain"] = field(default_factory=list, kw_only=True)

    def add_child(self, children: "ObjectDomain") -> None:
        self.childrens.append(children)

    def delete_child(self, children: "ObjectDomain") -> None:
        self.childrens.remove(children)

    def add_ner(self, ner: Ner) -> None:
        self.ners.append(ner)

    def delete_ner(self, ner: Ner) -> None:
        self.ners.remove(ner)

