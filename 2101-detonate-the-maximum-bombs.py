from typing import List
from collections import defaultdict
from tests import run_tests


def maximum_detonations(bombs: List[List[int]]) -> int:
    graph = defaultdict(list)
    res = 0

    for i in range(len(bombs)):
        for j in range(len(bombs)):
            if i != j and (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2 <= bombs[i][2] ** 2:
                graph[i].append(j)

    def dfs(node, visited):
        visited.add(node)

        for neib in graph[node]:
            if neib not in visited:
                dfs(neib, visited)
        nonlocal res
        res = max(res, len(visited))

    for i in range(len(bombs)):
        dfs(i, set())

    return res


# Time complexity: O(n^3)
# Space complexity: O(n^2)

tests = [
    ([[2, 1, 3], [6, 1, 4]], 2),
    ([[1, 1, 5], [10, 10, 5]], 1),
    ([[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]], 5),
]
run_tests(maximum_detonations, tests)
