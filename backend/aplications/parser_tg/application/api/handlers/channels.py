import logging
from typing import Container
from fastapi import (
    Depends,
    status,
)
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter

from backend.aplications.parser_tg.logic.init import init_conatainer
from backend.aplications.parser_tg.logic.commands.channels import CreateChannelsCommand
from backend.aplications.parser_tg.logic.mediator.base import Mediator
from backend.aplications.parser_tg.application.api.handlers.schemas import CreateChannelRequestSchema, CreateChannelResponseSchema, ErrorSchema


router = APIRouter(
    prefix='/channels',
)


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    description='Добавляет канал в бд',
    responses={
        status.HTTP_201_CREATED: {'model': CreateChannelResponseSchema},
        status.HTTP_400_BAD_REQUEST: {'model': ErrorSchema},
    },
)
async def create_channel_handler(
    schema: CreateChannelRequestSchema,
    container: Container = Depends(init_conatainer),
) -> CreateChannelResponseSchema:

    mediator: Mediator = container.resolve(Mediator)
    logging.warning(f'mediator: Mediator: {mediator}')
    try:
        channel, *_ = await mediator.handle_command(CreateChannelsCommand(url=schema.url))
    except Exception as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'error': exception})

    return CreateChannelResponseSchema.from_entity(channel)