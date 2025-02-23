from faststream.kafka import KafkaBroker, KafkaRouter
from faststream import Logger

router = KafkaRouter()

@router.subscriber("news-topic")
@router.publisher("analize-topic")
async def handle(
    logger: Logger,
    data,
    **kwargs):
    ...



@router.publisher("news-topic")
async def handle_publish_news_topic(
    logger: Logger,
):
    ...