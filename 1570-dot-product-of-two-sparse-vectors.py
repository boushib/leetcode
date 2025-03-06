from typing import List


class SparseVector:

    def __init__(self, nums: List[int]):
        self.non_zero_indexes = {}

        for i, n in enumerate(nums):
            if n != 0:
                self.non_zero_indexes[i] = n

    def dot_product(self, vec: List[int]) -> int:
        res = 0

        for k, v in vec.non_zero_indexes.items():
            if k in self.non_zero_indexes:
                res += v * self.non_zero_indexes[k]

        return res


# Time complexity: O(n)
# Space complexity: O(n)


sv1 = SparseVector([0, 1, 0, 0, 2, 0, 0])
sv2 = SparseVector([1, 0, 0, 0, 3, 0, 4])
sv3 = SparseVector([1, 0, 0, 2, 3])
sv4 = SparseVector([0, 3, 0, 4, 0])
sv5 = SparseVector([0, 1, 0, 0, 0])
sv6 = SparseVector([0, 0, 0, 0, 2])
print(sv1.dot_product(sv2))  # 6
print(sv3.dot_product(sv4))  # 8
print(sv5.dot_product(sv6))  # 0
