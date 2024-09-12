from tests import run_tests


def add_strings(num1: str, num2: str) -> str:
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    res = []

    while i >= 0 or j >= 0 or carry:
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0
        _sum = n1 + n2 + carry
        carry = _sum // 10
        res.append(str(_sum % 10))
        i -= 1
        j -= 1

    return "".join(res[::-1])


tests = [
    (("11", "123"), "134"),
    (("456", "77"), "533"),
    (("0", "0"), "0"),
]
run_tests(add_strings, tests)
