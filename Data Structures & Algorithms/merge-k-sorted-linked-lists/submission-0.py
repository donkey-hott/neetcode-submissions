# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []

        for l in lists:
            cur = l

            while cur:
                nodes.append(cur)
                cur = cur.next
        

        nodes.sort(key=lambda node: node.val)

        dummy = ListNode()
        cur = dummy

        for n in nodes:
            cur.next = n
            cur = cur.next
        return dummy.next
                