# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_path(root, node, res: list = []):
            if not root:
                return []
            if node.val < root.val:
                res.append(root)
                return find_path(root.left, node, res)
            if node.val > root.val:
                res.append(root)
                return find_path(root.right, node, res)
            if node.val == root.val:
                res.append(root)
                return res

        p_path = find_path(root, p, [])
        q_path = find_path(root, q, [])
        tmp = []
        for i, j in zip(p_path, q_path):
            if i == j:
                tmp.append(i)
        return tmp[-1]


t = TreeNode(6)
t.left = TreeNode(2)
t.right = TreeNode(8)
t.left.left = TreeNode(0)
t.left.right = TreeNode(4)
t.left.right.left = TreeNode(3)
t.left.right.right = TreeNode(5)
t.right.left = TreeNode(7)
t.right.right = TreeNode(9)
s = Solution()
p = TreeNode(2)
q = TreeNode(4)
print(s.lowestCommonAncestor(t, p, q).val)
