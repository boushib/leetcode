from typing import Optional


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_to_doubly_list(root: Optional[Node]) -> Optional[Node]:
    if not root:
        return None

    first_node, last_node = None, None

    def dfs(node):
        if not node:
            return None

        nonlocal first_node, last_node
        dfs(node.left)

        if not first_node:
            first_node = node
        else:
            last_node.right = node
            node.left = last_node

        last_node = node
        dfs(node.right)

    dfs(root)
    first_node.left, last_node.right = last_node, first_node
    return first_node


# Time complexity: O(n)
# Space complexity: O(n)


print(tree_to_doubly_list(Node(4, Node(2, Node(1), Node(3)), Node(5))))  # [1, 2, 3, 4, 5]
