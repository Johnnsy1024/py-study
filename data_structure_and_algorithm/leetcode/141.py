# Definition for singly-linked list.
"""
判断环形链表
"""
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            # 如果链表有环的话，指针的next应该永远不会为None
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True
