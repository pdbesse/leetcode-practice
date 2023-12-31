from typing import List

'''JUMP GAME'''
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# Example 1:
#     Input: nums = [2,3,1,1,4]
#     Output: true
#     Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
#     Input: nums = [3,2,1,0,4]
#     Output: false
#     Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

# Constraints:
#     1 <= nums.length <= 104
#     0 <= nums[i] <= 105

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n

        dp[n-1] = True

        for i in range(n-2,-1,-1):
            max_jump = min(i+nums[i], n-1)

            for j in range(i+1, max_jump+1):
                if dp[j]:
                    dp[i] = True
                    break
        
        return dp[0]
    
'''UNIQUE PATHS'''
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The test cases are generated so that the answer will be less than or equal to 2 * 109.

# Example 1:
#     Input: m = 3, n = 7
#     Output: 28

# Example 2:
#     Input: m = 3, n = 2
#     Output: 3
#     Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
#     1. Right -> Down -> Down
#     2. Down -> Down -> Right
#     3. Down -> Right -> Down

# Constraints:
#     1 <= m, n <= 100

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]

        return dp[m-1][n-1]
    
'''COIN CHANGE'''
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

# Example 1:
#     Input: coins = [1,2,5], amount = 11
#     Output: 3
#     Explanation: 11 = 5 + 5 + 1

# Example 2:
#     Input: coins = [2], amount = 3
#     Output: -1

# Example 3:
#     Input: coins = [1], amount = 0
#     Output: 0

# Constraints:
#     1 <= coins.length <= 12
#     1 <= coins[i] <= 231 - 1
#     0 <= amount <= 104

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float("inf")]*(amount+1) for _ in range(len(coins))]
        dp[0][0] = 0
        firstCoin = coins[0]
        for i in range(amount+1):
            if i >= firstCoin:
                dp[0][i] = dp[0][i-firstCoin] + 1

        for i in range(1,len(coins)):
            for j in range(amount+1):
                if j >= coins[i]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i]]+1)
                else:
                    dp[i][j] = dp[i-1][j]
        # print(dp)
        if dp[-1][-1] != float("inf"):
            return dp[-1][-1]
        else:
            return -1

'''LONGEST INCREASING SUBSEQUENCE'''
# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# Example 1:
#     Input: nums = [10,9,2,5,3,7,101,18]
#     Output: 4
#     Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Example 2:
#     Input: nums = [0,1,0,3,2,3]
#     Output: 4

# Example 3:
#     Input: nums = [7,7,7,7,7,7,7]
#     Output: 1

# Constraints:
#     1 <= nums.length <= 2500
#     -104 <= nums[i] <= 104

# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        tails = [0]*len(nums)
        size = 0

        for num in nums:
            left,right = 0,size
            while left < right:
                mid = left + (right-left)//2
                if tails[mid] < num:
                    left = mid+1
                else:
                    right = mid
            tails[left] = num
            size = max(size, left+1)
        
        return size