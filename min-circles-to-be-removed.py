from typing import List, Tuple
from tests import run_tests


def min_circles_to_be_removed(circles: List[Tuple[int, int]]) -> int:
    intervals = [(c - r, c + r) for c, r in circles]
    intervals.sort(key=lambda x: x[1])
    prev_end = float("-inf")
    non_overlapping = 0

    for start, end in intervals:
        if start > prev_end:
            non_overlapping += 1
            prev_end = end

    return len(circles) - non_overlapping


tests = [
    ([(0, 3), (2, 3), (4, 3)], 2),
    ([(1, 1), (4, 1), (7, 1), (10, 1)], 0),
    ([(1, 2), (3, 2), (5, 2), (7, 2)], 2),
]
run_tests(min_circles_to_be_removed, tests)
