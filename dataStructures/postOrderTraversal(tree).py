# Definition for a binary tree node.
import unittest
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postOrderRecursive(self, root: Optional[TreeNode], arr: List[int]):
        if root is None:
            return
        self.postOrderRecursive(root.left, arr)
        self.postOrderRecursive(root.right, arr)
        arr.append(root.val)

    def postOrderIterative(self, root: Optional[TreeNode], arr: List[int]):
        stack = []
        if root is not None:
            stack.append(root)
        while stack:
            r = stack.pop()
            if type(r) == int:
                arr.append(r)
            else:
                if r.val:
                    stack.append(r.val)
                if r.right:
                    stack.append(r.right)
                if r.left:
                    stack.append(r.left)

    def postOrderTraversal(self, root: Optional[TreeNode], recursive = True) -> List[int]:
        nodes_arr = []
        if recursive:
            self.postOrderRecursive(root, nodes_arr)
        else:
            self.postOrderIterative(root, nodes_arr)
        return nodes_arr
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        # Create a sample tree for testing
        #       1
        #      / \
        #     2   3
        #    / \
        #   4   5
        self.root = TreeNode(1)
        self.root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        self.root.right = TreeNode(3)

        # Instantiate the Solution class
        self.solution = Solution()

    def test_postOrderTraversal(self):
        # Test the postOrderTraversal function
        result = self.solution.postOrderTraversal(self.root)
        self.assertEqual(result, [4, 5, 2, 3, 1])
        result = self.solution.postOrderTraversal(self.root, recursive=False)
        self.assertEqual(result, [4, 5, 2, 3, 1])

if __name__ == '__main__':
    unittest.main()