"""
Main application script for running the ML model builder service.

This script initializes the ModelBuilderService, trains the ML model
and logs the output. It demonstrates the typical workflow of using
the ModelBuilderService in a practical application context.
"""

from loguru import logger

from model.model_builder import ModelBuilderService


@logger.catch
def main():
    """
    Run the application.

    Train a model and then save it to
    the model config folder.
    """
    logger.info('running the application...')
    ml_svc = ModelBuilderService()
    ml_svc.train_model()


if __name__ == '__main__':
    main()
