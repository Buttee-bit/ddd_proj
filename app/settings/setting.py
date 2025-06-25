from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Setings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )
    session_file: str = Field(..., alias='SESSION_FILE')
    tg_api_id: str = Field(..., alias='TG_API_ID')
    tg_api_hash: str = Field(..., alias='TG_API_HASH')

    BOT_TOKEN: str = Field(..., alias='BOT_TOKEN')

    mongodb_connection_uri: str = Field(..., alias='MONGODB_CONNECTION')

    mongodb_news_database_name: str = Field(..., alias='MONGODB_NEWS_DATABASE_NAME')
    mongodb_news_collection_name: str = Field(..., alias='MONGODB_NEWS_COLLECTION_NAME')

    mongodb_channels_database_name: str = Field(..., alias='MONGODB_CHANNELS_DATABASE_NAME')
    mongodb_channels_collection_name: str = Field(..., alias='MONGODB_CHANNELS_COLLECTION_NAME')

    mongodb_object_database_name: str = Field(..., alias='MONGODB_OBJECT_DATABASE_NAME')
    mongodb_object_collection_name: str = Field(..., alias='MONGODB_OBJECT_COLLECTION_NAME')


    mongodb_ner_database_name: str = Field(..., alias='MONGODB_NER_DATABASE_NAME')
    mongodb_ner_collection_persones_name: str = Field(..., alias='MONGODB_NER_COLLECTION_PERSONES_NAME')
    mongodb_ner_collection_unique_persones_name: str = Field(..., alias='MONGODB_NER_COLLECTION_UNIQUE_PERSONES_NAME')
    mongodb_ner_collection_organizations: str = Field(..., alias='MONGODB_NER_COLLECTION_ORGANIZATIONS')

    pulenty_server: str = Field(..., alias='PULENTY_SERVER')


    kafka_url: str = Field(..., alias='KAFKA_URL')