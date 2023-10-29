from pathlib import Path
import pickle as pk
from loguru import logger

from model import build_model
from config import settings

class ModelService:
    def __init__(self):
        self.model = None

    def load_model(self):
        #logger.info(f"loading model {settings.model_name}")
        model_path = Path(f'{settings.model_path}/{settings.model_name}')

        if not model_path.exists():
            logger.warning(f"Model {settings.model_path}/{settings.model_name} does not exist -> building a new model")
            build_model()

        self.model = pk.load(open(f'{settings.model_path}/{settings.model_name}', 'rb'))

    def predict(self, input_parameters):
        #1/0
        #logger.info(f"making predictions with input parameters {input_parameters}")
        return self.model.predict([input_parameters])
    
