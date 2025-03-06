from typing import Optional


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def insert_into_list(head: Optional[Node], v: int) -> Node:
    if not head:
        node = Node(v)
        node.next = node  # make it circular
        return node
    prev_node, curr_node = head, head.next

    while True:
        if prev_node.val <= v <= curr_node.val or (
            curr_node.val < prev_node.val and (v <= curr_node.val or v >= prev_node.val)
        ):
            prev_node.next = Node(v, curr_node)
            return head

        prev_node = curr_node
        curr_node = curr_node.next

        if prev_node == head:
            prev_node.next = Node(v, curr_node)
            return head


# Time complexity: O(n)
# Space complexity: O(1)
