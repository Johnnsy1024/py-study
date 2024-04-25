"""
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。


"""

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.check(root, root)

    def check(self, root1, root2):
        q = deque()
        q.append(root1)
        q.append(root2)
        # 初始队列中放进了两个节点，因此之后队列中出现的都是偶数个元素
        # 不会出现popleft之后再pop出现Node has no pop() method的错误
        while q:
            node1 = q.popleft()
            node2 = q.pop()
            if not node1 and not node2:
                continue
            if (not node1 and node2) or (node1 and not node2) or \
            (node1.val != node2.val):
                return False
            q.appendleft(node1.right)
            q.appendleft(node1.left)
            q.append(node2.left)
            q.append(node2.right)
        return True