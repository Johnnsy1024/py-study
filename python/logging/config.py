import logging.config
import os
from datetime import datetime
import json


def read_log_config(log_conf_dir: str) -> dict:
    with open(log_conf_dir, 'r') as f:
        log_conf = json.load(f)
    return log_conf


def save_log_dir() -> str:
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    log_file_path = os.path.join(cur_dir, 'log_file')

    return log_file_path


if __name__ == '__main__':
    log_file_name = f"Log {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.log"
    log_file_dir = os.path.join(save_log_dir(), log_file_name)
    log_config = read_log_config('log_config/log_config.json')
    # Dynamically assign log file name with datetime
    log_config['handlers']['file_handler']['filename'] = log_file_dir
    # set relative log configuraion
    logging.config.dictConfig(log_config)

    logger = logging.getLogger()
    logger.debug("这是调试信息")
    logger.info("这是信息日志")
    logger.warning("这是警告信息")
    logger.error("这是错误信息")
    logger.critical("这是严重错误信息")
