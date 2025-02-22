from dataclasses import dataclass
from backend.domain.values.base import BaseValueObject



@dataclass(frozen=True)
class Title(BaseValueObject):
    value: str

    # def validate(self):
    #     if len(self.value) < 3:
    #         raise ApplicationError('Title must be at least 3 characters long')


