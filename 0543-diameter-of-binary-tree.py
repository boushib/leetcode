from typing import Optional
from tests import run_tests


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    res = [0]

    def dfs(node):
        if not node:
            return 0

        left, right = dfs(node.left), dfs(node.right)
        res[0] = max(res[0], left + right)

        return 1 + max(left, right)

    dfs(root)
    return res[0]


tests = [(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)), 3)]
run_tests(diameter_of_binary_tree, tests)