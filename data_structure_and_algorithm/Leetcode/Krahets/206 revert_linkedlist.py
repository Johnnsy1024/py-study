"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return []
        prev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev


s = Solution()
t = ListNode(1)
t.next = ListNode(2)
t.next.next = ListNode(3)
t.next.next.next = ListNode(4)
t.next.next.next.next = ListNode(5)
s.reverseList(t)
