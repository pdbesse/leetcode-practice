from typing import List
import random

'''SHUFFLE AN ARRAY'''
# Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.
# Implement the Solution class:
# Solution(int[] nums) Initializes the object with the integer array nums.
# int[] reset() Resets the array to its original configuration and returns it.
# int[] shuffle() Returns a random shuffling of the array.
 
# Example 1:
#     Input
#     ["Solution", "shuffle", "reset", "shuffle"]
#     [[[1, 2, 3]], [], [], []]
#     Output
#     [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
#     Explanation
#     Solution solution = new Solution([1, 2, 3]);
#     solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
#                         // Any permutation of [1,2,3] must be equally likely to be returned.
#                         // Example: return [3, 1, 2]
#     solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
#     solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]

# Constraints:
#     1 <= nums.length <= 50
#     -106 <= nums[i] <= 106
#     All the elements of nums are unique.
#     At most 104 calls in total will be made to reset and shuffle.

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        self.nums = self.original
        self.original = list(self.original)
        return self.nums

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums) - 1, 0, -1):
            j = random.randint(0, i)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        
        return self.nums

'''MIN STACK'''
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
#     MinStack() initializes the stack object.
#     void push(int val) pushes the element val onto the stack.
#     void pop() removes the element on the top of the stack.
#     int top() gets the top element of the stack.
#     int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# Example 1:
# Input
#     ["MinStack","push","push","push","getMin","pop","top","getMin"]
#     [[],[-2],[0],[-3],[],[],[],[]]
# Output
#     [null,null,null,null,-3,null,0,-2]
# Explanation
#     MinStack minStack = new MinStack();
#     minStack.push(-2);
#     minStack.push(0);
#     minStack.push(-3);
#     minStack.getMin(); // return -3
#     minStack.pop();
#     minStack.top();    // return 0
#     minStack.getMin(); // return -2

# Constraints:
#     -231 <= val <= 231 - 1
#     Methods pop, top and getMin operations will always be called on non-empty stacks.
#     At most 3 * 104 calls will be made to push, pop, top, and getMin.

# Your MinStack object will be instantiated and called as such:
    # obj = MinStack()
    # obj.push(val)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()

class MinStack:
    def __init__(self):
        # stack to store elements
        self.stack = [] 
        # stack to store minimum value
        self.min_stack = [] 

    def push(self, val: int) -> None:
        # push element onto stack
        self.stack.append(val)
        # if the min stack is empty or the new value is less than or equal to the current minimum,
        # push the new value onto the min stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # if element being popped is the current minimum, pop it from the min stack as well
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        # pop element from stack
        self.stack.pop()

    def top(self) -> int:
        # return top element of the stack
        return self.stack[-1]
    
    def getMin(self) -> int:
        # return the current minimum value
        return self.min_stack[-1]