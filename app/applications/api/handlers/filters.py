from pydantic import BaseModel

from app.infra.repositoryes.filters.channels import GetAllChannelsFilters, GetNewsFilters


class GetChannelsFilters(BaseModel):
    limit: int = 10
    offset: int = 0

    def to_infra(self) -> GetAllChannelsFilters:
        return GetAllChannelsFilters(limit=self.limit, offset=self.offset)

class GetNewsFilters(GetChannelsFilters):
    def to_infra(self) -> GetNewsFilters:
        return GetNewsFilters(limit=self.limit, offset=self.offset)