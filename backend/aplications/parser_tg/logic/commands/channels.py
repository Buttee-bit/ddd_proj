from dataclasses import dataclass


from backend.aplications.parser_tg.domain.entity.channel.channel import Channel
from backend.aplications.parser_tg.infra.repositoryes.base import BaseChannelRepository
from backend.aplications.parser_tg.infra.tracing.handler import trace_custom
from backend.aplications.parser_tg.logic.commands.base import BaseCommand, CommandHandler


@dataclass(frozen=True)
class CreateChannelsCommand(BaseCommand):
    url: str


@dataclass(frozen=True)
class CreateChannelCommandHandler(CommandHandler[CreateChannelsCommand, Channel]):
    channels_repository: BaseChannelRepository

    @trace_custom(name="CreateChannelCommandHandler")
    async def handle(self, command) -> Channel:
        channel = Channel(
            url=command.url,
        )
        await self.channels_repository.add_channel(channel=channel)
        return channel
