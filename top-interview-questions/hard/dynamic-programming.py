from typing import List

'''MAXIMUM PRODUCT SUBARRAY'''
# Given an integer array nums, find a subarray that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.

# Example 1:
#     Input: nums = [2,3,-2,4]
#     Output: 6
#     Explanation: [2,3] has the largest product 6.

# Example 2:
#     Input: nums = [-2,0,-1]
#     Output: 0
#     Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

# Constraints:
#     1 <= nums.length <= 2 * 104
#     -10 <= nums[i] <= 10
#     The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_product = nums[0]
        min_product = nums[0]
        result = max_product
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_product, min_product = min_product, max_product
                
            max_product = max(nums[i], max_product * nums[i])
            min_product = min(nums[i], min_product * nums[i])
            
            result = max(result, max_product)
        
        return result
    
'''DECODE WAYS'''
# A message containing letters from A-Z can be encoded into numbers using the following mapping:
#     'A' -> "1"
#     'B' -> "2"
#     ...
#     'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
#     "AAJF" with the grouping (1 1 10 6)
#     "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
# Given a string s containing only digits, return the number of ways to decode it.
# The test cases are generated so that the answer fits in a 32-bit integer.

# Example 1:
#     Input: s = "12"
#     Output: 2
#     Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

# Example 2:
#     Input: s = "226"
#     Output: 3
#     Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

# Example 3:
#     Input: s = "06"
#     Output: 0
#     Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

# Constraints:
#     1 <= s.length <= 100
#     s contains only digits and may contain leading zero(s).

class Solution:
    def numDecodings(self, s: str) -> int:
        # Handle base cases
        if not s:
            return 0

        # Create a DP array to store the number of ways to decode a substring
        dp = [0] * (len(s) + 1)
        dp[0] = 1  # Empty string can be decoded in 1 way

        # Loop through the string
        for i in range(1, len(s) + 1):
            # Check if the current digit is not '0'
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]  # Add the number of ways from the previous position

            # Check if the current and previous digits form a valid mapping
            if i > 1 and '10' <= s[i - 2:i] <= '26':
                dp[i] += dp[i - 2]  # Add the number of ways from two positions back

        return dp[len(s)]  # The result is stored in the last position of the DP array
        