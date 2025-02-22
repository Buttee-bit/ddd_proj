from dataclasses import dataclass
from backend.aplications.parser_tg.domain.errors.base import ApplicationError



@dataclass
class TitleError(ApplicationError):
    value: str

    @property
    def message(self) -> str:
        return f'Ошибка валидации title: {self.value}'

