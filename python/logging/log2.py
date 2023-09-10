import logging
import datetime
from logging.handlers import RotatingFileHandler
import logging.config



logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(filename=f'Log {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.log')
file_handler.setLevel(logging.ERROR)

formatter = logging.Formatter("%(process)d %(asctime)s %(levelname)s %(name)s %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
for i in range(100, -100, -1):
    try:
        cal = 10/i
        logger.info(cal)
    except Exception as e:
        print(e)
        logger.error(f'Loop {i+1} failed')
    finally:
        logger.info(f'Loop {i+1} success!')
