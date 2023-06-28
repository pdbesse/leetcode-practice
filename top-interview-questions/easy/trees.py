from typing import List, Optional
from queue import Queue

'''MAXIMUM DEPTH OF A BINARY TREE'''
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
#     Input: root = [3,9,20,null,null,15,7]
#     Output: 3

# Example 2:
#     Input: root = [1,null,2]
#     Output: 2

# Constraints:
#     The number of nodes in the tree is in the range [0, 104].
#     -100 <= Node.val <= 100

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        depth = 0
        queue = Queue()
        queue.put(root)

        while not queue.empty():
            depth += 1
            level_size = queue.qsize()

            for _ in range(level_size):
                node = queue.get()

                if node.left:
                    queue.put(node.left)
                if node.right:
                    queue.put(node.right)

        return depth
    
'''VALIDATE BINARY SEARCH TREE'''
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Example 1:
#     Input: root = [2,1,3]
#     Output: true

# Example 2:
#     Input: root = [5,1,4,null,null,3,6]
#     Output: false
#     Explanation: The root node's value is 5 but its right child's value is 4.

# Constraints:
#     The number of nodes in the tree is in the range [1, 104].
#     -231 <= Node.val <= 231 - 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBSTHelper(root,min,max):
                if root is None:
                    return 'there is no BST'
                if root.val < min or root.val > max:
                    return False
                leftIsValid = isValidBSTHelper(root.left, min, root.val)
                return leftIsValid and isValidBSTHelper(root.right, root.val, max)
        return isValidBSTHelper(root, float('-inf'), float('inf'))