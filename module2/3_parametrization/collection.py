import pandas as pd
from config import settings



def load_data(path=settings.data_file_name): #data_file_name
    return pd.read_csv(path)
