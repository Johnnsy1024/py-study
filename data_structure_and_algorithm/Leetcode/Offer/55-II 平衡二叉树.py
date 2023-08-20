# Definition for a binary tree node.

"""
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def cal_depth(root):
            if not root:
                return 0 
            return max(cal_depth(root.left), cal_depth(root.right)) + 1

        def judge(root):
            if not root:
                return True
            if not root.left and not root.right:
                return True
            left = cal_depth(root.left)
            right = cal_depth(root.right)
            if abs(left - right) <= 1:
                return True
            else:
                return False
        if not root:
            return True
        return judge(root) and self.isBalanced(root.left) and self.isBalanced(root.right)

tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

