from dataclasses import dataclass
from backend.aplications.parser_tg.domain.values.base import BaseValueObject
from backend.aplications.parser_tg.domain.errors.news.title import TitleError


@dataclass(frozen=True)
class Title(BaseValueObject):
    value: str

    def validate(self):
        if len(self.value) < 3:
            raise TitleError(value=self.value)

    def as_generic_type(self):
        return self.value