'''HAPPY NUMBER'''
# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Example 1:
#     Input: n = 19
#     Output: true
#     Explanation:
#     12 + 92 = 82
#     82 + 22 = 68
#     62 + 82 = 100
#     12 + 02 + 02 = 1

# Example 2:
#     Input: n = 2
#     Output: false

# Constraints:
#     1 <= n <= 231 - 1

class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next_number(num):
            # Calculate sum of the squares of the digits
            total_sum = 0
            while num > 0:
                digit = num % 10
                total_sum += digit ** 2
                num //= 10
            return total_sum
        
        slow = fast = n
        while True:
            # Move slow pointer one step
            slow = get_next_number(slow)
            # Move fast pointer two steps
            fast = get_next_number(get_next_number(fast))

            # If fast pointer reaches 1, number is happy
            if fast == 1:
                return True
            # If there is a cycle, numeber is not happy
            if slow == fast:
                return False

'''FACTORIAL TRAILING ZEROES'''
# Given an integer n, return the number of trailing zeroes in n!.
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

# Example 1:
    # Input: n = 3
    # Output: 0
    # Explanation: 3! = 6, no trailing zero.

# Example 2:
    # Input: n = 5
    # Output: 1
    # Explanation: 5! = 120, one trailing zero.

# Example 3:
    # Input: n = 0
    # Output: 0

# Constraints:
    # 0 <= n <= 104

# Follow up: Could you write a solution that works in logarithmic time complexity?

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        divisor = 5
        while divisor <= n:
            count += n // divisor
            divisor *= 5
        return count