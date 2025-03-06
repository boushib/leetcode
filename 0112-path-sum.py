from typing import Optional
from tests import run_tests


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum_iterative(root: Optional[TreeNode], target_sum: int) -> bool:
    if not root:
        return False

    queue = [(root, target_sum - root.val)]

    while queue:
        node, curr_target_sum = queue.pop()

        if not node.left and not node.right and curr_target_sum == 0:
            return True

        if node.left:
            queue.append((node.left, curr_target_sum - node.left.val))

        if node.right:
            queue.append((node.right, curr_target_sum - node.right.val))

    return False


def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    if not root:
        return False

    if not root.left and not root.right:
        return root.val == target_sum

    return has_path_sum(root.left, target_sum - root.val) or has_path_sum(root.right, target_sum - root.val)


# Time complexity: O(n)
# Space complexity: O(n)


tests = [
    (
        (
            TreeNode(
                5,
                TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))),
            ),
            22,
        ),
        True,
    ),
    ((TreeNode(1, TreeNode(2), TreeNode(3)), 5), False),
    ((None, 0), False),
]
run_tests(has_path_sum, tests)
run_tests(has_path_sum_iterative, tests)
