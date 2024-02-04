# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder and not postorder:
            return None
        
        root_val = postorder[-1]
        root = TreeNode(root_val)
        idx = inorder.index(root_val)
        inorder_left = inorder[:idx]
        inorder_right = inorder[idx+1:]
        postorder_left = postorder[:idx]
        postorder_right = postorder[idx:-1]

        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root
    
s = Solution()
res = s.buildTree([9,3,15,20,7], [9,15,7,20,3])
print(res)