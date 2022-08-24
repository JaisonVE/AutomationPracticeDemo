import inspect
import logging


class LogGen:

    def loggen(loglevel=logging.DEBUG):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(loglevel)
        fh = logging.FileHandler("../Logs/automation.log")
        formatter1 = logging.Formatter('%(asctime)s - %(message)s')
        fh.setFormatter(formatter1)
        logger.addHandler(fh)
        return logger



