from typing import List
from tests import run_tests


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]

    for i in intervals[1:]:
        if i[0] <= res[-1][1]:
            res[-1][1] = max(i[1], res[-1][1])
        else:
            res.append(i)

    return res


tests = [
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ([[1, 4], [4, 5]], [[1, 5]]),
    ([[1, 4], [0, 4]], [[0, 4]]),
]
run_tests(merge_intervals, tests)
