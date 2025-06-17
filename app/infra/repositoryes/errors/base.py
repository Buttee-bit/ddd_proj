from dataclasses import dataclass

from app.domain.errors.base import ApplicationError



@dataclass
class infraionError(ApplicationError):
    @property
    def message(self) -> str:
        return f'Произошла ошибка инфраструктуры'