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

'''4SUM'''
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
#     0 <= a, b, c, d < n
#     a, b, c, and d are distinct.
#     nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# Example 1:
#     Input: nums = [1,0,-1,0,-2,2], target = 0
#     Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Example 2:
#     Input: nums = [2,2,2,2,2], target = 8
#     Output: [[2,2,2,2]]

# Constraints:
#     1 <= nums.length <= 200
#     -109 <= nums[i] <= 109
#     -109 <= target <= 109

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort the input array to simplify the process
        nums.sort()
        result = []
        
        for i in range(len(nums) - 3):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, len(nums) - 2):
                # Skip duplicates
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left, right = j + 1, len(nums) - 1
                
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
        
        return result

# '''NEXT PERMUTATION'''
# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

# Example 1:
#     Input: nums = [1,2,3]
#     Output: [1,3,2]

# Example 2:
#     Input: nums = [3,2,1]
#     Output: [1,2,3]

# Example 3:
#     Input: nums = [1,1,5]
#     Output: [1,5,1]

# Constraints:
#     1 <= nums.length <= 100
#     0 <= nums[i] <= 100

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find the first index from the right where nums[i] < nums[i+1]
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            # Find the first index from the right where nums[j] > nums[i]
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1

            # Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the subarray to the right of i
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
'''COMBINATION SUM II'''
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.


# Example 1:
#     Input: candidates = [10,1,2,7,6,1,5], target = 8
#     Output: 
#         [
#         [1,1,6],
#         [1,2,5],
#         [1,7],
#         [2,6]
#         ]

# Example 2:
#     Input: candidates = [2,5,2,1,2], target = 5
#     Output: 
#         [
#         [1,2,2],
#         [5]
#         ]

# Constraints:
#     1 <= candidates.length <= 100
#     1 <= candidates[i] <= 50
#     1 <= target <= 30

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, end, path):
            if target == 0:
                # If target is zero, we have our combination
                result.append(path)
                return
            if target < 0 or start == len(candidates):
                # If target is negative or we have exhausted candidates
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates to avoid duplicating combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Recursively try adding current candidate to path
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])
        
        # Sort candidates to handle duplicates efficiently
        candidates.sort()
        result = []
        backtrack(0, target, [])

        return result
    
'''SUDOKU SOLVER'''
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
#     - Each of the digits 1-9 must occur exactly once in each row.
#     - Each of the digits 1-9 must occur exactly once in each column.
#     - Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

# Example 1:
#     Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
#     Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
#     Explanation: The input board is shown above and the only valid solution is shown below:

# Constraints:
#     board.length == 9
#     board[i].length == 9
#     board[i][j] is a digit or '.'.
#     It is guaranteed that the input board has only one solution.

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(num, row, col):
            for i in range(9):
                if board[row][i] == num or board[i][col] == num or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                    return False
            return True

        def solve():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        for num in map(str, range(1, 10)):
                            if is_valid(num, row, col):
                                board[row][col] = num
                                if solve():
                                    return True
                                board[row][col] = "."
                        return False
            return True

        solve()