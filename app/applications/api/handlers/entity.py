import logging
from punq import Container
from fastapi import (
    Depends,
    status,
)
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter

from app.logic.init import init_conatainer
from app.logic.commands.ner_people import AddNerPeopleToDocumentCommand
from app.logic.mediator.base import Mediator

from app.applications.api.handlers.schemas import (
    TestAddEntityPersonToDocumentRequestSchema,
    TestAddEntityPersonToDocumentResponseSchema,
    ErrorSchema,
)

router = APIRouter(
    prefix='/entity',
)


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    description='AddNerPeopleToDocumentCommand',
    responses={
        status.HTTP_201_CREATED: {'model': TestAddEntityPersonToDocumentResponseSchema},
        status.HTTP_400_BAD_REQUEST: {'model': ErrorSchema},
    },
)
async def create_channel_handler(
    schema: TestAddEntityPersonToDocumentRequestSchema,
    container: Container = Depends(init_conatainer),
) -> TestAddEntityPersonToDocumentResponseSchema:

    mediator: Mediator = container.resolve(Mediator)
    try:
        entity, *_ = await mediator.handle_command(AddNerPeopleToDocumentCommand(
            document_oid=schema.document_oid,
        ))
        logging.warning(f'entity: {entity}')
    except Exception as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'error': exception})

    return TestAddEntityPersonToDocumentResponseSchema(
        test='test'
    )
