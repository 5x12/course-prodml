from pathlib import Path
import pickle as pk

from model.pipeline.model import build_model
from config.config import settings
from loguru import logger

class ModelService:
    def __init__(self):
        self.model = None

    def load_model(self):
        logger.info(f"checking the existance of model config file at {settings.model_path}/{settings.model_name}")
        model_path = Path(f'{settings.model_path}/{settings.model_name}')

        if not model_path.exists():
            logger.warning(f"model at {settings.model_path}/{settings.model_name} was not found -> building {settings.model_name}")
            build_model()

        logger.info(f"model {settings.model_name} exists! -> loading model configuration file")
        self.model = pk.load(open(f'{settings.model_path}/{settings.model_name}', 'rb'))

    def predict(self, input_parameters):
        logger.info(f"making prediction!")
        return self.model.predict([input_parameters])
    
