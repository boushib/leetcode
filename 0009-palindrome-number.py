from tests import run_tests


def is_palindrome(n: int) -> bool:
    if n < 0:
        return False

    original_n, reversed_n = n, 0

    while n:
        reversed_n = reversed_n * 10 + n % 10
        n //= 10

    return original_n == reversed_n


tests = [(121, True), (-121, False), (10, False)]
run_tests(is_palindrome, tests)
