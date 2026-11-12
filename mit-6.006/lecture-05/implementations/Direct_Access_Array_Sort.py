"""
MIT 6.006 — Lecture 5: Direct Access Array Sort

Sort items by using their keys as indices of a direct access array.

    1. Find the largest key and allocate an array of length u = max key + 1.
    2. Put each item x at index x.key.
    3. Read the array from left to right, returning items as they are found.

Complexity:
    Time:  Θ(n + u)
    Space: O(u)

Properties:
    In-place: No (needs the O(u) direct access array)
    Stable:   Not applicable (keys must be distinct)
    Linear when u = O(n), but cannot handle duplicate keys or large key ranges.
"""


class Item:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"Item({self.key}, {self.value!r})"


def direct_access_sort(A):
    """Sort A in place, assuming items have distinct non-negative integer keys."""
    u = 1 + max(x.key for x in A)             # O(n) find maximum key
    D = [None] * u                            # O(u) direct access array
    for x in A:                               # O(n) insert items
        assert D[x.key] is None, "duplicate key"
        D[x.key] = x
    i = 0
    for key in range(u):                      # O(u) read out items in order
        if D[key] is not None:
            A[i] = D[key]
            i += 1


if __name__ == "__main__":
    A = [Item(k) for k in (5, 2, 9, 0, 7)]
    direct_access_sort(A)
    print([x.key for x in A])                 # [0, 2, 5, 7, 9]
