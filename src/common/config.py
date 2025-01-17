import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # common
    app_name: str = "vanga-bot"
    debug: bool = True
    
    # tg-bot
    token: str = "7228537802:AAHc4PSiL4DTCIRKlgDM05vsWuKFW1sFTxk"
    admins: str = "00000000,000000001"
    
    # db
    name_database: str = "vanga_bot_database.db"


config = Settings()