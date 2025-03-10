from typing import List
from tests import run_tests


def diff_ways_to_add_parentheses(expression: str) -> List[int]:
    cache = {}

    def divide_and_conquer(s):
        if s in cache:
            return cache[s]

        res = []

        for i, c in enumerate(s):
            if c in "+-*":
                res_left = divide_and_conquer(s[:i])
                res_right = divide_and_conquer(s[i + 1 :])

                for left in res_left:
                    for right in res_right:
                        if c == "+":
                            res.append(left + right)
                        elif c == "-":
                            res.append(left - right)
                        elif c == "*":
                            res.append(left * right)

        if not res:  # s is just a number
            res.append(int(s))
        cache[s] = res
        return res

    return divide_and_conquer(expression)


# Time complexity: O(2^n)
# Space complexity: O(2^n)


tests = [
    ("2-1-1", [2, 0]),
    ("2*3-4*5", [-34, -10, -14, -10, 10]),
]
run_tests(diff_ways_to_add_parentheses, tests)
