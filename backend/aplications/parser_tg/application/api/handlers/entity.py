import logging
from typing import Container
from fastapi import (
    Depends,
    status,
)
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter

from backend.aplications.parser_tg.application.api.handlers.filters import GetChannelsFilters
from backend.aplications.parser_tg.logic.init import init_conatainer
from backend.aplications.parser_tg.logic.commands.ner_people import AddNerPeopleToDocumentCommand
from backend.aplications.parser_tg.logic.mediator.base import Mediator

from backend.aplications.parser_tg.application.api.handlers.schemas import (
    TestAddEntityPersonToDocumentRequestSchema,
    CreateChannelResponseSchema,
    TestAddEntityPersonToDocumentResponseSchema,
    ErrorSchema,
)

router = APIRouter(
    prefix='/entity',
)


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    description='Добавляет канал в бд',
    responses={
        status.HTTP_201_CREATED: {'model': TestAddEntityPersonToDocumentResponseSchema},
        status.HTTP_400_BAD_REQUEST: {'model': ErrorSchema},
    },
)
async def create_channel_handler(
    schema: TestAddEntityPersonToDocumentRequestSchema,
    container: Container = Depends(init_conatainer),
) -> CreateChannelResponseSchema:

    mediator: Mediator = container.resolve(Mediator)
    try:
        channel, *_ = await mediator.handle_command(AddNerPeopleToDocumentCommand(
            document_oid=schema.document_oid,
        ))
    except Exception as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'error': exception})

    return CreateChannelResponseSchema.from_entity(channel)
