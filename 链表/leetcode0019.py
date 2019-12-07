# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #哑节点，应对边界特殊情况
        dummy = ListNode(-1)
        dummy.next = head
        a, b = dummy, dummy
        # 快指针提前走n步
        while n > 0 and b:
            b, n = b.next, n-1
        
        if not b:
            return head
        # 同步走，知道快指针到最后一个节点
        while b.next:
            a, b = a.next, b.next
        a.next = a.next.next
        return dummy.next