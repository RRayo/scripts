# Definition for a binary tree node.
import unittest
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preOrderRecursive(self, root: Optional[TreeNode], arr: List[int]):
        if root is None:
            return
        arr.append(root.val)
        self.preOrderRecursive(root.left, arr)
        self.preOrderRecursive(root.right, arr)

    def preOrderIterative(self, root: Optional[TreeNode], arr: List[int]):
        stack = []
        if root is not None:
            stack.append(root)
        while stack:
            r = stack.pop()
            arr.append(r.val)
            if r.right:
                stack.append(r.right)
            if r.left:
                stack.append(r.left)

    def preorderTraversal(self, root: Optional[TreeNode], recursive = True) -> List[int]:
        nodes_arr = []
        if recursive:
            self.preOrderRecursive(root, nodes_arr)
        else:
            self.preOrderIterative(root, nodes_arr)
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

    def test_preorderTraversal(self):
        # Test the preorderTraversal function
        result = self.solution.preorderTraversal(self.root)
        self.assertEqual(result, [1, 2, 4, 5, 3])
        result = self.solution.preorderTraversal(self.root, recursive=False)
        self.assertEqual(result, [1, 2, 4, 5, 3])

if __name__ == '__main__':
    unittest.main()