class ListNode:
    def __init__(self, key = 0, val = 0, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {}
        self.ll = ListNode()
        self._cur_node = self.ll

    def _refresh(self, node: ListNode):
        if node == self._cur_node: return
        tmp_next, tmp_prev = node.next, node.prev

        self._cur_node.next = node
        node.prev = self._cur_node
        node.next = None
        self._cur_node = node
        tmp_prev.next =  tmp_next
        tmp_next.prev = tmp_prev

    def get(self, key: int) -> int:
        node = self.hash.get(key, None)

        if node:
            self._refresh(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        node = self.hash.get(key, None)

        if node:
            self._refresh(node)
            node.val = value
        else:
            if len(self.hash) == self.capacity:
                removed = self.ll.next
                next = removed.next
                if next:
                    self.ll.next = next
                    next.prev = self.ll
                else:
                    self.ll.next = None
                del self.hash[removed.key]
            node = ListNode(key, value)
            self._cur_node.next = node
            node.prev = self._cur_node
            self._cur_node = node
            self.hash[key] = node