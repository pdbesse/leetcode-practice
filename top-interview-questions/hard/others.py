from typing import List
import heapq

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
    
'''THE SKYLINE PROBLEM'''
# - A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.
# - The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:
#     - lefti is the x coordinate of the left edge of the ith building.
#     - righti is the x coordinate of the right edge of the ith building.
#     - heighti is the height of the ith building.
# - You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.
# - The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.
# Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]
# Example 1:
#     Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
#     Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
#     Explanation:
#         Figure A shows the buildings of the input.
#         Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
# Example 2:
#     Input: buildings = [[0,2,3],[2,5,3]]
#     Output: [[0,3],[5,0]]
# Constraints:
#     1 <= buildings.length <= 104
#     0 <= lefti < righti <= 231 - 1
#     1 <= heighti <= 231 - 1
#     buildings is sorted by lefti in non-decreasing order.

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Convert buildings into events
        events = [(L, -H, R) for L, R, H in buildings] + [(R, 0, 0) for _, R, _ in buildings]
        
        # Sort events
        events.sort()
        
        # Result and current heights
        res = [[0, 0]]
        hp = [(0, float('inf'))]
        
        for x, negH, R in events:
            while hp[0][1] <= x:
                heapq.heappop(hp)
            if negH:
                heapq.heappush(hp, (negH, R))
            if res[-1][1] != -hp[0][0]:
                res.append([x, -hp[0][0]])
                
        return res[1:]

'''LARGEST RECTANGLE IN A HISTOGRAM'''
# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

# Example 1:
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: 
#     The above is a histogram where width of each bar is 1.
#     The largest rectangle is shown in the red area, which has an area = 10 units.

# Example 2:
#     Input: heights = [2,4]
#     Output: 4

# Constraints:
#     1 <= heights.length <= 105
#     0 <= heights[i] <= 104

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Stack to store the indices of the bars
        max_area = 0

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        # Calculate the remaining rectangles in the stack
        while stack:
            height = heights[stack.pop()]
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)

        return max_area