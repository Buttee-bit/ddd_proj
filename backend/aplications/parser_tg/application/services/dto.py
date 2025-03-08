from pydantic import BaseModel


class ChannelDTO(BaseModel):
    oid: str
    url: str

class ListChannelDTO(BaseModel):
    channels: list[ChannelDTO]