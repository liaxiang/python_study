from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    val: int
    next: Optional["ListNode"] = None


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: 处理空链表或只有一个节点的情况
        if head is None or head.next is None:
            return head

        # Step 2: 双指针迭代反转
        prev: Optional[ListNode] = None
        cur: Optional[ListNode] = head

        while cur is not None:
            nxt = cur.next      # 先把“下一步要去哪”记下来
            cur.next = prev     # 让当前节点指向“前一个节点”（完成反转）
            prev = cur          # prev 前进
            cur = nxt           # cur 前进

        # Step 3: prev 会停在新的头节点
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


def to_list(head: Optional[ListNode]) -> list[int]:
    out: list[int] = []
    cur = head
    while cur is not None:
        out.append(cur.val)
        cur = cur.next
    return out


def to_arrow(head: Optional[ListNode], limit: int = 30) -> str:
    parts: list[str] = []
    cur = head
    steps = 0
    while cur is not None and steps < limit:
        parts.append(str(cur.val))
        cur = cur.next
        steps += 1
    if cur is not None:
        parts.append("…")
    parts.append("None")
    return " -> ".join(parts)


def reverse_list_trace(head: Optional[ListNode]) -> Optional[ListNode]:
    print("\n===== 开始逐步演示反转 =====")
    print("初始:", to_arrow(head))

    prev: Optional[ListNode] = None
    cur: Optional[ListNode] = head
    step = 0

    while cur is not None:
        nxt = cur.next

        print(f"\nStep {step}: (反转前)")
        print("  prev(已反转头):", to_arrow(prev))
        print("  cur(当前节点): ", cur.val)
        print("  nxt(下一节点): ", None if nxt is None else nxt.val)
        print("  未处理部分:    ", to_arrow(cur))

        # 关键一刀：把 cur 的 next 指回 prev
        cur.next = prev

        # 指针整体往前挪
        prev = cur
        cur = nxt
        step += 1

        print(f"Step {step}: (反转后)")
        print("  prev(已反转头):", to_arrow(prev))
        print("  cur(下一个要处理):", to_arrow(cur))

    print("\n===== 结束：反转完成 =====")
    print("结果:", to_arrow(prev))
    return prev


if __name__ == "__main__":
    head = build_list([1, 2, 3, 4])
    print("反转前:", to_list(head))
    new_head = Solution().reverseList(head)
    print("反转后:", to_list(new_head))

    # 逐步演示（会打印每一步指针变化）
    head2 = build_list([1, 2, 3, 4])
    reverse_list_trace(head2)