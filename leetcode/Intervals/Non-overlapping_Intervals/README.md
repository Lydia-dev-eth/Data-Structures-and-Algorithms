# Non-overlapping Intervals

> LeetCode 435 — Greedy / Sorting

## Problem

Given an array of intervals where `intervals[i] = [start_i, end_i]`, return the minimum number of intervals you need to remove to make the remaining intervals non-overlapping.

Two intervals that touch at an endpoint are considered non-overlapping.

### Example 1

```text
Input:  intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
```

We can remove `[1,3]`.

The remaining intervals are:

```text
[[1,2],[2,3],[3,4]]
```

They do not overlap.

### Example 2

```text
Input:  intervals = [[1,2],[1,2],[1,2]]
Output: 2
```

All three intervals overlap.

We can only keep one interval, so we must remove two.

### Example 3

```text
Input:  intervals = [[1,2],[2,3]]
Output: 0
```

The intervals touch at `2`, but they do not overlap.

Therefore, no intervals need to be removed.

---

## Approach — Greedy Algorithm

The main idea is to sort the intervals by their starting values and process them from left to right.

Whenever two intervals overlap, we remove one of them.

But which one should we remove?

**We should keep the interval that ends earlier.**

Why?

Because an interval that finishes earlier leaves more room for future intervals.

The solution uses three variables:

```python
intervals.sort(key=lambda x: x[0])

count = 0
end = intervals[0][1]
```

Where:

- `count` tracks the number of intervals to remove.
- `end` stores the ending point of the last kept interval.
- `intervals` contains the intervals sorted by their starting values.

The main idea is:

```text
Sort intervals
      ↓
Take the first interval
      ↓
Compare with the next interval
      ↓
Do they overlap?
   ┌──┴──┐
  No     Yes
   ↓      ↓
 Keep   Remove one
 both   and keep the
        earlier ending
      ↓
 Update end
      ↓
   Repeat
```

## Step 1 — Sort the Intervals

```python
intervals.sort(key=lambda x: x[0])
```

First, we sort the intervals by their starting values.

Why?

Because sorting allows us to process the intervals from left to right.

For example:

```python
intervals = [[1,2],[2,3],[3,4],[1,3]]
```

After sorting:

```python
[[1,2],[1,3],[2,3],[3,4]]
```

Now the intervals are arranged according to their starting points.

This makes it easier to determine whether the current interval overlaps with the previous one.

## Step 2 — Initialize the Variables

```python
count = 0
end = intervals[0][1]
```

We initialize two variables.

- `count = 0` because initially we have not removed any intervals.
- `end` stores the ending point of the first interval.

For example:

```python
intervals = [[1,2],[1,3],[2,3],[3,4]]
```

Initially:

```text
count = 0
end = 2
```

We use `end` to track the ending point of the interval we are keeping.

## Step 3 — Iterate Through the Remaining Intervals

```python
for i in range(1, len(intervals)):
```

We start from index `1` because the first interval is already being tracked by `end`.

For example:

```python
intervals = [[1,2],[1,3],[2,3],[3,4]]
```

We start processing:

```python
intervals[1] = [1,3]
```

For each interval, we compare its starting point with the ending point of the previously kept interval.

## Step 4 — Check if the Intervals Do Not Overlap

```python
if end <= intervals[i][0]:
    end = intervals[i][1]
```

If the previous interval ends before or exactly when the current interval starts, they do not overlap.

For example:

```python
previous = [1,2]
current = [2,3]
```

We compare:

```text
end = 2
current start = 2
```

Since:

```text
2 <= 2
```

the intervals do not overlap.

So we keep the current interval and update:

```python
end = intervals[i][1]
```

Now:

```text
end = 3
```

**Important:** We use `<=` because intervals that touch at an endpoint are considered non-overlapping.

For example:

```text
[1,2] [2,3]
```

These intervals can both remain.

## Step 5 — Handle Overlapping Intervals

This is the most important part of the algorithm.

```python
else:
    count += 1
    end = min(intervals[i][1], end)
```

If the current interval starts before the previous interval ends, they overlap.

We need to remove one of them.

But instead of always removing the current interval, we keep the interval that ends earlier.

Why?

Because keeping the interval with the smaller ending point gives us more space for future intervals.

### Example

Consider:

```python
intervals = [[1,3],[2,4]]
```

Visualize:

```text
[1-------3]
   [2-------4]
```

They overlap.

We have two choices:

**Choice 1 — Keep `[1,3]`**

```text
[1-------3]
```

**Choice 2 — Keep `[2,4]`**

```text
   [2-------4]
```

Both choices remove one interval.

However, keeping `[1,3]` is better because it finishes earlier.

We use:

```python
end = min(intervals[i][1], end)
```

Since:

```python
min(3,4) = 3
```

We keep:

```python
end = 3
```

And increment the removal count:

```python
count += 1
```

## Step 6 — Why Use `min()`?

The purpose of `min()` is to preserve the interval that ends earlier whenever an overlap occurs.

Consider:

```python
intervals = [[1,10],[2,3],[4,5]]
```

After sorting:

```python
[[1,10],[2,3],[4,5]]
```

Initially:

```python
end = 10
count = 0
```

The second interval overlaps with the first:

```text
[1-------------10]
   [2--3]
```

We have to remove one interval.

We keep `[2,3]` because it ends earlier:

```python
end = min(10,3)
```

Therefore:

```python
end = 3
count = 1
```

Now consider the next interval:

```text
[2--3]
     [4--5]
```

Since:

```text
3 <= 4
```

there is no overlap.

We can keep `[4,5]`.

Final result:

```python
count = 1
```

This is much better than keeping `[1,10]`, which would overlap with both remaining intervals.

**Key idea:** When intervals overlap, choosing the one that finishes earlier maximizes the space available for subsequent intervals.

---

## Why Does This Work?

The key property is that we want to keep as many non-overlapping intervals as possible.

Instead of directly deciding which intervals to remove, we make a greedy choice:

**Whenever two intervals overlap, keep the one that ends earlier.**

Why is this optimal?

Imagine two overlapping intervals:

```text
A = [1,10]
B = [2,5]
```

Both cannot be kept.

If we keep `[1,10]`, we may prevent several future intervals from being selected.

But if we keep `[2,5]`, we leave more room for subsequent intervals.

The earlier ending interval is always at least as good a choice for accommodating future intervals.

We handle two situations:

### Case 1 — No Overlap

```text
[1,3]    [3,5]
```

Since:

```text
3 <= 3
```

both intervals can remain.

We update:

```python
end = intervals[i][1]
```

### Case 2 — Overlap

```text
[1-------5]
   [2-------6]
```

Since:

```text
5 > 2
```

the intervals overlap.

We remove one and keep the interval that ends earlier:

```python
end = min(5,6)
```

We also increment:

```python
count += 1
```

The process continues until every interval has been considered.

---

## Example Walkthrough

Consider:

```python
intervals = [[1,2],[2,3],[3,4],[1,3]]
```

### Step 1 — Sort the Intervals

After sorting by starting values:

```python
[[1,2],[1,3],[2,3],[3,4]]
```

### Step 2 — Initialize

```python
count = 0
end = 2
```

We start with the first interval:

```text
[1,2]
```

### Step 3 — Process `[1,3]`

Compare:

```text
end = 2
current start = 1
```

Since:

```text
2 > 1
```

they overlap.

We increment:

```python
count = 1
```

Now keep the interval that ends earlier:

```python
end = min(2,3)
```

Therefore:

```python
end = 2
```

We keep `[1,2]`.

### Step 4 — Process `[2,3]`

Compare:

```text
end = 2
current start = 2
```

Since:

```text
2 <= 2
```

there is no overlap.

We keep the current interval:

```python
end = 3
```

### Step 5 — Process `[3,4]`

Compare:

```text
end = 3
current start = 3
```

Since:

```text
3 <= 3
```

there is no overlap.

We keep the current interval:

```python
end = 4
```

### Final Result

We removed only one interval:

```python
count = 1
```

Therefore, the answer is:

```text
1
```

---

## Complexity

### Time Complexity

**`O(n log n)`**

First, we sort the intervals:

```python
intervals.sort(key=lambda x: x[0])
```

Sorting takes:

```text
O(n log n)
```

Then we traverse the intervals once:

```python
for i in range(1, len(intervals)):
```

This takes:

```text
O(n)
```

Combining both operations:

```text
O(n log n) + O(n)
```

Therefore, the overall time complexity is:

```text
O(n log n)
```

### Space Complexity

The greedy scanning process uses only a constant number of variables:

```python
count
end
i
```

Therefore, the scanning algorithm itself uses:

```text
O(1)
```

The intervals are sorted in place. Python's sorting implementation may use up to `O(n)` temporary space in the worst case.

Therefore:

```text
Auxiliary Space: O(n) worst case for Python sorting.
Greedy Scan: O(1).
```

---

## Comparison

| Approach | Time | Space | Main Idea |
|---|---|---|---|
| Brute Force | Exponential in general | Depends on implementation | Try different combinations of intervals |
| Greedy + Sorting | `O(n log n)` | `O(n)` worst case in Python | Keep the interval that ends earlier |

The solution in `solution.py` uses **Greedy + Sorting**.

---

## Key Insight

The main insight is:

> **When two intervals overlap, always keep the interval that ends earlier.**

Why?

Because finishing earlier leaves more room for future intervals.

The important pattern is:

```text
Sort intervals
      ↓
Compare current interval with previous
      ↓
Do they overlap?
   ┌──┴──┐
  No     Yes
   ↓      ↓
 Keep   Remove one
 both   Keep earlier
        ending interval
      ↓
 Update end
      ↓
 Repeat
```

This is a classic Greedy Algorithm problem.

---

## What I Learned

- How to use sorting to simplify interval problems.
- How to detect overlapping intervals.
- Why intervals that touch at endpoints are non-overlapping.
- How Greedy Algorithms make locally optimal decisions.
- Why keeping the interval with the earlier ending point is beneficial.
- Why `min()` helps preserve the interval that finishes first.
- How to minimize removals by maximizing the number of intervals kept.
- Why the overall time complexity is `O(n log n)`.
- The difference between choosing intervals and removing intervals.

---

## Related Concepts

- Arrays
- Sorting
- Greedy Algorithms
- Intervals
- Non-overlapping Intervals
- Activity Selection Problem
- Interval Scheduling
- Time Complexity
- Space Complexity
