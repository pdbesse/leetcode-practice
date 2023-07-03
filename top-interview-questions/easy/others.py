from typing import List

'''NUMBER OF 1 BITS'''
# Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
# Note:
#     Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
#     In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.

# Example 1:
# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

# Example 2:
# Input: n = 00000000000000000000000010000000
# Output: 1
# Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

# Example 3:
# Input: n = 11111111111111111111111111111101
# Output: 31
# Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

# Constraints:
# The input must be a binary string of length 32.
 
# Follow up: If this function is called many times, how would you optimize it?

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        n_str = str(bin(n))[2:]
        for c in n_str:
            if c == '1':
                count += 1
        
        return count

'''HAMMING DISTANCE'''
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, return the Hamming distance between them.

# Example 1:
    # Input: x = 1, y = 4
    # Output: 2
    # Explanation:
    # 1   (0 0 0 1)
    # 4   (0 1 0 0)
    #        ↑   ↑
    # The above arrows point to positions where the corresponding bits are different.

# Example 2:
    # Input: x = 3, y = 1
    # Output: 1

# Constraints:
#     0 <= x, y <= 231 - 1

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        while x > 0 or y > 0:
            if (x & 1) != (y & 1):
                distance += 1
            x >>= 1
            y >>= 1

        return distance

'''REVERSE BITS'''
# Reverse bits of a given 32 bits unsigned integer.

# Note:
#     Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
#     In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.

# Example 1:
#     Input: n = 00000010100101000001111010011100
#     Output:    964176192 (00111001011110000010100101000000)
#     Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

# Example 2:
#     Input: n = 11111111111111111111111111111101
#     Output:   3221225471 (10111111111111111111111111111111)
#     Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
 
# Constraints:
#     The input must be a binary string of length 32

# Follow up: If this function is called many times, how would you optimize it?

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            # Shift result left by 1 and add the least significant bit of n
            result = (result << 1) | (n & 1)
            # Shift n right by 1
            n >>= 1
        
        return result

'''PASCAL'S TRIANGLE'''
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:
    # Input: numRows = 5
    # Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:
    # Input: numRows = 1
    # Output: [[1]]

# Constraints:
    # 1 <= numRows <= 30

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            row = [1] * (i+1)

            if i >= 2:
                for j in range(1, i):
                    row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            
            triangle.append(row)
        
        return triangle

'''VALID PARENTHESIS'''
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

# Example 1:
#     Input: s = "()"
#     Output: true

# Example 2:
#     Input: s = "()[]{}"
#     Output: true

# Example 3:
#     Input: s = "(]"
#     Output: false

# Constraints:
#     1 <= s.length <= 104
#     s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = {'(', '{', '['}
        closing = {')', '}', ']'}
        map = {'(': ')', '{': '}', '[': ']'}
        
        for c in s:
            if c in opening:
                stack.append(c)
            elif c in closing:
                if not stack:
                    return False
                top = stack.pop()
                if map[top] != c:
                    return False
        
        return len(stack) == 0

'''MISSING NUMBER'''
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:
#     Input: nums = [3,0,1]
#     Output: 2
#     Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:
#     Input: nums = [0,1]
#     Output: 2
#     Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:
#     Input: nums = [9,6,4,2,3,5,7,0,1]
#     Output: 8
#     Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 
# Constraints:
#     n == nums.length
#     1 <= n <= 104
#     0 <= nums[i] <= n
#     All the numbers of nums are unique.

# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Initialize missing as the last index
        missing = len(nums)

        for i, num in enumerate(nums):
            # XOR missing with the index and the number
            missing ^= i ^ num
        
        return missing