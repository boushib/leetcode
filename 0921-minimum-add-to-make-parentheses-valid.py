from tests import run_tests


def min_add_to_make_parentheses_valid(s: str) -> int:
    opening_parentheses = 0
    min_additions_needed = 0  # # of opening parentheses needed to match the single closing parentheses

    for c in s:
        if c == "(":
            opening_parentheses += 1
            continue

        if opening_parentheses > 0:
            opening_parentheses -= 1
        else:
            min_additions_needed += 1

    return min_additions_needed + opening_parentheses


# Time complexity: O(n)
# Space complexity: O(1)


tests = [
    ("())", 1),
    ("(((", 3),
]
run_tests(min_add_to_make_parentheses_valid, tests)
