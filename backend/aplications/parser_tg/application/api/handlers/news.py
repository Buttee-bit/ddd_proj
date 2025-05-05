import logging
from punq import Container

from fastapi import APIRouter, Depends, WebSocket, status
from fastapi.exceptions import HTTPException

from backend.aplications.parser_tg.application.api.handlers.filters import GetNewsFilters
from backend.aplications.parser_tg.application.api.handlers.schemas import ErrorSchema, GetLastNewsResponseSchema, GetNewsResponseSchema
from backend.aplications.parser_tg.logic.init import init_conatainer
from backend.aplications.parser_tg.logic.mediator.base import Mediator
from backend.aplications.parser_tg.logic.queries.news import GetNewslatestHandler, GetNewsLatestQuery

router = APIRouter(tags=['news'])


@router.websocket("/{user_id}/")
async def test_websocket():
    ...

@router.get('/',
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {'model': GetLastNewsResponseSchema},
        status.HTTP_400_BAD_REQUEST: {'model': ErrorSchema},
    },
    description='Показывает последние новости'
)
async def test_get_news(
    schema: GetNewsFilters = Depends(),
    container: Container = Depends(init_conatainer),
    ) -> GetLastNewsResponseSchema:
    mediator: Mediator  = container.resolve(Mediator)
    try:
        news, count = await mediator.handle_query(
            GetNewsLatestQuery(limit=schema.limit, offset=schema.offset)
        )
        logging.warning(f'news: {news}')
    except Exception as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                'error': exception
            }
        )
    return GetLastNewsResponseSchema(
        offset=schema.offset,
        limit=schema.limit,
        count=count,
        items=[GetNewsResponseSchema.from_entity(one_news) for one_news in news],
    )