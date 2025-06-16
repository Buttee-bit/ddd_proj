from dataclasses import dataclass
import logging


from backend.aplications.parser_tg.infra.telegram.tg import TgParsServices
from backend.aplications.parser_tg.domain.entity.channel.channel import Channel
from backend.aplications.parser_tg.domain.events.channels import NewChannelReceivedEvent
from backend.aplications.parser_tg.infra.brokers.base import BaseBroker
from backend.aplications.parser_tg.infra.repositoryes.channels.base import (
    BaseChannelRepository,
)
from backend.aplications.parser_tg.logic.commands.base import (
    BaseCommand,
    CommandHandler,
)


@dataclass(frozen=True)
class CreateChannelsCommand(BaseCommand):
    url: str


@dataclass(frozen=True)
class CreateChannelCommandHandler(CommandHandler[CreateChannelsCommand, Channel]):
    channels_repository: BaseChannelRepository
    broker: BaseBroker
    tg_services: TgParsServices

    async def handle(self, command: CreateChannelsCommand) -> Channel:
        entity = await self.tg_services.get_info_entity(channel_url=command.url)
        data = {
            "subscribers": entity.full_chat.participants_count,
            "title": entity.chats[0].title,
            "id_channel": entity.chats[0].id,
        }
        channel: Channel = await self.channels_repository.add_channel(
            url=command.url,
            subscribers=data["subscribers"],
            title=data["title"],
            id_channel=data["id_channel"],
        )
        await self.broker.send_message(
            topic="update-channels-telegramm",
            message=NewChannelReceivedEvent(link_channel=command.url),
        )

        return channel


@dataclass(frozen=True)
class SubscribeChannelCommand(BaseCommand):
    url: str


@dataclass(frozen=True)
class SubscribeChannelInfoCommandHandler(
    CommandHandler[SubscribeChannelCommand, Channel]
):
    telegram_service: TgParsServices
    channel_repo: BaseChannelRepository

    async def handle(self, command: SubscribeChannelCommand):
        await self.telegram_service.subscribe_to_channel(channel_url=command.url)
