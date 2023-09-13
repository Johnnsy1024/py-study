import logging.config
import os
from datetime import datetime
import json
import sys
from pydantic import BaseModel, StrictStr

class LoggerConfig(BaseModel):
    
    log_conf_dir: StrictStr
    log_file_dir: StrictStr='log_file'
    
    def read_log_config(self, log_conf_dir: str) -> dict:
        with open(log_conf_dir, 'r') as f:
            log_conf = json.load(f)
        return log_conf


    def save_log_dir(self) -> str:
        cur_dir = os.path.dirname(__file__)
        log_file_path = os.path.join(cur_dir, log_file_dir)

        return log_file_path


if __name__ == '__main__':
    os.chdir(sys.path[0])
    log_file_name = f"Log {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.log"
    log_conf_dir = os.path.join(os.path.dirname(__file__), )
    logger_config = LoggerConfig()
    
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
