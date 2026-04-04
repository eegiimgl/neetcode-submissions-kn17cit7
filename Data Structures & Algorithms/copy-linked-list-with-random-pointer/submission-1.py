
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        head_copy = Node(head.val)
        cur_copy = head_copy

        hash_map = {}

        cur = head
        while cur:
            hash_map[cur] = cur_copy
            cur = cur.next
            cur_copy.next = Node(cur.val) if cur else None
            cur_copy = cur_copy.next

        cur = head
        cur_copy = head_copy
        while cur:
            cur_copy.random = hash_map.get(cur.random)
            cur = cur.next
            cur_copy = cur_copy.next

        return head_copy