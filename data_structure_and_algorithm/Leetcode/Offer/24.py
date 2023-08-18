"""
经典翻转链表：
维护pre指针指向None
令cur指向头节点
维护一个tmp指向cur的next
令cur.next指向pre
更新pre为cur
令cur指向tmp
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode):
        pre = None
        cur = head
        while cur:
            #  设置tmp的原因：cur节点的next指针即将与原本链表连接断开
            #  设置tmp只是为了保留cur的下个节点的信息
            tmp = cur.next  # 打断当前节点与next节点之间的连接
            cur.next = pre  # 翻转指针
            pre = cur  # 每当当前指针进入到新的链表中之后，就将其赋给pre指针（因此当cur为None的时候，pre指向的就是新链表的最后一个节点）
            #  以上三步为一块
            cur = tmp
        return pre




from DataStructures.generate_link_list import generate_link_list

l = generate_link_list([1, 2, 3, 4, 5])
s = Solution()
print(s.reverseList(l))
#  方法2：递归
class Solution2(Solution):
    def reverseList(self, head: ListNode):
        if not head or not head.next:
            return head
        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newhead
l = generate_link_list([1, 2, 3, 4, 5])
s = Solution2()
res = s.reverseList(l)
print(s.reverseList(l))