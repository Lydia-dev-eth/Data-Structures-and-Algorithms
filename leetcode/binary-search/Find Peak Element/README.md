# Find Peak Element

## Problem

Given an array `nums`, find a **peak element** and return its index.

A peak element is an element that is **strictly greater than its neighbors**.

For the boundary elements, we imagine that the elements outside the array are `-∞`.

The problem guarantees that if there are multiple peaks, returning the index of **any** peak is valid.

### Example 1

```text
Input:  nums = [1,2,3,1]
Output: 2
```

`nums[2] = 3` is greater than both of its neighbors:

```text
1 < 3 > 1
```

So index `2` is a peak.

### Example 2

```text
Input:  nums = [1,2,1,3,5,6,4]
Output: 5
```

`nums[5] = 6` is a peak:

```text
3 < 6 > 4
```

Index `2` is also a peak because:

```text
2 > 1 < 3
```

So either `2` or `5` would be accepted.

---

## Approach — Recursive Binary Search

Instead of checking every element, I use **Binary Search** to eliminate half of the array at every step.

The important idea is to compare:

```python
nums[mid]
nums[mid + 1]
```

Then determine which direction contains a peak.

The helper function is:

```text
binary_search(nums, left, right)
```

where:

* `left` is the beginning of the current search range.
* `right` is the end of the current search range.

---

## Step 1 — Check if One Element Remains

```python
if left == right:
    return right
```

When `left` and `right` become equal, there is only one element left.

That element must be a peak.

For example:

```text
left
 ↓
[ 1, 2, 5, 3, 2 ]
       ↑
      right
```

If:

```text
left == right == 2
```

then we return:

```text
2
```

---

## Step 2 — Find the Middle

```python
mid = (left + right) // 2
```

We divide the current search range into two parts.

For example:

```text
[1, 2, 3, 4, 2, 1]
       ↑
      mid
```

We then compare:

```python
nums[mid]
```

with:

```python
nums[mid + 1]
```

---

## Step 3 — If We Are Going Downhill

```python
if nums[mid] > nums[mid + 1]:
    return binary_search(nums, left, mid)
```

Suppose we have:

```text
[1, 2, 5, 4, 3]
       ↑  ↑
      mid mid+1
```

Here:

```text
5 > 4
```

We are going **downhill**.

```text
        5
       / \
      ↑   ↓
   going downhill
```

This tells us that there must be a peak at `mid` or somewhere to its left.

So we keep:

```text
[left ... mid]
```

and discard everything to the right of `mid`.

---

## Step 4 — If We Are Going Uphill

Otherwise:

```python
return binary_search(nums, mid + 1, right)
```

Suppose:

```text
[1, 2, 3, 5, 7]
          ↑  ↑
         mid mid+1
```

Here:

```text
5 < 7
```

We are going **uphill**.

Since we are moving upward toward the right, there must eventually be a peak on the right side.

So we discard the left side and search:

```text
[mid + 1 ... right]
```

---

## Why Does This Work?

The key insight is:

> **When we compare `nums[mid]` with `nums[mid + 1]`, the direction tells us which half must contain a peak.**

There are only two possibilities.

### Going Downhill

```text
nums[mid] > nums[mid + 1]

       /\
      /  \
     /    \
    ↑      ↓
```

A peak exists on the **left side or at `mid`**.

So:

```text
search left half
```

### Going Uphill

```text
nums[mid] < nums[mid + 1]

       /
      /
     /
    ↑
```

A peak must exist on the **right side**.

So:

```text
search right half
```

We never need to know exactly where the peak is before searching.

We only need to know **which direction guarantees that a peak exists**.

---

## Example Walkthrough

Consider:

```text
nums = [1, 2, 3, 1]
```

Start:

```text
left = 0
right = 3
```

Calculate:

```text
mid = (0 + 3) // 2
mid = 1
```

Compare:

```text
nums[1] = 2
nums[2] = 3
```

Since:

```text
2 < 3
```

we are going uphill.

Therefore, search the right half:

```text
[3, 1]
 ↑
```

Now:

```text
left = 2
right = 3
mid = 2
```

Compare:

```text
nums[2] = 3
nums[3] = 1
```

Since:

```text
3 > 1
```

we are going downhill.

Therefore, search:

```text
left = 2
right = 2
```

Now:

```python
left == right
```

So we return:

```text
2
```

And:

```text
nums[2] = 3
```

is indeed a peak.

---

## Complexity

### Time Complexity

At every step, we eliminate approximately half of the remaining array.

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

The recursive call stack can contain approximately `log n` calls.

Therefore:

```text
O(log n)
```

An iterative version could reduce the auxiliary space to `O(1)`.

---

## Comparison

| Approach                |     Time |    Space | Idea                               |
| ----------------------- | -------: | -------: | ---------------------------------- |
| Linear Search           |     O(n) |     O(1) | Check elements one by one          |
| Recursive Binary Search | O(log n) | O(log n) | Follow the direction toward a peak |
| Iterative Binary Search | O(log n) |     O(1) | Same idea without recursion        |

The recursive solution is the approach used in `solution.py`.

---

## Key Insight

The main insight is:

> **We don't need to find the peak directly. We only need to determine which direction guarantees that a peak exists.**

Think of the array like a mountain trail:

```text
          peak
           /\
          /  \
         /    \
        /      \
_______/        \______
```

If you are walking **uphill**, keep going right.

If you are walking **downhill**, a peak is behind you or at your current position, so keep the left side.

Binary Search lets us repeatedly make this decision while cutting the search space in half.

---

## What I Learned

* How Binary Search can be used even when the problem is not explicitly a search for a target value.
* How comparing adjacent elements can reveal the direction toward a peak.
* Why an uphill slope guarantees a peak exists somewhere to the right.
* Why a downhill slope guarantees a peak exists at `mid` or somewhere to the left.
* How recursion can represent the repeated binary-search process.
* How to reduce a linear `O(n)` search to `O(log n)`.

---

## Related Concepts

* Arrays
* Binary Search
* Recursion
* Divide and Conquer
* Peak Finding
* Search Space Reduction
* Time Complexity
* Space Complexity
* Recursive Call Stack
* Greedy Direction Choice
