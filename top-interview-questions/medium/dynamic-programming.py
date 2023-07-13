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
        dp[m-1][n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                if i == m - 1:
                    dp[i][j] = dp[i][j + 1]
                elif j == n - 1:
                    dp[i][j] = dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
            
        return dp[0][0]