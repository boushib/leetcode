from tests import run_tests


def valid_parentheses(s: str) -> bool:
    stack = []
    parentheses_map = {"(": ")", "{": "}", "[": "]"}

    for c in s:
        if c in parentheses_map.keys():
            stack.append(c)
            continue

        if not stack or parentheses_map[stack.pop()] != c:
            return False

    return len(stack) == 0


tests = [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("(()", False),
]
run_tests(valid_parentheses, tests)
