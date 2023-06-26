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

'''FIRST UNIQUE CHARACTER IN A STRING'''
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:
    # Input: s = "leetcode"
    # Output: 0

# Example 2:
    # Input: s = "loveleetcode"
    # Output: 2

# Example 3:
    # Input: s = "aabb"
    # Output: -1

# Constraints:
    # 1 <= s.length <= 105
    # s consists of only lowercase English letters.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Time: O(n)
        # Space: O(n)
        # Create a dictionary to store the frequency of each character
        char_freq = {}
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        # Iterate through the string and return the index of the first character that has a frequency of 1
        for i in range(len(s)):
            if char_freq[s[i]] == 1:
                return i
        
        return -1
    
'''VALID ANAGRAM'''
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
    # Input: s = "anagram", t = "nagaram"
    # Output: true

# Example 2:
    # Input: s = "rat", t = "car"
    # Output: false

# Constraints:
    # 1 <= s.length, t.length <= 5 * 104
    # s and t consist of lowercase English letters.
    
    # Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        counts = [0]*26
        for c1,c2 in zip(s,t):
            counts[ord(c1) - ord('a')] += 1
            counts[ord(c2) - ord('a')] -= 1
        
        anagram = True
        for num in counts:
            if num != 0:
                anagram = False
        
        return anagram

'''VALID PALINDROME'''
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
    # Input: s = "A man, a plan, a canal: Panama"
    # Output: true
    # Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
    # Input: s = "race a car"
    # Output: false
    # Explanation: "raceacar" is not a palindrome.

# Example 3:
    # Input: s = " "
    # Output: true
    # Explanation: s is an empty string "" after removing non-alphanumeric characters.
    # Since an empty string reads the same forward and backward, it is a palindrome.

# Constraints:
    # 1 <= s.length <= 2 * 105
    # s consists only of printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''

        for c in s:
            if c.isalnum():
                new_s += c.lower()

        start,end = 0,len(new_s)-1
        while(start<end):
            if new_s[start] != new_s[end]:
                return False
            start += 1
            end -= 1
        
        return True

'''STRING TO INTEGERE (ATOI)'''
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
# The algorithm for myAtoi(string s) is as follows:
    # Read in and ignore any leading whitespace.
    # Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
    # Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
    # Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
    # If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
    # Return the integer as the final result.
# Note:
    # Only the space character ' ' is considered a whitespace character.
    # Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
 
# Example 1:
    # Input: s = "42"
    # Output: 42
    # Explanation: The underlined characters are what is read in, the caret is the current reader position.
    # Step 1: "42" (no characters read because there is no leading whitespace)
    #          ^
    # Step 2: "42" (no characters read because there is neither a '-' nor '+')
    #          ^
    # Step 3: "42" ("42" is read in)
    #            ^
    # The parsed integer is 42.
    # Since 42 is in the range [-231, 231 - 1], the final result is 42.

# Example 2:
    # Input: s = "   -42"
    # Output: -42
    # Explanation:
    # Step 1: "   -42" (leading whitespace is read and ignored)
    #             ^
    # Step 2: "   -42" ('-' is read, so the result should be negative)
    #              ^
    # Step 3: "   -42" ("42" is read in)
    #                ^
    # The parsed integer is -42.
    # Since -42 is in the range [-231, 231 - 1], the final result is -42.

# Example 3:
    # Input: s = "4193 with words"
    # Output: 4193
    # Explanation:
    # Step 1: "4193 with words" (no characters read because there is no leading whitespace)
    #          ^
    # Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
    #          ^
    # Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
    #              ^
    # The parsed integer is 4193.
    # Since 4193 is in the range [-231, 231 - 1], the final result is 4193.

# Constraints:
    # 0 <= s.length <= 200
    # s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Read and ignore any leading whitespace
        s = s.strip()
    
        # Step 2: Check if the number is negative or positive
        sign = 1
        if s and (s[0] == '-' or s[0] == '+'):
            if s[0] == '-':
                sign = -1
            s = s[1:]
        
        # Step 3: Read the digits until the next non-digit character or the end of the input
        num = 0
        for c in s:
            if not c.isdigit():
                break
            num = num * 10 + int(c)
        
        # Step 4: Apply sign and check for overflow
        num = sign * num
        num = max(min(num, 2**31 - 1), -2**31)
        
        # Step 5: Return the final result
        return num

'''IMPLEMENT strStr()'''
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
#     Input: haystack = "sadbutsad", needle = "sad"
#     Output: 0
#     Explanation: "sad" occurs at index 0 and 6.
#     The first occurrence is at index 0, so we return 0.

# Example 2:
#     Input: haystack = "leetcode", needle = "leeto"
#     Output: -1
#     Explanation: "leeto" did not occur in "leetcode", so we return -1.

# Constraints:
#     1 <= haystack.length, needle.length <= 104
#     haystack and needle consist of only lowercase English characters.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Time: O(n*m)
        # Space: O(1)
        # Edge case
        if not needle:
            return 0
        
        # Iterate through the haystack
        for i in range(len(haystack)):
            # Check if the substring starting at the current index matches the needle
            if haystack[i:i+len(needle)] == needle:
                return i
        
        return -1