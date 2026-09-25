# Find Minimum in Rotated Sorted Array

## Problem

Suppose an array was originally sorted in ascending order, but then it was rotated at some unknown position.

Given the rotated array `nums`, find and return its minimum element.

The array contains **unique values**.

### Example 1

```text
Input:  nums = [3,4,5,1,2]
Output: 1
```

The original sorted array was:

```text
[1,2,3,4,5]
```

It was rotated:

```text
[3,4,5,1,2]
```

So the minimum is:

```text
1
```

### Example 2

```text
Input:  nums = [4,5,6,7,0,1,2]
Output: 0
```

The minimum is:

```text
0
```

### Example 3

```text
Input:  nums = [11,13,15,17]
Output: 11
```

The array was not rotated, so the first element is the minimum.

---

## Approach — Recursive Binary Search

The array is a **rotated sorted array**, so we can use Binary Search instead of scanning every element.

The key is to compare:

```python
nums[mid]
```

with:

```python
nums[right]
```

This tells us which side contains the minimum.

The helper function searches between:

```text
left ... right
```

---

## Step 1 — Check if One Element Remains

```python
if left == right:
    return nums[left]
```

When `left` and `right` are equal, there is only one element left.

That element must be the minimum.

For example:

```text
[3, 4, 1, 2]

       ↑
   left = right
```

So we return:

```text
1
```

---

## Step 2 — Find the Middle

```python
mid = (left + right) // 2
```

The middle divides the current search range.

For example:

```text
[4,5,6,7,0,1,2]
       ↑
      mid
```

Now we compare `nums[mid]` with `nums[right]`.

---

## Step 3 — If `nums[mid] > nums[right]`

```python
if nums[mid] > nums[right]:
    return binary_search(mid + 1, right)
```

Consider:

```text
[4,5,6,7,0,1,2]
       ↑       ↑
      mid    right
       7       2
```

We have:

```text
nums[mid] > nums[right]
7 > 2
```

This tells us that the rotation point—and therefore the minimum—must be **to the right of `mid`**.

Why?

The left side is still part of the original increasing sequence:

```text
[4,5,6,7]
```

The smaller values appear after the rotation:

```text
[0,1,2]
```

So we discard the left half:

```text
[4,5,6,7 | 0,1,2]
            ↑
        search here
```

and search:

```python
binary_search(mid + 1, right)
```

---

## Step 4 — Otherwise, Search the Left Half

```python
else:
    return binary_search(left, mid)
```

Consider:

```text
[3,4,5,1,2]
     ↑     ↑
    mid   right
     5     2
```

Here:

```text
5 > 2
```

so we would search right.

But consider:

```text
[5,1,2,3,4]
     ↑     ↑
    mid   right
     2     4
```

Now:

```text
nums[mid] < nums[right]
2 < 4
```

The section from `mid` to `right` is already sorted:

```text
[2,3,4]
```

Therefore, the minimum could be `nums[mid]` itself or somewhere to its left.

So we keep `mid`:

```text
[left ... mid]
```

and search:

```python
binary_search(left, mid)
```

Notice that we use:

```text
mid
```

rather than:

```text
mid - 1
```

because `nums[mid]` could itself be the minimum.

---

## Why Does This Work?

The key idea is that a rotated sorted array consists of two increasing sections.

For example:

```text
[4,5,6,7,0,1,2]
 ↑---------↑ ↑---↑
 first part  second part
```

The minimum is exactly where the rotation occurs:

```text
[4,5,6,7, 0,1,2]
          ↑
       minimum
```

By comparing `nums[mid]` with `nums[right]`, we can determine which side contains that rotation point.

### Case 1 — `nums[mid] > nums[right]`

```text
nums[mid] > nums[right]
```

The rotation point must be to the **right**.

```text
[left ... mid | ... right]
              ↑
       minimum is here →
```

So:

```text
left = mid + 1
```

### Case 2 — `nums[mid] < nums[right]`

```text
nums[mid] < nums[right]
```

The right side is sorted.

The minimum is either:

* at `mid`, or
* somewhere to the left.

So:

```text
right = mid
```

We keep `mid` because it could be the answer.

---

## Example Walkthrough

Consider:

```text
nums = [4,5,6,7,0,1,2]
```

Start:

```text
left = 0
right = 6
```

Calculate:

```text
mid = 3
```

Compare:

```text
nums[3] = 7
nums[6] = 2
```

Since:

```text
7 > 2
```

search the right half:

```text
[0,1,2]
 ↑
 minimum
```

Now:

```text
left = 4
right = 6
mid = 5
```

Compare:

```text
nums[5] = 1
nums[6] = 2
```

Since:

```text
1 < 2
```

the minimum is at `mid` or to its left.

Search:

```text
left = 4
right = 5
```

Now:

```text
mid = 4
```

Compare:

```text
nums[4] = 0
nums[5] = 1
```

Again:

```text
0 < 1
```

So:

```text
right = mid
```

Now:

```text
left = 4
right = 4
```

Since:

```python
left == right
```

return:

```text
nums[4] = 0
```

---

## Complexity

### Time Complexity

Each recursive call eliminates approximately half of the search space.

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

### Space Complexity

The solution uses recursion.

The maximum recursion depth is `O(log n)`.

Therefore:

```text
O(log n)
```

An iterative version could reduce the auxiliary space to `O(1)`.

---

## Comparison

| Approach                |     Time |    Space | Main Idea                   |
| ----------------------- | -------: | -------: | --------------------------- |
| Linear Search           |     O(n) |     O(1) | Check every element         |
| Recursive Binary Search | O(log n) | O(log n) | Compare `mid` with `right`  |
| Iterative Binary Search | O(log n) |     O(1) | Same idea without recursion |

The solution in `solution.py` uses **recursive Binary Search**.

---

## Key Insight

The main insight is:

> **We don't need to find the minimum directly. We only need to determine which half contains the rotation point.**

The comparison:

```text
nums[mid] > nums[right]
```

means:

```text
minimum → right
```

while:

```text
nums[mid] < nums[right]
```

means:

```text
minimum → left or mid
```

The important detail is that in the second case we keep `mid` because it may itself be the minimum.

---

## What I Learned

* How a sorted array changes when it is rotated.
* How the minimum corresponds to the rotation point.
* How to use Binary Search on a problem without directly searching for a target value.
* Why comparing `nums[mid]` with `nums[right]` reveals which half contains the minimum.
* Why the right boundary becomes `mid`, not `mid - 1`, when the right side is sorted.
* How recursive Binary Search reduces the search space to `O(log n)`.
* How an iterative implementation could reduce recursive stack space to `O(1)`.

---

## Related Concepts

* Arrays
* Binary Search
* Rotated Sorted Arrays
* Recursion
* Divide and Conquer
* Search Space Reduction
* Sorted Data
* Rotation Point
* Time Complexity
* Space Complexity
* Recursive Call Stack
