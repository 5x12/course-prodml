import pandas as pd
from loguru import logger

from config.config import engine
from db.db_model import RentApartments
from sqlalchemy import select 


def load_data(path): #data_file_name
    logger.info(f"loading csv file at path {path}")
    return pd.read_csv(path)

def load_data_from_db():
    logger.info("extracting the table from the database")
    query = select(RentApartments)
    return pd.read_sql(query, engine)
