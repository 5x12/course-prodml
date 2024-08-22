"""
This module sets up the ML model configuration.

It utilizes Pydantic's BaseSettings for configuration management,
allowing settings to be read from environment variables and a .env file.
"""

from pydantic import DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class ModelSettings(BaseSettings):
    """
    ML model configuration settings for the application.

    Attributes:
        model_config (SettingsConfigDict): Model config, loaded from .env file.
        model_path (DirectoryPath): Filesystem path to the model.
        model_name (str): Name of the ML model.
    """

    model_config = SettingsConfigDict(
        env_file='config/.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )

    model_path: DirectoryPath
    model_name: str


model_settings = ModelSettings()
