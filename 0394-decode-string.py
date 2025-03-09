from tests import run_tests


def decode_string(s):
    stack = []

    for c in s:
        if c == "]":
            segment = []

            while stack and stack[-1] != "[":
                segment.append(stack.pop())

            stack.pop()  # pop the "[" character
            count = []

            while stack and stack[-1].isdigit():
                count.append(stack.pop())

            stack.append(int("".join(count[::-1])) * "".join(segment[::-1]))
        else:
            stack.append(c)

    return "".join(stack)


# Time complexity: O(n)
# Space complexity: O(k * n) with k max expamsion factor

tests = [
    ("3[a]2[bc]", "aaabcbc"),
    ("3[a2[c]]", "accaccacc"),
    ("2[abc]3[cd]ef", "abcabccdcdcdef"),
]
run_tests(decode_string, tests)
