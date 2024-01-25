# Definition for a binary tree node.
import unittest
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inOrderRecursive(self, root: Optional[TreeNode], arr: List[int]):
        if root is None:
            return
        self.inOrderRecursive(root.left, arr)
        arr.append(root.val)
        self.inOrderRecursive(root.right, arr)

    def inOrderIterative(self, root: Optional[TreeNode], arr: List[int]):
        stack = []
        if root is not None:
            stack.append(root)
        while stack:
            r = stack.pop()
            if type(r) == int:
                arr.append(r)
            else:
                if r.right:
                    stack.append(r.right)
                if r.val:
                    stack.append(r.val)
                if r.left:
                    stack.append(r.left)

    def inOrderTraversal(self, root: Optional[TreeNode], recursive = True) -> List[int]:
        nodes_arr = []
        if recursive:
            self.inOrderRecursive(root, nodes_arr)
        else:
            self.inOrderIterative(root, nodes_arr)
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

    def test_inOrderTraversal(self):
        # Test the inOrderTraversal function
        result = self.solution.inOrderTraversal(self.root)
        self.assertEqual(result, [4, 2, 5, 1, 3])
        result = self.solution.inOrderTraversal(self.root, recursive=False)
        self.assertEqual(result, [4, 2, 5, 1, 3])

if __name__ == '__main__':
    unittest.main()