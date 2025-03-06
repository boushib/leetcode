from typing import List
from tests import run_tests


def find_min_arrow_shots(points: List[List[int]]) -> int:
    res = 1
    points.sort(key=lambda x: x[1])
    next_end = points[0][1]

    for a, b in points:
        if a > next_end:
            res += 1
            next_end = b

    return res


# Time complexity: O(n log n)
# Space complexity: O(1)


tests = [
    ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
    ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
    ([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
]
run_tests(find_min_arrow_shots, tests)
