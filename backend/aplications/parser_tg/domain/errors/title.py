from dataclasses import dataclass
from backend.domain.errors.base import ApplicationError



@dataclass
class TitleError(ApplicationError):
    value: str

    @property
    def message(self) -> str:
        return f'Ошибка валидации title: {self.value}'

