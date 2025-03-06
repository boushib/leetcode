from tests import run_tests


class Node:

    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def lowest_common_ancestor(p: Node, q: Node) -> Node:
    node_a, node_b = p, q
    print(node_a, node_b, p, q)

    while node_a != node_b:
        # Swap at root top make sure node_a
        # and node_b travel the same distance
        node_a = node_a.parent if node_a else q
        node_b = node_b.parent if node_b else p
    return node_a  # or node_b


# Time complexity: O(h)
# Space complexity: O(1)


root_1 = Node(3, Node(5, Node(6), Node(2, Node(7), Node(4))), Node(1, Node(0), Node(8)))
root_2 = Node(1, Node(2))
tests = [
    ((root_1.left, root_1.right), root_1),
    ((root_1.left, root_1.left.right.right), root_1.left),
    ((root_2, root_2.left), root_2),
]
run_tests(lowest_common_ancestor, tests)
