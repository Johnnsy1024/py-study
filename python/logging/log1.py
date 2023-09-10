import logging
import datetime
import numpy as np


def logging_test(filename: str, level: logging):
    """测试日志记录

    Args:
        filename (str): 设置日志文件名
        :param level:
    """
    # level代表
    logging.basicConfig(filename=filename,
                        level=level, format='%(process)d %(asctime)s %(levelname)s %(name)s %(message)s')
    logging.debug('this is a bug')
    logging.warning('this is a warning')
    logging.info('this is an info')

fn = f"LogInfo {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.log"
lv = logging.DEBUG
logging_test(fn, lv)
