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
        out = []
        prime = [True for i in range(n+1)]
        p = 2

        while p*p <= n:
            if (prime[p] == True):
                for i in range(p*p, n+1, p):
                    prime[i] = False
            p += 1
        
        for p in range(2, n+1):
            if prime[p]:
                out.append[p]
        
        return out