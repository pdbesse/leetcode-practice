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

'''CONSTRUCT BINARY TREE FROM PREORDER AND INORDER TRAVERSAL'''
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Example 1:
#     Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
#     Output: [3,9,20,null,null,15,7]

# Example 2:
#     Input: preorder = [-1], inorder = [-1]
#     Output: [-1]

# Constraints:
#     1 <= preorder.length <= 3000
#     inorder.length == preorder.length
#     -3000 <= preorder[i], inorder[i] <= 3000
#     preorder and inorder consist of unique values.
#     Each value of inorder also appears in preorder.
#     preorder is guaranteed to be the preorder traversal of the tree.
#     inorder is guaranteed to be the inorder traversal of the tree.

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # Create the root node using the first element of the preorder traversal
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # Find the index of the root value in the inorder traversal
        root_index = inorder.index(root_val)
        
        # Recursively build the left and right subtrees
        root.left = self.buildTree(preorder[1:root_index+1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])
        
        return root