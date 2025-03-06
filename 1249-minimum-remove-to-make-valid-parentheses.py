from tests import run_tests


def min_remove_to_make_valid_parentheses(s: str) -> str:
    balanced = []
    balanced_count = 0

    for i in range(len(s)):
        c = s[i]

        if c == ")" and balanced_count == 0:
            continue

        if c == "(":
            balanced_count += 1

        if c == ")":
            balanced_count -= 1

        balanced.append(c)

    res = []
    balanced_count = 0

    for i in range(len(balanced) - 1, -1, -1):
        c = balanced[i]

        if c == "(" and balanced_count == 0:
            continue

        if c == "(":
            balanced_count -= 1

        if c == ")":
            balanced_count += 1

        res.append(c)

    return "".join(res[::-1])


# Time complexity: O(n)
# Space complexity: O(n)


tests = [("lee(t(c)o)de)", "lee(t(c)o)de"), ("a)b(c)d", "ab(c)d"), ("))((", "")]
run_tests(min_remove_to_make_valid_parentheses, tests)
