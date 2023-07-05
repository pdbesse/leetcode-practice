from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''ADD TWO NUMBERS'''
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
#     Input: l1 = [2,4,3], l2 = [5,6,4]
#     Output: [7,0,8]
#     Explanation: 342 + 465 = 807.

# Example 2:
#     Input: l1 = [0], l2 = [0]
#     Output: [0]

# Example 3:
#     Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
#     Output: [8,9,9,9,0,0,0,1]

# Constraints:
#     The number of nodes in each linked list is in the range [1, 100].
#     0 <= Node.val <= 9
#     It is guaranteed that the list represents a number that does not have leading zeros.

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Variable to store the carry-over
        carry = 0  
        # Head of the resulting linked list
        head = None  
        # Pointer to the previous node in the resulting linked list
        prev = None  
        
        while l1 or l2 or carry:
            # Calculate the sum of the current digits and the carry-over
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            # Create a new node with the sum % 10 and update the carry-over
            node = ListNode(sum % 10)
            carry = sum // 10
            
            if prev:
                prev.next = node
            else:
                head = node
                
            prev = node

        # Return the head of the resulting linked list
        return head 

'''ODD EVEN LINKED LIST'''
# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# Example 1:
#     Input: head = [1,2,3,4,5]
#     Output: [1,3,5,2,4]

# Example 2:
#     Input: head = [2,1,3,5,6,4,7]
#     Output: [2,3,6,7,1,5,4]

# Constraints:
#     The number of nodes in the linked list is in the range [0, 104].
#     -106 <= Node.val <= 106

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd_head = head
        even_head = head.next
        odd_ptr = odd_head
        even_ptr = even_head
        
        while even_ptr and even_ptr.next:
            odd_ptr.next = even_ptr.next
            odd_ptr = odd_ptr.next
            even_ptr.next = odd_ptr.next
            even_ptr = even_ptr.next
        
        odd_ptr.next = even_head
        even_ptr.next = None
        
        return odd_head