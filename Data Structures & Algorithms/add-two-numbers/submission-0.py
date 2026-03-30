# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        curr_node = dummy_node
        carry = 0
        while l1 or l2:
            curr = carry
            if l1:
                curr += l1.val
                l1 = l1.next
            
            if l2:
                curr += l2.val
                l2 = l2.next
            
            carry = curr // 10
            digit = curr % 10
            
            curr_node.next = ListNode(digit)
            curr_node = curr_node.next

        if carry == 1:
            curr_node.next = ListNode(1)

        return dummy_node.next