from dataclasses import dataclass
from app.domain.errors.base import ApplicationError



@dataclass
class TitleError(ApplicationError):
    value: str

    @property
    def message(self) -> str:
        return f'Ошибка валидации title: {self.value}'

