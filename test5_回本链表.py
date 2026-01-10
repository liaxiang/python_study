from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    val: int = 0
    next: Optional["ListNode"] = None

class Solution:
    # 版本 A：额外空间 O(n)（把值装进 list，再和倒序比较）
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst: list[int] = []

        cur = head
        while cur is not None:
            lst.append(cur.val)
            cur = cur.next

        return lst == lst[::-1]

    # 版本 B：额外空间 O(1)（原地做：找中点 -> 反转后半段 -> 比较 -> 恢复）
    def isPalindrome_O1(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # 1) 找中点（slow 走1步，fast 走2步）
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2) 反转后半段
        second = self._rev(slow.next)

        # 3) 比较
        p1, p2 = head, second
        ok = True
        while ok and p2:
            ok = (p1.val == p2.val)
            p1 = p1.next
            p2 = p2.next

        # 4) 恢复链表
        slow.next = self._rev(second)
        return ok

    def _rev(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next
        return prev


def build_list(values: list[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    for v in values[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


if __name__ == "__main__":
    head1 = build_list([1, 2, 2, 1])
    head2 = build_list([1, 2])

    s = Solution()
    print("版本A(list) head1:", s.isPalindrome(head1))  # True
    print("版本A(list) head2:", s.isPalindrome(head2))  # False

    head3 = build_list([1, 2, 2, 1])
    head4 = build_list([1, 2])
    print("版本B(O1)  head3:", s.isPalindrome_O1(head3))  # True
    print("版本B(O1)  head4:", s.isPalindrome_O1(head4))  # False