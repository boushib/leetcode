from typing import List
from tests import run_tests


def generate_parenthesis(n: int) -> List[str]:
    res = []

    def backtrack(curr_str, open_count, close_count):
        if len(curr_str) == 2 * n:
            res.append(curr_str)
            return None

        if open_count < n:
            backtrack(curr_str + "(", open_count + 1, close_count)
        if close_count < open_count:
            backtrack(curr_str + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return res


# Time complexity: 4^n / sqrt(n)
# Space complexity: 4^n / sqrt(n)

tests = [
    (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    (1, ["()"]),
]
run_tests(generate_parenthesis, tests)
