```python
"""
MIT 6.006 — Lecture 3: Selection Sort

Selection Sort repeatedly finds the maximum element in the unsorted
portion of the array and swaps it into its final position.

The sorted portion grows from right to left.

Example:
    [4, 2, 7, 1]
         ↓
    [4, 2, 1, 7]
         ↓
    [1, 2, 4, 7]

Complexity:
    Time:  Θ(n²)
    Space: O(1)

Properties:
    In-place: Yes
    Stable:   No
"""


def selection_sort(A):
    """
    Sort A in ascending order using Selection Sort.

    The algorithm scans the unsorted portion to find the maximum
    element, then swaps it into the last position of that portion.

    Time: Θ(n²)
    Space: O(1)
    """

    # Start from the last position and move toward the beginning.
    for i in range(len(A) - 1, 0, -1):

        # Assume A[i] is the maximum element.
        m = i

        # Find the maximum element in A[0:i].
        for j in range(i):
            if A[m] < A[j]:
                m = j

        # Move the maximum element to its final position.
        A[m], A[i] = A[i], A[m]
```
