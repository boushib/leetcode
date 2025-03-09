from typing import Optional, List
from collections import deque
from tests import run_tests


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_level_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    res = []

    def dfs(node, level):
        if not node:
            return None

        if len(res) <= level:
            res.append(deque([]))

        if level % 2 == 0:  # left to right
            res[level].append(node.val)
        else:
            res[level].appendleft(node.val)

        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)
    return [list(level) for level in res]


tests = [
    (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), [[3], [20, 9], [15, 7]]),
    (TreeNode(1), [[1]]),
    (None, []),
]
run_tests(zigzag_level_order_traversal, tests)
