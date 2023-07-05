from typing import List, Optional

'''CLIMBING STAIRS'''
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
#     Input: n = 2
#     Output: 2
#     Explanation: There are two ways to climb to the top.
#     1. 1 step + 1 step
#     2. 2 steps

# Example 2:
#     Input: n = 3
#     Output: 3
#     Explanation: There are three ways to climb to the top.
#     1. 1 step + 1 step + 1 step
#     2. 1 step + 2 steps
#     3. 2 steps + 1 step

# Constraints:
#     1 <= n <= 45

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

'''BEST TIME TO BUY AND SELL A STOCK'''
#     You are given an array prices where prices[i] is the price of a given stock on the ith day.
#     You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#     Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
#     Input: prices = [7,1,5,3,6,4]
#     Output: 5
#     Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#     Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
#     Input: prices = [7,6,4,3,1]
#     Output: 0
#     Explanation: In this case, no transactions are done and the max profit = 0.

# Constraints:
#     prices.length <= 105
#     0 <= prices[i] <= 104

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        dp = [0]*len(prices)
        min_price = prices[0]

        for i in range(1,len(prices)):
            min_price = min(min_price, prices[i])
            dp[i] = max(dp[i-1], prices[i] - min_price)

        return dp[-1]

'''MAXIMUM SUBARRAY'''
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:
#     Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#     Output: 6
#     Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:
#     Input: nums = [1]
#     Output: 1
#     Explanation: The subarray [1] has the largest sum 1.

# Example 3:
#     Input: nums = [5,4,-1,7,8]
#     Output: 23
#     Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

# Constraints:
#     1 <= nums.length <= 105
#     -104 <= nums[i] <= 104

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        
        return max_sum

'''HOUSE ROBBER'''
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:
#     Input: nums = [1,2,3,1]
#     Output: 4
#     Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#     Total amount you can rob = 1 + 3 = 4.

# Example 2:
#     Input: nums = [2,7,9,3,1]
#     Output: 12
#     Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#     Total amount you can rob = 2 + 9 + 1 = 12.

# Constraints:
#     1 <= nums.length <= 100
#     0 <= nums[i] <= 400

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        return dp[-1]