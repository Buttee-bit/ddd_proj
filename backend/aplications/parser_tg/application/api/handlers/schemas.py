from datetime import datetime
from pydantic import BaseModel, Field

from backend.aplications.parser_tg.application.api.schemas import (
    BaseQueryResponseSchema,
)
from backend.aplications.parser_tg.domain.entity.channel.channel import Channel
from backend.aplications.parser_tg.domain.entity.news.news import News


class ErrorSchema(BaseModel):
    error: str


class CreateChannelRequestSchema(BaseModel):
    url: str


class CreateChannelResponseSchema(BaseModel):
    oid: str
    url: str

    @classmethod
    def from_entity(cls, Chanel: Channel) -> "CreateChannelResponseSchema":
        return cls(
            oid=Chanel.oid,
            url=Chanel.url,
        )


class TestAddEntityPersonToDocumentRequestSchema(BaseModel):
    document_oid: str


class TestAddEntityPersonToDocumentResponseSchema(BaseModel):
    test: str


class GetMessagesQueryResponseSchema(
    BaseQueryResponseSchema[list[CreateChannelResponseSchema]]
): ...


class GetNewsResponseSchema(BaseModel):
    oid: str
    title: str
    text: str
    published_at: datetime
    media_url: set
    # channel_name: str

    @classmethod
    def from_entity(cls, news:News) -> "GetNewsResponseSchema":
        return cls(
            oid=news.oid,
            title=news.title,
            text=news.text,
            published_at=news.published_at,
            media_url=news.media_url,
        )


class GetLastNewsResponseSchema(BaseQueryResponseSchema[list[GetNewsResponseSchema]]): ...
