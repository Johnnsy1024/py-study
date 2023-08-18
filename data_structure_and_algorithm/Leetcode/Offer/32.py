from typing import List
from collections import deque


class Solution:

    def levelOrder(self, root):
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)

        while q:
            tmp_node = q.popleft()
            res.append(tmp_node.val)
            if tmp_node.left:
                q.append(tmp_node.left)
            if tmp_node.right:
                q.append(tmp_node.right)
        return res

