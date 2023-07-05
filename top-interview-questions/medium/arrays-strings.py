from typing import List

'''3SUM'''
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
#     Input: nums = [-1,0,1,2,-1,-4]
#     Output: [[-1,-1,2],[-1,0,1]]
#     Explanation: 
#     nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
#     nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
#     nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
#     The distinct triplets are [-1,0,1] and [-1,-1,2].
#     Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
#     Input: nums = [0,1,1]
#     Output: []
#     Explanation: The only possible triplet does not sum up to 0.

# Example 3:
#     Input: nums = [0,0,0]
#     Output: [[0,0,0]]
#     Explanation: The only possible triplet sums up to 0.

# Constraints:
#     3 <= nums.length <= 3000
#     -105 <= nums[i] <= 105

# Hints:
# -So, we essentially need to find three numbers x, y, and z such that they add up to the given value. If we fix one of the numbers say x, we are left with the two-sum problem at hand!
# - For the two-sum problem, if we fix one of the numbers, say x, we have to scan the entire array to find the next number y, which is value - x where value is the input parameter. Can we change our array somehow so that this search becomes faster?
# - The second train of thought for two-sum is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        n = len(nums)

        for i in range(n-2):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0: 
                    right -= 1
                else:
                    out.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    # Skip duplicates
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

        return out

'''SET MATRIX ZEROES'''
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Example 2:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# Constraints:
#     m == matrix.length
#     n == matrix[0].length
#     1 <= m, n <= 200
#     -231 <= matrix[i][j] <= 231 - 1

# Follow up:
#     A straightforward solution using O(mn) space is probably a bad idea.
#     A simple improvement uses O(m + n) space, but still not the best solution.
#     Could you devise a constant space solution?
# HINTS:
# - If any cell of the matrix has a zero we can record its row and column number using additional memory. But if you don't want to use extra memory then you can manipulate the array instead. i.e. simulating exactly what the question says.
# - Setting cell values to zero on the fly while iterating might lead to discrepancies. What if you use some other integer value as your marker? There is still a better approach for this problem with 0(1) space.
# - We could have used 2 sets to keep a record of rows/columns which need to be set to zero. But for an O(1) space solution, you can use one of the rows and and one of the columns to keep track of this information.
# - We can use the first cell of every row and column as a flag. This flag would determine whether a row or column has been set to zero.

"""
Do not return anything, modify matrix in-place instead.
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        
        firstRow = False
        firstCol = False
        
        # Step 1: Check if first row or first column needs to be set to zero
        for i in range(m):
            if matrix[i][0] == 0:
                firstCol = True
                break
        
        for j in range(n):
            if matrix[0][j] == 0:
                firstRow = True
                break
        
        # Step 2: Mark rows and columns based on zeros
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Step 3: Set cells to zero based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Step 4: Set first row and first column to zero if needed
        if firstRow:
            for j in range(n):
                matrix[0][j] = 0
        
        if firstCol:
            for i in range(m):
                matrix[i][0] = 0

'''GROUP ANAGRAMS'''
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
#     Input: strs = ["eat","tea","tan","ate","nat","bat"]
#     Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
#     Input: strs = [""]
#     Output: [[""]]

# Example 3:
#     Input: strs = ["a"]
#     Output: [["a"]]

# Constraints:
#     1 <= strs.length <= 104
#     0 <= strs[i].length <= 100
#     strs[i] consists of lowercase English letters.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_groups:
                anagram_groups[sorted_word].append(word)
            else:
                anagram_groups[sorted_word] = [word]
        
        return list(anagram_groups.values())

'''LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS'''
# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
    # Input: s = "abcabcbb"
    # Output: 3
    # Explanation: The answer is "abc", with the length of 3.

# Example 2:
#     Input: s = "bbbbb"
#     Output: 1
#     Explanation: The answer is "b", with the length of 1.

# Example 3:
#     Input: s = "pwwkew"
#     Output: 3
#     Explanation: The answer is "wke", with the length of 3.
#     Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Constraints:
#     0 <= s.length <= 5 * 104
#     s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        # Set to store characters in current window
        window = set()

        # Initialize start and end pointers
        start = 0
        end = 0

        # Initialize maximum length
        max_length = 0

        # Move the end pointer through the string
        while end < n:
            # If the character at the end pointer is not in the set, add it and move the pointer
            if s[end] not in window:
                window.add(s[end])
                end += 1
                max_length = max(max_length, end - start)
            # If the character at the end pointer is in the set, remove the character at the start pointer and move it
            else:
                window.remove(s[start])
                start += 1

        return max_length

'''LONGEST PALINDROMIC SUBSTRING'''
# Given a string s, return the longest palindromic substring in s.

# Example 1:
    # Input: s = "babad"
    # Output: "bab"
    # Explanation: "aba" is also a valid answer.

# Example 2:
    # Input: s = "cbbd"
    # Output: "bb"

# Constraints:
#     1 <= s.length <= 1000
#     s consist of only digits and English letters.

# Hints:
#     - How can we reuse a previously computed palindrome to compute a larger palindrome?
#     Hide Hint #2  
#     - If “aba” is a palindrome, is “xabax” a palindrome? Similarly is “xabay” a palindrome?
#     Hide Hint #3  
#     - Complexity based hint:
#         - If we use brute-force and check whether for every start and end position a substring is a palindrome we have O(n^2) start - end pairs and O(n)  
#           palindromic checks. Can we reduce the time for palindromic checks to O(1) by reusing some previous computation.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start = 0  # Starting index of the longest palindromic substring
        end = 0  # Ending index of the longest palindromic substring

        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)  # Check for odd-length palindromes
            len2 = self.expandAroundCenter(s, i, i + 1)  # Check for even-length palindromes
            max_len = max(len1, len2)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        # Expand around the center indices while the characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        # Return the length of the palindrome
        return right - left - 1

'''INCREASING TRIPLET SUBSTRING'''
# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

# Example 1:
#     Input: nums = [1,2,3,4,5]
#     Output: true
#     Explanation: Any triplet where i < j < k is valid.

# Example 2:
#     Input: nums = [5,4,3,2,1]
#     Output: false
#     Explanation: No triplet exists.

# Example 3:
#     Input: nums = [2,1,5,0,4,6]
#     Output: true
#     Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

# Constraints:
#     1 <= nums.length <= 5 * 105
#     -231 <= nums[i] <= 231 - 1

# Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = float('inf')
        min2 = float('inf')
        
        for num in nums:
            if num <= min1:
                min1 = num
            elif num <= min2:
                min2 = num
            else:
                return True
        
        return False
    
'''COUNT AND SAY'''
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
    # countAndSay(1) = "1"
    # countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.
# Given a positive integer n, return the nth term of the count-and-say sequence.

# Example 1:
    # Input: n = 1
    # Output: "1"
    # Explanation: This is the base case.

# Example 2:
    # Input: n = 4
    # Output: "1211"
    # Explanation:
    # countAndSay(1) = "1"
    # countAndSay(2) = say "1" = one 1 = "11"
    # countAndSay(3) = say "11" = two 1's = "21"
    # countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

# Constraints:
    # 1 <= n <= 30

# Hints:
    #     - Create a helper function that maps an integer to pairs of its digits and their frequencies. For example, if you call this function with "223314444411", then
    #     it maps it to an array of pairs [[2,2], [3,2], [1,1], [4,5], [1, 2]].
    #     - Create another helper function that takes the array of pairs and creates a new integer. For example, if you call this function with [[2,2], [3,2], [1,1], [4, 5], [1, 2]], it should create "22"+"23"+"11"+"54"+"21" = "2223115421".
    #     - Now, with the two helper functions, you can start with "1" and call the two functions alternatively n-1 times. The answer is the last integer you will obtain.

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        prev = self.countAndSay(n - 1)
        result = ""
        count = 1

        for i in range(1, len(prev)):
            if prev[i] == prev[i - 1]:
                count += 1
            else:
                result += str(count) + prev[i - 1]
                count = 1

        result += str(count) + prev[-1]
        return result