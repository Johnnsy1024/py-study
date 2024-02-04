class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A: TreeNode, B: TreeNode):
            if not B:
                return True
            if not A or A.val != B.val:
                return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        if not A or not B:
            return False
        from collections import deque
        q = deque([A])
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur.val == B.val:
                    if recur(cur, B):
                        return True
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return False