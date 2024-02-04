from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 广度优先
    def maxDepth1(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return 0
        q = deque()
        q.append(root)
        depth = 0
        while q:
            for i in range(len(q)):
                cur_node = q.popleft()
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            depth += 1
            
        return depth
    # 深度优先&递归
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_len = self.maxDepth(root.left)
        right_len = self.maxDepth(root.right)

        return 1 + max(left_len, right_len)