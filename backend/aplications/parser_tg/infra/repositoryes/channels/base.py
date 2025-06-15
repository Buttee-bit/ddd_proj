from abc import ABC, abstractmethod
from typing import Iterable

from backend.aplications.parser_tg.domain.entity.channel.channel import Channel


class BaseChannelRepository(ABC):

    @abstractmethod
    async def add_channel(self, url: str) -> None: ...

    @abstractmethod
    async def get_channel(self) -> Channel: ...

    @abstractmethod
    async def chek_exis_channel(self, url:str) -> bool: ...

    @abstractmethod
    async def get_all_channels_with_filter(
        self, limit: int, offset: int
    ) -> Iterable[Channel]: ...

    @abstractmethod
    async def get_all_channels(self) -> Iterable[Channel]: ...

    @abstractmethod
    async def update_channel_info(self, url_channel: str, data: dict) -> Channel: ...
