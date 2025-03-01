from dataclasses import dataclass

# from backend.aplications.parser_tg.domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class LogicException(Exception):
    @property
    def message(self):
        return 'В обработки запроса возникла ошибка'
