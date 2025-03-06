from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    a, b = head, None

    while a:
        next_node = a.next
        a.next = b
        b = a
        a = next_node

    return b


# Time complexity: O(n)
# Space complexity: O(1)
