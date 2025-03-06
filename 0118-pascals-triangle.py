from typing import List
from tests import run_tests


def generate_pascal_triangle(n: int) -> List[List[int]]:
    res = [[1]]

    for i in range(1, n):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = res[i - 1][j - 1] + res[i - 1][j]

        res.append(row)

    return res


# Time complexity: O(n^2)
# Space complexity: O(n^2)


tests = [(5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])]
run_tests(generate_pascal_triangle, tests)
