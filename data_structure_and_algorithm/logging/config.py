import logging.config
import os
from datetime import datetime
import json


#
# with open('log_config.json', 'r') as f:
#     log_config = json.load(f)
tmp = os.path.join(os.path.abspath(__file__))
log_file_name = f"Log {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.log"
# log_config['handlers']['file_handler']['filename'] = log_file_name

logging.config.dictConfig(log_config)

# # 现在您可以在代码中使用日志记录
logger = logging.getLogger()
logger.debug("这是调试信息")
logger.info("这是信息日志")
logger.warning("这是警告信息")
logger.error("这是错误信息")
logger.critical("这是严重错误信息")
