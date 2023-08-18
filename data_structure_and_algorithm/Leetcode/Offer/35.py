class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        new_node_map = {}
        cur = head
        while cur:
            # 以一个哈希表来存储原链表节点和新链表节点
            new_node_map[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            new_node_map[cur].next = new_node_map.get(cur.next)
            new_node_map[cur].random = new_node_map.get(cur.random)
            cur = cur.next
        return new_node_map[head]

