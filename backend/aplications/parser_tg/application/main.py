import logging
from faststream import FastStream, Logger, Depends
from faststream.kafka import KafkaBroker
from backend.aplications.parser_tg.application.services.tg import TgParsServices
from backend.aplications.parser_tg.ioc import _init_container
from punq import Container

broker = KafkaBroker()
app = FastStream(broker=broker)

@app.after_startup
async def start_telegram_listener(
    logger: Logger,
    container: Container = Depends(_init_container),
):
    async def handle_telegram_message(message: str):
        ...
        # logger.info(f"Получено сообщение из Telegram: {message}")
        # await broker.publish(message, topic="telegram_messages")
        # logger.info(f"Сообщение отправлено в Kafka: {message}")

    tg_services: TgParsServices = container.resolve(TgParsServices)


    tg_services.message_handler = handle_telegram_message

    await tg_services.start_listening()
    logger.info("Прослушивание сообщений Telegram запущено.")

@broker.subscriber("telegram_messages")
async def handle_telegram_message(data, logger: Logger): ...
    # logger.info(f"Получено сообщение из Kafka: {data}")