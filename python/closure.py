"""
Author: FaizalFeng fzx401@gmail.com
Date: 2024-02-04 20:01:23
LastEditors: FaizalFeng fzx401@gmail.com
LastEditTime: 2024-03-13 18:11:45
Copyright (c) 2024 by FaizalFeng, All Rights Reserved.
"""

"""
Author: FaizalFeng fzx401@gmail.com
Date: 2024-02-04 20:01:23
LastEditors: FaizalFeng fzx401@gmail.com
LastEditTime: 2024-03-08 15:19:01
Copyright (c) 2024 by FaizalFeng, All Rights Reserved.
"""


def wrapper_1(n):
    def inner_func():
        nonlocal n
        n -= 1
        return n

    return inner_func


def wrapper_2(n):
    cnt = 0

    def inner():
        nonlocal cnt  # 使用nonlocal修饰嵌套作用域变量，可以在外部函数执行结束后继续使用
        for i in range(n):
            if i % 2 == 0:
                cnt += 1
        return cnt

    return inner


def outer():
    a = 3

    def inner():
        nonlocal a
        a = a - 3

    return a


if __name__ == "__main__":
    wrapper1_inner_func = wrapper_1(5)
    print(wrapper1_inner_func())

    # wrapper_2_inner_func = wrapper_2(7)
    # print(wrapper_2_inner_func())
    # print(wrapper_2_inner_func())
    # print(wrapper_2_inner_func())
# s = wrapper(100)
# print(s())
# print(s())
# print(s())
# print(s())
