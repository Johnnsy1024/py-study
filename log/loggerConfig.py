
import logging.config
import os
from datetime import datetime
import json
import sys
from pydantic import BaseModel, StrictStr

class LoggerConfig(BaseModel):
    """一个读取Logger配置类

    Args:
        BaseModel (强制类型约束): pydantic标准父类
        log_conf_dir：日志配置文件目录
        log_file_dir：日志文件输出目录
    Returns:
        _type_: _description_
    """
    log_conf_dir: StrictStr
    log_file_dir: StrictStr='log_file'
    
    def read_log_config(self) -> dict:
        with open(self.log_conf_dir, 'r') as f:
            log_conf = json.load(f)
        return log_conf


    def save_log_dir(self) -> str:
        cur_dir = os.path.dirname(__file__)
        log_file_path = os.path.join(cur_dir, self.log_file_dir)

        return log_file_path


if __name__ == '__main__':

    import sys
    os.chdir(sys.path[0])
    log_file_name = f"Log {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.log"
    log_conf_dir = os.path.join(os.path.dirname(__file__), 'log_config/log_config.json')

    logger_config = LoggerConfig(log_conf_dir=log_conf_dir)
    log_file_dir = os.path.join(logger_config.save_log_dir(), log_file_name)
    
    log_config = logger_config.read_log_config()

    # 手动定义输出到文件的日志目录
    log_config['handlers']['file_handler']['filename'] = log_file_dir
    log_config['handlers']['file_handler']['level'] = logging.CRITICAL
    # set relative log configuraion
    logging.config.dictConfig(log_config)

    logger = logging.getLogger()
    logger.debug("这是调试信息")
    logger.info("这是信息日志")
    logger.warning("这是警告信息")
    logger.error("这是错误信息")
    logger.critical("这是严重错误信息")


