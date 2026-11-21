# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        p1, p2 = l1, l2
        remainder = 0

        while p1 or p2:
            p1_val = (p1 and p1.val) or 0
            p2_val = (p2 and p2.val) or 0

            cur_sum = p1_val + p2_val + remainder
            head.next = ListNode(cur_sum % 10)
            remainder = 1 if cur_sum > 9 else 0

            head = head.next
            if p1: p1 = p1.next
            if p2: p2 = p2.next
        if remainder > 0:
            head.next = ListNode(remainder)
        return dummy.next