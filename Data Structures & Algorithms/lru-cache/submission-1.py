class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:        
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.removeNode(node)
            self.addHead(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.removeNode(node)
        else:
            node = ListNode(key, value)
            self.cache[key] = node
            
        self.addHead(node)

        if len(self.cache) > self.capacity:
            to_remove = self.tail.prev
            self.removeNode(to_remove)
            del self.cache[to_remove.key]

    def removeNode(self, node):
        if node:
            node.next.prev = node.prev
            node.prev.next = node.next
    
    def addHead(self, node):
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head

    def printList(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next
