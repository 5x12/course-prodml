"""
Prediction API module.

This module contains endpoints to trigger a machine learning model
for predicting apartment price.

Endpoints:
    - GET /pred/:
        Returns a prediction for apartment price based on the query
        parameters provided in the request. Query parameters should
        match the schema defined in the Apartment class.
        Returns HTTP status 400 if input parameters are invalid.

    - POST /pred/:
        Returns a prediction for apartment price based on the JSON
        data provided in the request body. The request body should
        contain JSON data that matches the schema defined in the
        Apartment class.
        Returns HTTP status 400 if input parameters are invalid.
"""

from flask import Blueprint, abort, request
from pydantic import ValidationError

from schema.apartment import Apartment
from services import model_inference_service


bp = Blueprint('prediction', __name__, url_prefix='/pred')


@bp.get('/')
def get_prediction():
    """
    Return a prediction based on the query parameters.

    Returns:
        dict: A dictionary containing the prediction result.
    """
    try:
        apartment_features = Apartment(**request.args)
    except ValidationError:
        abort(code=400, description='Bad input params')  # noqa: WPS432

    prediction = model_inference_service.predict(
        list(apartment_features.model_dump().values()),
    )

    return {'prediction': prediction}


@bp.post('/')
def get_prediction_post():
    """
    Return a prediction based on the JSON data.

    Returns:
        dict: A dictionary containing the prediction result.
    """
    try:
        apartment_features = Apartment(**request.json)
    except ValidationError:
        abort(code=400, description='Bad input params')  # noqa: WPS432

    prediction = model_inference_service.predict(
        list(apartment_features.model_dump().values()),
    )

    return {'prediction': prediction}
