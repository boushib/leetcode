from typing import Optional


class TreeNode:

    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: Optional[TreeNode], p: TreeNode,
                           q: TreeNode) -> TreeNode:
    if not root:
        return None

    if root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    # p and q are found in the left and right sub-trees
    if left and right:
        return root

    return left if left else right
