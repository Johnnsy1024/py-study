"""
Author: FaizalFeng fzx401@gmail.com
Date: 2024-02-04 20:01:23
LastEditors: FaizalFeng fzx401@gmail.com
LastEditTime: 2024-03-13 18:03:53
Copyright (c) 2024 by FaizalFeng, All Rights Reserved.
"""


class MyClass:
    def __init__(self, value) -> None:
        self._value = value

    @property  # 默认已实现value.getter
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError("Value must not be negetive")
        self._value = new_value


if __name__ == "__main__":
    my_class = MyClass(10)
    my_class.value = 1
