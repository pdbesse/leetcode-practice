from typing import List, Optional
from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''WORD LADDER'''
#     A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#     Every adjacent pair of words differs by a single letter.
#     Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
#     sk == endWord
#     Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

# Example 1:
#     Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
#     Output: 5
#     Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

# Example 2:
#     Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
#     Output: 0
#     Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

# Constraints:
#     1 <= beginWord.length <= 10
#     endWord.length == beginWord.length
#     1 <= wordList.length <= 5000
#     wordList[i].length == beginWord.length
#     beginWord, endWord, and wordList[i] consist of lowercase English letters.
#     beginWord != endWord
#     All the words in wordList are unique.

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Create a set for faster word lookup
        wordSet = set(wordList)
        
        # If the endWord is not in the wordList, there's no valid sequence
        if endWord not in wordSet:
            return 0
        
        # Create a graph where each node has its neighbors
        def construct_graph(wordSet):
            graph = defaultdict(list)
            for word in wordSet:
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    graph[pattern].append(word)
            return graph
        
        graph = construct_graph(wordSet)
        
        # BFS to find the shortest transformation sequence
        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        
        while queue:
            current_word, level = queue.popleft()
            for i in range(len(current_word)):
                pattern = current_word[:i] + '*' + current_word[i+1:]
                for neighbor in graph[pattern]:
                    if neighbor == endWord:
                        return level + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
        return 0
    
'''SURROUNDED REGIONS'''
# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example 1:
#     Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
#     Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
#     Explanation: Notice that an 'O' should not be flipped if:
#     - It is on the border, or
#     - It is adjacent to an 'O' that should not be flipped.
#     The bottom 'O' is on the border, so it is not flipped.
#     The other three 'O' form a surrounded region, so they are flipped.

# Example 2:
#     Input: board = [["X"]]
#     Output: [["X"]]

# Constraints:
#     m == board.length
#     n == board[i].length
#     1 <= m, n <= 200
#     board[i][j] is 'X' or 'O'.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(row,col):
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != 'O':
                return
            
            # Mark current cell as 'M' (to be modified to 'X' later)
            board[row][col] = 'M'
            # Recursively traverse all four directions
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(row + dr, col + dc)

        if not board:
            return
        
        m, n = len(board), len(board[0])

        # Traverse boundary and mark all '0's and their connected regions with 'M'
        for row in range(m):
            if board[row][0] == 'O':
                dfs(row, 0)
            if board[row][n-1] == 'O':
                dfs(row, n - 1)
        
        for col in range(n):
            if board[0][col] == 'O':
                dfs(0, col)
            if board[m - 1][col] == 'O':
                dfs(m - 1, col)
        
        # Mark all remaining 'O's as 'X's and restore 'M's to 'O's
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'M':
                    board[row][col] = 'O'

'''LOWEST COMMON ANCESTOR OF A BINARY TREE'''
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Example 1:
#     Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
#     Output: 3
#     Explanation: The LCA of nodes 5 and 1 is 3.

# Example 2:
#     Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
#     Output: 5
#     Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

# Example 3:
#     Input: root = [1,2], p = 1, q = 2
#     Output: 1

# Constraints:
#     The number of nodes in the tree is in the range [2, 105].
#     -109 <= Node.val <= 109
#     All Node.val are unique.
#     p != q
#     p and q will exist in the tree.

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base cases
        if not root or root == p or root == q:
            return root
        
        # Recursively find LCA in left and right subtrees
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        # If both nodes are in different subtrees, current node is LCA
        if left_lca and right_lca:
            return root
        
        # If either node is found in sutree, return that node as LCA
        return left_lca if left_lca else right_lca
    
'''BINARY TREE MAXIMUM PATH SUM'''
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Example 1:
#     Input: root = [1,2,3]
#     Output: 6
#     Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

# Example 2:
#     Input: root = [-10,9,20,null,null,15,7]
#     Output: 42
#     Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

# Constraints:
#     The number of nodes in the tree is in the range [1, 3 * 104].
#     -1000 <= Node.val <= 1000

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Helper function to calculate max path sum for a node
        def maxPathSumHelper(node):
            if not node:
                return 0
            
            # Calculate max path sum for left and right subtrees
            left_max = maxPathSumHelper(node.left)
            right_max = maxPathSumHelper(node.right)

            # Calculate max path sum that includes current node
            # and either extends to its left or right subtree or includes
            # only the current node
            max_path_sum_through_node = max(left_max + node.val, right_max + node.val, node.val)

             # Calculate max path sum that passes through current node
            max_path_sum_passing_node = max(max_path_sum_through_node, left_max + node.val + right_max)

            # Update global maximum path sum if needed
            self.max_sum = max(self.max_sum, max_path_sum_passing_node)

            return max_path_sum_through_node

        # Initialize the global maximum path sum
        self.max_sum = float('-inf')  
        
        maxPathSumHelper(root)

        return self.max_sum
    




'''LONGEST INCREASING PATH IN A MATRIX'''
# Given an m x n integers matrix, return the length of the longest increasing path in matrix.
# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

# Example 1:
# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].

# Example 2:
# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

# Example 3:
# Input: matrix = [[1]]
# Output: 1

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# 0 <= matrix[i][j] <= 231 - 1

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(row, col):
            if memo[row][col] != 0:
                return memo[row][col]

            max_path = 1
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n and matrix[new_row][new_col] > matrix[row][col]:
                    max_path = max(max_path, 1 + dfs(new_row, new_col))

            memo[row][col] = max_path
            return max_path

        longest_path = 0
        for i in range(m):
            for j in range(n):
                longest_path = max(longest_path, dfs(i, j))

        return longest_path