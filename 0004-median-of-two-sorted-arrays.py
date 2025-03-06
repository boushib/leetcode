from typing import List
from tests import run_tests


def find_median_of_sorted_arrays(a: List[int], b: List[int]) -> float:
    half_size = (len(a) + len(b)) // 2

    if len(b) < len(a):
        a, b = b, a

    lo, hi = 0, len(a)

    while lo <= hi:
        mid_a = (lo + hi) // 2
        mid_b = half_size - mid_a
        a_left = a[mid_a - 1] if mid_a > 0 else float("-inf")
        a_right = a[mid_a] if mid_a < len(a) else float("inf")
        b_left = b[mid_b - 1] if mid_b > 0 else float("-inf")
        b_right = b[mid_b] if mid_b < len(b) else float("inf")

        # right partitions
        if a_left <= b_right and b_left <= a_right:
            if (len(a) + len(b)) % 2 == 1:
                return min(a_right, b_right)
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        elif a_left >= b_right:  # a is too large
            hi = mid_a - 1
        else:  # a is too small
            lo = mid_a + 1


tests = [
    (([], [1]), 1),
    (([1, 3], [2]), 2),
    (([], [2, 3]), 2.5),
    (([0, 0], [0, 0]), 0),
    (([1, 2], [3, 4]), 2.5),
    (([1, 2], [1, 1, 1]), 1),
]
run_tests(find_median_of_sorted_arrays, tests)
