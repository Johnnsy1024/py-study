from logging import StreamHandler, FileHandler
import logging
import datetime

# 通过logging.getLogger先新建一个logger
logger = logging.getLogger(__name__)
# 新建一个StreamHandler，StreamHandler
stream_handler = StreamHandler()
stream_handler.setLevel(logging.WARNING)

logger.addHandler(stream_handler)

file_handler = FileHandler(f"LogInfo {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.log")
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)

logger.warning('this is a debug test')
logger.error('this is an error test')