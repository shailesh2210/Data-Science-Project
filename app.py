import sys
sys.path.append(r"D:\Practice Machine Learning")
from src.ml_project.logger import logging
from src.ml_project.exception import CustomException
from src.ml_project.components.data_ingestion import DataIngestion , DataIngestionConfig

if __name__ == "__main__":
    logging.info("Testing Logging")
    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom Exception Testing")
        raise CustomException(e,sys)