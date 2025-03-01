from dataclasses import dataclass
from datetime import datetime

from backend.aplications.parser_tg.domain.entity.news.news import News
from backend.aplications.parser_tg.infra.repositoryes.base import BaseNewsRepository
from backend.aplications.parser_tg.logic.commands.base import BaseCommand, CommandHandler


@dataclass(frozen=True)
class CreateNewsCommand(BaseCommand):
    title: str
    text: str
    published_at: datetime


@dataclass(frozen=True)
class CreateNewsCommandHandler(CommandHandler[CreateNewsCommand, News]):
    news_repository: BaseNewsRepository

    async def handle(self, command) -> News:
        news = News(
            title=command.title,
            text=command.text,
            published_at=command.published_at
        )
        await self.news_repository.add_news(news=news)
        return News