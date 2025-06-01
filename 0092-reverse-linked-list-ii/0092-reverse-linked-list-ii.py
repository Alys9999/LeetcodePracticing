# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == 1:
            return self.reverseN(head, right)
        h = head
        for _ in range(left -2):
            h = h.next
        h.next = self.reverseN(h.next, right - left + 1)
        # return self.reverseN(h.next, right - left + 1)
        return head
    def reverseN(self, root:ListNode, n:int):
        if not root or not root.next:
            return root
        head = root
        pre = None
        nxt = root.next
        while n > 0:
            head.next = pre
            pre = head
            head = nxt
            if nxt:
                nxt = nxt.next
            n -= 1
        root.next = head
        return pre
            
            
