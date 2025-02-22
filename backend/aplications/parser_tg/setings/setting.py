from pydantic_settings import BaseSettings
from pydantic import Field


class ParserTgSettings(BaseSettings):
    session_file: str = Field(..., alias='SESSION_FILE')
    tg_api_id: str = Field(..., alias='TG_API_ID')
    tg_api_hash: str = Field(..., alias='TG_API_HASH')

    class Config:
        env_file = ".env"