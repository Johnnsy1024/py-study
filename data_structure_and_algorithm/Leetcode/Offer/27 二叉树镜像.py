# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        # 交换左右子树
        root.left, root.right = root.right, root.left
        
        # 递归处理左右子树
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        
        return root