from typing import List

'''PRODUCT OF ARRAY EXCEPT SELF'''
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
    # Input: nums = [1,2,3,4]
    # Output: [24,12,8,6]

# Example 2:
    # Input: nums = [-1,1,0,-3,3]
    # Output: [0,0,9,0,0]

# Constraints:
    # 2 <= nums.length <= 105
    # -30 <= nums[i] <= 30
    # The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # Calculate the product of all the elements to the left of each element
        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i-1]
        
        # Calculate the product of all the elements to the right of each element
        right_product = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        return answer
    
'''SPIRAL MATRIX'''
# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
#     Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#     Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
#     Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#     Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Constraints:
#     m == matrix.length
#     n == matrix[i].length
#     1 <= m, n <= 10
#     -100 <= matrix[i][j] <= 100

# Hints:
#     - Well for some problems, the best way really is to come up with some algorithms for simulation. Basically, you need to simulate what the problem asks us to do.
#     - We go boundary by boundary and move inwards. That is the essential operation. First row, last column, last row, first column, and then we move inwards by 1 and repeat. That's all. That is all the simulation that we need.
#     - Think about when you want to switch the progress on one of the indexes. If you progress on i out of [i, j], you'll shift in the same column. Similarly, by changing values for j, you'd be shifting in the same row. Also, keep track of the end of a boundary so that you can move inwards and then keep repeating. It's always best to simulate edge cases like a single column or a single row to see if anything breaks or not.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return result
        
        result = []
        row_start, row_end = 0, len(matrix) - 1
        col_start, col_end = 0, len(matrix[0]) - 1
        
        while row_start <= row_end and col_start <= col_end:
            # Traverse right
            for j in range(col_start, col_end + 1):
                result.append(matrix[row_start][j])
            row_start += 1
            
            # Traverse down
            for i in range(row_start, row_end + 1):
                result.append(matrix[i][col_end])
            col_end -= 1
            
            # Traverse left
            if row_start <= row_end:
                for j in range(col_end, col_start - 1, -1):
                    result.append(matrix[row_end][j])
                row_end -= 1
            
            # Traverse up
            if col_start <= col_end:
                for i in range(row_end, row_start - 1, -1):
                    result.append(matrix[i][col_start])
                col_start += 1
        
        return result

'''4SUM II'''
# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

# Example 1:
#     Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
#     Output: 2
#     Explanation:
#     The two tuples are:
#     1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
#     2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

# Example 2:
#     Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
#     Output: 1

# Constraints:
#     n == nums1.length
#     n == nums2.length
#     n == nums3.length
#     n == nums4.length
#     1 <= n <= 200
#     -228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dict = {}
        # Store sums of nums1 and nums2
        for num1 in nums1:
            for num2 in nums2:
                sum = num1 + num2
                if sum in dict:
                    dict[sum] += 1
                else:
                    dict[sum] = 1
        
        # Iterate through nums3 and nums4 to find sums and count occurences
        result = 0
        for num3 in nums3:
            for num4 in nums4:
                target = -(num3 + num4)
                if target in dict:
                    result += dict[target]
        
        return result

'''CONTAINER WITH MOST WATER'''
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Example 1:
#     Input: height = [1,8,6,2,5,4,8,3,7]
#     Output: 49
#     Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
#     Input: height = [1,1]
#     Output: 1

# Constraints:
#     n == height.length
#     2 <= n <= 105
#     0 <= height[i] <= 104
# Hints:
#     - If you simulate the problem, it will be O(n^2) which is not efficient.
#     - Try to use two-pointers. Set one pointer to the left and one to the right of the array. Always move the pointer that points to the lower line.
#     - How can you calculate the amount of water at each step?

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate area between pointers
            area = min(height[left], height[right]) * (right - left)
            # Update max_area if current area is greater
            max_area = max(max_area, area)
            # Move lowest line pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area