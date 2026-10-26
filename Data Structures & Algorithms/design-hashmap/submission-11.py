class ListNode:
    def __init__(self, k = -1, v = -1):
        self.key = k
        self.val = v
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 101
        self.buckets = [ListNode()] * self.size
    
    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        cur = self.buckets[self._hash(key)]
        
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.buckets[self._hash(key)]

        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.buckets[self._hash(key)]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)