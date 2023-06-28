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
                if root.val <= min or root.val >= max:
                    return False
                leftIsValid = isValidBSTHelper(root.left, min, root.val)
                return leftIsValid and isValidBSTHelper(root.right, root.val, max)
        return isValidBSTHelper(root, float('-inf'), float('inf'))
    
'''SYMMETRIC TREE'''
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:
#     Input: root = [1,2,2,3,4,4,3]
#     Output: true

# Example 2:
#     Input: root = [1,2,2,null,3,null,3]
#     Output: false

# Constraints:
#     The number of nodes in the tree is in the range [1, 1000].
#     -100 <= Node.val <= 100

# Follow up: Could you solve it both recursively and iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# RECURSIVE SOLUTION
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 'there is no tree'
        def isSymmetricHelper(left: TreeNode, right: TreeNode) -> bool:
            if left is None and right is None:
                return True
            if left is None or right is None or left.val != right.val:
                return False
            return isSymmetricHelper(left.left, right.right) and isSymmetricHelper(left.right, right.left)
        return isSymmetricHelper(root.left, root.right)

# ITERATIVE SOLUTION
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        queue = Queue()
        queue.put(root.left)
        queue.put(root.right)
        
        while not queue.empty():
            left = queue.get()
            right = queue.get()
            
            if left is None and right is None:
                continue
            if left is None or right is None or left.val != right.val:
                return False
            
            queue.put(left.left)
            queue.put(right.right)
            queue.put(left.right)
            queue.put(right.left)
        
        return True

'''BINARY TREE LEVEL ORDER TRAVERSAL'''
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Example 1:
#     Input: root = [3,9,20,null,null,15,7]
#     Output: [[3],[9,20],[15,7]]

# Example 2:
#     Input: root = [1]
#     Output: [[1]]

# Example 3:
#     Input: root = []
#     Output: []

# Constraints:
#     The number of nodes in the tree is in the range [0, 2000].
#     -1000 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        out = []
        q = Queue()
        q.put(root)

        while not q.empty():
            level = []
            next_level = Queue()

            while not q.empty():
                node = q.get()
                level.append(node.val)

                if node.left:
                    next_level.put(node.left)
                if node.right:
                    next_level.put(node.right)
                
            out.append(level)
            q = next_level
        
        return out
        