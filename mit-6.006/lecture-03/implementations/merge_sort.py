```python
"""
MIT 6.006 — Lecture 3: Merge Sort

Merge Sort uses divide and conquer:

    1. Divide the array into two halves.
    2. Recursively sort each half.
    3. Merge the two sorted halves.

Complexity:
    Time:  Θ(n log n)
    Space: O(n)

Properties:
    In-place: No (standard implementation)
    Stable:   Yes, when equal elements preserve their original order
"""


def merge_sort(A, a=0, b=None):
    """
    Sort the sub-array A[a:b] using Merge Sort.

    The range uses Python's half-open convention:

        A[a:b]

    includes a but excludes b.

    Time: O(n log n)
    Space: O(n)
    """

    # If no ending position was provided, sort the entire array.
    if b is None:
        b = len(A)

    # Continue dividing while there is more than one element.
    if 1 < b - a:

        # Find the middle of the current range.
        c = (a + b + 1) // 2

        # Recursively sort the left half.
        merge_sort(A, a, c)

        # Recursively sort the right half.
        merge_sort(A, c, b)

        # Copy the two sorted halves.
        L, R = A[a:c], A[c:b]

        # Pointers for the left and right halves.
        i, j = 0, 0

        # Merge L and R back into A[a:b].
        while a < b:

            # Take from L if R is exhausted, or if L's current
            # element is smaller than R's current element.
            if (j >= len(R)) or (i < len(L) and L[i] < R[j]):
                A[a] = L[i]
                i += 1

            else:
                # Otherwise take the next element from R.
                A[a] = R[j]
                j += 1

            # Move to the next position in the original array.
            a += 1
```
