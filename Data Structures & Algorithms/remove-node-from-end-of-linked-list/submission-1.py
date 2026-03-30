# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        curr = head
        while curr:
            curr = curr.next
            N += 1
        
        i = N - n
        if i == 0:
            head = head.next
        else:
            curr = head
            while curr:
                i -= 1
                if i == 0:
                    curr.next = curr.next.next if curr.next else None
                curr = curr.next

        return head