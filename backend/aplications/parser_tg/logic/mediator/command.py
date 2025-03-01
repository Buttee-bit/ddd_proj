from abc import ABC, abstractmethod
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Iterable

from backend.aplications.parser_tg.logic.commands.base import CT, CR, BaseCommand, CommandHandler


@dataclass(eq=False)
class CommandMediator(ABC):
    command_map: dict[CT, CommandHandler] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True
    )

    @abstractmethod
    def register_command(self, command: CT, command_handler: CommandHandler[CT, CR]):
        ...

    @abstractmethod
    def handle_command(self, command: BaseCommand) -> Iterable[CR]:
        ...
