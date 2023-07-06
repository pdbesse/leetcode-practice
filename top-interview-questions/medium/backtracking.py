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