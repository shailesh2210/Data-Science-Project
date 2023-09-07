import os
import sys
sys.path.append(r"D:\Practice Machine Learning")
from src.ml_project.exception import CustomException
from src.ml_project.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

def read_sql_data():
    logging.info("Reading sql database started!!")
    try:
        mydb = pymysql.connect(host=host , user=user , password=password, db=db)
        logging.info("Connection Established", mydb)

        df = pd.read_sql_query("Select * from students", mydb)
        print(df.head())

        return df

    except Exception as e:
        raise CustomException(e,sys)