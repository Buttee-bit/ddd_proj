from dataclasses import dataclass

from backend.aplications.parser_tg.domain.errors.base import ApplicationError



@dataclass
class InfraionError(ApplicationError):
    @property
    def message(self) -> str:
        return f'Произошла ошибка инфраструктуры'