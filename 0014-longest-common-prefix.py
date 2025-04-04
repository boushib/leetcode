from typing import List
from tests import run_tests


def longest_common_prefix(strs: List[str]) -> str:
    min_size = min(len(s) for s in strs)
    res = ""

    for i in range(min_size):
        c = strs[0][i]
        for s in strs[1:]:
            if s[i] != c:
                return res
        res += c

    return res


# Time complexity: O(n * m), where n is the number of strings and m is the size of the smallest string
# Space complexity: O(m)


tests = [
    (["flower", "flow", "flight"], "fl"),
    (["dog", "racecar", "car"], ""),
]
run_tests(longest_common_prefix, tests)
