import os
import sys
sys.path.append(r"D:\Practice Machine Learning")
from src.ml_project.exception import CustomException
from src.ml_project.logger import logging
import pandas as pd
from dataclasses import dataclass
from src.ml_project.utils import read_sql_data
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join("artifacts", "train.csv")
    test_data_path = os.path.join("artifacts", "test.csv")
    raw_data_path = os.path.join("artifacts", "raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            #reading code
            df = read_sql_data()
            logging.info("Reading Dataset from Mysql Database")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False , header=True)

            train_set , test_set = train_test_split(df, test_size=0.2, random_state=42)

            df.to_csv(self.ingestion_config.train_data_path , index=False , header = True)
            df.to_csv(self.ingestion_config.test_data_path, index=False , header=True)

            logging.info("Data Ingestion Completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)