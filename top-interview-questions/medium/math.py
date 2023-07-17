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

'''EXCEL SHEET COLUMN NUMBER'''
# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.
# For example:
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
#     ...

# Example 1:
#     Input: columnTitle = "A"
#     Output: 1

# Example 2:
#     Input: columnTitle = "AB"
#     Output: 28

# Example 3:
#     Input: columnTitle = "ZY"
#     Output: 701

# Constraints:
#     1 <= columnTitle.length <= 7
#     columnTitle consists only of uppercase English letters.
#     columnTitle is in the range ["A", "FXSHRXW"].

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            value = ord(char) - ord('A') + 1
            result = result * 26 + value

        return result
    
'''POW(X,N)'''
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Example 1:
#     Input: x = 2.00000, n = 10
#     Output: 1024.00000

# Example 2:
#     Input: x = 2.10000, n = 3
#     Output: 9.26100

# Example 3:
#     Input: x = 2.00000, n = -2
#     Output: 0.25000
#     Explanation: 2-2 = 1/22 = 1/4 = 0.25

# Constraints:
#     -100.0 < x < 100.0
#     -231 <= n <= 231-1
#     n is an integer.
#     Either x is not zero or n > 0.
#     -104 <= xn <= 104

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2

        return result
    
'''SQRT(X)'''
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# Example 1:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

# Constraints:
# 0 <= x <= 231 - 1

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        left = 1
        right = x

        while left <= right:
            mid = left + (right-left) // 2
            sqrt = x // mid

            if sqrt == mid:
                return mid
            elif sqrt < mid:
                right = mid - 1
            else:
                left = mid + 1

        return right