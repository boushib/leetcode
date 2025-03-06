from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        res = []
        curr = self

        while curr:
            res.append(curr.val)
            curr = curr.next

        return " -> ".join(map(str, res))


def add_two_numbers(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
    curr_node = dummy_node = ListNode(-1)
    carry = 0

    while a or b or carry:
        x, y = a.val if a else 0, b.val if b else 0
        _sum = x + y + carry
        curr_node.next = ListNode(_sum % 10)
        carry = _sum // 10
        a = a.next if a else a
        b = b.next if b else b
        curr_node = curr_node.next

    return dummy_node.next


# Time complexity: O(max(n, m))
# Space complexity: O(max(n, m))


print(
    add_two_numbers(
        ListNode(2, ListNode(4, ListNode(3))),
        ListNode(5, ListNode(6, ListNode(4))),
    )
)
# [7,0,8]
