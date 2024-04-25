# 自定义类迭代器,手动实现__iter__和__next__方法
class Iterator:
    def __init__(self, custom_list: list) -> None:
        self.custom_list = custom_list
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            x = self.custom_list[self.idx]
        except IndexError:
            raise StopIteration
        self.idx += 1
        return x


if __name__ == "__main__":
    test_iterator = iter([1, 2, 3, 4])
    print(next(test_iterator))
    print(next(test_iterator))
    print(next(test_iterator))
    print(next(test_iterator))
    print(next(test_iterator))
