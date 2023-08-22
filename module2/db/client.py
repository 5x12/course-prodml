import pandas as pd
from conf.conf import logging

#connection to db

def get_data(dir: str) -> pd.DataFrame:
    """
    This function extracts data from ...
    """
    logging.info('Extracting df')
    df = pd.read_csv(dir)
    logging.info('Df is extracted')

    return df


'''
!pickle in Jupyter module:
> load / save

!2

pipeline

load data < db
sqlite
sqlalchemy

write data 
>?

!docker
> bentoml (api for model)
> docker-compose

API 
db
api
model

!MLFlow

'''