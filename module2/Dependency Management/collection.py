import pandas as pd



def load_data(path="rent_apartments.csv"):
    return pd.read_csv(path)