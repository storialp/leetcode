# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        starter = ListNode()
        p1 = list1
        p2 = list2
        current = starter
        while p1 and p2:
            if p1.val >= p2.val:
                current.next = ListNode(p2.val)
                p2 = p2.next
            else:
                current.next = ListNode(p1.val)
                p1 = p1.next
            current = current.next
        if not p1 and p2:
            current.next = p2
        elif not p2 and p1:
            current.next = p1
        else:
            return starter.next
        return starter.next