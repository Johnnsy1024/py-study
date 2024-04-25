# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional
# 递归
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def recur(l1, l2, cur):
            if not l1 and not l2:
                return
            if not l1 and l2:
                cur.next = l2
                return 
            if not l2 and l1:
                cur.next = l1
                return

            if l1.val <= l2.val:
                cur.next = l1
                cur = cur.next
                recur(l1.next, l2, cur)
            else:
                cur.next = l2
                cur = cur.next
                recur(l1, l2.next, cur)

        if not list1 and not list2:
            return
        if not list1:
            return list2
        if not list2:
            return list1
        tmp = ListNode(-1)
        cur = tmp
        recur(list1, list2, cur)
        return tmp.next
    
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

# 迭代
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return 
        if not list1:
            return list2
        if not list2:
            return list1
        tmp = ListNode(-1)
        cur = tmp
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            else:
                cur.next = list2
                cur = cur.next
                list2 = list2.next
        
        while list1:
            cur.next = list1
            cur = cur.next
            list1 = list1.next
        while list2:
            cur.next = list2
            cur = cur.next
            list2 = list2.next
        return tmp.next
    
s = Solution()
s.mergeTwoLists(l1, l2)