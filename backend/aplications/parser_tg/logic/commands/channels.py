from dataclasses import dataclass
import logging


from backend.aplications.parser_tg.application.scrapping.tg import TgParsServices
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

@dataclass(frozen=True)
class UpdateChannelInfoCommand(BaseCommand):
    url: str


@dataclass(frozen=True)
class UpdateChannelInfoCommandHandler(CommandHandler[UpdateChannelInfoCommand, Channel]):
    telegram_service: TgParsServices
    channel_repo: BaseChannelRepository

    async def handle(self, command: UpdateChannelInfoCommand):
        entity = await self.telegram_service.subscribe_to_channel(channel_url=command.url)
        data = {
            'subscribers': entity.full_chat.participants_count,
            'title': entity.chats[0].title,
            'id_channel': entity.chats[0].id,
        }
        await self.channel_repo.update_channel_info(url_channel=command.url, data=data)