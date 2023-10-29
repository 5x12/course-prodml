
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
import pickle as pk
from preparation import prepare_data
from loguru import logger

from config import settings

def build_model():
    # to train and then save the model we need:

    #1. load preprocessed dataset
    df = prepare_data()
    #2. identify X and y
    X, y = get_X_y(df)
    #3. split the dataset
    X_train, X_test, y_train, y_test = split_train_test(X, y)
    #4. train the model
    rf = train_model(X_train, y_train)
    #5. evaluate the model
    score = evaluate_model(rf, X_test, y_test)
    #6. save the model in a configuration file
    save_model(rf)

def get_X_y(data, 
            col_X = ['area', 
                  'constraction_year', 
                  'bedrooms', 
                  'garden', 
                  'balcony_yes', 
                  'parking_yes', 
                  'furnished_yes', 
                  'garage_yes', 
                  'storage_yes'],
            col_y = 'rent'):
    
    #logger.info("defining X and y variables")

    return data[col_X], data[col_y]

def split_train_test(X, y):
    #logger.info("splitting data into train and test sets")
    X_train, X_test, y_train, y_test = train_test_split(X, 
                                                        y, 
                                                        test_size=0.2)
    
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):

    #logger.info("training a model with hyperparameters")

    grid_space = {'n_estimators': [100, 200, 300], 
                  'max_depth': [3, 6, 9, 12]}
    
    grid = GridSearchCV(RandomForestRegressor(), 
                        param_grid=grid_space, 
                        cv=5, 
                        scoring = 'r2')
    
    model_grid = grid.fit(X_train, y_train)

    return model_grid.best_estimator_

def evaluate_model(model, X_test, y_test):
    #logger.info(f'evaluating model performance: score = {model.score(X_test, y_test)}')
    return model.score(X_test, y_test)

def save_model(model):
    #logger.info("saving model to a directory")
    #logger.debug(f"saving as {settings.model_name} to {settings.model_path}")
    pk.dump(model, open(f'{settings.model_path}/{settings.model_name}', 'wb')) #model_path + model_name


