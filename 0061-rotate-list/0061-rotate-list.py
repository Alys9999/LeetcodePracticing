# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        l = 0
        lenCheck = head
        while lenCheck:
            l += 1
            lenCheck = lenCheck.next

        k = k%l
        if k == 0:
            return head

        slow = head
        fast = head

        for _ in range(k):
            fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        temp = slow.next
        slow.next = None
        fast.next = head
        return temp

        