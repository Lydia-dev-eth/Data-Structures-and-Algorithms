# Binary Search

## Problem

Given a sorted array `nums` and a target value, return the index of `target` if it exists in the array.

If the target does not exist, return `-1`.

### Example 1

```text
Input:  nums = [-1,0,3,5,9,12], target = 9
Output: 4
```

Because:

```text
nums[4] = 9
```

### Example 2

```text
Input:  nums = [-1,0,3,5,9,12], target = 2
Output: -1
```

`2` does not exist in the array.

---

## Approach — Recursive Binary Search

Because the array is **sorted**, we do not need to check every element.

Instead, we repeatedly check the middle element and eliminate half of the remaining search space.

The solution uses a helper function:

```text
binary_search(nums, left, right)
```

where:

* `left` is the beginning of the current search range.
* `right` is the end of the current search range.

---

### Step 1 — Check if the Search Range Is Empty

```python
if left > right:
    return -1
```

If `left` becomes greater than `right`, there are no elements left to search.

This means the target does not exist.

For example:

```text
left = 4
right = 3
```

There is no valid search range:

```text
[ nothing ]
```

So we return:

```text
-1
```

---

### Step 2 — Find the Middle

```python
mid = (left + right) // 2
```

The middle index divides the current search range into two parts.

For example:

```text
[-1, 0, 3, 5, 9, 12]
       ↑
      mid
```

---

### Step 3 — Check the Middle Element

```python
if nums[mid] == target:
    return mid
```

If the middle element is the target, we are done.

For example:

```text
nums[mid] = 9
target = 9
```

So:

```text
return mid
```

---

### Step 4 — Search the Right Half

If:

```python
nums[mid] < target
```

then the target must be somewhere to the **right** of `mid`.

Why?

Because the array is sorted.

For example:

```text
[1, 3, 5, 7, 9, 12]
       ↑
      mid = 5
```

If our target is `9`:

```text
5 < 9
```

Everything to the left of `5` is even smaller.

So we can ignore it.

We search:

```python
return binary_search(nums, mid + 1, right)
```

---

### Step 5 — Search the Left Half

If:

```python
nums[mid] > target
```

then the target must be somewhere to the **left** of `mid`.

For example:

```text
[1, 3, 5, 7, 9, 12]
          ↑
         mid
```

If the target is `3` and:

```text
7 > 3
```

we can ignore everything to the right of `7`.

So we search:

```python
return binary_search(nums, left, mid - 1)
```

---

## Why Does This Work?

The key property is that the array is **sorted**.

Every time we compare the target with the middle element, we can eliminate approximately half of the remaining elements.

For example:

```text
n
↓
n / 2
↓
n / 4
↓
n / 8
↓
...
```

Instead of searching:

```text
1 → 2 → 3 → 4 → 5 → ...
```

we repeatedly cut the search space in half.

That is why Binary Search is much faster than a linear search for large sorted arrays.

---

## Complexity

### Time Complexity

Each recursive call eliminates approximately half of the remaining elements.

Therefore:

```text
O(log n)
```

For example:

```text
1,000,000 elements
        ↓
500,000
        ↓
250,000
        ↓
...
```

Only about `log₂(n)` comparisons are needed.

### Space Complexity

This implementation uses **recursion**.

Each recursive call remains on the call stack until the search finishes.

The maximum recursion depth is:

```text
O(log n)
```

Therefore:

```text
Space: O(log n)
```

An iterative binary search could reduce the auxiliary space to `O(1)`.

---

## Comparison

| Approach                |     Time |    Space | Requires Sorted Array |
| ----------------------- | -------: | -------: | --------------------- |
| Linear Search           |     O(n) |     O(1) | ❌                     |
| Recursive Binary Search | O(log n) | O(log n) | ✅                     |
| Iterative Binary Search | O(log n) |     O(1) | ✅                     |

Binary Search is faster asymptotically, but it requires the array to be sorted.

---

## Key Insight

The main insight is:

> **A sorted array gives us information that allows us to throw away half of the search space after every comparison.**

The important pattern is:

```text
Check middle
     ↓
 ┌───┴───┐
left    right
 ↓        ↓
discard one half
     ↓
repeat
```

This is one of the most important examples of **divide-and-conquer** thinking.

---

## What I Learned

* How Binary Search uses a sorted array to eliminate half of the search space.
* How to maintain `left` and `right` boundaries.
* How to calculate the middle index.
* How recursion can naturally represent the repeated search.
* Why Binary Search is `O(log n)` instead of `O(n)`.
* The difference between recursive and iterative Binary Search.
* Why sorting is what makes Binary Search possible.

---

## Related Concepts

* Arrays
* Binary Search
* Recursion
* Divide and Conquer
* Two-Pointer Boundaries
* Sorted Data
* Search Algorithms
* Time Complexity
* Space Complexity
* Recursive Call Stack
