class MyClass:
    def __init__(self, value) -> None:
        self._value = value

    @property
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
