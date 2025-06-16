from dataclasses import dataclass
from backend.aplications.parser_tg.domain.errors.base import ApplicationError



class TextValidationError(ApplicationError):
    oid_news: str

    @property
    def message(self) -> str:
        return f'В данной новостей нет текста: {self.oid_news}'