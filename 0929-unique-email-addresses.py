from typing import List
from tests import run_tests


def unique_email_count(emails: List[str]) -> int:
    unique_emails = set()

    for email in emails:
        username, domain = email.split("@")
        id = username.split("+")[0].replace(".", "")
        unique_emails.add(id + "@" + domain)

    return len(unique_emails)


tests = [
    (["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"], 2),
    (["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"], 3),
]
run_tests(unique_email_count, tests)
