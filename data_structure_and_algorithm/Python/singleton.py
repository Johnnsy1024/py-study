class Singleton:
    __instance = None

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("该类已经有一个实例存在！")
        else:
            Singleton.__instance = self

# 使用单例模式创建对象
obj1 = Singleton.get_instance()
obj2 = Singleton.get_instance()
print(obj1 is obj2)  # 输出: True

def singleton(cls):
    _instance = {}

    def _singleton_wrapper(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return _singleton_wrapper

@singleton
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
s1 = Student('xiaoming', 12)
s2 = Student('xiaohong', 14)
print(s1)
print(s2)
print(s1.name)
print(s1.age)
print(s2.name)
print(s2.age)