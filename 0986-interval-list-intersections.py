from typing import List
from tests import run_tests


def interval_intersection(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    res = []
    i, j = 0, 0

    while i < len(a) and j < len(b):
        start, end = max(a[i][0], b[j][0]), min(a[i][1], b[j][1])

        if start <= end:
            res.append([start, end])

        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1

    return res


tests = [
    (
        (
            [[0, 2], [5, 10], [13, 23], [24, 25]],
            [[1, 5], [8, 12], [15, 24], [25, 26]],
        ),
        [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]],
    ),
    (([[1, 3], [5, 9]], []), []),
]
run_tests(interval_intersection, tests)
