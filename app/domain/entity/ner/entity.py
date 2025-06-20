from dataclasses import dataclass, field

from app.domain.entity.base import BaseEntity


@dataclass
class Ner(BaseEntity):
    value: str
    type: str
    props: str
    id_news: set = field(default_factory=set, kw_only=False)

    @classmethod
    def create_ner(cls, data: dict) -> "Ner":
        return cls(
            value=data["value"],
            props=data["props"],
            type=data["type"],
        )

    def _add_oid_news(self, oid: str):
        return self.id_news.add(oid)

    def update_props_ner(self, data: dict):
        self.props += "; " + data["props"]
