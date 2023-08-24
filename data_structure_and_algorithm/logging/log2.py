import logging
import datetime


logger = logging.getLogger('Loop Record')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(filename=f'Log {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.log')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(process)d %(asctime)s %(levelname)s %(name)s %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
for i in range(1000, -1000, -1):
    try:
        cal = 10/i
    except Exception as e:
        print(e)
        logger.info('failed')
    finally:
        logging.info(f'Loop {i+1} success!')
