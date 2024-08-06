"""
This module provides functionality for building a ML model.

It contains the ModelBuilderService class that offers methods to
train a model, and save it to a specified directory.
"""

from loguru import logger

from config import model_settings
from model.pipeline.model import build_model


class ModelBuilderService:
    """
    A service class for building and saving the ML model.

    This class provides functionalities to train a ML model and
    save it to a specified path.

    Attributes:
        model_path: Directory to save the model to.
        model_name: Name of the saved model.

    Methods:
        __init__: Constructor that initializes the ModelBuilderService.
        train_model: Trains the model and saves it to a specified directory.
    """

    def __init__(self) -> None:
        """Initialize the ModelBuilderService."""
        self.model_path = model_settings.model_path
        self.model_name = model_settings.model_name

    def train_model(self) -> None:
        """Train the model from a specified path, and save to model's dir."""
        logger.info(
            f'building the model config file at '
            f'{self.model_path}/{self.model_name}',
        )
        build_model()
