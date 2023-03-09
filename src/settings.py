from functools import lru_cache

from pydantic import BaseSettings


class SettingsApp(BaseSettings):
    SERVER_HOST: str
    SERVER_PORT: int


@lru_cache
def get_settings_app() -> SettingsApp:
    return SettingsApp()


settings_app = get_settings_app()
