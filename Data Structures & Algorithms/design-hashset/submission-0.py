class MyHashSet:

    def __init__(self):
        self.hashmap = [None]

    def add(self, key: int) -> None:
        if key > len(self.hashmap) - 1:
            self.hashmap.extend([None] *  max(1, (key+1) - len(self.hashmap)))
        self.hashmap[key] = key

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hashmap[key] = None   
        return None

    def contains(self, key: int) -> bool:
        return key < len(self.hashmap) and self.hashmap[key] is not None
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)