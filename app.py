import sys
sys.path.append(r"D:\Practice Machine Learning")
from src.ml_project.logger import logging
from src.ml_project.exception import CustomException

if __name__ == "__main__":
    logging.info("Testing Logging")
    
    try:
        a = 1/0
    except Exception as e:
        logging.info("Custom Exception Testing")
        raise CustomException(e,sys)