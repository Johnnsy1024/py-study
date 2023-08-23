from typing import Union
from binarySearchTree import *
from pydantic import BaseModel, StrictFloat, StrictInt
from collections import deque

class AVLTree(BinarySearchTree, BaseModel):

    val : Union[StrictInt, StrictFloat] = None
    
    def insert(self, root : "AVLTree", value: Union[int, float], is_root: bool=True) -> None:
        if root.val:
            if value < root.val:
                if root.left is None:
                    root.left = AVLTree(val=value)
                else:
                    root.left.insert(root.left, value, is_root=False)
            elif value > root.val:
                if root.right is None:
                    root.right = AVLTree(val=value)
                else:
                    root.right.insert(root.right, value, is_root=False)
            # 判断插入新节点后的二叉树是否还是AVL树，根据情况进行旋转
            if is_root:
                q = deque([root])
                while q:
                    cur = q.popleft()
                    self.avg_adjust(cur)
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
        else:
            root.val = value
    
    def height(self, node : "AVLTree") -> int:
        if not node:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1
    
    def balance_factor(self, node : "AVLTree") -> int:
        """返回当前node节点的左右子树平衡因子

        Args:
            node (AVLTree): 当前树根节点

        Returns:
            整数: 当前根节点左右子树高度之差
        """
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def avg_adjust(self, node : "AVLTree") -> None:
        if not node:
            raise ValueError("该根节点为空！")
        # 左侧较重
        if self.balance_factor(node) > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.left_rotate(node.left)
            self.right_rotate(node) 
        # 右侧较重
        if self.balance_factor(node) < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.right_rotate(node.right)
            self.left_rotate(node)
    
    @property
    def is_avg(self) -> bool:
        if not self:
            return True
        left_height = self.height(node=self)
        right_height = self.height(node=self)
        if abs(self.balance_factor(self)) <= 1:
            if self.left and self.right:
                return self.left.is_avg and self.right.is_avg
            else:
                return True            
        else:
            return False
    
    def left_rotate(self, node : "AVLTree") -> "AVLTree":
        new_node = AVLTree(val=node.val)
        new_node.left = node.left
        new_node.right = node.right.left
        node.val = node.right.val
        node.right = node.right.right
        node.left = new_node
        return node
    
    def right_rotate(self, node : "AVLTree") -> "AVLTree":
        new_node = AVLTree(val=node.val)
        new_node.left = node.left.right
        new_node.right = node.right
        node.val = node.left.val
        node.right = new_node
        node.left = node.left.left
        return node
        
if __name__ == "__main__":
    import random  
    random.seed(2)

    tree = AVLTree()
    for i in range(1000):
        tree.insert(root=tree, value=i)
    print(tree.is_avg)