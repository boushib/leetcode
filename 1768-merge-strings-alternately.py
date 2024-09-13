from tests import run_tests


def merge_strings_alternately(s, t):
    size_s, size_t = len(s), len(t)
    chars = []

    for i in range(max(size_s, size_t)):
        if i < size_s:
            chars.append(s[i])
        if i < size_t:
            chars.append(t[i])

    return "".join(chars)


tests = [(("abc", "pqr"), "apbqcr"), (("ab", "pqrs"), "apbqrs"), (("abcd", "pq"), "apbqcd")]
run_tests(merge_strings_alternately, tests)
