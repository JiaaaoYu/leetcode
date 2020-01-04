# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not (head and head.next):
            return True
        
        dummy = ListNode(-1)
        dummy.next = head
        fast, slow = dummy, dummy
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            
        cur, pre = slow.next, None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        a = dummy.next
        b = pre
        while b:
            if a.val != b.val:
                return False
            a, b = a.next, b.next
            
        return True