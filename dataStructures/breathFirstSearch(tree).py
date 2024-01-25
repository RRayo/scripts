# Definition for a binary tree node.
import unittest
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def breathFirstIterative(self, root: Optional[TreeNode], arr: List[int]):
        if root is None:
            return []

        stack = [root]

        while stack:
            level_nodes = []
            next_level_stack = []

            for node in stack:
                if node:
                    level_nodes.append(node.val)
                    if node.left:
                        next_level_stack.append(node.left)
                    if node.right:
                        next_level_stack.append(node.right)

            if level_nodes:
                arr.append(level_nodes)

            stack = next_level_stack


    def levelOrder(self, root: Optional[TreeNode]) -> List[int]:
        nodes_arr = []
        self.breathFirstIterative(root, nodes_arr)
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

        #       1
        #      / \
        #     2   3
        #    /     \
        #   4       5
        self.root2 = TreeNode(1)
        self.root2.left = TreeNode(2, TreeNode(4), None)
        self.root2.right = TreeNode(3, None, TreeNode(5))

        # Instantiate the Solution class
        self.solution = Solution()

    def test_levelOrder(self):
        # Test the levelOrder function
        result = self.solution.levelOrder(self.root)
        self.assertEqual(result, [[1], [2,3], [4,5]])

        result = self.solution.levelOrder(self.root2)
        self.assertEqual(result, [[1], [2,3], [4,5]])

        

if __name__ == '__main__':
    unittest.main()