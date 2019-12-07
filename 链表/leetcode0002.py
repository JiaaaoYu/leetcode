# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur, carry = dummy, 0
        while l1 or l2:
            total = 0
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            total += carry
            carry = total // 10
            cur.next = ListNode(total % 10)
            cur = cur.next
        if carry > 0:
            cur.next = ListNode(carry)
        
        return dummy.next
        
            