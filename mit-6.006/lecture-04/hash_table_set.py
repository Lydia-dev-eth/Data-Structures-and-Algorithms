"""
MIT 6.006 — Lecture 4: Hash Table Set (chaining + universal hashing)

A Hash Table maps keys from a huge range (size u) into a small table (size m = O(n)).
Collisions are handled by chaining: each slot holds a list of items.

    1. Pick a random hash function h(k) = ((a*k + b) mod p) mod m.
    2. insert / find / delete work on the chain at index h(k).
    3. Rebuild the table (new size, new random a and b) when it gets
       too full or too empty, so that m stays Theta(n).

Complexity:
    build:                    O(n) expected
    find:                     O(1) expected
    insert / delete:          O(1) amortized, expected
    find_min / find_max /
    find_next / find_prev:    O(n)
    Space:                    O(n)

Properties:
    Expected chain size <= 1 + (n - 1) / m = O(1) when m = Omega(n).
    The expectation is over the random choice of hash function,
    not over the input keys.
    No useful ordering: order operations scan every item.
"""

from random import randint


class Item:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"Item({self.key}, {self.value!r})"


class HashTableSet:
    def __init__(self):
        self.p = 2**31 - 1            # prime larger than the key range
        self.size = 0                 # n = number of stored items
        self.A = []                   # the table: list of chains
        self._rebuild(1)              # start with a small table

    # ---------- hashing ----------

    def _new_hash(self):
        self.a = randint(1, self.p - 1)    # a != 0
        self.b = randint(0, self.p - 1)

    def _hash(self, k):                    # O(1)
        return ((self.a * k + self.b) % self.p) % len(self.A)

    # ---------- resizing ----------

    def _rebuild(self, n):                 # O(n)
        """New table with m = 2 * max(n, 1) slots and a new random hash."""
        old_items = [x for chain in self.A for x in chain]
        self._new_hash()
        self.A = [[] for _ in range(2 * max(n, 1))]
        for x in old_items:
            self.A[self._hash(x.key)].append(x)

    def _resize(self, n):
        m = len(self.A)
        if n >= m or n <= m // 4:          # too full or too empty
            self._rebuild(n)

    # ---------- Set interface ----------

    def __len__(self):
        return self.size

    def __iter__(self):                    # O(n + m), no particular order
        for chain in self.A:
            yield from chain

    def build(self, X):                    # O(n) expected
        for x in X:
            self.insert(x)

    def find(self, k):                     # O(1) expected
        for x in self.A[self._hash(k)]:
            if x.key == k:
                return x
        return None

    def insert(self, x):                   # O(1) amortized, expected
        """Insert x. If the key exists, replace it and return False."""
        chain = self.A[self._hash(x.key)]
        for i, y in enumerate(chain):
            if y.key == x.key:
                chain[i] = x
                return False
        self._resize(self.size + 1)
        self.A[self._hash(x.key)].append(x)   # hash may have changed
        self.size += 1
        return True

    def delete(self, k):                   # O(1) amortized, expected
        """Remove and return the item with key k (None if absent)."""
        chain = self.A[self._hash(k)]
        for i, x in enumerate(chain):
            if x.key == k:
                chain.pop(i)
                self.size -= 1
                self._resize(self.size)
                return x
        return None

    # ---------- Order operations: all O(n) ----------

    def find_min(self):
        out = None
        for x in self:
            if out is None or x.key < out.key:
                out = x
        return out

    def find_max(self):
        out = None
        for x in self:
            if out is None or x.key > out.key:
                out = x
        return out

    def find_next(self, k):                # smallest key > k
        out = None
        for x in self:
            if x.key > k and (out is None or x.key < out.key):
                out = x
        return out

    def find_prev(self, k):                # largest key < k
        out = None
        for x in self:
            if x.key < k and (out is None or x.key > out.key):
                out = x
        return out

    def iter_order(self):                  # O(n^2): n calls to find_next
        x = self.find_min()
        while x:
            yield x
            x = self.find_next(x.key)


def has_duplicates(A):
    """DUPLICATES problem: expected O(n) using a hash table."""
    seen = HashTableSet()
    for a in A:
        if seen.find(a) is not None:
            return True
        seen.insert(Item(a))
    return False


if __name__ == "__main__":
    h = HashTableSet()
    h.build(Item(k, f"v{k}") for k in (12, 7, 22, 3, 5, 10_000_000))

    print(len(h))                          # 6
    print(h.find(22))                      # Item(22, 'v22')
    print(h.find(99))                      # None
    print(h.find_min(), h.find_max())      # Item(3, 'v3') Item(10000000, 'v10000000')
    print(h.find_next(7))                  # Item(12, 'v12')
    h.delete(22)
    print([x.key for x in h.iter_order()]) # [3, 5, 7, 12, 10000000]

    print(has_duplicates([4, 8, 15, 16, 23, 42]))   # False
    print(has_duplicates([4, 8, 15, 8]))            # True
