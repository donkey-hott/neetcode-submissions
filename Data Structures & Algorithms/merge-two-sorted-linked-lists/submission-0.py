# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = list1, list2
        ans = ListNode()
        cur = ans

        while cur1 or cur2:            
            if cur1 and not cur2:
                cur.next = ListNode(cur1.val)
                cur1 = cur1.next
            elif cur2 and not cur1:
                cur.next = ListNode(cur2.val)
                cur2 = cur2.next
            else:
                if cur1.val < cur2.val:
                    cur.next = ListNode(cur1.val)
                    cur1 = cur1.next
                else:
                    cur.next = ListNode(cur2.val)
                    cur2 = cur2.next
            cur = cur.next

        return ans.next