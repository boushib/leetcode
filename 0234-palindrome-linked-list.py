from typing import Optional
from tests import run_tests


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome_linked_list(head: Optional[ListNode]) -> bool:
    # Find the mid node
    slow_ptr, fast_ptr = head, head

    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    # Reverse second hald of the list
    curr_node = slow_ptr
    prev_node = None

    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    # Compare first and second halves
    left_node = head
    right_node = prev_node

    while left_node and right_node:
        if left_node.val != right_node.val:
            return False
        left_node, right_node = left_node.next, right_node.next

    return True


tests = [
    (ListNode(1, ListNode(2, ListNode(2, ListNode(1)))), True),
    (ListNode(1, ListNode(2, ListNode(1))), True),
    (ListNode(1, ListNode(2)), False),
]
run_tests(is_palindrome_linked_list, tests)
