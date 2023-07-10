from typing import List
import heapq

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

'''TOP K FREQUENT ELEMENTS'''
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
#     Input: nums = [1,1,1,2,2,3], k = 2
#     Output: [1,2]

# Example 2:
#     Input: nus = [1], k = 1
#     Output: [1]

# Constraints:
#     1 <= nums.length <= 105
#     -104 <= nums[i] <= 104
#     k is in the range [1, the number of unique elements in the array].
#     It is guaranteed that the answer is unique.

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a dictionary to store the frequency of each element
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        # Create a list of tuples from the dictionary and sort it
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        # Return the first k elements of the sorted list
        return [sorted_freq[i][0] for i in range(k)]

'''KTH LARGE ELEMENT IN AN ARRAY'''
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?

# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

# Constraints:
# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for i in range(k):
            heapq.heappush(pq, nums[i])
        
        for num in nums[k:]:
            if num > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, num)
            
        return pq[0]

'''FIND PEAK ELEMENT'''
# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
# You must write an algorithm that runs in O(log n) time.

# Example 1:
#     Input: nums = [1,2,3,1]
#     Output: 2
#     Explanation: 3 is a peak element and your function should return the index number 2.

# Example 2:
#     Input: nums = [1,2,1,3,5,6,4]
#     Output: 5
#     Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

# Constraints:
#     1 <= nums.length <= 1000
#     -231 <= nums[i] <= 231 - 1
#     nums[i] != nums[i + 1] for all valid i.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        
        return left