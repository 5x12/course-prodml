# data_file_name - path to our csv file in collection.py
# model_path - the folder containing model config files
# model_name - the name of the model we should use

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath
from sqlalchemy import create_engine
from loguru import logger 

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='config/.env', env_file_encoding='utf-8')

    model_path: DirectoryPath
    model_name: str
    log_level: str
    db_conn_str: str
    rent_apart_table_name: str

settings = Settings()

logger.remove()
logger.add("logs/app.log", rotation="1 day", retention="2 days", compression="zip", level=settings.log_level)

engine = create_engine(settings.db_conn_str) 