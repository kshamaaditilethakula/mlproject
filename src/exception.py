import sys
import logging

def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()  # Extract traceback information.
    file_name = exc_tb.tb_frame.f_code.co_filename  # File name where the error occurred.
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name, exc_tb.tb_lineno, str(error)
)
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)  # Initialize the base Exception with the original message.
        self.error_message = error_message_detail(error_message, error_detail=error_detail)  # Customize the error message with details.

    def __str__(self):
        return self.error_message  # When the exception is printed, it shows the detailed error message.

if __name__ =="__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Division by 0")
        raise CustomException(e,sys)