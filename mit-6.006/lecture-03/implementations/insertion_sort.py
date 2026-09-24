```python
"""
MIT 6.006 — Lecture 3: Insertion Sort

Insertion Sort builds a sorted prefix of the array one element at
a time. Each new element is moved left until it reaches its correct
position.

Example:
    [5, 2, 4, 1]
    [2, 5, 4, 1]
    [2, 4, 5, 1]
    [1, 2, 4, 5]

Complexity:
    Best:  Θ(n)
    Worst: Θ(n²)
    Space: O(1)

Properties:
    In-place: Yes
    Stable:   Yes
"""


def insertion_sort(A):
    """
    Sort A in ascending order using Insertion Sort.

    Time:
        Best:  Θ(n)
        Worst: Θ(n²)

    Space: O(1)
    """

    # Start from the second element.
    for i in range(1, len(A)):

        # Move A[i] left until it reaches its correct position.
        j = i

        while j > 0 and A[j] < A[j - 1]:

            # Swap the current element with the larger element before it.
            A[j - 1], A[j] = A[j], A[j - 1]

            j -= 1
```
