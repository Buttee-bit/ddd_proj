from dataclasses import dataclass
from datetime import datetime

from app.domain.entity.news.news import News
from app.infra.repositoryes.news.base import BaseNewsRepository
from app.logic.commands.base import BaseCommand, CommandHandler


@dataclass(frozen=True)
class CreateNewsCommand(BaseCommand):
    title: str
    text: str
    published_at: datetime
    oid_channel: str


@dataclass(frozen=True)
class CreateNewsCommandHandler(CommandHandler[CreateNewsCommand, News]):
    news_repository: BaseNewsRepository

    async def handle(self, command: CreateNewsCommand) -> News:
        news = News(
            title=command.title,
            text=command.text,
            published_at=command.published_at,
            id_channel=command.oid_channel,
        )
        await self.news_repository.add_news(news=news)
        return news