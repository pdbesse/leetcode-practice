from typing import List

'''FIZZ BUZZ'''
# Given an integer n, return a string array answer (1-indexed) where:
    # answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    # answer[i] == "Fizz" if i is divisible by 3.
    # answer[i] == "Buzz" if i is divisible by 5.
    # answer[i] == i (as a string) if none of the above conditions are true.

# Example 1:
#     Input: n = 3
#     Output: ["1","2","Fizz"]

# Example 2:
#     Input: n = 5
#     Output: ["1","2","Fizz","4","Buzz"]

# Example 3:
#     Input: n = 15
#     Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

# Constraints:
#     1 <= n <= 104

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                out.append('FizzBuzz')
            elif i % 3 == 0:
                out.append('Fizz')
            elif i % 5 == 0:
                out.append('Buzz')
            else:
                out.append(str(i))

        return out
    
'''COUNT PRIMES'''
# Given an integer n, return the number of prime numbers that are strictly less than n.

# Example 1:
#     Input: n = 10
#     Output: 4
#     Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# Example 2:
#     Input: n = 0
#     Output: 0

# Example 3:
#     Input: n = 1
#     Output: 0

# Constraints:
#     0 <= n <= 5 * 106

# HINT: use Sieve of Eratosthenes

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        prime = [True for i in range(n+1)]
        p = 2

        while p*p < n:
            if prime[p]:
                for i in range(p*p, n+1, p):
                    prime[i] = False
            p += 1
        
        count = 0
        for p in range(2, n):
            if prime[p]:
                count += 1
        
        return count

'''POWER OF THREE'''
# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.

# Example 1:
    # Input: n = 27
    # Output: true
    # Explanation: 27 = 3^3

# Example 2:
    # Input: n = 0
    # Output: false
    # Explanation: There is no x where 3x = 0.

# Example 3:
    # Input: n = -1
    # Output: false
    # Explanation: There is no x where 3x = (-1).

# Constraints:
#     -231 <= n <= 231 - 1

# Follow up: Could you solve it without loops/recursion?
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1

'''ROMAN TO INTEGER'''
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#     I can be placed before V (5) and X (10) to make 4 and 9. 
#     X can be placed before L (50) and C (100) to make 40 and 90. 
#     C can be placed before D (500) and M (1000) to make 400 and 900.

# Given a roman numeral, convert it to an integer.

# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# Constraints:
#     1 <= s.length <= 15
#     s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
#     It is guaranteed that s is a valid roman numeral in the range [1, 3999].

# HINT: Problem is simpler to solve by working the string from back to front and using a map.

class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        out = 0
        prev = 0

        for c in reversed(s):
            cur = map[c]
            if cur < prev:
                out -= cur
            else: 
                out += cur
                prev = cur
        
        return out