import logging
from typing import Container
from fastapi import (
    Depends,
    status,
)
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter



from app.applications.api.handlers.filters import GetChannelsFilters
from app.applications.api.schemas import ErrorSchema
from app.logic.init import init_conatainer
from app.logic.commands.channels import CreateChannelsCommand
from app.logic.mediator.base import Mediator
from app.applications.api.handlers.channels.schemas import CreateChannelRequestSchema, CreateChannelResponseSchema, GetMessagesQueryResponseSchema
from app.logic.queries.channels import GetChannelsQueryWithFilter


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
    try:
        channel, *_ = await mediator.handle_command(CreateChannelsCommand(url=schema.url))
    except Exception as exception:
        raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED, detail={'error': exception.message})

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
            GetChannelsQueryWithFilter(filters=filters.to_app.infra()),
        )
        return GetMessagesQueryResponseSchema(
            count=len(channels),
            limit=filters.limit,
            offset=filters.offset,
            items=[CreateChannelResponseSchema.from_entity(channel) for channel in channels]
        )

    except Exception as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={'error': str(exception)}  # Ensure error is string
        )
