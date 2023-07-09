from typing import List

'''SORTING COLORS'''
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# Example 1:
#     Input: nums = [2,0,2,1,1,0]
#     Output: [0,0,1,1,2,2]

# Example 2:
#     Input: nums = [2,0,1]
#     Output: [0,1,2]

# Constraints:
#     n == nums.length
#     1 <= n <= 300
#     nums[i] is either 0, 1, or 2.

# Follow up: Could you come up with a one-pass algorithm using only constant extra space?

# Hints:
#     - A rather straight forward solution is a two-pass algorithm using counting sort.
#     - Iterate the array counting number of 0's, 1's, and 2's.
#     - Overwrite array with the total number of 0's, then 1's and followed by 2's.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointer for zeroes
        left = 0
        # Pointer for twos
        right = len(nums) - 1
        # Pointer for iteration
        current = 0

        while current <= right:
            if nums[current] == 0:
                nums[current], nums[left] = nums[left], nums[current]
                current += 1
                left += 1
            elif nums[current] == 2:
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1
            else:
                current += 1

