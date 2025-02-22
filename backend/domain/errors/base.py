from dataclasses import dataclass



@dataclass
class ApplicationError(Exception):
    message: str

    @property
    def message(self) -> str:
        return f'Произошла ошибка приложения'