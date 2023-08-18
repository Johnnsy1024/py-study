class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1, self.stack2 = [], []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        if not self.stack2 or self.stack2[-1] >= x:
            self.stack2.append(x)

    def pop(self) -> None:
        if self.stack1.pop() == self.stack2[-1]:
            self.stack2.pop()

    def top(self) -> int:
        return self.stack1[-1]

    def min(self) -> int:
        if not self.stack2:
            return []
        return self.stack2[-1]


stack = MinStack()
stack.push(0)
stack.push(1)
stack.push(0)
print('stack\'s min', stack.min())
stack.pop()
print('stack\'s min', stack.min())