from typing import List, Optional
from queue import Queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


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

'''POPULATING NEXT RIGHT POINTERS IN EACH NODE'''
# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. 
# The binary tree has the following definition:
#     struct Node {
#     int val;
#     Node *left;
#     Node *right;
#     Node *next;
#     }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.

# Example 1:
#     Input: root = [1,2,3,4,5,6,7]
#     Output: [1,#,2,3,#,4,5,6,7,#]
#     Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

# Example 2:
#     Input: root = []
#     Output: []

# Constraints:
#     The number of nodes in the tree is in the range [0, 212 - 1].
#     -1000 <= Node.val <= 1000

# Follow-up:
#     You may only use constant extra space.
#     The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        leftmost = root
        # continue to last lever
        while leftmost.left:
            head = leftmost
            while head:
                # Connect children of current node
                head.left.next = head.right
                # Connect right child of current node to left child of next node
                if head.next:
                    head.right.next = head.next.left
                # Move to next node on current level
                head = head.next

            # Move to next level
            leftmost = leftmost.left
        
        return root
                
'''KTH SMALLEST ELEMENT IN A BST'''
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Example 1:
# Input: root = [3,1,4,null,2], k = 1
# Output: 1

# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3

# Constraints:
#     The number of nodes in the tree is n.
#     1 <= k <= n <= 104
#     0 <= Node.val <= 104
 
# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

# Hints:
#     - Try to utilize the property of a BST.
#     - Try in-order traversal. (Credits to @chan13)
#     - What if you could modify the BST node's structure?
#     - The optimal runtime complexity is O(height of BST).

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = None
        self.inorderTraversal(root, k)
        return self.result

    def inorderTraversal(self, node: Optional[TreeNode], k: int) -> None:
        if node is None:
            return

        self.inorderTraversal(node.left, k)

        self.count += 1
        if self.count == k:
            self.result = node.val
            return

        self.inorderTraversal(node.right, k)

'''INORDER SUCCESSOR OF BST'''
# Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.
# The successor of a node p is the node with the smallest key greater than p.val.

# Example 1:
#     Input: root = [2,1,3], p = 1
#     Output: 2
#     Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.

# Example 2:
#     Input: root = [5,3,6,2,4,null,null,1], p = 6
#     Output: null
#     Explanation: There is no in-order successor of the current node, so the answer is null.

# Constraints:
#     The number of nodes in the tree is in the range [1, 104].
#     -105 <= Node.val <= 105
#     All Nodes will have unique values.

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None

        while root:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right

        return successor
                

'''NUMBER OF ISLANDS'''
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:
#     Input: grid = [
#     ["1","1","1","1","0"],
#     ["1","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
#     ]
#     Output: 1

# Example 2:
#     Input: grid = [
#     ["1","1","0","0","0"],
#     ["1","1","0","0","0"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
#     ]
#     Output: 3

# Constraints:
#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 300
#     grid[i][j] is '0' or '1'.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        count = 0

        def DFS(row,col):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] != '1':
                return
            
            # Mark current cell as visited
            grid[row][col] = '0'

            # Explore neighbor cells
            # Up
            DFS(row-1, col)
            # Down
            DFS(row+1, col)
            # Left
            DFS(row, col-1)
            # Right
            DFS(row, col+1)

        # Iterate over each cell in grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    DFS(i,j)
        
        return count