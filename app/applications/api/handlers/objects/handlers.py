import logging
from fastapi import (
    Depends,
    status,
)
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter

from punq import Container

from app.applications.api.handlers.objects.schemas import (
    CreateMainObjectRequest,
    CreateMainObjectResponse,
    EdditMainObjectRequest,
)
from app.applications.api.schemas import ErrorSchema
from app.logic.commands.objects import CreateObjectCommand, UpdateNerOrganizationObjectCommand
from app.logic.init import init_conatainer
from app.logic.mediator.base import Mediator


router = APIRouter(prefix="/object", tags=["object"])


@router.post(
    "",
    status_code=status.HTTP_200_OK,
    description="Возврщает основные объекты",
    responses={
        status.HTTP_200_OK: {"model": CreateMainObjectResponse},
        status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
    },
)
async def handle_get_all_objects(
    schema: CreateMainObjectRequest,
    container: Container = Depends(init_conatainer),
) -> CreateMainObjectResponse:
    mediator: Mediator = container.resolve(Mediator)
    try:
        object_, *_ = await mediator.handle_command(
            command=CreateObjectCommand(name=schema.name)
        )
        return CreateMainObjectResponse.from_entity(object=object_)
    except Exception as e:
        return ErrorSchema(error=e.message)


@router.get('/{oid}')
# Супер лонг дринк
async def get_one_domain_object_handler():
    ...


@router.put('/{object_oid}/ner/{oid}')
async def put_ner_domain_object_handler(
    object_oid:str,
    oid:str,
    schema: EdditMainObjectRequest,
    container: Container = Depends(init_conatainer),
):
    mediator: Mediator = container.resolve(Mediator)
    object_ = await mediator.handle_command(
                command=UpdateNerOrganizationObjectCommand(oid_domain_object=object_oid, oid_ner=oid, type=schema.type.value)
            )
    logging.warning(f'object_: {object_}')