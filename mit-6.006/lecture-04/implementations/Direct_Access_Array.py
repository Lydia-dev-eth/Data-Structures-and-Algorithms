"""
MIT 6.006 — Lecture 4: Direct Access Array

A Direct Access Array stores an item with key k at index k of a static array.
Random access in memory lets us jump straight to the slot.

    1. Allocate an array of length u (keys are integers in 0 ... u-1).
    2. insert(x) writes x at index x.key.
    3. find(k) reads index k.

Complexity:
    build:                    O(u)
    find / insert / delete:   O(1)
    find_min / find_max /
    find_next / find_prev:    O(u)
    Space:                    O(u)

Properties:
    Keys must be unique integers in the range 0 ... u-1.
    Fast find, but wasteful when u is much larger than n.
    Order operations must scan the whole array.
"""


class Item:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"Item({self.key}, {self.value!r})"


class DirectAccessArray:
    def __init__(self, u):
        self.u = u
        self.A = [None] * u                       # O(u)

    def find(self, k):                            # O(1)
        return self.A[k]

    def insert(self, x):                          # O(1)
        self.A[x.key] = x

    def delete(self, k):                          # O(1)
        x = self.A[k]
        self.A[k] = None
        return x

    def find_min(self):                           # O(u)
        for x in self.A:
            if x is not None:
                return x
        return None

    def find_max(self):                           # O(u)
        for i in range(self.u - 1, -1, -1):
            if self.A[i] is not None:
                return self.A[i]
        return None

    def find_next(self, k):                       # O(u)  smallest key > k
        for i in range(k + 1, self.u):
            if self.A[i] is not None:
                return self.A[i]
        return None

    def find_prev(self, k):                       # O(u)  largest key < k
        for i in range(k - 1, -1, -1):
            if self.A[i] is not None:
                return self.A[i]
        return None

    def delete_max(self):                         # O(u)
        x = self.find_max()
        if x is not None:
            self.A[x.key] = None
        return x

    def __iter__(self):                           # O(u), in key order
        for x in self.A:
            if x is not None:
                yield x


if __name__ == "__main__":
    d = DirectAccessArray(10)
    for k in (2, 5, 7):
        d.insert(Item(k, f"v{k}"))

    print(d.find(5))          # Item(5, 'v5')
    print(d.find(4))          # None
    print(d.find_min())       # Item(2, 'v2')
    print(d.find_max())       # Item(7, 'v7')
    print(d.find_next(5))     # Item(7, 'v7')
    print(d.find_prev(5))     # Item(2, 'v2')
    d.delete(5)
    print(list(d))            # [Item(2, 'v2'), Item(7, 'v7')]
