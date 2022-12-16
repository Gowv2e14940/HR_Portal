import logging
import os
import pathlib


class Log():
    @staticmethod
    def logCreate():
        path1 = pathlib.Path().absolute()
        print("path is", path1)
        path2 = os.path.join(path1, "Logs", "hrportal.log")
        print("path2 is", path2)
        logging.basicConfig(filename="hrportal.log",format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger