"""
MIT 6.006 — Lecture 5: Counting Sort

Counting Sort fixes direct access array sort by allowing duplicate keys.
It counts how many items have each key, then uses cumulative sums to
compute the final position of every item.

    1. Count how many items have each key.
    2. Turn the counts into cumulative sums (D[k] = number of items with key <= k).
    3. Walk the input BACKWARDS and place each item at index D[key] - 1,
       then decrement D[key].

Complexity:
    Time:  Θ(n + u)
    Space: O(n + u)

Properties:
    In-place: No
    Stable:   Yes (because step 3 walks the input backwards)
    Linear when u = O(n).
"""


class Item:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"Item({self.key}, {self.value!r})"


def counting_sort(A, key=lambda x: x.key, u=None):
    """Stable sort of A in place by key(x), a non-negative integer.

    u = 1 + the largest possible key. If not given, it is computed from A.
    """
    if not A:
        return
    if u is None:
        u = 1 + max(key(x) for x in A)        # O(n) find maximum key
    D = [0] * u                               # O(u) counts
    for x in A:                               # O(n) count keys
        D[key(x)] += 1
    for k in range(1, u):                     # O(u) cumulative sums
        D[k] += D[k - 1]
    for x in reversed(list(A)):               # O(n) move items into place
        D[key(x)] -= 1
        A[D[key(x)]] = x


def counting_sort_chains(A):
    """Same result using one chain (list) per key. Also stable, Θ(n + u)."""
    if not A:
        return
    u = 1 + max(x.key for x in A)             # O(n)
    D = [[] for _ in range(u)]                # O(u) direct access array of chains
    for x in A:                               # O(n) append keeps input order
        D[x.key].append(x)
    i = 0
    for chain in D:                           # O(u) read out in key order
        for x in chain:
            A[i] = x
            i += 1


if __name__ == "__main__":
    A = [Item(2, "a"), Item(0, "b"), Item(2, "c"), Item(1, "d")]
    counting_sort(A)
    print(A)   # [Item(0, 'b'), Item(1, 'd'), Item(2, 'a'), Item(2, 'c')]  (a before c: stable)

    B = [Item(2, "a"), Item(0, "b"), Item(2, "c"), Item(1, "d")]
    counting_sort_chains(B)
    print(B)   # same result
