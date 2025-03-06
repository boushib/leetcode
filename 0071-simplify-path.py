from tests import run_tests


def simplify_path(path: str) -> str:
    stack = []

    for c in path.split("/"):
        if c == "" or c == ".":
            continue

        if c == "..":
            if stack:
                stack.pop()
        else:
            stack.append(c)

    return "/" + "/".join(stack)


# Time complexity: O(n)
# Space complexity: O(n)


tests = [
    ("/home/", "/home"),
    ("/home//foo/", "/home/foo"),
    ("/home/user/Documents/../Pictures", "/home/user/Pictures"),
    ("/../", "/"),
    ("/.../a/../b/c/../d/./", "/.../b/d"),
]
run_tests(simplify_path, tests)
