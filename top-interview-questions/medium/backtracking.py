from typing import List

'''LETTER COMBINATIONS OF A PHONE NUMBNER'''
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:
#     Input: digits = "23"
#     Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:
#     Input: digits = ""
#     Output: []

# Example 3:
#     Input: digits = "2"
#     Output: ["a","b","c"]

# Constraints:
#     0 <= digits.length <= 4
#     digits[i] is a digit in the range ['2', '9'].

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        combinations = []
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(combo, next_digits):
            if len(next_digits) == 0:
                combinations.append(combo)
            else:
                for letter in digit_map[next_digits[0]]:
                    backtrack(combo + letter, next_digits[1:])

        backtrack('', digits)

        return combinations

'''GENERATE PARANTHESES'''
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:
    # Input: n = 3
    # Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
    # Input: n = 1
    # Output: ["()"]

# Constraints:
    # 1 <= n <= 8   

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lst = []
        self.helper(n, n, '', lst)

        return lst

    def helper(self, left_count: int, right_count: int, current: str, lst: List[str]):
        # Base case: If both left_count and right_count are zero, we have a valid combination
        if left_count == 0 and right_count == 0:
            lst.append(current)
            return
        
        # Recursive cases
        # If there are more left parentheses left, add one
        if left_count > 0:
            self.helper(left_count - 1, right_count, current + '(', lst)
        # If there are more right parentheses left, add one
        if right_count > left_count:
            self.helper(left_count, right_count - 1, current + ')', lst)

'''PERMUTATIONS'''
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:
#     Input: nums = [1,2,3]
#     Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
#     Input: nums = [0,1]
#     Output: [[0,1],[1,0]]

# Example 3:
#     Input: nums = [1]
#     Output: [[1]]

# Constraints:
#     1 <= nums.length <= 6
#     -10 <= nums[i] <= 10
#     All the integers of nums are unique.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        out = []
        def backtrack(first=0):
            if first == n:
                out.append(nums[:])
            for i in range(first, n):
                # Swap current element with first element
                nums[first], nums[i] = nums[i], nums[first]
                # Generate all permutations starting from next element
                backtrack(first + 1)
                # Restore original list state
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)

        backtrack()

        return out

'''SUBSETS'''
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
#     Input: nums = [1,2,3]
#     Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
#     Input: nums = [0]
#     Output: [[],[0]]

# Constraints:
#     1 <= nums.length <= 10
#     -10 <= nums[i] <= 10
#     All the numbers of nums are unique.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            # Add current subset to output
            out.append(path[:])

            # Find all possible choices for next element
            for i in range(start, n):
                path.append(nums[i])
                # Move to next element
                backtrack(i + 1, path)
                # Remove last element (backtrack)
                path.pop()
        
        n = len(nums)
        out = []
        backtrack(0, [])

        return out

'''WORD SEARCH'''
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
#     Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
#     Output: true

# Example 2:
#     Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
#     Output: true

# Example 3:
#     Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
#     Output: false

# Constraints:
#     m == board.length
#     n = board[i].length
#     1 <= m, n <= 6
#     1 <= word.length <= 15
#     board and word consists of only lowercase and uppercase English letters.
 
# Follow up: Could you use search pruning to make your solution faster with a larger board?

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row, col, word_idx):
            if word_idx == len(word):
                return True

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[word_idx]:
                return False

            # Mark the current cell as visited
            temp = board[row][col]
            board[row][col] = ''

            # Explore the neighboring cells
            found = (backtrack(row - 1, col, word_idx + 1) or
                     backtrack(row + 1, col, word_idx + 1) or
                     backtrack(row, col - 1, word_idx + 1) or
                     backtrack(row, col + 1, word_idx + 1))

            # Restore the cell's value
            board[row][col] = temp

            return found

        # Iterate over each cell in the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True

        return False