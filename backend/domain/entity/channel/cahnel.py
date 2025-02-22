from dataclasses import dataclass
from backend.domain.entity.base import BaseEntity



@dataclass
class Channel(BaseEntity):
    name: str
    description: str
    url: str

