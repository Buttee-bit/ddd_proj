from dataclasses import dataclass
from app.domain.values.base import BaseValueObject
from app.domain.errors.news.title import TitleError


@dataclass(frozen=True)
class Title(BaseValueObject):
    value: str

    def validate(self):
        if len(self.value) < 3:
            raise TitleError(value=self.value)

    def as_generic_type(self):
        return self.value