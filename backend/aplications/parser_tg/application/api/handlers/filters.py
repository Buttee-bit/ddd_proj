from pydantic import BaseModel


from backend.aplications.parser_tg.infra.repositoryes.filters.channels import GetAllChannelsFilters


class GetChannelsFilters(BaseModel):
    limit: int = 10
    offset: int = 0

    def to_infra(self) -> GetAllChannelsFilters:
        return GetAllChannelsFilters(limit=self.limit, offset=self.offset)