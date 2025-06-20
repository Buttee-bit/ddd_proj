from dataclasses import dataclass

from app.infra.repositoryes.ners.base import  DefaultNerRepository

@dataclass
class PeopleNerRepository(DefaultNerRepository):
    ...