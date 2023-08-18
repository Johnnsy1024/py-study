"""
从尾到头打印链表
"""
from typing import List
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []
        return self.reversePrint(head.next) + [head.val]