from typing import List, Optional
from queue import Queue

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