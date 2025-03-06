from tests import run_tests


def calculate(s: str) -> int:
    res = 0
    curr_n = 0
    prev_n = 0
    op = "+"
    SUPPORTED_OPS = set(["+", "-", "*", "/"])

    for i, c in enumerate(s):
        if c.isdigit():
            curr_n = curr_n * 10 + int(c)

        if c in SUPPORTED_OPS or i == len(s) - 1:
            if op == "+":
                res += prev_n
                prev_n = curr_n
            if op == "-":
                res += prev_n
                prev_n = -curr_n
            if op == "*":
                prev_n *= curr_n
            if op == "/":
                prev_n = int(prev_n / curr_n)

            curr_n = 0
            op = c

    return res + prev_n


# Time complexity: O(n)
# Space complexity: O(1)


tests = [("3+2*2", 7), (" 3/2 ", 1), (" 3+5 / 2 ", 5)]
run_tests(calculate, tests)
