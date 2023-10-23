from pathlib import Path
import pickle as pk

from model import build_model
from config import settings

class ModelService:
    def __init__(self):
        self.model = None

    def load_model(self):
        model_path = Path(f'{settings.model_path}/{settings.model_name}')

        if not model_path.exists():
            build_model()

        self.model = pk.load(open(f'{settings.model_path}/{settings.model_name}', 'rb'))

    def predict(self, input_parameters):
        return self.model.predict([input_parameters])
    
