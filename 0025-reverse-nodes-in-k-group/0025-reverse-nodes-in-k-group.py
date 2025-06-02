# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        cur.next = head

        while cur:
            if not self.checkN(cur.next, k):
                break
            res = self.reverseN(cur.next, k)
            cur.next = res
            for _ in range(k):
                cur = cur.next
        return dummy.next

    def reverseN(self, root, k):
        pre = None
        cur = root
        nxt = root.next
        while k > 0:
            cur.next = pre
            pre = cur
            cur = nxt
            nxt = nxt.next if nxt else None
            k-=1
        root.next = cur
        return pre
    
    # true if there is enough nodes left
    def checkN(self, root, k):
        check = root
        for _ in range(k):
            if not check:
                return False
            check = check.next
        return True

