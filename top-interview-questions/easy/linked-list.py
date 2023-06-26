from typing import List, Optional, ListNode

'''DELETE NODE IN A LINKED LIST'''
# There is a singly-linked list head and we want to delete a node node in it.
# You are given the node to be deleted node. You will not be given access to the first node of head.
# All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.
# Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:
    # The value of the given node should not exist in the linked list.
    # The number of nodes in the linked list should decrease by one.
    # All the values before node should be in the same order.
    # All the values after node should be in the same order.

# Custom testing:
#     For the input, you should provide the entire linked list head and the node to be given node. node should not be the last node of the list and should be an actual node in the list.
#     We will build the linked list and pass the node to your function.
#     The output will be the entire list after calling your function.
 
# Example 1:
#     Input: head = [4,5,1,9], node = 5
#     Output: [4,1,9]
#     Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

# Example 2:
#     Input: head = [4,5,1,9], node = 1
#     Output: [4,5,9]
#     Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

# Constraints:
#     The number of the nodes in the given list is in the range [2, 1000].
#     -1000 <= Node.val <= 1000
#     The value of each node in the list is unique.
#     The node to be deleted is in the list and is not a tail node.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
:type node: ListNode
:rtype: void Do not return anything, modify node in-place instead.
"""
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

'''REMOVE NTH NODE FROM END OF LIST'''
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
#     Input: head = [1,2,3,4,5], n = 2
#     Output: [1,2,3,5]

# Example 2:
#     Input: head = [1], n = 1
#     Output: []

# Example 3:
#     Input: head = [1,2], n = 1
#     Output: [1]

# Constraints:
#     The number of nodes in the list is sz.
#     1 <= sz <= 30
#     0 <= Node.val <= 100
#     1 <= n <= sz

# Follow up: Could you do this in one pass?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head

        # Initialize fast and slow pointers
        fast = dummy
        slow = dummy

        # Move the fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # Move both pointers simultaneously
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # Remove the nth node from the end
        slow.next = slow.next.next

        return dummy.next