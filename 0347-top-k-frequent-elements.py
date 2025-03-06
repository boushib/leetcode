from typing import List
from tests import run_tests


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    count = {}
    res = []

    for n in nums:
        count[n] = count.get(n, 0) + 1

    freq = [[] for _ in range(len(nums))]

    for n, occ in count.items():
        freq[occ - 1].append(n)

    for i in range(len(freq) - 1, -1, -1):
        for n in freq[i]:
            res.append(n)

            if len(res) == k:
                return res


tests = [
    (([1, 1, 1, 2, 2, 3], 2), [1, 2]),
    (([1], 1), [1]),
]
run_tests(top_k_frequent, tests)
