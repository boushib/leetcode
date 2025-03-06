from typing import List, Optional
from collections import deque, defaultdict
from tests import run_tests


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def vertical_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    cols = defaultdict(list)
    min_col, max_col = 0, 0
    queue = deque([(root, 0, 0)])  # (node, row, column)

    while queue:
        node, r, c = queue.popleft()
        min_col = min(min_col, c)
        max_col = max(max_col, c)
        cols[c].append((r, node.val))

        if node.left:
            queue.append((node.left, r + 1, c - 1))
        if node.right:
            queue.append((node.right, r + 1, c + 1))

    return [[v for _, v in sorted(cols[c], key=lambda x: (x[0], x[1]))] for c in range(min_col, max_col + 1)]


tests = [
    (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), [[9], [3, 15], [20], [7]]),
    (
        TreeNode(3, TreeNode(9, TreeNode(4), TreeNode(0)), TreeNode(8, TreeNode(1), TreeNode(7))),
        [[4], [9], [3, 0, 1], [8], [7]],
    ),
    (
        TreeNode(
            3, TreeNode(9, TreeNode(4), TreeNode(0, TreeNode(5), TreeNode(2))), TreeNode(8, TreeNode(1), TreeNode(7))
        ),
        [[4], [9, 5], [3, 0, 1], [8, 2], [7]],
    ),
    (None, []),
]
run_tests(vertical_order, tests)
