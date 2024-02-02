"""
This module sets up the logger configuration.

It utilizes Pydantic's BaseSettings for configuration management,
allowing settings to be read from environment variables and a .env file.
"""

from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict


class LoggerSettings(BaseSettings):
    """
    Logger configuration settings for the application.

    Attributes:
        model_config (SettingsConfigDict): Model config, loaded from .env file.
        log_level (str): Logging level for the application.
    """

    model_config = SettingsConfigDict(
        env_file='config/.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )

    log_level: str


def configure_logging(log_level: str) -> None:
    """
    Configure the logging for the application.

    Args:
        log_level (str): The log level to be set for the logger.
    """
    logger.remove()
    logger.add(
        'logs/app.log',
        rotation='1 day',
        retention='2 days',
        compression='zip',
        level=log_level,
    )


configure_logging(log_level=LoggerSettings().log_level)
