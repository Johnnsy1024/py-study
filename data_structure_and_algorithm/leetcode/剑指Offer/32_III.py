import collections

from pythonds.trees.binaryTree import BinaryTree

b = BinaryTree(3)
b.insertLeft(9)
b.insertRight(20)
b.getRightChild().insertLeft(15)
b.getRightChild().insertRight(7)
class Solution:
    def levelOrder(self, root):
        if not root: return []
        res, deque = [], collections.deque([root])
        while deque:
            tmp = collections.deque()
            for _ in range(len(deque)): # 这里的长度不会动态更新
                node = deque.popleft()
                if len(res) % 2: tmp.appendleft(node.val) # 偶数层 -> 队列头部
                else: tmp.append(node.val) # 奇数层 -> 队列尾部
                if node.getLeftChild(): deque.append(node.getLeftChild())
                if node.getRightChild(): deque.append(node.getRightChild())
            res.append(list(tmp))
        return res
if __name__ == "__main__":
    s = Solution()
    print(s.levelOrder(b))