from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

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
    
'''SORT LIST'''
# Given the head of a linked list, return the list after sorting it in ascending order.

# Example 1:
#     Input: head = [4,2,1,3]
#     Output: [1,2,3,4]

# Example 2:
#     Input: head = [-1,5,3,4,0]
#     Output: [-1,0,3,4,5]

# Example 3:
#     Input: head = []
#     Output: []

# Constraints:
#     The number of nodes in the list is in the range [0, 5 * 104].
#     -105 <= Node.val <= 105

# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Helper function to find middle of linked list
        def find_middle(node):
            slow, fast = node, node
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None
            return slow
        
        # Helper function to merge two sorted linked lists
        def merge(l1, l2):
            dummy = ListNode()
            current = dummy
            
            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            
            current.next = l1 if l1 else l2
            
            return dummy.next
        
        # Recursive merge sort
        def merge_sort(node):
            if not node or not node.next:
                return node
            
            mid = find_middle(node)
            left = merge_sort(node)
            right = merge_sort(mid)
            return merge(left, right)
        
        return merge_sort(head)
    
'''COPY LIST WITH RANDOM POINTER'''
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.
# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
# Return the head of the copied linked list.
# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
# - val: an integer representing Node.val
# - random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

# Example 1:
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

# Example 2:
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]

# Example 3:
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]

# Constraints:
# 0 <= n <= 1000
# -104 <= Node.val <= 104
# Node.random is null or is pointing to some node in the linked list.

# Hints:
# - Just iterate the linked list and create copies of the nodes on the go. Since a node can be referenced from multiple nodes due to the random pointers, ensure you are not making multiple copies of the same node. 
# - You may want to use extra space to keep old_node ---> new_node mapping to prevent creating multiple copies of the same node.
# - We can avoid using extra space for old_node ---> new_node mapping by tweaking the original linked list. Simply interweave the nodes of the old and copied list. For example: Old List: A --> B --> C --> D InterWeaved List: A --> A' --> B --> B' --> C --> C' --> D --> D'
# - The interweaving is done using next pointers and we can make use of interweaved structure to get the correct reference nodes for random pointers.

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Create dictionary to map original nodes to their copies
        node_map = {}
        
        # Step 1: Create new nodes and interweave them with original list
        current = head
        while current:
            new_node = Node(current.val)
            node_map[current] = new_node
            new_node.next = current.next
            current.next = new_node
            current = new_node.next
        
        # Step 2: Set random pointers for copied nodes
        current = head
        while current:
            if current.random:
                current.next.random = node_map[current.random]
            current = current.next.next
        
        # Step 3: Separate copied list from original list
        new_head = head.next
        current = head
        while current:
            temp = current.next
            current.next = temp.next
            if temp.next:
                temp.next = temp.next.next
            current = current.next
        
        return new_head