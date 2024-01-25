from collections import deque
from typing import Optional
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def parse_tree_from_array(self, nodes):
        if not nodes:
            return None

        root = TreeNode(val=nodes[0])
        queue = deque([root])
        i = 1

        while queue and i < len(nodes):
            current_node = queue.popleft()

            # Parse left child
            if i < len(nodes) and nodes[i] is not None:
                current_node.left = TreeNode(val=nodes[i])
                queue.append(current_node.left)
            i += 1

            # Parse right child
            if i < len(nodes) and nodes[i] is not None:
                current_node.right = TreeNode(val=nodes[i])
                queue.append(current_node.right)
            i += 1

        return root
    
    def printTree(self, root):
        if not root:
            return
        self.printTree(root.left)
        print(root.val, end=" ")
        self.printTree(root.right)



class Solution:

    def mirrorTree(self, root: Optional[TreeNode]):
        if not root:
            return None
        return TreeNode(root.val, self.mirrorTree(root.right), self.mirrorTree(root.left))
    
    def isSymmetricRecursive(self, root: Optional[TreeNode]) -> bool:
        def check_symmetry(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            left_symmetry = check_symmetry(left.left, right.right)
            right_symetry = check_symmetry(left.right, right.left)
            return left.val == right.val and left_symmetry and right_symetry

        if not root:
            return True

        return check_symmetry(root.left, root.right)


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        # check if children nodes are the same
        # check if right of left children is same as left of right children
        # R2: invert right child and check if both sides are the same

        left_tree = root.left
        right_tree = root.right
        if not right_tree and not left_tree:
            return True
        if right_tree and not left_tree:
            return False
        if not right_tree and left_tree:
            return False
        mirrored_right_tree = self.mirrorTree(right_tree)

        queue_left = [left_tree]
        queue_mirror_right = [mirrored_right_tree]

        while queue_left and queue_mirror_right:
            if len(queue_left) != len(queue_mirror_right):
                return False
            node_left = queue_left.pop()
            node_right = queue_mirror_right.pop()
            if node_left and not node_right:
                return False
            if not node_left and node_right:
                return False
            
            if node_left.val != node_right.val:
                return False
            if node_left.left and node_right.left:
                queue_left.append(node_left.left)
                queue_mirror_right.append(node_right.left)
            elif node_left.left or node_right.left:
                return False
            
            if node_left.right and node_right.right:
                queue_left.append(node_left.right)
                queue_mirror_right.append(node_right.right)
            elif node_left.right or node_right.right:
                return False
        return True


class TestSolution(unittest.TestCase):
    def setUp(self):

        # Create a sample tree for testing
        #      1
        #     / \
        #    2   2
        #   / \ / \
        #  3  4 4  3
        self.root = TreeNode().parse_tree_from_array([1,2,2,3,4,4,3])

        #       1
        #      / \
        #     2   2
        #      \   \
        #       3   3
        self.root2 = TreeNode().parse_tree_from_array([1,2,2,None,3,None,3])

        # Instantiate the Solution class
        self.solution = Solution()

    def test_isSymmetric(self):
        # Test the isSymmetric function
        result = self.solution.isSymmetric(self.root)
        self.assertEqual(result, True)

        result = self.solution.isSymmetric(self.root2)
        self.assertEqual(result, False)

        

if __name__ == '__main__':
    unittest.main()

    # trees = TreeNode()
    # root = trees.parse_tree_from_array([1,2,2,None,3,None,3])
    # solution = Solution()
    # mirror_tree = solution.mirrorTree(root)
    # trees.printTree(root)
    # print('\n')
    # trees.printTree(mirror_tree)
