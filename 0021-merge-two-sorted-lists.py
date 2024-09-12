from typing import Optional
from tests import run_tests


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_list(self):
        res = []
        curr = self

        while curr:
            res.append(curr.val)
            curr = curr.next

        return res


def merge_two_lists(a: Optional[ListNode],
                    b: Optional[ListNode]) -> Optional[ListNode]:
    curr_node = dummy_node = ListNode()

    while a and b:
        if a.val < b.val:
            curr_node.next = a
            a = a.next
        else:
            curr_node.next = a
            b = b.next

        curr_node = curr_node.next

    if a:
        curr_node.next = a
    if b:
        curr_node.next = b

    return dummy_node.next


tests = [((ListNode(1, ListNode(2, ListNode(4))),
           ListNode(1, ListNode(3, ListNode(4)))), [1, 1, 2, 3, 4, 4]),
         ((None, ListNode(0)), [0]), ((None, None), [])]

run_tests(merge_two_lists, tests)
