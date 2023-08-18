class CQueue:

    def __init__(self):
        self.stack1, self.stack2 = [], []
    def _exchange(self, stack1: list, stack2: list) -> None:
        """
        将stack1的元素依次pop出去压入stack2中
        :param stack1:
        :param stack2:
        :return:
        """
        while stack1:
            tmp = stack1.pop()
            stack2.append(tmp)
    def appendTail(self, value: int) -> None:
        if self.stack1:
            self.stack1.append(value)
        else:
            self._exchange(self.stack2, self.stack1)
            self.stack1.append(value)


    def deleteHead(self) -> int:
        """
        每次删除完head之后都要恢复stack1
        :return:
        """
        if not self.stack1:
            return -1
        #  把stack1中的元素按规则压入stack2中
        self._exchange(self.stack1, self.stack2)
        #  弹出stack2栈尾元素
        res = self.stack2.pop()
        if self.stack2:
            self._exchange(self.stack2, self.stack1)
        return res

o = CQueue()
o.deleteHead()
o.appendTail(5)
o.appendTail(2)
o.deleteHead()
o.deleteHead()