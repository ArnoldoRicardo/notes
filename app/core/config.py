import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET: secrets.token_urlsafe(32)

    class Config:
        case_sensitive = True


settings = Settings()
