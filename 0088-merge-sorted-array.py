from typing import List
from tests import run_tests


def merge_sorted_arrays(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    # Assign bigger values starting from the end
    i = m + n - 1
    m -= 1
    n -= 1

    while m >= 0 and n >= 0:
        if nums1[m] > nums2[n]:
            nums1[i] = nums1[m]
            m -= 1
        else:
            nums1[i] = nums2[n]
            n -= 1

        i -= 1

    while n >= 0:
        nums1[n] = nums2[n]
        n -= 1

    return nums1


tests = [
    (([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3), [1, 2, 2, 3, 5, 6]),
    (([1], 1, [], 0), [1]),
    (([0], 0, [1], 1), [1]),
]
run_tests(merge_sorted_arrays, tests)
