from magic_method import Players


# 函数装饰器实现单例
def singleton(cls):
    # 以类为传入参数,并用字典存储类的实例
    _instance = {}

    def inner():
        # 如果没有创建过当前传入类的实例，则对该类进行实例化
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]

    return inner


class Singleton:
    def __init__(self) -> None:
        pass


# __new__()方法实现单例


player1 = Players(3)
player2 = Players(4)
print(id(player1) == id(player2))
