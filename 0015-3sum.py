from typing import List
from tests import run_tests


def three_sum(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    for i in range(len(nums)):
        if nums[i] > 0:
            break

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        lo, hi = i + 1, len(nums) - 1

        while lo < hi:
            _sum = nums[lo] + nums[hi] + nums[i]

            if _sum < 0:
                lo += 1
            elif _sum > 0:
                hi -= 1
            else:
                res.append([nums[lo], nums[hi], nums[i]])
                lo += 1
                hi -= 1

                while lo < len(nums) and nums[lo] == nums[lo - 1]:
                    lo += 1

    return res


tests = [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 0, 0], [[0, 0, 0]]),
    ([0, 0, 0, 0], [[0, 0, 0]]),
    ([0, 1, 1], []),
]
run_tests()
