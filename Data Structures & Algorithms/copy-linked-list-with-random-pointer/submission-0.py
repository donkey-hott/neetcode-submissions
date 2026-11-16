"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        seen = {}

        def getNode(node):
            if node is None: return None

            if node not in seen:
                new_node = Node(node.val)
                seen[node] = new_node
                new_node.next = getNode(node.next)
                new_node.random = getNode(node.random)
            return seen[node]

        return getNode(head)