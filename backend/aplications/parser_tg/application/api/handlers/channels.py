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
from backend.aplications.parser_tg.logic.commands.channels import CreateChannelsCommand
from backend.aplications.parser_tg.logic.mediator.base import Mediator
from backend.aplications.parser_tg.application.api.handlers.schemas import CreateChannelRequestSchema, CreateChannelResponseSchema, ErrorSchema, GetMessagesQueryResponseSchema
from backend.aplications.parser_tg.logic.queries.channels import GetChannelsQueryWithFilter


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


@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    description='Возвращает все каналы из бд',
    responses={
        status.HTTP_200_OK: {'model': GetMessagesQueryResponseSchema},
        status.HTTP_400_BAD_REQUEST: {'model': ErrorSchema},
    },
)
async def get_channels_handler(
    container: Container = Depends(init_conatainer),
    filters: GetChannelsFilters = Depends(),
) -> GetMessagesQueryResponseSchema:  # Changed return type
    mediator: Mediator = container.resolve(Mediator)

    try:
        channels = await mediator.handle_query(
            GetChannelsQueryWithFilter(filters=filters.to_infra()),
        )
    except Exception as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={'error': str(exception)}  # Ensure error is string
        )

    return GetMessagesQueryResponseSchema(
        count=len(channels),
        limit=filters.limit,
        offset=filters.offset,
        items=[CreateChannelResponseSchema.from_entity(channel) for channel in channels]
    )