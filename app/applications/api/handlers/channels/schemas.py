from pydantic import BaseModel

from app.applications.api.schemas import BaseQueryResponseSchema
from app.domain.entity.channel.channel import Channel

class CreateChannelRequestSchema(BaseModel):
    url: str


class CreateChannelResponseSchema(BaseModel):
    oid: str
    url: str
    id_channel: int
    subscribers: int
    title: str

    @classmethod
    def from_entity(cls, Chanel: Channel) -> "CreateChannelResponseSchema":
        return cls(
            oid=Chanel.oid,
            url=Chanel.url,
            id_channel=Chanel.id_channel,
            subscribers=Chanel.subscribers,
            title=Chanel.title,
        )



class GetMessagesQueryResponseSchema(
    BaseQueryResponseSchema[list[CreateChannelResponseSchema]]
): ...
