from collections import defaultdict
from dataclasses import dataclass, field
import logging
from typing import Iterable

from backend.aplications.parser_tg.domain.events import BaseEvent
from backend.aplications.parser_tg.logic.commands.base import CR, CT, BaseCommand, CommandHandler
from backend.aplications.parser_tg.logic.events.base import ER, ET, EventHandler
from backend.aplications.parser_tg.logic.exceptions.mediator import CommandHandlersNotRegisteredException
from backend.aplications.parser_tg.logic.mediator.command import CommandMediator
from backend.aplications.parser_tg.logic.mediator.event import EventMediator


@dataclass(eq=False)
class Mediator(CommandMediator, EventMediator):
    events_map: dict[ET, EventHandler] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True,
    )
    commands_map: dict[CT, CommandHandler] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True,
    )
    def register_event(self, event: ET, event_handlers: Iterable[EventHandler[ET, ER]]):
        self.events_map[event].extend(event_handlers)

    def register_command(self, command: CT, command_handlers: Iterable[CommandHandler[CT, CR]]):
        self.commands_map[command].extend(command_handlers)

    async def publish(self, events: Iterable[BaseEvent]) -> Iterable[ER]:
        result = []

        for event in events:
            handlers: Iterable[EventHandler] = self.events_map[event.__class__]
            result.extend([await handler.handle(event) for handler in handlers])

        return result

    async def handle_command(self, command: BaseCommand) -> Iterable[CR]:
        command_type = command.__class__
        handlers = self.commands_map.get(command_type)
        if not handlers:
            raise CommandHandlersNotRegisteredException(command_type)

        return [await handler.handle(command) for handler in handlers]
