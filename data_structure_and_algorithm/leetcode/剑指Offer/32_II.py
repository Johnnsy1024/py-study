from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        res, queue = [], deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        res = [[root.val]]
        q = deque()
        q.append(root)
        while q:
            tmp = []
            tmp_node = q.popleft()
            if tmp_node.left:
                q.append(tmp_node.left)
                tmp.append(tmp_node.left.val)
            if tmp_node.right:
                q.append(tmp_node.right)
                tmp.append(tmp_node.right.val)
            if tmp:
                res.append(tmp)
        return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)

s = Solution()
print(s.levelOrder(root))
