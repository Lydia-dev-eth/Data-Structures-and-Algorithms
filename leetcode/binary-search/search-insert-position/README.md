# Search Insert Position

## Problem

Given a **sorted array of distinct integers** and a target value, return the index if the target is found. If it is not found, return the index where it would be inserted to keep the array sorted.

You must write an algorithm with **O(log n)** runtime complexity.

### Examples

**Example 1**

```text
Input: nums = [1, 3, 5, 6], target = 5
Output: 2
```

Explanation: The target `5` exists at index `2`.

**Example 2**

```text
Input: nums = [1, 3, 5, 6], target = 2
Output: 1
```

Explanation: The target `2` is not present. Inserting it at index `1` gives `[1, 2, 3, 5, 6]`.

**Example 3**

```text
Input: nums = [1, 3, 5, 6], target = 7
Output: 4
```

Explanation: The target `7` belongs at the end of the array, at index `4`.

---

## Approach — Recursive Binary Search

Instead of checking every element, we use **binary search** to eliminate half of the search range at each step.

The important idea is that when the target is not found, the final value of `left` identifies where the target should be inserted.

### Step 1: Check whether the search range is empty

```python
if left > right:
    return left
```

`left` and `right` represent the boundaries of the current search range.

If `left > right`, there are no elements left to examine.

But why return `left` instead of `-1`?

Because this problem does not ask us to return `-1` when the target is missing. It asks us to return the target's **insertion index**.

At this point, `left` indicates the correct position for the target.

For example:

```text
nums = [1, 3, 5, 6]
target = 2
```

Binary search eventually reaches:

```text
left = 1
right = 0
```

Since `left > right`, the search ends and returns `1`.

Inserting `2` at index `1` keeps the array sorted.

### Step 2: Find the middle element

```python
mid = (left + right) // 2
```

We calculate the middle index of the current search range.

For example:

```text
nums = [1, 3, 5, 6]
left = 0
right = 3

mid = (0 + 3) // 2
mid = 1
```

Therefore:

```text
Index:  0  1  2  3
Nums:  [1, 3, 5, 6]
           ↑
          mid
```

The middle value is `3`.

Because the array is sorted, we can compare the target with this value to determine which half could contain the target.

### Step 3: Check whether the target is found

```python
if target == nums[mid]:
    return mid
```

If the target equals the middle element, we have found it.

We return its index immediately.

For example:

```text
nums = [1, 3, 5, 6]
target = 5
```

When `mid = 2`:

```text
nums[mid] = 5
target = 5
```

The target is found, so we return `2`.

### Step 4: Search the right half

```python
if target > nums[mid]:
    return binary_search(nums, mid + 1, right, target)
```

If the target is greater than the middle value, it must be to the right of `mid`, if it exists.

We can eliminate the left half, including `mid`.

For example:

```text
nums = [1, 3, 5, 6]
target = 6
```

Initially:

```text
left = 0
right = 3
mid = 1
nums[mid] = 3
```

Since `6 > 3`, we search the right half:

```python
binary_search(nums, 2, 3, 6)
```

The search range becomes:

```text
[5, 6]
 ↑  ↑
left right
```

We continue until we find the target.

### Step 5: Search the left half

```python
else:
    return binary_search(nums, left, mid - 1, target)
```

If the target is smaller than the middle value, we search the left half.

We eliminate the right half, including `mid`.

For example:

```text
nums = [1, 3, 5, 6]
target = 2
```

Initially:

```text
left = 0
right = 3
mid = 1
nums[mid] = 3
```

Since `2 < 3`, we search the left half:

```python
binary_search(nums, 0, 0, 2)
```

Now the search range contains only the value `1`.

Because `2 > 1`, the next call becomes:

```python
binary_search(nums, 1, 0, 2)
```

Now `left > right`, so we return `left`, which is `1`.

That is exactly where `2` should be inserted.

---

## Step-by-Step Walkthrough

Let's trace the algorithm using:

```python
nums = [1, 3, 5, 6]
target = 2
```

### First call

```text
left = 0
right = 3
mid = (0 + 3) // 2 = 1
nums[mid] = 3
```

Since `2 < 3`, search the left half.

```text
New range: left = 0, right = 0
```

### Second call

```text
left = 0
right = 0
mid = (0 + 0) // 2 = 0
nums[mid] = 1
```

Since `2 > 1`, search the right half.

```text
New range: left = 1, right = 0
```

### Third call

```text
left = 1
right = 0
```

Now:

```python
left > right
```

The search range is empty, so we return:

```python
return left
```

The result is:

```text
Output: 1
```

The target belongs at index `1`.

### Visual summary

```text
Original array:
[1, 3, 5, 6]
    ↑
   mid

Target 2 is smaller than 3.
Search left half.

[1]
 ↑
mid

Target 2 is greater than 1.
Search right of index 0.

left = 1
right = 0

left > right → return 1
```

---

## Why Does This Work?

Binary search works because the array is sorted.

At every step, we compare the target with the middle element.

* If the target equals the middle element, we return its index.
* If the target is greater, we search the right half.
* If the target is smaller, we search the left half.

Each comparison eliminates approximately half of the remaining search range.

The key difference between this problem and ordinary binary search is what happens when the target is missing.

In ordinary binary search, we might return `-1` when the search range becomes empty.

Here, we return `left`.

Why?

When the search ends:

* Every element before `left` is smaller than the target.
* Every element at or after `left` is greater than the target, if such an element exists.

Therefore, `left` is the correct insertion index.

This also handles insertion at the beginning or end of the array.

---

## Complexity

### Time Complexity: O(log n)

Each recursive call eliminates approximately half of the remaining search range.

For an array of size `n`, binary search requires at most approximately `log₂(n)` steps.

Therefore, the time complexity is:

**O(log n)**

### Space Complexity: O(log n)

This implementation uses recursion.

Each recursive call adds a frame to the call stack, and there can be approximately `log₂(n)` recursive calls before the search ends.

Therefore, the auxiliary space complexity is:

**O(log n)**

An iterative binary search implementation could reduce the auxiliary space complexity to **O(1)**.

---

## Comparison

| Approach                                | Time Complexity | Space Complexity | Explanation                                                              |
| --------------------------------------- | --------------- | ---------------- | ------------------------------------------------------------------------ |
| Linear Search                           | O(n)            | O(1)             | Checks elements one by one to find the target or its insertion position. |
| Recursive Binary Search — this solution | O(log n)        | O(log n)         | Eliminates half of the search range at each step using recursion.        |
| Iterative Binary Search                 | O(log n)        | O(1)             | Uses a loop instead of recursive calls.                                  |

### Why is binary search better than linear search here?

Because the array is already sorted, we do not need to examine every element.

Binary search uses the ordering to eliminate half of the remaining possibilities at each step.

For large arrays, this can significantly reduce the number of comparisons.

---

## Key Insight

**When binary search finishes without finding the target, `left` gives the insertion position.**

The condition:

```python
if left > right:
    return left
```

is the most important part of this solution.

Instead of treating an unsuccessful search as a failure, we use the final search boundaries to determine where the missing target belongs.

For example:

```text
nums = [1, 3, 5, 6]
target = 4
```

The correct insertion position is index `2`:

```text
[1, 3, 4, 5, 6]
       ↑
    index 2
```

Binary search eventually returns `left = 2`.

No additional shifting or insertion is needed because the problem asks only for the index, not for a modified array.

---

## What I Learned

* How recursive binary search divides a sorted array into smaller search ranges.
* Why we use `mid + 1` and `mid - 1` to eliminate the middle element after comparing it with the target.
* How the final value of `left` identifies the insertion position when the target is absent.
* How one binary search algorithm can solve both searching and insertion-position problems.
* Why recursive binary search uses O(log n) auxiliary space due to its call stack.
* How sorted data allows us to achieve O(log n) time instead of O(n).

---

## Related Concepts

* Binary Search
* Recursion
* Search Boundaries
* Sorted Arrays
* Insertion Position
* Lower Bound
* Time and Space Complexity
