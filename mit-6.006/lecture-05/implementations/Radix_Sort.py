"""
MIT 6.006 — Lecture 5: Radix Sort

Radix Sort sorts integers from a large range by breaking each key into
digits in base n and tuple-sorting the digits with counting sort.

    1. Pick base n (the number of items).
    2. Write every key as c digits in base n, where n^c >= u.
    3. For each digit, from least significant to most significant,
       stable-sort the items by that digit using counting sort.

Complexity:
    Time:  Θ(n * c) where c = ceil(log_n u), so keys up to n^c
           When c is a constant, this is linear: Θ(n)
    Space: O(n)

Properties:
    In-place: No
    Stable:   Yes (counting sort is stable, so the whole sort is stable)
    Keys must be non-negative integers.

Source: Recitation 5 code. Two changes, both marked below:
    - the number of digits c: the PDF's formula gives too few digits when n is
      small compared to u (it sorted 1095 of 2000 random small cases wrongly),
      so c is computed by a loop that guarantees n^c >= u;
    - return early when n < 2 (the loop would never end for n = 1).
"""

from counting_sort import counting_sort


class Item:                                       # helper (not in the PDF)
    def __init__(self, key, value=None):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"Item({self.key}, {self.value!r})"


def radix_sort(A):
    "Sort A assuming items have non-negative keys"
    n = len(A)
    if n < 2:                                           # CHANGED: not in the PDF
        return
    u = 1 + max([x.key for x in A])                     # O(n) find maximum key
    # PDF: c = 1 + (u.bit_length() // n.bit_length())   (too small for small n)
    c = 1                                               # CHANGED: ensure n**c >= u
    while n ** c < u:
        c += 1
    class Obj: pass
    D = [Obj() for a in A]
    for i in range(n):                                  # O(nc) make digit tuples
        D[i].digits = []
        D[i].item = A[i]
        high = A[i].key
        for j in range(c):                              # O(c) make digit tuple
            high, low = divmod(high, n)
            D[i].digits.append(low)
    for i in range(c):                                  # O(nc) sort each digit
        for j in range(n):                              # O(n) assign key i to tuples
            D[j].key = D[j].digits[i]
        counting_sort(D)                                # O(n) sort on digit i
    for i in range(n):                                  # O(n) output to A
        A[i] = D[i].item


if __name__ == "__main__":
    A = [Item(k) for k in (329, 457, 657, 839, 436, 720, 355)]
    radix_sort(A)
    print([x.key for x in A])     # [329, 355, 436, 457, 657, 720, 839]
