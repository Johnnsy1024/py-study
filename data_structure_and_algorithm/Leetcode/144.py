# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        # 这里是函数嵌套，只有外层函数return内层函数，且内层函数用到了外层函数的local variable时才是闭包
        def dfs(node):
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res
class Solution:
    def preorderTraversal(self, root):
        if not root:
            return 
        print(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        # def dfs(node):
        #     if not node:
        #         return
        #     res.append(node.val)
        #     dfs(node.left)
        #     dfs(node.right)
        # dfs(root)
        # return res