import sys
import logging

def error_message_details(error,error_detail:sys):
    _,_,exe_tb=error_detail.exc_info() # which file and which line the error has occured
    file_name=exe_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in Python Script name [{0}] Line No. [{1}] Error Message [{2}]".format(file_name, exe_tb.tb_lineno, str(error))
    #f"Error occured in python script name [{file_name}] line number [{exe_tb.tb_lineno}] error message[{str(error)}]"

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(self,error_message)
        self.error_message=error_message_details(error_message,error_detail=error_detail)

    def __str__(self):  # __str__ is to print() the value

        return self.error_message


if __name__ == "__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e,sys)
    
    #python3.8 src/exception.py

