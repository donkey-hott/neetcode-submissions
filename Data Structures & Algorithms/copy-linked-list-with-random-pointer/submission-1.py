"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.seen = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return None

        if head not in self.seen:
            new_node = Node(head.val)
            self.seen[head] = new_node
            new_node.next = self.copyRandomList(head.next)
            new_node.random = self.seen.get(head.random)
        return self.seen[head]
