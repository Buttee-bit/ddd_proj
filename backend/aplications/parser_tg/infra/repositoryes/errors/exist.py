from dataclasses import dataclass
from backend.aplications.parser_tg.domain.errors.base import ApplicationError



@dataclass
class ExisInDBError(ApplicationError):
    value: str

    @property
    def message(self) -> str:
        return f'Данная сущность в базе данных уже есть: {self.value}'

