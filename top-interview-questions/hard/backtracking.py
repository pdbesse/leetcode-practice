from typing import List

'''PALINDROME PARTITIONING'''
# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

# Example 1:
#     Input: s = "aab"
#     Output: [["a","a","b"],["aa","b"]]

# Example 2:
#     Input: s = "a"
#     Output: [["a"]]

# Constraints:
#     1 <= s.length <= 16
#     s contains only lowercase English letters.

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(subs):
            return subs == subs[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()

        result = []
        backtrack(0, [])
        return result
    
'''WORD SEARCH II'''
# Given an m x n board of characters and a list of strings words, return all words on the board.
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

# Example 1:
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]

# Example 2:
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []

# Constraints:
#     m == board.length
#     n == board[i].length
#     1 <= m, n <= 12
#     board[i][j] is a lowercase English letter.
#     1 <= words.length <= 3 * 104
#     1 <= words[i].length <= 10
#     words[i] consists of lowercase English letters.
#     All the strings of words are unique.

# Hints:
#     - You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
#     - If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def backtrack(node, r, c, path):
            letter = board[r][c]
            curr_node = node[letter]
            if "end" in curr_node:
                result.add(path)
            board[r][c] = "#"  # Mark the cell as visited
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < len(board) and 0 <= new_c < len(board[0]) and board[new_r][new_c] in curr_node:
                    backtrack(curr_node, new_r, new_c, path + board[new_r][new_c])
            
            board[r][c] = letter  # Restore the cell
            
        result = set()
        root = {}
        
        for word in words:
            node = root
            for letter in word:
                if letter not in node:
                    node[letter] = {}
                node = node[letter]
            node["end"] = True
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in root:
                    backtrack(root, r, c, board[r][c])
        
        return list(result)