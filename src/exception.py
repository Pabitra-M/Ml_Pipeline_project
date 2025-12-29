import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    return (
        f"Error occurred in script: {file_name} "
        f"at line number: {line_number} | "
        f"Error message: {error}"
    )


class CustomException(Exception):
    def __init__(self, error, error_details: sys):
        self.error_message = error_message_detail(error, error_details)
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message



if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.error("Division by zero error", exc_info=True)
        raise CustomException(e, sys)