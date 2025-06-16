
from dataclasses import dataclass
from backend.aplications.parser_tg.domain.values.base import BaseValueObject
from backend.aplications.parser_tg.domain.errors.news.text import TextValidationError


@dataclass(frozen=True)
class Text(BaseValueObject):
    value: str

    def validate(self):
        if len(self.value) < 3:
            raise TextValidationError(value=self.value)

    def as_generic_type(self):
        return self.value