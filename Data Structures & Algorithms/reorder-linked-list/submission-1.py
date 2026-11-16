# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find the middle
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. Reverse the second half, disconnecting it from the first one
        second = slow.next
        prev = slow.next = None

        # 3. Merge to halves
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first = head
        second = prev

        while second:
            first_tmp, second_tmp = first.next, second.next
            first.next = second
            second.next = first_tmp
            second = second_tmp
            first = first_tmp

