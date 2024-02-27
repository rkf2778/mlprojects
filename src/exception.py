import sys
from src.logger import logging

# Configure logging to display INFO level messages
logging.basicConfig(level=logging.INFO)

def error_message_detail(error, error_details):
    _, _, exc_tb = error_details.exc_info()  # Use traceback.exc_info() directly
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    
    return error_message
    
class CustomerException(Exception):
    def __init__(self, error_message, error_details):
        Exception.__init__(self, error_message)  # Correct call to the base class constructor
        self.error_message = error_message_detail(error_message, error_details)
        
    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Div by zero")
        raise CustomerException(e, sys)
