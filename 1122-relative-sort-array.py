from typing import List
from tests import run_tests


def relative_sort_array(arr1: List[int], arr2: List[int]) -> List[int]:
    count = {}
    res = []
    mx = float("-inf")

    for n in arr1:
        count[n] = count.get(n, 0) + 1
        mx = max(mx, n)

    for n in arr2:
        while count[n] > 0:
            res.append(n)
            count[n] -= 1

    for i in range(int(mx + 1)):
        while count.get(i, 0) > 0:
            res.append(i)
            count[i] -= 1

    return res


tests = [(([2, 3, 1, 3, 2, 4, 6, 7, 9, 2,
            19], [2, 1, 4, 3, 9, 6]), [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]),
         (([28, 6, 22, 8, 44, 17], [22, 28, 8, 6]), [22, 28, 8, 6, 17, 44])]
run_tests(relative_sort_array, tests)
