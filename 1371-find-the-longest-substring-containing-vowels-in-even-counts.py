from tests import run_tests


def find_the_longest_substring(s: str) -> int:
    vowel_index = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
    bitmask = 0
    seen = {0: -1}
    res = 0

    for i, c in enumerate(s):
        if c in vowel_index:
            bitmask ^= 1 << vowel_index[c]
        if bitmask in seen:
            res = max(res, i - seen[bitmask])
        else:
            seen[bitmask] = i

    return res


tests = [
    ("eleetminicoworoep", 13),
    ("leetcodeisgreat", 5),
    ("bcbcbc", 6),
]
run_tests(find_the_longest_substring, tests)
