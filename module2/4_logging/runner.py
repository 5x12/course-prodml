from model_service import ModelService

from loguru import logger

@logger.catch
def main():
    ml_svc = ModelService()
    ml_svc.load_model()
    pred = ml_svc.predict([85, 2015, 2, 20, 1, 1, 0, 0, 1])
    logger.info(pred)

if __name__ == '__main__':
    main()

