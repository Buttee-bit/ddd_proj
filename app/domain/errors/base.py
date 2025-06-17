from dataclasses import dataclass



@dataclass
class ApplicationError(Exception):
    @property
    def message(self) -> str:
        return f'Произошла ошибка приложения'