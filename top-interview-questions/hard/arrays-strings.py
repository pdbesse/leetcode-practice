from typing import List

'''PRODUCT OF ARRAY EXCEPT SELF'''
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
    # Input: nums = [1,2,3,4]
    # Output: [24,12,8,6]

# Example 2:
    # Input: nums = [-1,1,0,-3,3]
    # Output: [0,0,9,0,0]

# Constraints:
    # 2 <= nums.length <= 105
    # -30 <= nums[i] <= 30
    # The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # Calculate the product of all the elements to the left of each element
        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i-1]
        
        # Calculate the product of all the elements to the right of each element
        right_product = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        return answer
    
'''SPIRAL MATRIX'''
# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
#     Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#     Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
#     Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#     Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Constraints:
#     m == matrix.length
#     n == matrix[i].length
#     1 <= m, n <= 10
#     -100 <= matrix[i][j] <= 100

# Hints:
#     - Well for some problems, the best way really is to come up with some algorithms for simulation. Basically, you need to simulate what the problem asks us to do.
#     - We go boundary by boundary and move inwards. That is the essential operation. First row, last column, last row, first column, and then we move inwards by 1 and repeat. That's all. That is all the simulation that we need.
#     - Think about when you want to switch the progress on one of the indexes. If you progress on i out of [i, j], you'll shift in the same column. Similarly, by changing values for j, you'd be shifting in the same row. Also, keep track of the end of a boundary so that you can move inwards and then keep repeating. It's always best to simulate edge cases like a single column or a single row to see if anything breaks or not.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return result
        
        result = []
        row_start, row_end = 0, len(matrix) - 1
        col_start, col_end = 0, len(matrix[0]) - 1
        
        while row_start <= row_end and col_start <= col_end:
            # Traverse right
            for j in range(col_start, col_end + 1):
                result.append(matrix[row_start][j])
            row_start += 1
            
            # Traverse down
            for i in range(row_start, row_end + 1):
                result.append(matrix[i][col_end])
            col_end -= 1
            
            # Traverse left
            if row_start <= row_end:
                for j in range(col_end, col_start - 1, -1):
                    result.append(matrix[row_end][j])
                row_end -= 1
            
            # Traverse up
            if col_start <= col_end:
                for i in range(row_end, row_start - 1, -1):
                    result.append(matrix[i][col_start])
                col_start += 1
        
        return result

'''4SUM II'''
# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

# Example 1:
#     Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
#     Output: 2
#     Explanation:
#     The two tuples are:
#     1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
#     2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

# Example 2:
#     Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
#     Output: 1

# Constraints:
#     n == nums1.length
#     n == nums2.length
#     n == nums3.length
#     n == nums4.length
#     1 <= n <= 200
#     -228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dict = {}
        # Store sums of nums1 and nums2
        for num1 in nums1:
            for num2 in nums2:
                sum = num1 + num2
                if sum in dict:
                    dict[sum] += 1
                else:
                    dict[sum] = 1
        
        # Iterate through nums3 and nums4 to find sums and count occurences
        result = 0
        for num3 in nums3:
            for num4 in nums4:
                target = -(num3 + num4)
                if target in dict:
                    result += dict[target]
        
        return result

'''CONTAINER WITH MOST WATER'''
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Example 1:
#     Input: height = [1,8,6,2,5,4,8,3,7]
#     Output: 49
#     Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
#     Input: height = [1,1]
#     Output: 1

# Constraints:
#     n == height.length
#     2 <= n <= 105
#     0 <= height[i] <= 104
# Hints:
#     - If you simulate the problem, it will be O(n^2) which is not efficient.
#     - Try to use two-pointers. Set one pointer to the left and one to the right of the array. Always move the pointer that points to the lower line.
#     - How can you calculate the amount of water at each step?

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate area between pointers
            area = min(height[left], height[right]) * (right - left)
            # Update max_area if current area is greater
            max_area = max(max_area, area)
            # Move lowest line pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
    
'''GAME OF LIFE'''
# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

# Example 1:
    # Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    # Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

# Example 2:
    # Input: board = [[1,1],[1,0]]
    # Output: [[1,1],[1,1]]

# Constraints:
#     m == board.length
#     n == board[i].length
#     1 <= m, n <= 25
#     board[i][j] is 0 or 1.

# Follow up:
    # Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
    # In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        # Define a helper function to count live neighbors
        def count_live_neighbors(row: int, col: int) -> int:
            count = 0
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for dr, dc in directions:
                r = row + dr
                c = col + dc
                if 0 <= r < rows and 0 <= c < cols and abs(board[r][c]) == 1:
                    count += 1
            return count

        # Update the state of the board based on the rules of the Game of Life
        for r in range(rows):
            for c in range(cols):
                live_neighbors = count_live_neighbors(r, c)
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1  # Mark live cell that will die as -1
                elif board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2  # Mark dead cell that will become live as 2

        # Restore the marked cells to their correct values
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == -1:
                    board[r][c] = 0
                elif board[r][c] == 2:
                    board[r][c] = 1

'''FIRST MISSING POSITIVE'''
# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

# Example 1:
#     Input: nums = [1,2,0]
#     Output: 3
#     Explanation: The numbers in the range [1,2] are all in the array.

# Example 2:
#     Input: nums = [3,4,-1,1]
#     Output: 2
#     Explanation: 1 is in the array but 2 is missing.

# Example 3:
#     Input: nums = [7,8,9,11,12]
#     Output: 1
#     Explanation: The smallest positive integer 1 is missing.

# Constraints:
#     1 <= nums.length <= 105
#     -231 <= nums[i] <= 231 - 1

# Hints: 
# - Think about how you would solve the problem in non-constant space. Can you apply that logic to the existing space?
# - We don't care about duplicates or non-positive integers
# - Remember that O(2n) = O(n)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Remove non-positive integers and duplicates
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Step 2: Find the first index where nums[i] != i+1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # Step 3: All elements are in their correct positions, so the missing positive is n+1
        return n + 1