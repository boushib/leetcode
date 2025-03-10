from typing import List
from tests import run_tests


def merge_accounts(accounts: List[List[str]]) -> List[List[str]]:
    graph = {}
    email_to_name = {}

    for acc in accounts:
        name = acc[0]
        first_email = acc[1]

        for email in acc[1:]:
            if first_email not in graph:
                graph[first_email] = []
            if email not in graph:
                graph[email] = []

            graph[first_email].append(email)
            graph[email].append(first_email)
            email_to_name[email] = name

    visited = set()
    res = []

    def dfs(email, comp):
        visited.add(email)
        comp.append(email)

        for nb in graph[email]:
            if nb not in visited:
                dfs(nb, comp)

    for email in graph:
        if email not in visited:
            comp = []
            dfs(email, comp)
            res.append([email_to_name[email]] + sorted(comp))
    return res


# Time complexity: O(n * log(n))
# Space complexity: O(n)


tests = [
    (
        [
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ],
        [
            ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ],
    ),
    (
        [
            ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
            ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
            ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
            ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
            ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"],
        ],
        [
            ["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
            ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
            ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
            ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"],
            ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"],
        ],
    ),
]
run_tests(merge_accounts, tests)
