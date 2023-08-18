import logging

# 实例化一个Logger
logger = logging.getLogger('my_logger')

# 设定日志输出等级
logger.setLevel(logging.DEBUG)

# 设定日志输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 实例化一个FileHandler，用于写入日志文件
file_handler = logging.FileHandler('test.log')
file_handler.setFormatter(formatter)

# 添加到Logger
logger.addHandler(file_handler)

# 输出日志
logger.debug('this is a debug message')
logger.info('this is an info message')
logger.warning('this is a warning message')
logger.critical('fuck')
logger.info('我来试一试 ')
