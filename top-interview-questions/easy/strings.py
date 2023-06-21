from typing import List, Optional

'''REVERSE STRING'''
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 
# Constraints:
# 1 <= s.length <= 105
# s[i] is a printable ascii character.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        # Time: O(n)
        # Space: O(1)
        """
        Do not return anything, modify s in-place instead.
        """
        # Two pointer approach
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        # Pythonic way
        # s.reverse()

'''REVERSE INTEGER'''
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

# Constraints:
# -231 <= x <= 231 - 1

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x = abs(x)
        else:
            sign = 1
        
        # Convert the integer to a string and reverse it
        reversed_str = str(x)[::-1]
        
        # Convert the reversed string back to an integer
        reversed_int = int(reversed_str)
        
        # Apply the sign to the reversed integer
        reversed_int *= sign
        
        # Check if the reversed integer is within the 32-bit signed integer range
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0
        
        return reversed_int