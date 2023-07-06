from typing import List, Optional
from queue import Queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''BINARY TREE INORDER TRAVERSAL'''
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Example 1:
#     Input: root = [1,null,2,3]
#     Output: [1,3,2]

# Example 2:
#     Input: root = []
#     Output: []

# Example 3:
#     Input: root = [1]
#     Output: [1]

# Constraints:
#     The number of nodes in the tree is in the range [0, 100].
#     -100 <= Node.val <= 100

# Follow up: Recursive solution is trivial, could you do it iteratively?

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        stack = []
        current = root

        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            traversal.append(current.val)
            current = current.right

        return traversal
    
'''BINARY TREE ZIGZAG LEVEL ORDER TRAVERSAL'''
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

# Example 1:
#     Input: root = [3,9,20,null,null,15,7]
#     Output: [[3],[20,9],[15,7]]

# Example 2:
#     Input: root = [1]
#     Output: [[1]]

# Example 3:
#     Input: root = []
#     Output: []

# Constraints:
#     The number of nodes in the tree is in the range [0, 2000].
#     -100 <= Node.val <= 100

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        traversal = []
        q = Queue()
        q.put(root)
        level = 0

        while not q.empty():
            level_size = q.qsize()
            level_values = []

            for _ in range(level_size):
                node = q.get()
                level_values.append(node.val)

                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)

            if level % 2 == 1:
                level_values = level_values[::-1]

            traversal.append(level_values)
            level += 1

        return traversal