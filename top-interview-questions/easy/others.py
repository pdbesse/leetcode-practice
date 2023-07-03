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