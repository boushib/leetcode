from typing import List
from tests import run_tests

class MergeSort:
    def __init__(self, nums: List[int]) -> None:
        self.nums = nums
        self.temp = [0] * len(nums)

    def merge(self, start: int, mid: int, end: int) -> None:
        for i in range(start, end + 1):
            self.temp[i] = self.nums[i]

        left, right = start, mid + 1
        current = start

        while left <= mid and right <= end:
            if self.temp[left] <= self.temp[right]:
                self.nums[current] = self.temp[left]
                left += 1
            else:
                self.nums[current] = self.temp[right]
                right += 1
            current += 1

        while left <= mid:
            self.nums[current] = self.temp[left]
            left += 1
            current += 1

        while right <= end:
            self.nums[current] = self.temp[right]
            right += 1
            current += 1

    def merge_sort(self, start: int, end: int) -> None:
        if start < end:
            mid = (start + end) // 2
            self.merge_sort(start, mid)
            self.merge_sort(mid + 1, end)
            self.merge(start, mid, end)

    def sort(self) -> List[int]:
        self.merge_sort(0, len(self.nums) - 1)
        return self.nums

def sort_array(nums: List[int]) -> List[int]:
    return MergeSort(nums).sort()

# Time complexity: O (n * log(n))
# Space complexity: O (n)

tests = [
    ([1], [1]),
    ([2, 1], [1, 2]),
    ([5, 2, 3, 1], [1, 2, 3, 5]),
    ([10, -5, 3, 0, 2], [-5, 0, 2, 3, 10]),
    ([5, 1, 1, 2, 0, 0], [0, 0, 1, 1, 2, 5]),
    ([3, 0, -1, 8, 7, 2], [-1, 0, 2, 3, 7, 8]),
]
run_tests(sort_array, tests)
