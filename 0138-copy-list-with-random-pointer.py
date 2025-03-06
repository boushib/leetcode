from typing import Optional


class Node:
    def __init__(self, val: int, next=None, random=None):
        self.val = int(val)
        self.next = next
        self.random = random


def copy_random_list(head: Optional[Node]) -> Optional[Node]:
    node_map = {None: None}  # (node -> node clone)
    curr_node = head

    while curr_node:
        node_map[curr_node] = Node(curr_node.val)
        curr_node = curr_node.next

    curr_node = head

    while curr_node:
        node_map[curr_node].next = node_map[curr_node.next]
        node_map[curr_node].random = node_map[curr_node.random]
        curr_node = curr_node.next

    return node_map[head]


# Time complexity: O(n)
# Space complexity: O(n)
