from dataclasses import dataclass

from app.logic.exceptions.base import logicException


@dataclass(eq=False)
class EventHandlersNotRegisteredException(logicException):
    event_type: type

    @property
    def message(self):
        return f'Не удалось найти обработчики для события: {self.event_type}'


@dataclass(eq=False)
class CommandHandlersNotRegisteredException(logicException):
    command_type: type

    @property
    def message(self):
        return f'Не удалось найти обработчики для команды: {self.command_type}'
