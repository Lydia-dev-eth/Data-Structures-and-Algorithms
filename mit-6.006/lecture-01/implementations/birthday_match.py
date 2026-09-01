"""
Birthday Matching
MIT 6.006 — Lecture 1

Two implementations of the same problem:

1. Naive approach
   Time: O(n²)
   Space: O(1) auxiliary

2. Hash-table approach
   Expected time: O(n)
   Space: O(n)
"""


def birthday_match_naive(students):
    """
    Compare each student's birthday with all previous students.

    Time: O(n²)
    Space: O(1) auxiliary
    """
    for i in range(len(students)):
        for j in range(i):
            if students[i][1] == students[j][1]:
                return students[i], students[j]

    return None


def birthday_match_hash(students):
    """
    Store previously seen birthdays in a hash table.

    Expected time: O(n)
    Space: O(n)
    """
    seen = {}

    for name, birthday in students:
        if birthday in seen:
            return name, seen[birthday]

        seen[birthday] = name

    return None
students = [
    ("Alice", "January 10"),
    ("Bob", "March 5"),
    ("Charlie", "January 10"),
]

print(birthday_match_naive(students))
print(birthday_match_hash(students))
