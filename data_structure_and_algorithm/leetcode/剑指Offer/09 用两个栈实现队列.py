class CQueue:

    def __init__(self):
        # stack1为主栈，stack2为副栈，主栈存储队列数值，副栈作为删除头部元素时的中转空间
        self.stack1 = []
        self.stack2 = []
    def appendTail(self, value: int) -> None:
        self.stack1.append(value)
    def deleteHead(self) -> int:
        """
        每次删除完head之后都要恢复stack1
        :return:
        """
        if not self.stack1:
            return -1
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        res = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        #  把stack1中的元素按规则压入stack2中
        return res

o = CQueue()
o.deleteHead()
o.appendTail(5)
o.appendTail(2)
print(o.deleteHead())
print(o.deleteHead())