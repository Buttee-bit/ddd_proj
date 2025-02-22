from pydantic_settings import BaseSettings
from pydantic import Field


class ParserTgSettings(BaseSettings):
    session_file: str = Field(..., alias='SESSION_FILE')

    class Config:
        env_file = ".env"