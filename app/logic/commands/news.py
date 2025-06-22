from dataclasses import dataclass
from datetime import datetime

from app.domain.entity.news.news import News
from app.infra.repositoryes.news.base import BaseNewsRepository
from app.logic.commands.base import BaseCommand, CommandHandler


@dataclass(frozen=True)
class CreateNewsCommand(BaseCommand):
    news: News


@dataclass(frozen=True)
class CreateNewsCommandHandler(CommandHandler[CreateNewsCommand, News]):
    news_repository: BaseNewsRepository

    async def handle(self, command: CreateNewsCommand) -> News:
        await self.news_repository.add_news(news=command.news)
