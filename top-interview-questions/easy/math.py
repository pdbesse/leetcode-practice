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