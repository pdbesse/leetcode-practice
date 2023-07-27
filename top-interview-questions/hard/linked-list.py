from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''MERGE K SORTED LISTS'''
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:
#     Input: lists = [[1,4,5],[1,3,4],[2,6]]
#     Output: [1,1,2,3,4,4,5,6]
#     Explanation: The linked-lists are:
#     [
#     1->4->5,
#     1->3->4,
#     2->6
#     ]
#     merging them into one sorted list:
#     1->1->2->3->4->4->5->6

# Example 2:
#     Input: lists = []
#     Output: []

# Example 3:
#     Input: lists = [[]]
#     Output: []

# Constraints:
#     k == lists.length
#     0 <= k <= 104
#     0 <= lists[i].length <= 500
#     -104 <= lists[i][j] <= 104
#     lists[i] is sorted in ascending order.
#     The sum of lists[i].length will not exceed 104.

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for idx, head in enumerate(lists):
            if head:
                # Use idx as tiebreaker to handle cases where nodes have same value.
                # Smaller idx gets higher priority in min-heap.
                heapq.heappush(min_heap, (head.val, idx, head))
        
        # Create dummy node to simplify merging process
        dummy = ListNode()
        current = dummy
        
        while min_heap:
            # Get smallest node from min-heap
            val, idx, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            
            # Move to next node in list associated with popped node
            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))
        
        return dummy.next