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

'''BEST TIME TO BUY AND SELL A STOCK WITH COOLDOWN'''
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
#     After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# Example 1:
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

# Example 2:
# Input: prices = [1]
# Output: 0

# Constraints:
# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            n = len(prices)
            
            if n <= 1:
                return 0
            
            # Initialize arrays to keep track of the maximum profit on each day
            # where `buy[i]` represents the maximum profit if the last action is a buy on day `i`,
            # and `sell[i]` represents the maximum profit if the last action is a sell on day `i`.
            buy = [0] * n
            sell = [0] * n
            
            # Base cases
            buy[0] = -prices[0]  # Buying on the first day
            sell[0] = 0
            
            for i in range(1, n):
                # To get the maximum profit at day `i`, we can either:
                # 1. Keep the profit from the previous day (no action on day `i`).
                # 2. Buy on day `i`, which means we need to take the maximum of the profit from `buy[i-2]` minus the price on day `i` or `sell[i-1]` minus the price on day `i`.
                buy[i] = max(buy[i-1], (sell[i-2] if i >= 2 else 0) - prices[i])
                
                # To get the maximum profit at day `i`, we can either:
                # 1. Keep the profit from the previous day (no action on day `i`).
                # 2. Sell on day `i`, which means we add the profit from the previous buy (`buy[i-1]`) to the price on day `i`.
                sell[i] = max(sell[i-1], buy[i-1] + prices[i])
            
            return sell[n-1]  # The maximum profit on the last day (sell[n-1]) is the answer.

'''PERFECT SQUARES'''
# Given an integer n, return the least number of perfect square numbers that sum to n.
# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

# Example 1:
#     Input: n = 12
#     Output: 3
#     Explanation: 12 = 4 + 4 + 4.

# Example 2:
#     Input: n = 13
#     Output: 2
#     Explanation: 13 = 4 + 9.

# Constraints:
#     1 <= n <= 104

class Solution:
    def numSquares(self, n: int) -> int:
        # Create a list to store the minimum number of perfect squares needed for each number from 0 to n
        dp = [0] * (n + 1)
        
        # Calculate the minimum number of perfect squares needed for each number
        for i in range(1, n + 1):
            # Initialize with the maximum possible value
            dp[i] = i
            
            # Check each perfect square number less than or equal to i
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        
        return dp[n]