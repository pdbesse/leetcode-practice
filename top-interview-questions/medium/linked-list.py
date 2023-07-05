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
        
        return odd_head

'''INTERSECTION OF TWO LINKED LISTS'''
# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
# The test cases are generated such that there are no cycles anywhere in the entire linked structure.
# Note that the linked lists must retain their original structure after the function returns.

# Custom Judge:
#     The inputs to the judge are given as follows (your program is not given these inputs):
#         - intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
#         - listA - The first linked list.
#         - listB - The second linked list.
#         - skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
#         - skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
#     The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

# Example 1:
#     Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
#     Output: Intersected at '8'
#     Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
#     From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
#     - Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.

# Example 2:
#     Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
#     Output: Intersected at '2'
#     Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
#     From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

# Example 3:
#     Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
#     Output: No intersection
#     Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
#     Explanation: The two lists do not intersect, so return null.

# Constraints:
#     The number of nodes of listA is in the m.
#     The number of nodes of listB is in the n.
#     1 <= m, n <= 3 * 104
#     1 <= Node.val <= 105
#     0 <= skipA < m
#     0 <= skipB < n
#     intersectVal is 0 if listA and listB do not intersect.
#     intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

# Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None

        # Calculate the lengths of both lists
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)

        # Move the head of the longer list forward
        if lenA > lenB:
            for _ in range(lenA - lenB):
                headA = headA.next
        elif lenB > lenA:
            for _ in range(lenB - lenA):
                headB = headB.next

        # Traverse both lists to find the intersection
        while headA is not None and headB is not None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None

    def getLength(self, head: ListNode) -> int:
        length = 0
        while head is not None:
            length += 1
            head = head.next
        return length