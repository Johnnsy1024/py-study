class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        cur = head
        dic = {}
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        return dic[head]


# The method of recursion
def copyRandomList(head: "Node") -> "Node":
    cache_dict = {}

    def find(h: "Node"):
        if not h:
            return
        if h in cache_dict:
            return cache_dict.get(h)
        root = Node(h.val)
        cache_dict[h] = root
        root.next = find(h.next)
        root.random = find(h.random)
        return root

    return find(head)


if __name__ == '__main__':
    ll = Node(7)
    ll.next = Node(13)
    ll.random = None
    ll.next.next = Node(11)
    ll.next.random = ll
    res = copyRandomList(ll)
    pass
