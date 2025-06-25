from datetime import datetime
from pydantic import BaseModel, Field
from app.applications.api.schemas import BaseQueryResponseSchema
from app.domain.entity.object.object import ObjectDomain


class CreateMainObjectRequest(BaseModel):
    name: str

class CreateMainObjectResponse(BaseModel):
    oid: str
    created_at: datetime
    name: str

    @classmethod
    def from_entity(cls, object: ObjectDomain) -> "CreateMainObjectResponse":
        return cls(
            oid=object.oid,
            name=object.main_name,
            created_at = object.created_at,
        )

class TypeEddit(BaseModel):
    value: str = Field(default='add', examples=['add', 'del'])

class EdditMainObjectRequest(BaseModel):
    type: TypeEddit
