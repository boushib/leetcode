from tests import run_tests


def longest_substring_without_repeating_chars(s: str) -> int:
    res = 0
    left = 0
    char_set = set()

    for c in s:
        while c in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(c)
        res = max(res, len(char_set))

    return res


tests = [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3)]
run_tests(longest_substring_without_repeating_chars, tests)
