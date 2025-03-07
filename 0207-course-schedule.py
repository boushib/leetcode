from typing import List
from tests import run_tests


def can_finish_courses(n: int, prereq: List[List[int]]) -> bool:
    graph = {i: [] for i in range(n)}

    for a, b in prereq:
        graph[a].append(b)

    visited = set()

    def dfs(course):
        if graph[course] == []:
            return True
        if course in visited:
            return False

        visited.add(course)

        for nb in graph[course]:
            if not dfs(nb):
                return False

        visited.remove(course)
        graph[course] = []
        return True

    for i in range(n):
        if not dfs(i):
            return False

    return True


tests = [
    ((2, [[1, 0]]), True),
    ((2, [[1, 0], [0, 1]]), False),
]
run_tests(can_finish_courses, tests)
