"""
Author: FaizalFeng fzx401@gmail.com
Date: 2024-02-04 20:01:23
LastEditors: FaizalFeng fzx401@gmail.com
LastEditTime: 2024-03-13 17:23:32
Copyright (c) 2024 by FaizalFeng, All Rights Reserved.
"""

from functools import partial


def speak(name: str):
    return f"hello, {name}"


print(partial(speak, "Tom")())
