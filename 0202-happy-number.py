from tests import run_tests


def sum_of_squares(n):
    res = 0

    while n:
        d = n % 10
        res += d * d
        n //= 10

    return res


def is_happy_number(n: int) -> bool:
    seen = set()  # can be solve with O(1) memory using LinkedList cycle

    while n not in seen:
        seen.add(n)
        n = sum_of_squares(n)

        if n == 1:
            return True

    return False


# Time complexity: O(log(n))
# Space complexity: O(log(n))


tests = [(19, True), (2, False)]
run_tests(is_happy_number, tests)
