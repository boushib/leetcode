from tests import run_tests


def rotate_string(s: str, t: str) -> bool:
    return len(s) == len(t) and t in s + s


tests = [(("abcde", "cdeab"), True), (("abcde", "abced"), False)]
run_tests(rotate_string, tests)
