from typing import List, Optional

'''MERGE SORTED ARRAY'''
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Example 1:
#     Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#     Output: [1,2,2,3,5,6]
#     Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
#     The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:
#     Input: nums1 = [1], m = 1, nums2 = [], n = 0
#     Output: [1]
#     Explanation: The arrays we are merging are [1] and [].
#     The result of the merge is [1].

# Example 3:
#     Input: nums1 = [0], m = 0, nums2 = [1], n = 1
#     Output: [1]
#     Explanation: The arrays we are merging are [] and [1].
#     The result of the merge is [1].
#     Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

# Constraints:
#     nums1.length == m + n
#     nums2.length == n
#     0 <= m, n <= 200
#     1 <= m + n <= 200
#     -109 <= nums1[i], nums2[j] <= 109

# Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""
Do not return anything, modify nums1 in-place instead.
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m-1
        p2 = n-1
        p = m+n-1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

'''FIRST BAD VERSION'''
# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# Example 1:
#     Input: n = 5, bad = 4
#     Output: 4
#     Explanation:
#     call isBadVersion(3) -> false
#     call isBadVersion(5) -> true
#     call isBadVersion(4) -> true
#     Then 4 is the first bad version.

# Example 2:
#     Input: n = 1, bad = 1
#     Output: 1

# Constraints:
#     <= bad <= n <= 231 - 1

# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass
class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        p1 = 1
        p2 = n

        while p1 < p2:
            mid = p1 + (p2 - p1) // 2
            if isBadVersion(mid):
                p2 = mid
            else:
                p1 = mid + 1
        
        return p1