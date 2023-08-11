from typing import List

'''WIGGLE SORT II'''
# Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
# You may assume the input array always has a valid answer.

# Example 1:
#     Input: nums = [1,5,1,1,6,4]
#     Output: [1,6,1,5,1,4]
#     Explanation: [1,4,1,5,1,6] is also accepted.

# Example 2:
#     Input: nums = [1,3,2,2,3,1]
#     Output: [2,3,1,3,1,2]

# Constraints:
#     1 <= nums.length <= 5 * 104
#     0 <= nums[i] <= 5000
#     It is guaranteed that there will be an answer for the given input nums.

# Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?

"""
Do not return anything, modify nums in-place instead.
"""

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        sorted_nums = sorted(nums)
        
        # Initialize indices for the smaller and larger halves.
        smaller_idx = (n + 1) // 2 - 1
        larger_idx = n - 1
        
        result = [0] * n
        
        # Fill odd indices with larger elements.
        for i in range(1, n, 2):
            result[i] = sorted_nums[larger_idx]
            larger_idx -= 1
        
        # Fill even indices with smaller elements.
        for i in range(0, n, 2):
            result[i] = sorted_nums[smaller_idx]
            smaller_idx -= 1
        
        nums[:] = result  # Copy the result back to the original array