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

'''WORD BREAK'''
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:
#     Input: s = "leetcode", wordDict = ["leet","code"]
#     Output: true
#     Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:
#     Input: s = "applepenapple", wordDict = ["apple","pen"]
#     Output: true
#     Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#     Note that you are allowed to reuse a dictionary word.

# Example 3:
#     Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
#     Output: false

# Constraints:
#     1 <= s.length <= 300
#     1 <= wordDict.length <= 1000
#     1 <= wordDict[i].length <= 20
#     s and wordDict[i] consist of only lowercase English letters.
#     All the strings of wordDict are unique.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        wordSet = set(wordDict)

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        
        return dp[n]
    
'''WORD BREAK II'''
# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:
#     Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
#     Output: ["cats and dog","cat sand dog"]

# Example 2:
#     Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
#     Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
#     Explanation: Note that you are allowed to reuse a dictionary word.

# Example 3:
#     Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
#     Output: []

# Constraints:
#     1 <= s.length <= 20
#     1 <= wordDict.length <= 1000
#     1 <= wordDict[i].length <= 10
#     s and wordDict[i] consist of only lowercase English letters.
#     All the strings of wordDict are unique.
#     Input is generated in a way that the length of the answer doesn't exceed 105.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Create set of valid words for faster lookup
        wordSet = set(wordDict)
        n = len(s) + 1

        # DP array to store possible sentences for each index
        dp = [[] for _ in range(n)]
        dp[0] = ['']

        for end in range(1, n):
            for start in range(end):
                word = s[start:end]
                if word in wordSet:
                    for prev_sent in dp[start]:
                        if prev_sent:
                            dp[end].append(prev_sent + ' ' + word)
                        else:
                            dp[end].append(word)
        
        return dp[len(s)]

'''BURST BALLONS'''
# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.
# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.
# Return the maximum coins you can collect by bursting the balloons wisely.

# Example 1:
    # Input: nums = [3,1,5,8]
    # Output: 167
    # Explanation:
    # nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
    # coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

# Example 2:
    # Input: nums = [1,5]
    # Output: 10

# Constraints:
    # n == nums.length
    # 1 <= n <= 300
    # 0 <= nums[i] <= 100

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        new_nums = [1] + nums + [1]
        memo = {}

        def dp(i, j):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            max_coins = 0
            for k in range(i, j + 1):
                max_coins = max(max_coins, dp(i, k - 1) + dp(k + 1, j) + new_nums[i - 1] * new_nums[k] * new_nums[j + 1])

            memo[(i, j)] = max_coins
            return max_coins

        return dp(1, n)