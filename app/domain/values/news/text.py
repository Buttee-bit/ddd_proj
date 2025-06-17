
from dataclasses import dataclass
from app.domain.values.base import BaseValueObject
from app.domain.errors.news.text import TextValidationError


@dataclass(frozen=True)
class Text(BaseValueObject):
    value: str

    def validate(self):
        if len(self.value) < 3:
            raise TextValidationError(value=self.value)

    def as_generic_type(self):
        return self.value