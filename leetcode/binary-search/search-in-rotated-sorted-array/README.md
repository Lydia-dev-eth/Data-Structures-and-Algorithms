# Search in Rotated Sorted Array

## Problem

Given an array of distinct integers `nums`, originally sorted in ascending order but rotated at an unknown position, return the index of `target` if it exists in the array.

If the target does not exist, return `-1`.

The solution must run in **O(log n)** time.

### Example 1

```text
Input:  nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

Because:

```text
nums[4] = 0
```

### Example 2

```text
Input:  nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

The target `3` does not exist in the array.

### Example 3

```text
Input:  nums = [1], target = 0
Output: -1
```

The only element is `1`, so the target cannot be found.

---

## Approach — Recursive Binary Search

I use **Recursive Binary Search** to find the target without scanning every element.

The challenge is that the array is rotated, so the entire array is not necessarily sorted.

For example:

```text
[4, 5, 6, 7, 0, 1, 2]
```

However, at every step, **at least one half of the current search range is sorted**.

My solution identifies the sorted half, checks whether the target belongs to it, and eliminates the half that cannot contain the target.

The helper function is:

```text
binary_search(nums, left, right)
```

* `left`: beginning of the current search range.
* `right`: end of the current search range.
* `mid`: middle index of the current range.

---

## Step 1 — Check if the Search Range Is Empty

```python
if left > right:
    return -1
```

If `left` becomes greater than `right`, there are no elements left to search.

Therefore, the target does not exist in the array.

For example:

```text
left = 4
right = 3
```

The search range is empty, so we return:

```text
-1
```

This is the base case of the recursion.

---

## Step 2 — Find the Middle

```python
mid = (left + right) // 2
```

The middle index divides the current search range into two parts.

For example:

```text
nums = [4, 5, 6, 7, 0, 1, 2]

left = 0
right = 6
mid = 3
```

Therefore:

```text
nums[mid] = 7
```

We first check whether the middle element is the target.

```python
if nums[mid] == target:
    return mid
```

If it is, we return its index immediately.

Otherwise, we determine which half is sorted.

---

## Step 3 — Check Whether the Left Half Is Sorted

```python
if nums[left] <= nums[mid]:
```

If the leftmost element is less than or equal to the middle element, the left half is sorted.

For example:

```text
[4, 5, 6, 7, 0, 1, 2]
 ↑           ↑
left        mid
```

Here:

```text
nums[left] = 4
nums[mid] = 7
```

Since:

```text
4 <= 7
```

the left half is sorted:

```text
[4, 5, 6, 7]
```

Now we need to determine whether the target belongs to this half.

### Step 3.1 — Check Whether the Target Is in the Sorted Left Half

```python
if nums[left] <= target < nums[mid]:
    return binary_search(nums, left, mid - 1)
```

The target belongs to the left half if:

```text
nums[left] <= target < nums[mid]
```

For example:

```text
nums = [4, 5, 6, 7, 0, 1, 2]
target = 5
```

The sorted left half is:

```text
[4, 5, 6, 7]
```

Since:

```text
4 <= 5 < 7
```

the target must be in the left half.

We search:

```python
binary_search(nums, left, mid - 1)
```

We use `mid - 1` because we already checked `nums[mid]`.

### Step 3.2 — Otherwise, Search the Right Half

```python
else:
    return binary_search(nums, mid + 1, right)
```

If the target does not belong to the sorted left half, we search the right half.

For example:

```text
nums = [4, 5, 6, 7, 0, 1, 2]
target = 1
```

The left half is:

```text
[4, 5, 6, 7]
```

Since `1` is not within the range from `4` to `7`, we discard the left half.

We search:

```text
[0, 1, 2]
```

using:

```python
binary_search(nums, mid + 1, right)
```

---

## Step 4 — Otherwise, the Right Half Is Sorted

```python
else:
```

If the left half is not sorted, the right half must be sorted.

For example:

```text
[6, 7, 0, 1, 2, 3, 4]
```

The middle element is `1`.

The left half contains the rotation point:

```text
[6, 7, 0, 1]
```

The right half is sorted:

```text
[1, 2, 3, 4]
```

Now we check whether the target belongs to the sorted right half.

### Step 4.1 — Check Whether the Target Is in the Sorted Right Half

```python
if nums[mid] < target <= nums[right]:
    return binary_search(nums, mid + 1, right)
```

The target belongs to the right half if:

```text
nums[mid] < target <= nums[right]
```

For example:

```text
nums = [6, 7, 0, 1, 2, 3, 4]
target = 3
```

Since:

```text
1 < 3 <= 4
```

the target belongs to the sorted right half.

We search:

```python
binary_search(nums, mid + 1, right)
```

### Step 4.2 — Otherwise, Search the Left Half

```python
else:
    return binary_search(nums, left, mid - 1)
```

If the target does not belong to the sorted right half, we search the left half.

For example:

```text
nums = [6, 7, 0, 1, 2, 3, 4]
target = 7
```

Since `7` is not in the sorted right half's value range, we search the left half.

---

## Why Does This Work?

The key observation is:

> **Even though the entire array is rotated, at least one half of the current search range is always sorted.**

Consider:

```text
[4, 5, 6, 7, 0, 1, 2]
```

The array consists of two increasing sections:

```text
[4, 5, 6, 7] [0, 1, 2]
```

The rotation disrupts the ordering between the two sections, but each individual section remains sorted.

At every recursive call, we do three things:

1. Find the middle element.
2. Identify which half is sorted.
3. Determine whether the target can belong to that half.

If the target belongs to the sorted half, we search there.

Otherwise, we search the other half.

This allows us to discard half of the search range at every step.

---

## Example Walkthrough

Consider:

```text
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
```

### First Call

```text
left = 0
right = 6
mid = 3
```

The middle element is:

```text
nums[3] = 7
```

The target is not `7`.

Check whether the left half is sorted:

```text
nums[left] <= nums[mid]
4 <= 7
```

Yes, the left half is sorted:

```text
[4, 5, 6, 7]
```

Check whether the target belongs to this half:

```text
4 <= 0 < 7
```

False.

Therefore, search the right half:

```text
left = mid + 1 = 4
right = 6
```

### Second Call

The current search range is:

```text
[0, 1, 2]
```

Calculate:

```text
left = 4
right = 6
mid = 5
```

The middle element is:

```text
nums[5] = 1
```

The target is not `1`.

Check whether the left half is sorted:

```text
nums[4] <= nums[5]
0 <= 1
```

Yes.

Now check whether the target belongs to this half:

```text
0 <= 0 < 1
```

True.

Therefore, search the left portion:

```text
left = 4
right = 4
```

### Third Call

Now:

```text
left = 4
right = 4
mid = 4
```

We find:

```text
nums[4] = 0
```

The target has been found.

Return:

```text
4
```

---

## Complexity

### Time Complexity

At every recursive call, we eliminate approximately half of the remaining search range.

```text
n
↓
n/2
↓
n/4
↓
n/8
↓
...
```

Therefore:

```text
O(log n)
```

This satisfies the problem's required time complexity.

### Space Complexity

The solution uses recursion.

Each recursive call adds a frame to the call stack. Since the search range is halved at each step, the maximum recursion depth is:

```text
O(log n)
```

Therefore:

```text
Space Complexity: O(log n)
```

An iterative implementation could achieve `O(1)` auxiliary space.

---

## Comparison

| Approach                |     Time |    Space | Main Idea                                             |
| ----------------------- | -------: | -------: | ----------------------------------------------------- |
| Linear Search           |     O(n) |     O(1) | Check each element                                    |
| Recursive Binary Search | O(log n) | O(log n) | Identify the sorted half and eliminate the other half |
| Iterative Binary Search | O(log n) |     O(1) | Same search strategy without recursion                |

The recursive binary-search approach is used in `solution.py`.

---

## Key Insight

The main insight is:

> **Don't try to find the rotation point first. Identify the sorted half, check whether the target belongs to it, and eliminate the half that cannot contain the target.**

The important decisions are:

```text
Is the left half sorted?
        |
     Yes / No
      /     \
Check left  Right half
range       is sorted
  |             |
Search left   Check right
or right      range
```

Binary Search is still possible because one half remains sorted, even when the entire array is not.

---

## What I Learned

* How rotation changes an otherwise sorted array.
* Why at least one half of the search range is sorted.
* How to identify the sorted half using `nums[left] <= nums[mid]`.
* How to determine whether the target belongs to the sorted half.
* Why the search range can be halved at every recursive call.
* How to adapt Binary Search when the entire array is not sorted.
* Why the solution achieves `O(log n)` time complexity.
* The difference between recursive and iterative Binary Search in auxiliary space.

---

## Related Concepts

* Arrays
* Binary Search
* Rotated Sorted Arrays
* Recursion
* Divide and Conquer
* Sorted Subarrays
* Search Space Reduction
* Time Complexity
* Space Complexity
* Recursive Call Stack
