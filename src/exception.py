import sys


def error_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    error_message = f"Error occurred in script: {file_name} at line number: {line_no} error message: {str(error)}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_messsage, error_detail:sys):
        super().init__(error_messsage)
        self.error_message = error_detail(error_messsage, error_detail=error_detail)

    def __str__(self):
        return self.error_message