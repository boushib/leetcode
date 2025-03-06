from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    if not node:
        return None

    node_map = {}  # node -> clone

    def dfs(n):
        if n in node_map:
            return node_map[n]

        node_map[n] = Node(n.val)

        for neib in n.neighbors:
            node_map[n].neighbors.append(dfs(neib))

        return node_map[n]

    return dfs(node)


# Time complexity: O(n)
# Space complexity: O(n)
