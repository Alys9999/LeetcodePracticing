# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        left = head
        right = self.reverse(slow)
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
        
    def reverse(self, root):
        dummy = None
        cur = root
        while cur:
            temp = cur.next
            cur.next = dummy
            dummy = cur
            cur = temp
        return dummy