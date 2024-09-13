from typing import List
from tests import run_tests


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    count = {}

    for n in nums:
        count[n] = count.get(n, 0) + 1

    freq = [[] for _ in range(len(nums))]

    for k, v in count.values():
        freq[v - 1].append(k)


tests = [(([1, 1, 1, 2, 2, 3], 2), [1, 2]), (([1], 1), [1])]
run_tests(top_k_frequent, tests)
