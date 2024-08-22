"""
This module provides functionality for making predictions.

It contains the ModelInferenceService class, which offers methods
to load a model from a file, and to make predictions using the loaded model.
"""

import pickle as pk
from pathlib import Path

from loguru import logger

from config import model_settings


class ModelInferenceService:
    """
    A service class for making predictions.

    This class provides functionalities to load a ML model from
    a specified path, and make predictions using the loaded model.

    Attributes:
        model: ML model managed by this service. Initially set to None.
        model_path: Directory to extract the model from.
        model_name: Name of the saved model to use.

    Methods:
        __init__: Constructor that initializes the ModelService.
        load_model: Loads the model from file.
        predict: Makes a prediction using the loaded model.
    """

    def __init__(self) -> None:
        """Initialize the ModelInferenceService."""
        self.model = None
        self.model_path = model_settings.model_path
        self.model_name = model_settings.model_name

    def load_model(self) -> None:
        """
        Load the model from a specified path.

        Raises:
            FileNotFoundError: If the model file not exist at specified dir.
        """
        logger.info(
            f'checking the existance of model config file at '
            f'{self.model_path}/{self.model_name}',
        )

        model_path = Path(
            f'{self.model_path}/{self.model_name}',
        )

        if not model_path.exists():
            raise FileNotFoundError('Model file does not exist!')

        logger.info(
            f'model {self.model_name} exists! -> '
            'loading model configuration file',
        )

        with open(model_path, 'rb') as model_file:
            self.model = pk.load(model_file)

    def predict(self, input_parameters: list) -> list:
        """
        Make a prediction using the loaded model.

        Takes input parameters and passes it to the model, which
        was loaded using a pickle file.

        Args:
            input_parameters (list): The input data for making a prediction.

        Returns:
            list: The prediction result from the model.
        """
        logger.info('making prediction!')
        return self.model.predict([input_parameters]).tolist()
