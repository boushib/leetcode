from typing import List, Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        res = ""
        curr_node = self

        while curr_node:
            if res:
                res += " -> "
            res += str(curr_node.val)
            curr_node = curr_node.next

        return res


def merge_two_sorted_lists(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
    dummy_node = ListNode()
    curr_node = dummy_node

    while a and b:
        if a.val < b.val:
            curr_node.next = a
            a = a.next
        else:
            curr_node.next = b
            b = b.next

        curr_node = curr_node.next

    if a:
        curr_node.next = a

    if b:
        curr_node.next = b

    return dummy_node.next


def merge_k_sorted_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None

    while len(lists) > 1:
        merged_lists = []

        for i in range(0, len(lists), 2):
            a = lists[i]
            b = lists[i + 1] if i + 1 < len(lists) else None
            merged_lists.append(merge_two_sorted_lists(a, b))

        lists = merged_lists

    return lists[0]


print(
    merge_k_sorted_lists(
        [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]
    )
)
