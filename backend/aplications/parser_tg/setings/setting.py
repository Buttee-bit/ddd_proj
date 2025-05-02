from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    session_file: str = Field(..., alias='SESSION_FILE')
    tg_api_id: str = Field(..., alias='TG_API_ID')
    tg_api_hash: str = Field(..., alias='TG_API_HASH')

    mongodb_connection_uri: str = Field(..., alias='MONGODB_CONNECTION')

    mongodb_news_database_name: str = Field(..., alias='MONGODB_NEWS_DATABASE_NAME')
    mongodb_news_collection_name: str = Field(..., alias='MONGODB_NEWS_COLLECTION_NAME')

    mongodb_channels_database_name: str = Field(..., alias='MONGODB_CHANNELS_DATABASE_NAME')
    mongodb_channels_collection_name: str = Field(..., alias='MONGODB_CHANNELS_COLLECTION_NAME')


    mongodb_ner_database_name: str = Field(..., alias='MONGODB_NER_DATABASE_NAME')
    mongodb_ner_collection_persones_name: str = Field(..., alias='MONGODB_NER_COLLECTION_PERSONES_NAME')
    mongodb_ner_collection_unique_persones_name: str = Field(..., alias='MONGODB_NER_COLLECTION_UNIQUE_PERSONES_NAME')


    pulenty_server: str = Field(..., alias='PULENTY_SERVER')



    class Config:
        env_file = ".env"