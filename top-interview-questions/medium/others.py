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