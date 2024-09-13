from tests import run_tests


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def closest_value(root: TreeNode, target: float) -> int:
    res = root.val
    curr_node = root

    while curr_node:
        res = min(res, curr_node.val, key=lambda x: (abs(target - x), x))
        curr_node = curr_node.left if target < curr_node.val else curr_node.right

    return res


tests = [
    ((TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5)), 3.714286), 4),
    ((TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5)), 3.5), 3),
    ((TreeNode(1), 4.428571), 1),
]
run_tests(closest_value, tests)
