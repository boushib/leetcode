from tests import run_tests


def is_palindrome(s: str) -> bool:
    lo, hi = 0, len(s) - 1

    while lo < hi:
        while lo < hi and not s[lo].isalnum():
            lo += 1

        while lo < hi and not s[hi].isalnum():
            hi -= 1

        if s[lo].lower() != s[hi].lower():
            return False

        lo += 1
        hi -= 1

    return True


tests = [("A man, a plan, a canal: Panama", True), ("race a car", False),
         (" ", True)]
run_tests(is_palindrome, tests)
