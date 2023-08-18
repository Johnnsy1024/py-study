"""
删除链表节点
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def delete_node(self, head: ListNode, val: int) -> ListNode:
        #  判断head是否为要删除的节点
        if head.val == val:
            head = head.next
            print('The node has been deleted!')
            return head
        #  维护一个指针指向头节点
        cur = head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                print('The node has been deleted!')
                return head
            else:
                cur = cur.next
        print('No node to be deleted!')
        return -1

def generate_link_list(nums:list):
    i = 1
    cur = ListNode(nums[0])
    head = cur
    while i < len(nums):
        cur.next = ListNode(nums[i])
        # print('cur_before')
        # print(id(cur))
        # print('head_before')
        # print(id(head))
        cur = cur.next  # 在此时cur已经变成了一个新变量
        # print('cur_after')
        # print(id(cur))
        # print('head_after')
        # print(id(head))
        i += 1
    return head

l1 = generate_link_list([4, 5, 1, 9])
val = 1
s = Solution()
s.delete_node(l1, val)