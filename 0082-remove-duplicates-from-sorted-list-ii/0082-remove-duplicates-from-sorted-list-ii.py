# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-1)
        left = dummy
        right = head
        while right:
            if right.next and right.val == right.next.val:
                while right.next and right.val == right.next.val:
                    right = right.next
                right = right.next
                if not right:
                    left.next = None
            else:
                left.next = right
                left = left.next
                right = right.next
        return dummy.next



        
