from typing import Optional
from tests import run_tests


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def range_sum_bst(root: Optional[TreeNode], low: int, high: int) -> int:
    if not root:
        return 0

    if root.val < low:
        return range_sum_bst(root.right, low, high)
    if root.val > high:
        return range_sum_bst(root.left, low, high)

    return root.val + range_sum_bst(root.left, low, high) + range_sum_bst(root.right, low, high)


# Time complexity: O(n)
# Space complexity: O(n)


tests = [
    ((TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18))), 7, 15), 32),
    (
        (
            TreeNode(
                10,
                TreeNode(5, TreeNode(3, TreeNode(1)), TreeNode(7, TreeNode(6))),
                TreeNode(15, TreeNode(13), TreeNode(18)),
            ),
            6,
            10,
        ),
        23,
    ),
]
run_tests(range_sum_bst, tests)
