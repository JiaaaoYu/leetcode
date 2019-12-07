# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        h = None
        while head:
            nxt = head.next
            head.next = h
            h = head
            head = nxt
        return h