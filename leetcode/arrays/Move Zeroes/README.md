# Move Zeroes

## Problem

Given an integer array `nums`, move all `0`s to the end of the array while maintaining the relative order of the non-zero elements.

The modification must be done **in-place**, meaning we should modify the original array instead of creating another array.

### Example 1

```text
Input:  [0,1,0,3,12]
Output: [1,3,12,0,0]
```

### Example 2

```text
Input:  [0]
Output: [0]
```

---

## Approach — Two Pointers

I used two pointers, `slow` and `fast`, together with a `count` variable.

### Step 1 — Use `fast` to scan the array

```python
for fast in range(len(nums)):
```

`fast` visits every element in the array.

Its job is to **find the non-zero elements**.

---

### Step 2 — Use `slow` to place non-zero elements

```python
slow = 0
```

`slow` represents the position where the next non-zero number should be placed.

Whenever `nums[fast]` is not zero:

```python
nums[slow] = nums[fast]
slow += 1
```

So the non-zero values are moved toward the beginning of the array while keeping their original order.

For example:

```text
[0, 1, 0, 3, 12]

fast finds 1 → put it at index 0
[1, 1, 0, 3, 12]

fast finds 3 → put it at index 1
[1, 3, 0, 3, 12]

fast finds 12 → put it at index 2
[1, 3, 12, 3, 12]
```

At this point, all non-zero elements are in their correct positions.

---

### Step 3 — Count the zeros

Whenever `fast` finds a zero:

```python
count += 1
```

For:

```text
[0, 1, 0, 3, 12]
```

there are `2` zeros.

So:

```text
count = 2
```

---

### Step 4 — Put the zeros at the end

After all non-zero elements have been placed:

```python
i = len(nums) - count
```

For the example:

```text
len(nums) = 5
count = 2

i = 5 - 2
i = 3
```

So we start putting zeros at index `3`:

```text
[1, 3, 12, 0, 0]
```

The loop:

```python
while count > 0:
    nums[i] = 0
    i += 1
    count -= 1
```

fills the remaining positions with zeros.

---

## Why Does This Work?

The important idea is that we separate the problem into two parts:

```text
1. Move all non-zero elements to the front.
2. Fill the remaining positions with zeros.
```

The `slow` pointer tells us exactly where the next non-zero element belongs.

The `fast` pointer searches for those non-zero elements.

The `count` variable tells us how many zeros need to be placed at the end.

---

## Complexity

### Time Complexity

```text
O(n)
```

We scan the array once with `fast` and then scan the zeros again.

Together this is still:

```text
O(n)
```

### Space Complexity

```text
O(1)
```

We only use a few variables (`slow`, `fast`, `count`, and `i`).

We do not create another array.

---

## Comparison

| Approach     | Time | Space | In-place |
| ------------ | ---: | ----: | -------- |
| Extra Array  | O(n) |  O(n) | ❌        |
| Two Pointers | O(n) |  O(1) | ✅        |

The two-pointer approach is better because it satisfies the **in-place** requirement without using extra array space.

---

## Key Insight

The main insight is:

> We don't need to physically move every zero.

Instead, we can first **overwrite the beginning of the array with all non-zero values**, preserving their order.

Then we know that everything after `slow` must become zero.

This turns the problem into:

```text
Find non-zero elements → place them at the front → fill the rest with zeros
```

This is a useful example of the **two-pointer technique** and **in-place array manipulation**.

---

## What I Learned

* How two pointers can process an array in-place.
* `fast` can be used to scan/search through an array.
* `slow` can represent the position where the next valid element should go.
* We can preserve the relative order of non-zero elements.
* We can solve the problem with `O(1)` extra space.
* Sometimes we can solve an array problem by overwriting elements instead of explicitly swapping them.
* The problem demonstrates the **time-space tradeoff**: an extra array would use `O(n)` space, while the two-pointer solution uses `O(1)`.

---

## Related Concepts

* Arrays
* Two Pointers
* In-Place Algorithms
* Array Traversal
* Stable Ordering
* Time Complexity
* Space Complexity
* Overwriting Elements
* Time-Space Tradeoff
