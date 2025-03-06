from typing import Optional
from tests import run_tests


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_root_to_leaf_numbers(root: Optional[TreeNode]) -> int:
    def dfs(node, curr_sum):
        if not node:
            return 0

        curr_sum = 10 * curr_sum + node.val

        if not node.left and not node.right:
            return curr_sum

        return dfs(node.left, curr_sum) + dfs(node.right, curr_sum)

    return dfs(root, 0)


# Time complexity: O(n)
# Space complexity: O(n)


tests = [
    (TreeNode(1, TreeNode(2), TreeNode(3)), 25),
    (TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0)), 1026),
]
run_tests(sum_root_to_leaf_numbers, tests)
