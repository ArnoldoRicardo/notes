import secrets

from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET: str = secrets.token_urlsafe(32)

    class Config:
        case_sensitive = True


settings = Settings()
