from dataclasses import dataclass
from datetime import datetime

from backend.aplications.parser_tg.domain.entity.channel.channel import Channel
from backend.aplications.parser_tg.infra.repositoryes.base import BaseChannelRepository
from backend.aplications.parser_tg.logic.commands.base import BaseCommand, CommandHandler


@dataclass(frozen=True)
class CreateChannelsCommand(BaseCommand):
    url: str


@dataclass(frozen=True)
class CreateChannelCommandHandler(CommandHandler[CreateChannelsCommand, Channel]):
    channels_repository: BaseChannelRepository

    async def handle(self, command) -> Channel:
        channel = Channel(
            url=command.url,
        )
        await self.channels_repository.add_channel(channel=channel)
        return channel
