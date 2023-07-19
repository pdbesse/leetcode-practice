from typing import List

'''SUM OF TWO INTEGERS'''
# Given two integers a and b, return the sum of the two integers without using the operators + and -.

# Example 1:
#     Input: a = 1, b = 2
#     Output: 3

# Example 2:
#     Input: a = 2, b = 3
#     Output: 5

# Constraints:
#     -1000 <= a, b <= 1000

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask to get the last 32 bits
        mask = 0xFFFFFFFF
        # Bit mask for a single bit
        bit_mask = 0x1

        while b != 0:
            # Calculate the sum without considering the carry
            sum_without_carry = (a ^ b) & mask
            # Calculate the carry
            carry = ((a & b) << 1) & mask
            # Update a and b for the next iteration
            a = sum_without_carry
            b = carry

        # Convert the 32-bit sum to signed integer
        if a & (bit_mask << 31):
            a = ~(a ^ mask)
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)
    
'''EVALUATE REVERSE POLISH NOTATION'''
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
# Evaluate the expression. Return an integer that represents the value of the expression.
# Note that:
#     The valid operators are '+', '-', '*', and '/'.
#     Each operand may be an integer or another expression.
#     The division between two integers always truncates toward zero.
#     There will not be any division by zero.
#     The input represents a valid arithmetic expression in a reverse polish notation.
#     The answer and all the intermediate calculations can be represented in a 32-bit integer.

# Example 1:
#     Input: tokens = ["2","1","+","3","*"]
#     Output: 9
#     Explanation: ((2 + 1) * 3) = 9

# Example 2:
#     Input: tokens = ["4","13","5","/","+"]
#     Output: 6
#     Explanation: (4 + (13 / 5)) = 6

# Example 3:
#     Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
#     Output: 22
#     Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
#     = ((10 * (6 / (12 * -11))) + 17) + 5
#     = ((10 * (6 / -132)) + 17) + 5
#     = ((10 * 0) + 17) + 5
#     = (0 + 17) + 5
#     = 17 + 5
#     = 22

# Constraints:
#     1 <= tokens.length <= 104
#     tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])

        for token in tokens:
            if token in operators:
                operand2 = stack.pop()
                operand1 = stack.pop()

                result =  self.performOperation(token, operand1, operand2)
                stack.append(result)
            else:
                operand = int(token)
                stack.append(operand)
        
        return stack.pop()
    
    def performOperation(self, op, operand1, operand2):
        if op == '+':
            return operand1 + operand2
        elif op == '-':
            return operand1 - operand2
        elif op == '*':
            return operand1 * operand2
        elif op == '/':
            return int(operand1 / operand2)

        return 0

'''MAJORITY ELEMENT'''
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
#     Input: nums = [3,2,3]
#     Output: 3

# Example 2:
#     Input: nums = [2,2,1,1,1,2,2]
#     Output: 2

# Constraints:
#     n == nums.length
#     1 <= n <= 5 * 104
#     -109 <= nums[i] <= 109

# Follow-up: Could you solve the problem in linear time and in O(1) space?

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate