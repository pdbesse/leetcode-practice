from typing import List
from functools import cmp_to_key

'''LARGEST NUMBER'''
# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
# Since the result may be very large, so you need to return a string instead of an integer.

# Example 1:
#     Input: nums = [10,2]
#     Output: "210"

# Example 2:
#     Input: nums = [3,30,34,5,9]
#     Output: "9534330"

# Constraints:
#     1 <= nums.length <= 100
#     0 <= nums[i] <= 109

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert integers to strings for comparison
        nums_str = [str(num) for num in nums]

        # Define a custom comparison function
        def compare(x, y):
            return int(y + x) - int(x + y)  # Compare y + x and x + y to determine order

        # Sort the numbers using the custom comparison function
        nums_str.sort(key=cmp_to_key(compare))

        # Join the sorted strings to form the largest number
        largest_num = ''.join(nums_str)

        # Remove leading zeros
        largest_num = largest_num.lstrip('0')

        # If the result is an empty string, return '0'
        return largest_num if largest_num else '0'