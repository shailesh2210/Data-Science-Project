import sys
sys.path.append(r"D:\Practice Machine Learning")
from src.ml_project.logger import logging

def error_message_detail(error, error_details:sys):
    _,_, exec_tb = error_details.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    error_message = "Error Occured in Python script name [{0}] line_number [{1}] error_message [{2}]".format(
        file_name , exec_tb.tb_lineno , str(error))
    
    return error_message

class CustomException(Exception):
    def __init__(self , error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message , error_details)

    def __str__(self):
        return self.error_message