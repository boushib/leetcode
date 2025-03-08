from typing import List
from collections import deque
from tests import run_tests


def find_course_order(n: int, prereq: List[List[int]]) -> List[int]:
    res = []
    graph = {i: [] for i in range(n)}
    in_degree = [0] * n

    for a, b in prereq:
        graph[b].append(a)
        in_degree[a] += 1

    queue = deque([c for c in range(n) if in_degree[c] == 0])

    while queue:
        course = queue.popleft()
        res.append(course)

        for nb in graph[course]:
            in_degree[nb] -= 1

            if in_degree[nb] == 0:
                queue.append(nb)

    return res if len(res) == n else []


tests = [
    ((2, [[1, 0]]), [0, 1]),
    ((4, [[1, 0], [2, 0], [3, 1], [3, 2]]), [0, 2, 1, 3]),
    ((1, []), [0]),
]
run_tests(find_course_order, tests)
