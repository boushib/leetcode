from typing import Optional, List
from tests import run_tests


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    res = []

    def dfs(node, depth):
        if node is None:
            return None

        if depth == len(res):
            res.append(node.val)

        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)

    dfs(root, 0)
    return res


# Time complexity: O(n)
# Space complexity: O(n)


tests = [
    (TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4))), [1, 3, 4]),
    (TreeNode(1, None, TreeNode(3)), [1, 3]),
    (None, []),
]
run_tests(right_side_view, tests)
