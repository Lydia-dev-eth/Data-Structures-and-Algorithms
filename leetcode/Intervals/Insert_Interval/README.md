# Insert Interval

> LeetCode 57 — Arrays / Intervals

## Problem

You are given an array of non-overlapping intervals sorted in ascending order by their starting values.

You are also given a new interval `newInterval`.

Insert the new interval into the existing intervals and merge any overlapping intervals.

Return the resulting array of non-overlapping intervals.

### Example 1

```text
Input:  intervals = [[1,3],[6,9]]
        newInterval = [2,5]

Output: [[1,5],[6,9]]
```

Because:

- `[1,3]` overlaps with `[2,5]`.
- They merge into `[1,5]`.
- `[6,9]` does not overlap with `[1,5]`.

### Example 2

```text
Input:  intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        newInterval = [4,8]

Output: [[1,2],[3,10],[12,16]]
```

Because:

- `[3,5]` overlaps with `[4,8]`.
- `[6,7]` also overlaps.
- `[8,10]` also overlaps because they share the endpoint `8`.
- All three intervals merge into `[3,10]`.

---

## Approach — Linear Scan

Since the existing intervals are already sorted and non-overlapping, we do not need to sort them again.

Instead, we traverse the intervals using a single pointer and divide the process into three main parts.

1. Add intervals that come before `newInterval`.
2. Merge all intervals that overlap with `newInterval`.
3. Add the remaining intervals that come after the merged interval.

The solution uses:

```python
i = 0
n = len(intervals)
b = []
```

where:

- `i` tracks the current interval.
- `n` stores the total number of intervals.
- `b` stores the final merged intervals.

The main idea is:

```text
Original Intervals + New Interval
              |
       Scan from Left
              |
    ┌─────────┼──────────┐
    ↓         ↓          ↓
  Before   Overlapping  After
    ↓         ↓          ↓
  Append    Merge      Append
    └─────────┼──────────┘
              ↓
       Final Intervals
```

## Step 1 — Initialize the Variables

```python
i = 0
n = len(intervals)
b = []
```

We initialize three variables.

- `i` starts at `0` because we begin from the first interval.
- `n` stores the number of existing intervals.
- `b` is an empty list that will contain the final result.

For example:

```python
intervals = [[1,3],[6,9]]
newInterval = [2,5]

i = 0
n = 2
b = []
```

We will process the intervals from left to right.

---

## Step 2 — Add Intervals That Come Before the New Interval

```python
while i < n and intervals[i][1] < newInterval[0]:
    b.append(intervals[i])
    i += 1
```

First, we identify intervals that are completely before `newInterval`.

We check:

```python
intervals[i][1] < newInterval[0]
```

Where:

- `intervals[i][1]` is the ending value of the current interval.
- `newInterval[0]` is the starting value of the new interval.

If the current interval ends before the new interval starts, they cannot overlap.

So we simply add the current interval to `b`.

### Example

```python
intervals = [[1,2],[3,5],[6,9]]
newInterval = [4,7]
```

For the first interval:

```text
[1,2]    [4,7]
```

We compare:

```text
2 < 4
```

Since this is true, `[1,2]` comes before the new interval.

So we append it:

```python
b = [[1,2]]
```

Then move to the next interval:

```python
i += 1
```

**Important:** We use `<` instead of `<=` because intervals that touch at an endpoint are considered overlapping.

For example:

```text
[1,4] and [4,5]
```

These intervals must be merged.

---

## Step 3 — Find and Merge Overlapping Intervals

This is the most important part of the algorithm.

```python
while i < n and intervals[i][0] <= newInterval[1]:
    newInterval[0] = min(intervals[i][0], newInterval[0])
    newInterval[1] = max(intervals[i][1], newInterval[1])
    i += 1
```

Now we process intervals that overlap with `newInterval`.

We check:

```python
intervals[i][0] <= newInterval[1]
```

Where:

- `intervals[i][0]` is the starting value of the current interval.
- `newInterval[1]` is the ending value of the new interval.

If the current interval starts before or at the end of `newInterval`, they overlap.

### Example

```python
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
```

The first interval `[1,2]` was already added because it comes before the new interval.

Now we process:

```text
[3,5] and [4,8]
```

Because:

```text
3 <= 8
```

They overlap.

We update the new interval:

```python
newInterval[0] = min(3,4)
newInterval[1] = max(5,8)
```

So:

```python
newInterval = [3,8]
```

### Why Use `min()` and `max()`?

We need to preserve the complete range covered by both intervals.

The starting value must be the smaller starting point:

```python
newInterval[0] = min(intervals[i][0], newInterval[0])
```

The ending value must be the larger ending point:

```python
newInterval[1] = max(intervals[i][1], newInterval[1])
```

For example:

```text
[3,5]
   [4,8]
```

After merging:

```text
[3------8]
```

### Continue Checking Other Intervals

After merging `[3,5]` and `[4,8]`, the new interval becomes:

```python
newInterval = [3,8]
```

We continue checking the next interval:

```text
[6,7]
```

Since:

```text
6 <= 8
```

it also overlaps.

We update:

```python
newInterval[0] = min(6,3)
newInterval[1] = max(7,8)
```

The result remains:

```python
newInterval = [3,8]
```

Now check:

```text
[8,10]
```

Since:

```text
8 <= 8
```

it also overlaps because the intervals share an endpoint.

We update:

```python
newInterval[0] = min(8,3)
newInterval[1] = max(10,8)
```

Now:

```python
newInterval = [3,10]
```

The next interval is:

```text
[12,16]
```

Since:

```text
12 <= 10
```

is false, we stop merging.

**Important:** We keep updating `newInterval` because merging one interval can make it overlap with additional intervals.

---

## Step 4 — Add the Merged Interval

After processing all overlapping intervals:

```python
b.append(newInterval)
```

We append the final merged interval to the result.

For example:

```python
newInterval = [3,10]
```

The result becomes:

```python
b = [[1,2],[3,10]]
```

If no intervals overlap with the new interval, we simply insert it into its correct position.

---

## Step 5 — Add the Remaining Intervals

```python
while i < n:
    b.append(intervals[i])
    i += 1
```

At this point, every remaining interval comes after the merged interval.

Why?

Because the original intervals are already sorted.

And we have already processed every interval that could overlap with `newInterval`.

Therefore, we can simply append the remaining intervals without checking for overlap.

For example:

```python
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
```

After merging:

```python
b = [[1,2],[3,10]]
```

The remaining interval is:

```python
[12,16]
```

We append it:

```python
b = [[1,2],[3,10],[12,16]]
```

---

## Step 6 — Return the Result

```python
return b
```

After processing all the intervals, `b` contains the final sorted, non-overlapping intervals.

For example:

```python
[[1,2],[3,10],[12,16]]
```

We return this result.

---

## Why Does This Work?

The key property is that the original intervals are already sorted and non-overlapping.

This allows us to process them from left to right without sorting.

We divide the intervals into three groups:

### Case 1 — Intervals Before the New Interval

```text
[1,2]     [4,7]
```

If:

```python
intervals[i][1] < newInterval[0]
```

the current interval is completely before the new interval.

We can safely append it.

### Case 2 — Overlapping Intervals

```text
[3,5]
   [4,8]
```

If:

```python
intervals[i][0] <= newInterval[1]
```

the current interval overlaps with the new interval.

We merge them using:

```python
min()
max()
```

We continue expanding the new interval until no more overlaps exist.

### Case 3 — Intervals After the New Interval

```text
[3,10]       [12,16]
```

Once the current interval starts after the merged interval ends, no further overlaps are possible.

Since the original intervals are sorted, all remaining intervals can simply be appended.

The process looks like:

```text
             Intervals
                 |
            Start Scan
                 |
        Is interval before?
                 |
          ┌──────┴──────┐
         Yes             No
          ↓               ↓
       Append       Does it overlap?
                         |
                   ┌─────┴─────┐
                  Yes           No
                   ↓             ↓
                 Merge        Append
                   |             |
                   ↓             ↓
             Expand new      Add remaining
              interval        intervals
                   |
                   ↓
             Final Result
```

---

## Example Walkthrough

Consider:

```python
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
```

Initially:

```python
i = 0
b = []
newInterval = [4,8]
```

### First Interval: `[1,2]`

Check:

```text
2 < 4
```

True.

Append it:

```python
b = [[1,2]]
```

Move the pointer:

```python
i = 1
```

### Second Interval: `[3,5]`

Check:

```text
3 <= 8
```

True.

Merge:

```python
newInterval = [3,8]
```

### Third Interval: `[6,7]`

Check:

```text
6 <= 8
```

True.

Merge:

```python
newInterval = [3,8]
```

### Fourth Interval: `[8,10]`

Check:

```text
8 <= 8
```

True.

Merge:

```python
newInterval = [3,10]
```

### Fifth Interval: `[12,16]`

Check:

```text
12 <= 10
```

False.

Stop merging.

Append the merged interval:

```python
b = [[1,2],[3,10]]
```

Finally, append the remaining interval:

```python
b = [[1,2],[3,10],[12,16]]
```

The final output is:

```python
[[1,2],[3,10],[12,16]]
```

---

## Complexity

### Time Complexity

**`O(n)`**

We traverse the existing intervals from left to right.

Each interval is processed at most once.

The algorithm has three scanning phases:

1. Find intervals before the new interval.
2. Find and merge overlapping intervals.
3. Append the remaining intervals.

Together, these operations take linear time.

Therefore:

```text
O(n)
```

For example:

```text
n intervals
     ↓
Check each interval once
     ↓
Finish
```

We do not need to sort the intervals because they are already sorted.

### Space Complexity

**`O(n)`**

We create a new result list `b` that may contain all the original intervals plus the new interval.

Therefore, the output requires:

```text
O(n)
```

The algorithm also uses only a constant number of additional variables:

```text
O(1)
```

So the auxiliary space excluding the output list is:

```text
O(1)
```

---

## Comparison

| Approach | Time | Space | Main Idea |
|---|---|---|---|
| Brute Force | `O(n log n)` | `O(n)` | Add the interval, sort everything, then merge |
| Linear Scan | `O(n)` | `O(n)` | Process before, overlapping, and after intervals |
| Sorting + Merge | `O(n log n)` | `O(n)` | Sort intervals and merge overlaps |

The solution in `solution.py` uses **Linear Scan**.

---

## Key Insight

The main insight is:

> **Because the original intervals are already sorted and non-overlapping, we only need one pass to insert and merge the new interval.**

The important pattern is:

```text
Scan from left to right
        ↓
Append intervals before newInterval
        ↓
Merge overlapping intervals
        ↓
Append the merged interval
        ↓
Append remaining intervals
        ↓
Return final result
```

The most important part is continuously updating the boundaries of `newInterval`.

One merge may expand the interval enough to overlap with additional intervals.

---

## What I Learned

- How to insert an interval into an already sorted array.
- Why the original intervals do not need to be sorted again.
- How to identify intervals that come before the new interval.
- How to detect overlapping intervals using their starting and ending values.
- Why `min()` updates the starting boundary.
- Why `max()` updates the ending boundary.
- Why touching endpoints are considered overlapping.
- How one pointer can process an entire array in a single pass.
- Why the time complexity is `O(n)` instead of `O(n log n)`.
- How to divide an interval problem into before, overlapping, and after regions.

---

## Related Concepts

- Arrays
- Intervals
- Interval Insertion
- Overlapping Intervals
- Sorting
- Linear Scan
- Two Pointers
- Greedy Algorithms
- Time Complexity
- Space Complexity
