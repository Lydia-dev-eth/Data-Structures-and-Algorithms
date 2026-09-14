# Search Insert Position

## Problem

Given a sorted array of distinct integers and a target value, return the index if the target is found.

If the target is not found, return the index where it would be inserted in order.

The algorithm must run in **O(log n)** time.

### Example

Input:

```text
nums = [1, 3, 5, 6]
target = 5
```

Output:

```text
2
```

Because `5` is already at index `2`.

Another example:

```text
nums = [1, 3, 5, 6]
target = 2
```

Output:

```text
1
```

Because `2` should be inserted between `1` and `3`.

---

## Approach — Recursive Binary Search

I used binary search because the array is sorted.

Instead of checking every element one by one, I repeatedly divide the search range in half.

I use three important values:

* `left` — beginning of the current search range
* `right` — end of the current search range
* `mid` — middle position of the current range

For example:

```text
nums = [1, 3, 5, 6]
target = 4
```

Initially:

```text
left = 0
right = 3
```

Calculate:

```text
mid = (left + right) // 2
    = (0 + 3) // 2
    = 1
```

So:

```text
nums[mid] = 3
```

Since:

```text
4 > 3
```

the target must be to the right of `mid`.

Therefore:

```text
left = mid + 1
```

The search continues recursively using the smaller range.

### When the target is found

If:

```python
target == nums[mid]
```

I return `mid` because that is the target's index.

### When the target is greater

If:

```python
target > nums[mid]
```

the target must be on the right side.

So I recursively search:

```python
binary_search(nums, mid + 1, right, target)
```

### When the target is smaller

If:

```python
target < nums[mid]
```

the target must be on the left side.

So I recursively search:

```python
binary_search(nums, left, mid - 1, target)
```

### The important part — insertion position

The base case is:

```python
if left > right:
    return left
```

This happens when there are no more positions left to search.

At that point, `left` represents the correct position where the target should be inserted.

For example:

```text
nums = [1, 3, 5, 6]
target = 4
```

Eventually:

```text
left = 2
right = 1
```

Since:

```text
left > right
```

the search ends and we return:

```text
2
```

So `4` would be inserted at index `2`:

```text
[1, 3, 4, 5, 6]
       ↑
    index 2
```

### Complexity

* **Time:** O(log n)
* **Space:** O(log n) because of the recursive call stack

---

## Comparison

This problem can also be solved using linear search, but binary search is the appropriate approach because the problem requires **O(log n)** time.

| Approach                |     Time | Extra Space | Main Idea                                     |
| ----------------------- | -------: | ----------: | --------------------------------------------- |
| Linear Search           |     O(n) |        O(1) | Check elements from left to right             |
| Recursive Binary Search | O(log n) |    O(log n) | Repeatedly eliminate half of the search range |

The recursive binary search satisfies the required time complexity.

---

## Key Insight

The most important observation is that the array is **sorted**.

Because of this, we do not need to search every element.

At every step:

* If `target > nums[mid]`, ignore the left half.
* If `target < nums[mid]`, ignore the right half.
* If they are equal, return `mid`.

The other important insight is that when the search finishes:

```python
left > right
```

`left` is exactly the position where the target belongs.

So the same binary search can handle both cases:

1. **Target exists** → return its index.
2. **Target does not exist** → return its insertion position.

---

## What I Learned

* How binary search works on a sorted array.
* How to implement binary search recursively.
* How `left`, `right`, and `mid` define the current search range.
* How each recursive call eliminates half of the remaining elements.
* Why binary search takes O(log n) time.
* How recursion introduces O(log n) space through the call stack.
* How the final `left` value can represent the insertion position.
* The connection between binary search and the **lower bound** concept.

---

## Related Concepts

* Arrays
* Sorted Arrays
* Binary Search
* Recursion
* Lower Bound
* Divide and Conquer
* Time Complexity
* Space Complexity
