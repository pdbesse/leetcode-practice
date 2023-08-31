from typing import List

'''QUEUE RECONSTRUCTION BY HEIGHT'''
# You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.
# Reconstruct and return the queue that is represented by the input array people. The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).

# Example 1:
#     Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
#     Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
#     Explanation:
#         Person 0 has height 5 with no other people taller or the same height in front.
#         Person 1 has height 7 with no other people taller or the same height in front.
#         Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
#         Person 3 has height 6 with one person taller or the same height in front, which is person 1.
#         Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
#         Person 5 has height 7 with one person taller or the same height in front, which is person 1.
#         Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.

# Example 2:
#     Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
#     Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]

# Constraints:
#     1 <= people.length <= 2000
#     0 <= hi <= 106
#     0 <= ki < people.length
#     It is guaranteed that the queue can be reconstructed.

# Hints:
    # - What can you say about the position of the shortest person? If the position of the shortest person is i, how many people would be in front of the shortest person?
    # - Once you fix the position of the shortest person, what can you say about the position of the second shortest person?

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort the people array in descending order of height (h) and ascending order of k
        people.sort(key=lambda x: (-x[0], x[1]))

        # Initialize an empty result array
        queue = []

        # Insert people into the result array based on their k value
        for person in people:
            queue.insert(person[1], person)

        return queue
    
# '''TRAPPING RAIN WATER'''
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:
#     Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
#     Output: 6
#     Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
#     Input: height = [4,2,0,3,2,5]
#     Output: 9

# Constraints:
#     n == height.length
#     1 <= n <= 2 * 104
#     0 <= height[i] <= 105

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        left = 0
        right = n - 1
        left_max = right_max = trapped_water = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    trapped_water += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    trapped_water += right_max - height[right]
                right -= 1
        
        return trapped_water