from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_binary_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    root.left, root.right = root.right, root.left

    invert_binary_tree(root.left)
    invert_binary_tree(root.right)

    return root


def invert_binary_tree_iterative(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    queue = deque([root])

    while queue:
        node = queue.popleft()
        node.left, node.right = node.right, node.left

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return root


# Time complexity: O(n)
# Space complexity: O(n)
