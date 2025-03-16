from pydantic import BaseModel, Field

from backend.aplications.parser_tg.application.api.schemas import BaseQueryResponseSchema
from backend.aplications.parser_tg.domain.entity.channel.channel import Channel


class ErrorSchema(BaseModel):
    error: str

class CreateChannelRequestSchema(BaseModel):
    url: str


class CreateChannelResponseSchema(BaseModel):
    oid: str
    url: str

    @classmethod
    def from_entity(cls, Chanel: Channel) -> 'CreateChannelResponseSchema':
        return cls(
            oid=Chanel.oid,
            url=Chanel.url,
        )


class TestAddEntityPersonToDocumentRequestSchema(BaseModel):
    document_oid: str


class TestAddEntityPersonToDocumentResponseSchema(BaseModel):
    test: str


class GetMessagesQueryResponseSchema(BaseQueryResponseSchema[list[CreateChannelResponseSchema]]):
    ...
