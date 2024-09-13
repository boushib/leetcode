from typing import List


class SparseVector:

    def __init__(self, nums: List[int]):
        self.non_zero_indexes = {}

        for i, n in enumerate(nums):
            if n != 0:
                self.non_zero_indexes[i] = n

    def dot_product(self, vec: List[int]) -> int:
        res = 0

        for i in range(len(vec)):
            if i in self.non_zero_indexes:
                res += self.non_zero_indexes[i] * vec[i]

        return res


# vec1, vec2 = [1,0,0,2,3], [0,3,0,4,0] # 8
# vec1, vec2 = [0,1,0,0,0], [0,0,0,0,2] # 0
vec1, vec2 = [0, 1, 0, 0, 2, 0, 0], [1, 0, 0, 0, 3, 0, 4]  # 6
sv = SparseVector(vec1)
print(sv.dot_product(vec2))
