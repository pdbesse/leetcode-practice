from collections import deque
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
    
'''LONGEST CONSECUTIVE SEQUENCE'''
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Example 1:
#     Input: nums = [100,4,200,1,3,2]
#     Output: 4
#     Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
#     Input: nums = [0,3,7,2,5,8,4,6,0,1]
#     Output: 9

# Constraints:
#     0 <= nums.length <= 105
#     -109 <= nums[i] <= 109

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        max_length = 0

        for num in num_set:
            # Check if current num is start of sequence
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                # Calculate length of sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                max_length = max(max_length, current_length)
            
        return max_length

'''FIND THE DUPLICATE NUMBER'''
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

# Example 1:
#     Input: nums = [1,3,4,2,2]
#     Output: 2

# Example 2:
#     Input: nums = [3,1,3,4,2]
#     Output: 3

# Constraints:
#     1 <= n <= 105
#     nums.length == n + 1
#     1 <= nums[i] <= n
#     All the integers in nums appear only once except for precisely one integer which appears two or more times.
 
# Follow up:
#     How can we prove that at least one duplicate number must exist in nums?
#     Can you solve the problem in linear runtime complexity?

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Find intersection of two pointers
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        # Find entrance to cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
    
'''BASIC CALCULATOR II'''
# Given a string s which represents an expression, evaluate this expression and return its value. 
# The integer division should truncate toward zero.
# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().


# Example 1:
#     Input: s = "3+2*2"
#     Output: 7

# Example 2:
#     Input: s = " 3/2 "
#     Output: 1

# Example 3:
#     Input: s = " 3+5 / 2 "
#     Output: 5

# Constraints:
#     1 <= s.length <= 3 * 105
#     s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
#     s represents a valid expression.
#     All the integers in the expression are non-negative integers in the range [0, 231 - 1].
#     The answer is guaranteed to fit in a 32-bit integer.

class Solution:
    def calculate(self, s: str) -> int:
        def perform_operation(num2, num1, operator):
            if operator == '+':
                return num1 + num2
            elif operator == '-':
                return num1 - num2
            elif operator == '*':
                return num1 * num2
            elif operator == '/':
                return num1 // num2  # Integer division, truncates toward zero

        def precedence(op):
            if op == '+' or op == '-':
                return 1
            elif op == '*' or op == '/':
                return 2
            return 0

        # Remove all spaces from the input string
        s = s.replace(" ", "")
        
        num_stack = []  # Stack to store operands (numbers)
        op_stack = []   # Stack to store operators (+, -, *, /)

        i = 0
        while i < len(s):
            if s[i].isdigit():  # If it's a digit, extract the entire number
                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1
                num = int(s[i:j])
                num_stack.append(num)
                i = j
            else:  # If it's an operator, process the operator based on precedence
                while (len(op_stack) > 0 and 
                       precedence(op_stack[-1]) >= precedence(s[i])):
                    num2 = num_stack.pop()
                    num1 = num_stack.pop()
                    operator = op_stack.pop()
                    result = perform_operation(num2, num1, operator)
                    num_stack.append(result)
                op_stack.append(s[i])
                i += 1
        
        # Perform any remaining operations left in the stacks
        while len(op_stack) > 0:
            num2 = num_stack.pop()
            num1 = num_stack.pop()
            operator = op_stack.pop()
            result = perform_operation(num2, num1, operator)
            num_stack.append(result)
        
        return num_stack[0]

'''SLIDING MAXIMUM WINDOW'''
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.

# Example 1:
#     Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
#     Output: [3,3,5,5,6,7]
#     Explanation: 
#     Window position                Max
#     ---------------               -----
#     [1  3  -1] -3  5  3  6  7       3
#     1 [3  -1  -3] 5  3  6  7       3
#     1  3 [-1  -3  5] 3  6  7       5
#     1  3  -1 [-3  5  3] 6  7       5
#     1  3  -1  -3 [5  3  6] 7       6
#     1  3  -1  -3  5 [3  6  7]      7

# Example 2:
#     Input: nums = [1], k = 1
#     Output: [1]

# Constraints:
#     1 <= nums.length <= 105
#     -104 <= nums[i] <= 104
#     1 <= k <= nums.length
# Hints:
#     - How about using a data structure such as deque (double-ended queue)? 
#     - The queue size need not be the same as the window’s size. 
#     - Remove redundant elements and the queue should store only elements that need to be considered.

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        result = []
        window = deque()

        for i in range(len(nums)):
            # Remove elements from the front that are no longer part of the window
            while window and window[0] < i - k + 1:
                window.popleft()

            # Remove elements from the back that are smaller than the current element
            while window and nums[window[-1]] < nums[i]:
                window.pop()

            # Append the current element's index to the back of the deque
            window.append(i)

            # If the current index is greater than or equal to k - 1,
            # add the maximum element to the result list
            if i >= k - 1:
                result.append(nums[window[0]])

        return result
    
'''MINIMUM WINDOW SUBSTRING'''
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.

# Example 1:
    # Input: s = "ADOBECODEBANC", t = "ABC"
    # Output: "BANC"
    # Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:
    # Input: s = "a", t = "a"
    # Output: "a"
    # Explanation: The entire string s is the minimum window.

# Example 3:
    # Input: s = "a", t = "aa"
    # Output: ""
    # Explanation: Both 'a's from t must be included in the window.
    # Since the largest window of s only has one 'a', return empty string.

# Constraints:
#     m == s.length
#     n == t.length
#     1 <= m, n <= 105
#     s and t consist of uppercase and lowercase English letters.

# Follow up: Could you find an algorithm that runs in O(m + n) time?

# Hints: 
#     - Use two pointers to create a window of letters in s, which would have all the characters from t.
#     - Expand the right pointer until all the characters of t are covered. 
#     - Once all the characters are covered, move the left pointer and ensure that all the characters are still covered to minimize the subarray size.
#     - Continue expanding the right and left pointers until you reach the end of s.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Initialize two dictionaries to store the frequency of characters in strings s and t
        char_count_s = {}
        char_count_t = {}
        for char in t:
            char_count_t[char] = char_count_t.get(char, 0) + 1
        
        # Function to check if all characters of t are covered in the current window
        def is_window_valid():
            for char, count in char_count_t.items():
                if char_count_s.get(char, 0) < count:
                    return False
            return True
        
        left, right = 0, 0
        min_window = float('inf')  # Initialize with a large value
        result = ""
        
        while right < len(s):
            # Expand the window to the right
            char_count_s[s[right]] = char_count_s.get(s[right], 0) + 1
            
            # Shrink the window from the left if it's valid and try to minimize the size
            while is_window_valid() and left <= right:
                window_size = right - left + 1
                if window_size < min_window:
                    min_window = window_size
                    result = s[left:right+1]
                
                char_count_s[s[left]] -= 1
                left += 1
            
            right += 1
        
        return result