# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA:
            return
        if not headB:
            return
        cur = headA
        length_A = 1
        while cur.next:
            cur = cur.next
            length_A += 1
        cur = headB
        length_B = 1
        while cur.next:
            cur = cur.next
            length_B += 1
        skip = abs(length_A - length_B)

        if skip == 0:
            while headA != headB:
                headA = headA.next
                headB = headB.next
            return headA

        if length_A < length_B:
            pb = 0
            while pb < skip:
                headB = headB.next
                pb += 1
            while headA != headB:
                headA = headA.next
                headB = headB.next
            return headA
        else:
            pa = 0
            while pa < skip:
                headA = headA.next
                pa += 1
            while headA != headB:
                headA = headA.next
                headB = headB.next
            return headA
