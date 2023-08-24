import logging

# 直接在当前模块下运行，该__name__为__main__
# 其他模块调用该模块时，该__name__为当前模块名"logger"
# 注意：使用logging.getLogger()方法，__name__相同的情况下，返回的logger是同一个
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO) # logger的level由低到高分为DEBUG、INFO、WARNING、ERROR、CRITICAL五类

# getLogger中要传入的名字参数中间用"."来表示
p = logging.getLogger('log1')
p.setLevel(logging.WARNING)
p1 = logging.getLogger('log1.c1')
pass
