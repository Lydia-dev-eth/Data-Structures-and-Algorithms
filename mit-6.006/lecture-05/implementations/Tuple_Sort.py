"""
MIT 6.006 — Lecture 5: Tuple Sort

Tuple Sort sorts items by several keys (a lexicographic order) using a
STABLE sorting algorithm as a subroutine.

    1. Order the keys from most important (k1) to least important (kd).
    2. Stable-sort by the LEAST important key.
    3. Repeat for each more important key, ending with the most important.

Complexity:
    Time:  d * (time of one stable sort)
           With counting sort on keys < u: Θ(d * (n + u))
    Space: O(n + u)

Properties:
    Requires a stable subroutine, otherwise later rounds destroy earlier ones.
    Works like sorting a spreadsheet by several columns.

Note: the PDF describes tuple sort in words only (no code). This code is
written from that description and reuses the PDF's counting_sort, setting
x.key to the current part before each pass (the same trick radix_sort uses).
"""

from counting_sort import counting_sort


class Item:
    def __init__(self, *parts):
        self.parts = parts                    # (k1, k2, ..., kd), k1 most important

    def __repr__(self):
        return f"Item{self.parts}"


def tuple_sort(A, d):
    "Sort A lexicographically by x.parts[0], ..., x.parts[d-1] (non-negative ints)"
    for i in range(d - 1, -1, -1):            # least important -> most important
        for x in A:
            x.key = x.parts[i]                # O(n) assign key i
        counting_sort(A)                      # stable sort on key i


if __name__ == "__main__":
    A = [Item(2, 1), Item(1, 2), Item(2, 0), Item(1, 1)]
    tuple_sort(A, d=2)
    print(A)   # [Item(1, 1), Item(1, 2), Item(2, 0), Item(2, 1)]
