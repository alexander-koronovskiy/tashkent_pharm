from functools import lru_cache

from pydantic import BaseSettings


class SettingsDB(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str


@lru_cache
def get_settings_db() -> SettingsDB:
    return SettingsDB()


settings_db = get_settings_db()
