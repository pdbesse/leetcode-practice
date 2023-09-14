from typing import List

'''DUPLICATE ZEROS'''
# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

# Example 1:
#     Input: arr = [1,0,2,3,0,4,5,0]
#     Output: [1,0,0,2,3,0,0,4]
#     Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

# Example 2:
#     Input: arr = [1,2,3]
#     Output: [1,2,3]
#     Explanation: After calling your function, the input array is modified to: [1,2,3]

# Hints:
    # - This is a great introductory problem for understanding and working with the concept of in-place operations. The problem statement clearly states that we are to modify the array in-place. That does not mean we cannot use another array. We just don't have to return anything.
    # - A better way to solve this would be without using additional space. The only reason the problem statement allows you to make modifications in place is that it hints at avoiding any additional memory.
    # - The main problem with not using additional memory is that we might override elements due to the zero duplication requirement of the problem statement. How do we get around that?
    # - If we had enough space available, we would be able to accommodate all the elements properly. The new length would be the original length of the array plus the number of zeros. Can we use this information somehow to solve the problem?

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Count the number of zeros
        zeros = 0
        for num in arr:
            if num == 0:
                zeros += 1

        # Iterate backwards
        for i in range(len(arr) - 1, -1, -1):
            # If the current number is zero, duplicate it
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < len(arr):
                    arr[i + zeros] = 0
                if i + zeros + 1 < len(arr):
                    arr[i + zeros + 1] = 0
            # Else, shift the number to the right
            else:
                if i + zeros < len(arr):
                    arr[i + zeros] = arr[i]

'''ZIGZAG CONVERSION'''
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
#     string convert(string s, int numRows);

# Example 1:
#     Input: s = "PAYPALISHIRING", numRows = 3
#     Output: "PAHNAPLSIIGYIR"

# Example 2:
#     Input: s = "PAYPALISHIRING", numRows = 4
#     Output: "PINALSIGYAHRPI"
#     Explanation:
#         P     I    N
#         A   L S  I G
#         Y A   H R
#         P     I

# Example 3:
#     Input: s = "A", numRows = 1
#     Output: "A"

# Constraints:
#     1 <= s.length <= 1000
#     s consists of English letters (lower-case and upper-case), ',' and '.'.
#     1 <= numRows <= 1000

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        current_row, direction = 0, 1

        for char in s:
            rows[current_row] += char

            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1

            current_row += direction

        return ''.join(rows)
    
'''3SUM CLOSEST'''
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

# Example 1:
#     Input: nums = [-1,2,1,-4], target = 1
#     Output: 2
#     Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:
#     Input: nums = [0,0,0], target = 1
#     Output: 0
#     Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

# Constraints:
#     3 <= nums.length <= 500
#     -1000 <= nums[i] <= 1000
#     -104 <= target <= 104

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')

        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(target - total) < abs(closest):
                    closest = target - total

                if total < target:
                    left += 1
                else:
                    right -= 1

            if closest == 0:
                break

        return target - closest
    
'''COMBINATION SUM'''
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Example 1:
#     Input: candidates = [2,3,6,7], target = 7
#     Output: [[2,2,3],[7]]
#     Explanation:
#         2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
#         7 is a candidate, and 7 = 7.
#         These are the only two combinations.

# Example 2:
#     Input: candidates = [2,3,5], target = 8
#     Output: [[2,2,2,2],[2,3,3],[3,5]]

# Example 3:
#     Input: candidates = [2], target = 1
#     Output: []

# Constraints:
#     1 <= candidates.length <= 30
#     2 <= candidates[i] <= 40
#     All elements of candidates are distinct.
#     1 <= target <= 40

class Solution:
    def combinationSum(self, candidates, target):
        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()

        result = []
        backtrack(0, target, [])
        return result