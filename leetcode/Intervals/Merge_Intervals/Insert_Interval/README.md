# Merge Intervals

> LeetCode 56 — Divide and Conquer / Sorting

## Problem

Given an array of intervals where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

### Example 1

```text
Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
```

Because:

- `[1,3]` and `[2,6]` overlap, so they merge into `[1,6]`.
- `[8,10]` does not overlap with `[1,6]`.
- `[15,18]` does not overlap with `[8,10]`.

### Example 2

```text
Input:  intervals = [[1,4],[4,5]]
Output: [[1,5]]
```

Because the intervals overlap at `4`, so they merge into `[1,5]`.

---

## Approach — Divide and Conquer (Merge Sort)

Instead of sorting all the intervals first and then merging them, we can use **Divide and Conquer**.

The idea is to divide the intervals into two halves, recursively merge each half, and then combine the results.

This approach is similar to Merge Sort.

The solution uses two functions:

```python
merge(intervals)
```

Divides the intervals into smaller groups and recursively merges them.

```python
merge_intervals(left, right)
```

Combines two already sorted and non-overlapping interval lists while merging any overlapping intervals.

The main process is:

```text
Original Intervals
        ↓
      Divide
     /      \
Left Half  Right Half
    ↓          ↓
 Recursively Merge
     \        /
      Merge Both
          ↓
   Final Intervals
```

## Step 1 — Check the Base Case

```python
if len(intervals) <= 1:
    return intervals
```

If the array contains zero or one interval, there is nothing to merge.

For example:

```python
intervals = [[1,3]]
```

There is only one interval, so we return it directly.

This is the base case that stops the recursion.

## Step 2 — Divide the Intervals

```python
mid = len(intervals) // 2
```

We calculate the middle index to divide the intervals into two halves.

For example:

```python
intervals = [[1,3],[2,6],[8,10],[15,18]]
```

The middle index is:

```python
mid = 2
```

We divide the intervals using slicing:

```python
intervals[:mid]
intervals[mid:]
```

This gives:

```text
Left Half:

[[1,3],[2,6]]

Right Half:

[[8,10],[15,18]]
```

## Step 3 — Recursively Merge Both Halves

```python
L = self.merge(intervals[:mid])
R = self.merge(intervals[mid:])
```

We recursively call `merge()` on both halves.

Each half is divided again until every group contains only one interval.

For example:

```text
[[1,3],[2,6],[8,10],[15,18]]
             |
          Divide
         /      \
   [[1,3],[2,6]] [[8,10],[15,18]]
         |              |
       Divide          Divide
       /   \           /    \
    [1,3] [2,6]     [8,10] [15,18]
```

Now each group contains one interval.

Since a single interval is already sorted and cannot overlap with another interval inside its group, the recursion starts returning the results.

Each recursive call combines its two halves.

Eventually, we get:

```python
L = [[1,6]]
R = [[8,10],[15,18]]
```

Both lists are now sorted and contain no overlapping intervals.

## Step 4 — Merge the Two Halves

```python
merg = self.merge_intervals(L, R)
return merg
```

After recursively merging both halves, we combine their results.

The important point is that:

- `L` is already sorted and contains no overlapping intervals.
- `R` is already sorted and contains no overlapping intervals.

Now we only need to merge these two sorted lists.

For example:

```python
L = [[1,3]]
R = [[2,6]]
```

Since `[1,3]` and `[2,6]` overlap, they become:

```python
[[1,6]]
```

This operation is handled by `merge_intervals()`.

## Step 5 — Initialize the Pointers

Inside `merge_intervals()`:

```python
i, j, l1, l2 = 0, 0, len(left), len(right)

b = []
```

We use two pointers to traverse the two sorted interval lists.

Where:

- `i` tracks the current interval in `left`.
- `j` tracks the current interval in `right`.
- `l1` stores the length of `left`.
- `l2` stores the length of `right`.
- `b` stores the final merged intervals.

For example:

```python
left = [[1,3],[8,10]]
right = [[2,6],[15,18]]
```

Initially:

```text
i = 0
j = 0

b = []
```

We compare the intervals and process them in increasing order of their starting values.

## Step 6 — Process the Intervals

```python
while i < l1 or j < l2:
```

We continue processing until both lists are exhausted.

There are three possible situations.

### Case 1 — The Left List Is Exhausted

```python
if i == l1:
    interval = right[j]
    j += 1
```

If there are no intervals left in the left list, we take the next interval from the right list.

For example:

```python
left = [[1,3]]
right = [[2,6],[8,10]]
```

After processing `[1,3]`, we may still have intervals remaining in the right list.

So we take:

```python
interval = right[j]
```

Then move the right pointer forward.

### Case 2 — The Right List Is Exhausted

```python
elif j == l2:
    interval = left[i]
    i += 1
```

If there are no intervals left in the right list, we take the next interval from the left list.

This ensures that every interval is processed.

### Case 3 — Both Lists Have Intervals

```python
else:
    if left[i][0] <= right[j][0]:
        interval = left[i]
        i += 1
    else:
        interval = right[j]
        j += 1
```

We compare the starting values of the current intervals.

If:

```python
left[i][0] <= right[j][0]
```

we take the interval from the left list.

Otherwise, we take the interval from the right list.

Why?

Because we want to process intervals in increasing order of their starting points.

For example:

```python
left = [[1,3],[8,10]]
right = [[2,6],[15,18]]
```

Comparing:

```text
left[0][0]  = 1
right[0][0] = 2
```

Since:

```text
1 < 2
```

we take:

```python
interval = [1,3]
```

Then move the left pointer forward.

## Step 7 — Check if the Intervals Overlap

This is the most important part of the algorithm.

```python
if not b or b[-1][1] < interval[0]:
    b.append(interval)
```

There are two situations.

### Case 1 — The Result List Is Empty

If `b` is empty, we simply add the current interval.

For example:

```python
b = []
interval = [1,3]
```

We add:

```python
b = [[1,3]]
```

### Case 2 — The Intervals Do Not Overlap

We check:

```python
b[-1][1] < interval[0]
```

Where:

- `b[-1][1]` is the ending value of the previous interval.
- `interval[0]` is the starting value of the current interval.

If the previous interval ends before the current interval starts, there is no overlap.

For example:

```python
previous = [1,3]
current = [5,8]
```

Because:

```text
3 < 5
```

The intervals do not overlap.

So we append the current interval:

```python
b.append(interval)
```

## Step 8 — Merge Overlapping Intervals

```python
else:
    b[-1][1] = max(b[-1][1], interval[1])
```

If the previous interval overlaps with the current interval, we merge them.

For example:

```python
previous = [1,3]
current = [2,6]
```

The intervals overlap because:

```text
3 >= 2
```

We update the ending value:

```python
b[-1][1] = max(3,6)
```

The result becomes:

```python
b = [[1,6]]
```

Why use `max()`?

Because the merged interval must end at the larger of the two ending values.

It also handles cases where one interval is completely inside another.

For example:

```python
previous = [1,10]
current = [3,5]
```

The merged interval remains:

```python
[1,10]
```

## Step 9 — Return the Merged Intervals

```python
return b
```

After processing every interval, `b` contains the final sorted, non-overlapping intervals.

For example:

```python
left = [[1,3],[8,10]]
right = [[2,6],[15,18]]
```

The merging process produces:

```python
[[1,6],[8,10],[15,18]]
```

We return this result.

---

## Implementation

```python
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # If there is zero or one interval, it is already merged.
        if len(intervals) <= 1:
            return intervals

        # Divide the intervals into two halves.
        mid = len(intervals) // 2

        # Recursively merge the left half.
        L = self.merge(intervals[:mid])

        # Recursively merge the right half.
        R = self.merge(intervals[mid:])

        # Merge the two sorted halves.
        merg = self.merge_intervals(L, R)

        return merg

    def merge_intervals(self, left, right):

        # Initialize pointers for both sorted lists.
        i, j, l1, l2 = 0, 0, len(left), len(right)

        # Store the final merged intervals.
        b = []

        # Process intervals until both lists are exhausted.
        while i < l1 or j < l2:

            # If the left list is exhausted, take from the right.
            if i == l1:
                interval = right[j]
                j += 1

            # If the right list is exhausted, take from the left.
            elif j == l2:
                interval = left[i]
                i += 1

            # Otherwise, take the interval with the smaller start.
            else:
                if left[i][0] <= right[j][0]:
                    interval = left[i]
                    i += 1
                else:
                    interval = right[j]
                    j += 1

            # If there is no overlap, add the current interval.
            if not b or b[-1][1] < interval[0]:
                b.append(interval)

            # Otherwise, merge the overlapping intervals.
            else:
                b[-1][1] = max(b[-1][1], interval[1])

        return b


# Time Complexity: O(n log n)
# Space Complexity: O(n) — temporary lists and merging results.
# Recursion Stack: O(log n).
```

## Why Does This Work?

The key idea is that we use **Divide and Conquer** to solve a larger problem by breaking it into smaller problems.

Every recursive call returns a sorted list of non-overlapping intervals.

When two sorted lists are combined, we:

1. Compare their starting values.
2. Take the interval that starts first.
3. Check whether it overlaps with the previous interval.
4. Merge overlapping intervals.
5. Otherwise, add a new interval.

Because both input lists are already sorted, we can merge them using two pointers without sorting them again.

### Example Walkthrough

Consider:

```python
intervals = [[1,3],[2,6],[8,10],[15,18]]
```

After dividing and recursively merging:

```python
L = [[1,6]]
R = [[8,10],[15,18]]
```

Now we merge both lists.

First:

```text
[1,6] and [8,10]
```

Since:

```text
6 < 8
```

they do not overlap.

So we add `[8,10]`.

Next:

```text
[8,10] and [15,18]
```

Since:

```text
10 < 15
```

they do not overlap either.

The final result is:

```python
[[1,6],[8,10],[15,18]]
```

---

## Complexity

### Time Complexity

**`O(n log n)`**

The algorithm divides the intervals into two halves until each group contains one interval.

At every recursion level, the merging process examines each interval once.

For example:

```text
Level 1:  n intervals       → O(n)

Level 2:  n intervals       → O(n)

Level 3:  n intervals       → O(n)

              ...
```

There are approximately `log n` levels.

Therefore:

```text
O(n) × O(log n)
```

Final time complexity:

```text
O(n log n)
```

### Space Complexity

**`O(n)` auxiliary space**

The implementation creates temporary lists through:

- Array slicing (`intervals[:mid]` and `intervals[mid:]`).
- Recursive results.
- The merged output list `b`.

Together, these require `O(n)` auxiliary space.

The recursion stack itself requires:

```text
O(log n)
```

Therefore:

```text
Auxiliary Space: O(n)
Recursion Stack: O(log n)
```

---

## Comparison

| Approach | Time | Space | Main Idea |
|---|---|---|---|
| Sorting + Linear Merge | `O(n log n)` | `O(n)` | Sort by starting point, then merge |
| Recursive Divide and Conquer | `O(n log n)` | `O(n)` | Recursively divide and merge intervals |
| Brute Force | Can be `O(n²)` | Depends on implementation | Repeatedly compare and merge intervals |

The solution in `solution.py` uses **Recursive Divide and Conquer**.

---

## Key Insight

The main insight is:

> **Instead of merging all intervals at once, recursively merge smaller groups of intervals and combine their results.**

The important pattern is:

```text
Divide
  ↓
Solve smaller problems
  ↓
Merge sorted results
  ↓
Check overlapping intervals
  ↓
Combine when necessary
  ↓
Return final result
```

This is an application of the Merge Sort pattern to interval problems.

---

## What I Learned

- How Divide and Conquer works.
- How to apply the Merge Sort idea to interval problems.
- How recursion breaks a large problem into smaller problems.
- How to merge two sorted lists using two pointers.
- How to detect overlapping intervals.
- Why `max()` is used to update the ending point.
- Why merging two sorted lists takes `O(n)` time.
- Why the overall time complexity is `O(n log n)`.
- The difference between sorting intervals and merging overlapping intervals.

---

## Related Concepts

- Arrays
- Sorting
- Merge Sort
- Divide and Conquer
- Recursion
- Two Pointers
- Intervals
- Overlapping Intervals
- Time Complexity
- Space Complexity
- Recursive Call Stack
