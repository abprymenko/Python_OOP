from logging import *
class Logger:
    def __init__(self, level:int, filename:str):
        basicConfig(level=level,
                    filename=filename,
                    filemode='a',
                    format='Logging message: %(asctime)s : %(levelname)s - %(message)s')
    def Log(self, level:int, message:str):
        if level == DEBUG:
            debug(message)
        elif level == INFO:
            info(message)
        elif level == WARNING:
            warning(message)
        elif level == ERROR:
            error(message)
        else:
            critical(message)