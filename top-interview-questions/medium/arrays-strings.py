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