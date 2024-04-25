from typing import Literal


class CustomError(Exception):
    def __init__(
        self, message_1: str = "Custom error occurred", message_2: str = "test"
    ) -> None:
        self.message_1 = message_1
        self.message_2 = message_2
        super().__init__(self.message_1, self.message_2)


def custom_func(val: int) -> Literal[0]:
    if val < 0:
        raise CustomError()
    return 0


if __name__ == "__main__":
    custom_func(-1)
