from dataclasses import dataclass


@dataclass
class GetAllChannelsFilters:
    limit: int = 10
    offset: int = 0


@dataclass
class GetNewsFilters:
    limit: int = 10
    offset: int = 0
