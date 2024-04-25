"""
Author: FaizalFeng fzx401@gmail.com
Date: 2024-02-04 20:01:23
LastEditors: FaizalFeng fzx401@gmail.com
LastEditTime: 2024-03-13 18:04:21
Copyright (c) 2024 by FaizalFeng, All Rights Reserved.
"""


# 单例实现
class Players:
    # 类属性既可以通过cls.xxx访问，也可以通过self.xxx访问
    # 上述访问方式在类作用域范围外也是一样的,例如:
    # Players.xxx
    # player = Players()
    # player.xxx
    _instance = None

    def __new__(cls, val: int) -> Self:
        # 内存中分配空间给当前类的实例
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

        # 调用基类object的构造器,传入当前类cls,返回构造好的当前类的实例

    def __init__(self, val: int) -> None:
        self.val = val


if __name__ == "__main__":
    player1 = Players(3)
    player2 = Players(3)
    pass
