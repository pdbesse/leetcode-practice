from typing import List
from functools import cmp_to_key
from collections import defaultdict

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

'''MAX POINTS ON A LINE'''
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

# Example 1:
#     Input: points = [[1,1],[2,2],[3,3]]
#     Output: 3

# Example 2:
#     Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
#     Output: 4

# Constraints:
#     1 <= points.length <= 300
#     points[i].length == 2
#     -104 <= xi, yi <= 104
#     All the points are unique.

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        
        max_points = 0
        
        for i, point1 in enumerate(points):
            slopes = defaultdict(int)  # To store slopes and their frequencies
            duplicate = 1  # To count duplicate points with the same (x, y) coordinates
            
            for j, point2 in enumerate(points):
                if i != j:
                    if point1 == point2:
                        duplicate += 1
                    else:
                        # Calculate the slope and handle vertical lines (infinite slope)
                        slope = float('inf') if point1[0] == point2[0] else (point2[1] - point1[1]) / (point2[0] - point1[0])
                        slopes[slope] += 1
            
            # Update the maximum number of points on the same line
            max_points = max(max_points, duplicate + max(slopes.values(), default=0))
        
        return max_points