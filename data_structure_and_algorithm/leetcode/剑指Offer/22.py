from DataStructures.LinkedList.linkedList import Node, LinkList


class Solution:
    def getKthFromEnd(self, head: Node, k: int):
        slow = head
        fast = head
        while fast.next and k > 1:
            fast = fast.next
            k -= 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        return slow


if __name__ == '__main__':
    test_linklist = LinkList([1, 2, 3, 4, 5])
    s = Solution()
    res = s.getKthFromEnd(test_linklist.head, 1)
    pass
    print('si')
