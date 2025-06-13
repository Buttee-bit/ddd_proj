from dataclasses import dataclass


from backend.aplications.parser_tg.domain.entity.channel.channel import Channel
from backend.aplications.parser_tg.domain.events.channels import NewChannelReceivedEvent
from backend.aplications.parser_tg.infra.brokers.base import BaseBroker
from backend.aplications.parser_tg.infra.repositoryes.channels.base import BaseChannelRepository
from backend.aplications.parser_tg.logic.commands.base import BaseCommand, CommandHandler


@dataclass(frozen=True)
class CreateChannelsCommand(BaseCommand):
    url: str


@dataclass(frozen=True)
class CreateChannelCommandHandler(CommandHandler[CreateChannelsCommand, Channel]):
    channels_repository: BaseChannelRepository
    broker: BaseBroker

    async def handle(self, command: CreateChannelsCommand) -> Channel:

        channel = await self.channels_repository.add_channel(url=command.url)
        await self.broker.send_message(
            topic='update-channels-telegramm',
            message=NewChannelReceivedEvent(
                link_channel=command.url
            )
        )

        return channel
