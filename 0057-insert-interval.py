from typing import List
from tests import run_tests


def insert_interval(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    res = []
    i, n = 0, len(intervals)

    # prior to the new interval
    while i < n and intervals[i][1] < new_interval[0]:
        res.append(intervals[i])
        i += 1

    # overlapping with the new interval
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    res.append(new_interval)

    # post the new interval
    while i < n:
        res.append(intervals[i])
        i += 1

    return res


# Time complexity: O(n)
# Space complexity: O(1) - ignoring output storage


tests = [
    (([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]]),
    (([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]), [[1, 2], [3, 10], [12, 16]]),
]
run_tests(insert_interval, tests)
