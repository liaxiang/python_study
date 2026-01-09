from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p = headA
        q = headB
        while q is not q:
            p = p.next if p.next is not None else q
            q = q.next if q.next is not None else p
        return p