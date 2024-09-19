# from heapq import heapify, heappop
from typing import List
from tests import run_tests


def find_kth_largest(nums: List[int], k: int) -> int:
    """
    max_heap = [-n for n in nums]
    heapify(max_heap)

    while max_heap and k >= 0:
        k -= 1

        if k == 0:
            return -heappop(max_heap)

        heappop(max_heap)

    return -1
    """
    mn, mx = min(nums), max(nums)
    count = [0] * (mx - mn + 1)

    for n in nums:
        count[n - mn] += 1

    for i in range(len(count) - 1, -1, -1):
        k -= count[i]

        if k <= 0:
            return mn + i

    return -1


tests = [(([3, 2, 1, 5, 6, 4], 2), 5), (([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)]
run_tests(find_kth_largest, tests)
