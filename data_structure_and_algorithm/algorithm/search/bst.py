"""
二叉搜索树
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        pass

    def bstify(self, arr, start, end):
        if start > end:
            return None
        mid = start + (end - start) // 2
        node = Node(arr[mid])  # 二叉搜索树的重点为建立一个中间节点和其左右两侧节点
        node.left = self.bstify(arr, start, mid - 1)
        node.right = self.bstify(arr, mid + 1, end)
        return node

    def insert(self, value, t):
        if not t:
            return Node(value)
        if value == t.data:
            raise RuntimeError("该二叉搜索树中已有该值！")
        elif value > t.data:
            t.right = self.insert(value, t.right)
        else:
            t.left = self.insert(value, t.left)
        return t
        # while t:
        #     if value == t.data:
        #         raise RuntimeError("该二叉搜索树中已有该值！")
        #     elif value > t.data and not t.right:
        #         t.right = Node(value)
        #         break
        #     elif value > t.data and t.right:
        #         t = t.right
        #     elif value < t.data and not t.left:
        #         t.left = Node(value)
        #         break
        #     elif value < t.data and t.left:
        #         t = t.left
        # return t

    def find(self, value, t: Node):
        while t:
            if value > t.data:
                t = t.right
            elif value < t.data:
                t = t.left
            else:
                return True
        return False

    def findmin(self, t: Node):
        while t.left:
            t = t.left
        return t

    def delete(self, value, t: Node):
        if not t:
            return t
        if value > t.data:
            #  如果要删除的值大于当前根节点，那么照着根节点一路删下去
            #  当前根节点的右孩子为删除之后的子树的根节点
            #  至于是怎么删的，具体就不用管了
            t.right = self.delete(value, t.right)
        elif value < t.data:
            #  同上
            t.left = self.delete(value, t.left)
        else:
            if not t.left:
                return t.right
            if not t.right:
                return t.left
            #  当前节点有左子树和右子树
            #  选择右子树中的最小值节点或左子树中的最大值节点来代替要删除的节点
            min_node = self.findmin(t.right)
            t.data = min_node.data
            t.right = self.delete(min_node.data, t.right)
        return t


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bst = BST()
tree = bst.bstify(nums, 0, len(nums) - 1)
# print(bst.findmin(tree).data)
# print(bst.find(12, tree))
# new_tree = bst.insert(7, tree)
# bst.delete(7, tree)
print(bst.find(7, tree))
# 在arr中查找target是否存在
