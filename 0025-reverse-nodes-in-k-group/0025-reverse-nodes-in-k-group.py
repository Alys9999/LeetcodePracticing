# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        dummy = ListNode(0)
        cur = dummy
        nxt = head
        
        while cur:
            if not self.checkN(nxt, k):
                cur.next = nxt
                return dummy.next
            res = self.reverseN(nxt, k)
            cur.next = res
            for _ in range(k):
                cur = cur.next
            nxt = cur.next

        
    def reverseN(self, root, k: int):
        pre = None
        cur = root
        nxt = root.next

        while k > 0:
            cur.next = pre
            pre = cur
            cur = nxt
            nxt = nxt.next if nxt else None
            k -= 1
        root.next = cur
        return pre

    def checkN(self, root, k):
        check = root
        for _ in range(k):
            if not check: return False
            check = check.next
        return True