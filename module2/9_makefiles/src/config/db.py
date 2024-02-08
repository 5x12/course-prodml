"""
This module sets up the database configuration.

It utilizes Pydantic's BaseSettings for configuration management,
allowing settings to be read from environment variables and a .env file.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine


class DbSettings(BaseSettings):
    """
    Database configuration settings for the application.

    Attributes:
        model_config (SettingsConfigDict): Model config, loaded from .env file.
        db_conn_str (str): Database connection string.
        rent_apart_table_name (str): Name of the rental apartments table in DB.
    """

    model_config = SettingsConfigDict(
        env_file='config/.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )

    db_conn_str: str
    rent_apart_table_name: str


db_settings = DbSettings()


engine = create_engine(db_settings.db_conn_str)
