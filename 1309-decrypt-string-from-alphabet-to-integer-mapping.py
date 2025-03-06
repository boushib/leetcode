from tests import run_tests


def freq_alphabets(s: str) -> str:
    res = []
    n = len(s)
    alphabets = "-abcdefghijklmnopqrstuvwxyz"
    i = 0

    while i < n:
        if i < n - 2 and s[i + 2] == "#":
            res.append(alphabets[int(s[i] + s[i + 1])])
            i += 3
        else:
            res.append(alphabets[int(s[i])])
            i += 1

    return "".join(res)


# Time complexity: O(n)
# Space complexity: O(n)


tests = [("10#11#12", "jkab"), ("1326#", "acz")]
run_tests(freq_alphabets, tests)
