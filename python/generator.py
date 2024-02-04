"""
以下两种生成1、2、3的生成器方式相同
"""


def generator_1():
    n = 1
    while n < 4:
        yield n
        n += 1


def generator_2():
    yield 1
    yield 2
    yield 3


if __name__ == "__main__":
    #! 混合使用next和循环
    g = generator_1()
    for i in g:
        print(next(g))
