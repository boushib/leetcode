from tests import run_tests


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count_s, count_t = {}, {}

    for i in range(len(s)):
        count_s[s[i]] = count_s.get(s[i], 0) + 1
        count_t[t[i]] = count_t.get(t[i], 0) + 1

    for k, v in count_s.items():
        if v != count_t.get(k, 0):
            return False

    return True


# Time complexity: O(n)
# Space complexity: O(n)


tests = [(("anagram", "nagaram"), True), (("rat", "car"), False)]
run_tests(is_anagram, tests)
