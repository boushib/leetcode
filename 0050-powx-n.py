from tests import run_tests


def my_pow(x: float, n: int) -> float:
    if n < 0:
        n = -n
        x = 1 / x

    res = 1

    while n > 0:
        if n % 2 == 1:
            res *= x
            n -= 1

        x *= x
        n = n // 2

    return round(res, 5)


tests = [((2.00000, 10), 1024.00000), ((2.10000, 3), 9.26100), ((2.00000, -2), 0.25000), ((200, 0), 1.00000)]
run_tests(my_pow, tests)
