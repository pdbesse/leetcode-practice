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

'''FIND THE CELEBRITY'''
# Suppose you are at a party with n people labeled from 0 to n - 1 and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know the celebrity, but the celebrity does not know any of them.
# Now you want to find out who the celebrity is or verify that there is not one. You are only allowed to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).
# You are given a helper function bool knows(a, b) that tells you whether a knows b. Implement a function int findCelebrity(n). There will be exactly one celebrity if they are at the party.
# Return the celebrity's label if there is a celebrity at the party. If there is no celebrity, return -1.

# Example 1:
#     Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
#     Output: 1
#     Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

# Example 2:
#     Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
#     Output: -1
#     Explanation: There is no celebrity.

# Constraints:
#     n == graph.length == graph[i].length
#     2 <= n <= 100
#     graph[i][j] is 0 or 1.
#     graph[i][i] == 1

# Follow up: If the maximum number of allowed calls to the API knows is 3 * n, could you find a solution without exceeding the maximum number of calls?

# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    pass
class Solution:
    def findCelebrity(self, n: int) -> int:
        # Start with first person as candidate
        candidate = 0

        # Find potential celebrity candidate
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i

        # Verify if candidate is celebrity
        for i in range(n):
            if i != candidate:
                # If candidate knows someone or someone doesn't know candidate, return -1
                if knows(candidate, i) or not knows(i, candidate):
                    return -1
        
        # Return candidate if they satisfy celebrity condition
        return candidate

'''TASK SCHEDULER'''
# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
# Return the least number of units of times that the CPU will take to finish all the given tasks.

# Example 1:
#     Input: tasks = ["A","A","A","B","B","B"], n = 2
#     Output: 8
#     Explanation: 
#     A -> B -> idle -> A -> B -> idle -> A -> B
#     There is at least 2 units of time between any two same tasks.

# Example 2:
#     Input: tasks = ["A","A","A","B","B","B"], n = 0
#     Output: 6
#     Explanation: On this case any permutation of size 6 would work since n = 0.
#     ["A","A","A","B","B","B"]
#     ["A","B","A","B","A","B"]
#     ["B","B","B","A","A","A"]
# ...
# And so on.

# Example 3:
#     Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
#     Output: 16
#     Explanation: 
#     One possible solution is
#     A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

# Constraints:
#     1 <= task.length <= 104
#     tasks[i] is upper-case English letter.
#     The integer n is in the range [0, 100].

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = [0] * 26  # Assuming only uppercase English letters
        
        for task in tasks:
            task_counts[ord(task) - ord('A')] += 1
        
        task_counts.sort(reverse=True)
        
        max_freq = task_counts[0]
        max_count = 0
        
        for freq in task_counts:
            if freq == max_freq:
                max_count += 1
            else:
                break
        
        total_intervals = (max_freq - 1) * (n + 1) + max_count
        
        return max(total_intervals, len(tasks))