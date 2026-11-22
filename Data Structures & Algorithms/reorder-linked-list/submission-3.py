# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        f, s = head, prev

        while s:
            tmp_f, tmp_s = f.next, s.next

            f.next = s
            s.next = tmp_f
            f = tmp_f
            s = tmp_s