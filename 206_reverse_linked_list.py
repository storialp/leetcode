# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        if current == None:
            return current
        l, r = current, current.next
        l.next = None
        while r != None:
            original_next = r.next
            r.next = l
            l = r
            r = original_next
        return l
            
            