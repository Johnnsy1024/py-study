from typing import Callable
from loguru import logger


def wrapper(func: Callable):
    def wrap_func(*args, **kwargs):
        logger.info("正在修饰函数")
        func(*args, **kwargs)
        logger.info("修饰完毕")

    return wrap_func


@wrapper
def test():
    print("success")


test()
