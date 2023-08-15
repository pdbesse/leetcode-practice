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

'''REMOVE INVALID PARENTHESIS'''
# Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.
# Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

# Example 1:
#     Input: s = "()())()"
#     Output: ["(())()","()()()"]

# Example 2:
#     Input: s = "(a)())()"
#     Output: ["(a())()","(a)()()"]

# Example 3:
#     Input: s = ")("
#     Output: [""]

# Constraints:
#     1 <= s.length <= 25
#     s consists of lowercase English letters and parentheses '(' and ')'.
#     There will be at most 20 parentheses in s.

# Hints:
#     - Since we do not know which brackets can be removed, we try all the options! We can use recursion.
#     - In the recursion, for each bracket, we can either use it or remove it.
#     - Recursion will generate all the valid parentheses strings but we want the ones with the least number of parentheses deleted.
#     - We can count the number of invalid brackets to be deleted and only generate the valid strings in the recusrion.

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
        
        result = []
        visited = set()
        queue = [(s, 0)]
        found = False
        
        while queue:
            current, level = queue.pop(0)
            
            if is_valid(current):
                result.append(current)
                found = True
            
            if found:
                # We've already found valid strings at this level,
                # so we don't need to explore further
                continue
            
            for i in range(level, len(current)):
                if current[i] not in '()':
                    continue
                
                next_string = current[:i] + current[i+1:]
                if next_string not in visited:
                    visited.add(next_string)
                    queue.append((next_string, i))
        
        return result
    
'''WILDCARD MATCHING'''
# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

# Example 1:
#     Input: s = "aa", p = "a"
#     Output: false
#     Explanation: "a" does not match the entire string "aa".

# Example 2:
#     Input: s = "aa", p = "*"
#     Output: true
#     Explanation: '*' matches any sequence.

# Example 3:
#     Input: s = "cb", p = "?a"
#     Output: false
#     Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

# Constraints:
#     0 <= s.length, p.length <= 2000
#     s contains only lowercase English letters.
#     p contains only lowercase English letters, '?' or '*'.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}  # Memoization dictionary
        
        def backtrack(s_index, p_index):
            if (s_index, p_index) in memo:
                return memo[(s_index, p_index)]
            
            if p_index == len(p):
                return s_index == len(s)
            
            if s_index < len(s) and (p[p_index] == '?' or p[p_index] == s[s_index]):
                result = backtrack(s_index + 1, p_index + 1)
            elif p[p_index] == '*':
                result = any(backtrack(i, p_index + 1) for i in range(s_index, len(s) + 1))
            else:
                result = False
            
            memo[(s_index, p_index)] = result
            return result
        
        return backtrack(0, 0)

    
'''REGULAR EXPRESSION MATCHING'''
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
#     - '.' Matches any single character.​​​​
#     - '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Example 1:
#     Input: s = "aa", p = "a"
#     Output: false
#     Explanation: "a" does not match the entire string "aa".

# Example 2:
#     Input: s = "aa", p = "a*"
#     Output: true
#     Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

# Example 3:
#     Input: s = "ab", p = ".*"
#     Output: true
#     Explanation: ".*" means "zero or more (*) of any character (.)".

# Constraints:
#     1 <= s.length <= 20
#     1 <= p.length <= 20
#     s contains only lowercase English letters.
#     p contains only lowercase English letters, '.', and '*'.
#     It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pass