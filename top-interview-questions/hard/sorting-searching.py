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

'''KTH SMALLEST ELEMENT IN A SORTED LIST'''
# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
# You must find a solution with a memory complexity better than O(n2).

# Example 1:
#     Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
#     Output: 13
#     Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

# Example 2:
#     Input: matrix = [[-5]], k = 1
#     Output: -5

# Constraints:
#     n == matrix.length == matrix[i].length
#     1 <= n <= 300
#     -109 <= matrix[i][j] <= 109
#     All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
#     1 <= k <= n2

# Follow up:
#     Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
#     Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left, right = matrix[0][0], matrix[n - 1][n - 1]

        while left < right:
            mid = left + (right - left) // 2
            count = self.countLessEqual(matrix, mid, n)
            
            if count < k:
                left = mid + 1
            else:
                right = mid
        
        return left
    
    def countLessEqual(self, matrix: List[List[int]], target: int, n: int) -> int:
        count = 0
        row, col = n - 1, 0
        
        while row >= 0 and col < n:
            if matrix[row][col] <= target:
                count += row + 1
                col += 1
            else:
                row -= 1
        
        return count
    
'''MEDIAN OF TWO SORTED ARRAYS'''
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:
#     Input: nums1 = [1,3], nums2 = [2]
#     Output: 2.00000
#     Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
#     Input: nums1 = [1,2], nums2 = [3,4]
#     Output: 2.50000
#     Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Constraints:
#     nums1.length == m
#     nums2.length == n
#     0 <= m <= 1000
#     0 <= n <= 1000
#     1 <= m + n <= 2000
#     -106 <= nums1[i], nums2[i] <= 106

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Combine sorted arrays
        merged = []
        i, j = 0, 0
        n = len(nums1)
        m = len(nums2)

        while i < n and j < m:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        # Add remaining elements from nums1 and nums2
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])

        # Calculate median
        merged_len = len(merged)
        if merged_len % 2 == 0:
            mid = merged_len // 2
            median = (merged[mid-1] + merged[mid]) / 2
        else:
            mid = merged_len // 2
            median = merged[mid]
        
        return median