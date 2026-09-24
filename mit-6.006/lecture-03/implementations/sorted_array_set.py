```python
"""
MIT 6.006 — Lecture 3
Sorted Array Set

A Set stores items according to their keys rather than their positions.

This implementation uses a sorted Array_Seq as the underlying data
structure. Because the array is kept sorted, binary search can be used
for efficient lookup operations.

Main tradeoff:

    Search       → O(log n)
    Insert       → O(n)
    Delete       → O(n)

The O(log n) search comes from binary search.
The O(n) insertion/deletion comes from shifting elements in the array.
"""


class Sorted_Array_Set:

    def __init__(self):
        # Store the set using an Array_Seq.
        self.A = Array_Seq()

    def __len__(self):
        # The Array_Seq already maintains its size.
        # O(1)
        return len(self.A)

    def __iter__(self):
        # Iterate through the elements in sorted order.
        # O(n)
        yield from self.A

    def iter_order(self):
        # Since the array is already sorted, normal iteration
        # produces the elements in order.
        yield from self

    def build(self, X):
        """
        Build the set from an iterable X.

        The elements are first placed into the underlying array
        and then sorted.
        """
        self.A.build(X)
        self._sort()

    def _sort(self):
        """
        Sort the underlying array.

        TODO: Implement the sorting algorithm from the lecture.
        """
        pass

    def _binary_search(self, k, i, j):
        """
        Find the position where key k belongs in A[i:j+1].

        Returns the index where k is found, or the position where
        k should be inserted if it is not present.

        Time: O(log n)
        """

        if i > j:
            return i

        m = (i + j) // 2
        x = self.A.get_at(m)

        if x.key > k:
            return self._binary_search(k, i, m - 1)

        if x.key < k:
            return self._binary_search(k, m + 1, j)

        return m

    def find_min(self):
        """
        Return the item with the smallest key.

        Time: O(1)
        """
        if len(self) > 0:
            return self.A.get_at(0)
        return None

    def find_max(self):
        """
        Return the item with the largest key.

        Time: O(1)
        """
        if len(self) > 0:
            return self.A.get_at(len(self) - 1)
        return None

    def find(self, k):
        """
        Find the item with key k.

        Binary search is used to locate the key.

        Time: O(log n)
        """
        if len(self) == 0:
            return None

        i = self._binary_search(k, 0, len(self) - 1)
        x = self.A.get_at(i)

        if x.key == k:
            return x

        return None

    def find_next(self, k):
        """
        Find the smallest item whose key is greater than k.

        Time: O(log n)
        """
        if len(self) == 0:
            return None

        i = self._binary_search(k, 0, len(self) - 1)
        x = self.A.get_at(i)

        if x.key > k:
            return x

        if i + 1 < len(self):
            return self.A.get_at(i + 1)

        return None

    def find_prev(self, k):
        """
        Find the largest item whose key is smaller than k.

        Time: O(log n)
        """
        if len(self) == 0:
            return None

        i = self._binary_search(k, 0, len(self) - 1)
        x = self.A.get_at(i)

        if x.key < k:
            return x

        if i > 0:
            return self.A.get_at(i - 1)

        return None

    def insert(self, x):
        """
        Insert item x while maintaining sorted order.

        If an item with the same key already exists, replace it.

        Binary search: O(log n)
        Array insertion: O(n)

        Overall: O(n)
        """

        if len(self.A) == 0:
            self.A.insert_first(x)
            return True

        i = self._binary_search(x.key, 0, len(self.A) - 1)
        k = self.A.get_at(i).key

        # If the key already exists, replace the existing item.
        if k == x.key:
            self.A.set_at(i, x)
            return False

        # Insert before or after the located position.
        if k > x.key:
            self.A.insert_at(i, x)
        else:
            self.A.insert_at(i + 1, x)

        return True

    def delete(self, k):
        """
        Delete and return the item with key k.

        Binary search finds the item, then Array_Seq performs
        the deletion.

        Overall: O(n)
        """

        i = self._binary_search(k, 0, len(self.A) - 1)

        assert self.A.get_at(i).key == k

        return self.A.delete_at(i)
```
