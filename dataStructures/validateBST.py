from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # R1 get the inorder elements and compare them
        # R2 check if max(root.left) < root.val and root.val < min(root.right) 

        # R1
        # def inorderArray(root, arr):
        #     if not root:
        #         return
        #     inorderArray(root.left, arr)
        #     arr.append(root.val)
        #     inorderArray(root.right, arr)
        
        # arr_inorder = []
        # inorderArray(root, arr_inorder)
        # print(arr_inorder)

        # previous_n = None
        # for n in arr_inorder:
        #     if previous_n is not None and previous_n >= n:
        #         return False
        #     previous_n = n
        # return True

        # R2
        if not root:
            return True
        if not root.left and not root.right:
            return True
        
        left_validation = True
        right_validation = True
        if root.left:
            left_validation = root.val > root.left.val and self.isValidBST(root.left)
        if root.right:
            right_validation = root.val < root.right.val and self.isValidBST(root.right)
        
        return left_validation and right_validation