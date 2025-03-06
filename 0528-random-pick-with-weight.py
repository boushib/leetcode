from typing import List
from random import random


class RandomPickWithWeight:
    def __init__(self, nums: List[int]):
        self.sum = 0
        self.prefix_sum = []

        for n in nums:
            self.sum += n
            self.prefix_sum.append(self.sum)

    def pick_index(self) -> int:
        target = self.sum * random()
        lo, hi = 0, len(self.prefix_sum) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if target > self.prefix_sum[mid]:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo


# Time complexity: O(n)
# Space complexity: O(n)


rp = RandomPickWithWeight([1, 2, 3])
print(rp.pick_index())
print(rp.pick_index())
print(rp.pick_index())
print(rp.pick_index())
print(rp.pick_index())
print(rp.pick_index())
