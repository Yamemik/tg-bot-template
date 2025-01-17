import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # common
    app_name: str = "tmp-bot"
    debug: bool = True
    
    # tg-bot
    token: str = "token"
    admins: str = "00000000,000000001"
    
    # db
    name_database: str = "bot_database.db"


config = Settings()