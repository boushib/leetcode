from typing import Optional
from tests import run_tests


class ListNode:

    def __init__(self, _val=0, _next=None):
        self.val = _val
        self.next = _next


def get_intersection_node(head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
    a, b = head_a, head_b

    while a != b:
        a = a.next if a else head_b
        b = b.next if b else head_a

    return a


a = ListNode(8, ListNode(4, ListNode(5)))
b = ListNode(2, ListNode(4))
tests = [
    ((ListNode(4, ListNode(1, a)), ListNode(5, ListNode(6, ListNode(1, a)))), a),
    ((ListNode(1, ListNode(9, ListNode(1, b))), ListNode(3, b)), b),
    ((ListNode(2, ListNode(6, ListNode(4))), ListNode(1, ListNode(5))), None),
]
run_tests(get_intersection_node, tests)
