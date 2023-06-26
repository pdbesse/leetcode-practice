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

'''REVERSE LINKED LIST'''
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
#     Input: head = [1,2,3,4,5]
#     Output: [5,4,3,2,1]

# Example 2:
#     Input: head = [1,2]
#     Output: [2,1]

# Example 3:
#     Input: head = []
#     Output: []

# Constraints:
#     The number of nodes in the list is the range [0, 5000].
#     -5000 <= Node.val <= 5000

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next

class Solution:
    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        return prev
    
    # def reverseListRecursive(head):
    #     if not head or not head.next:
    #         return head

    #     reversed_head = Solution.reverseListRecursive(head.next)
    #     head.next.next = head
    #     head.next = None

    #     return reversed_head

'''MERGE TWO SORTED LISTS'''
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Example 1:
#     Input: list1 = [1,2,4], list2 = [1,3,4]
#     Output: [1,1,2,3,4,4]

# Example 2:
#     Input: list1 = [], list2 = []
#     Output: []

# Example 3:
#     Input: list1 = [], list2 = [0]
#     Output: [0]

# Constraints:
#     The number of nodes in both lists is in the range [0, 50].
#     -100 <= Node.val <= 100
#     Both list1 and list2 are sorted in non-decreasing order.

# Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        prev = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            
            prev = prev.next
        
        prev.next = list1 if list1 else list2

        return dummy.next
