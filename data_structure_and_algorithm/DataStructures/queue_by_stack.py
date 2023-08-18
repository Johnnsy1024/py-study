"""
用容量大小不同的两个栈来构建队列，两个栈的容量大小若分别为m和n（m>n），则队列的最大容量为2n+1
原因：出队栈的容量为n，而执行将入队栈的元素全部转移到出队栈中时，可以pop一次，所以两个栈在同一时刻最多保持该状态：
入队栈为n+1个元素（为出队操作做准备） 出队栈为n个元素（受容量所限）
"""

class QueueUsingStack:
    def __init__(self):
        self.stack_in = [] # 代表队列中现有的元素
        self.stack_out = []
    
    def enqueue(self, item):
        self.stack_in.append(item)
    
    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            return None
        
        return self.stack_out.pop()
    
    @property
    def is_empty(self):
        return len(self.stack_in) == 0 and len(self.stack_out) == 0
    
    def size(self):
        return len(self.stack_in) + len(self.stack_out)
            
        