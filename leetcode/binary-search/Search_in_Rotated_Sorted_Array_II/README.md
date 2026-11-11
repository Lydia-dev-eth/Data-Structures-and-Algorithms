# Search in Rotated Sorted Array II

> LeetCode 81 — Binary Search

## Problem

Given an integer array `nums` sorted in non-decreasing order and rotated at an unknown pivot, determine whether a given `target` exists in the array.

The array may contain duplicate values.

Return `True` if the target exists in the array. Otherwise, return `False`.

### Example 1

Input:
```python
nums = [2,5,6,0,0,1,2]
target = 0
```

Output:
```python
True
```

Because `0` exists in the array.

### Example 2

Input:
```python
nums = [2,5,6,0,0,1,2]
target = 3
```

Output:
```python
False
```

Because `3` does not exist in the array.

---

## Approach — Modified Binary Search

Because the array was originally sorted and then rotated, at least one half of the current search range is sorted.

Instead of checking every element, we use binary search to identify the sorted half and determine whether the target belongs there.

However, there is one important complication:

**The array can contain duplicates.**

Sometimes duplicate values make it impossible to determine which half is sorted.

When this happens, we shrink both boundaries and continue searching.

The solution uses a recursive helper function:

```python
binary_search(left, right)
```

where:

- `left` is the beginning of the current search range.
- `right` is the end of the current search range.

## Step 1 — Check if the Search Range Is Empty

```python
if left > right:
    return False
```

If `left` becomes greater than `right`, there are no elements left to search.

This means the target does not exist.

For example:

```python
left = 4
right = 3
```

There is no valid search range:

```text
[ nothing ]
```

So we return:

```python
False
```

## Step 2 — Find the Middle

```python
mid = (right + left) // 2
```

The middle index divides the current search range into two parts.

For example:

```text
[2, 5, 6, 0, 0, 1, 2]
          ↑
         mid
```

We use the middle element to decide which part of the array to search.

## Step 3 — Check the Middle Element

```python
if nums[mid] == target:
    return True
```

If the middle element is the target, we have found it.

For example:

```python
nums[mid] = 0
target = 0
```

So:

```python
return True
```

## Step 4 — Handle Duplicates

This is the important difference between regular Binary Search and Search in Rotated Sorted Array II.

```python
elif nums[left] == nums[mid] == nums[right]:
    return binary_search(left + 1, right - 1)
```

Sometimes the values at the left, middle, and right positions are equal.

For example:

```text
[1, 0, 1, 1, 1]
 ↑     ↑     ↑
left  mid  right
```

Here:

```python
nums[left] == nums[mid] == nums[right]
```

We cannot determine which half is sorted just by looking at these values.

Why?

Because duplicates hide the information we need to identify the sorted half.

Since we already checked that `nums[mid]` is not the target, and both boundary values equal `nums[mid]`, we can safely eliminate both boundaries.

So we shrink the search range:

```python
return binary_search(left + 1, right - 1)
```

For example:

```text
Before:

[1, 0, 1, 1, 1]
 ↑     ↑     ↑
left  mid  right

After:

[0, 1, 1]
 ↑     ↑
left  right
```

This allows us to continue searching.

**Important:** This is why the worst-case time complexity can become `O(n)` instead of `O(log n)`.

## Step 5 — Identify the Sorted Left Half

```python
elif nums[left] <= nums[mid]:
```

If this condition is true, the left half is sorted.

For example:

```text
[1, 3, 5, 7, 0, 0, 1]
 ↑        ↑
left     mid
```

The left portion:

```text
[1, 3, 5, 7]
```

is sorted.

Now we check whether the target belongs to this range.

```python
if nums[left] <= target < nums[mid]:
    return binary_search(left, mid - 1)
```

If the target is between the first and middle elements, search the left half.

Otherwise, search the right half:

```python
else:
    return binary_search(mid + 1, right)
```

Why does this work?

Because the left half is sorted.

If the target does not belong to that half, we can safely eliminate it.

## Step 6 — Identify the Sorted Right Half

If the left half is not sorted, the right half must be sorted:

```python
else:
```

For example:

```text
[6, 7, 0, 1, 2, 3, 4]
 ↑        ↑        ↑
left     mid     right
```

The right portion:

```text
[1, 2, 3, 4]
```

is sorted.

Now we check whether the target belongs to the right half.

```python
if nums[mid] < target <= nums[right]:
    return binary_search(mid + 1, right)
```

If the target is between the middle and right elements, search the right half.

Otherwise, search the left half:

```python
else:
    return binary_search(left, mid - 1)
```

Because the right half is sorted, we can determine whether the target belongs there.

---

## Why Does This Work?

The key property is that the original array was sorted before rotation.

Even after rotation, at least one half of the current search range is sorted, unless duplicates make the sorted half ambiguous.

We handle both situations:

**Case 1 — We can identify the sorted half**

We determine whether the target belongs in that half and eliminate the other half.

**Case 2 — Duplicates make the sorted half ambiguous**

We shrink both boundaries:

```python
left += 1
right -= 1
```

This allows the algorithm to continue without incorrectly discarding a possible target.

The search process looks like:

```text
Current search range
        ↓
Find middle
        ↓
Is middle the target?
   ┌────┴────┐
  Yes        No
   ↓          ↓
 True     Check duplicates
              ↓
       ┌──────┴──────┐
      Yes            No
       ↓              ↓
  Shrink both    Find sorted half
  boundaries          ↓
                  Check target
                  range
                      ↓
               Search one half
                      ↓
                   Repeat
```

## Complexity

### Time Complexity

**Best/typical case: `O(log n)`**

When we can identify the sorted half, approximately half of the search space is eliminated at each step.

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

**Worst case: `O(n)`**

When duplicates make it impossible to identify the sorted half, we may only remove two elements per recursive call.

For example:

```python
nums = [1, 1, 1, 1, 1, 1, 1]
target = 2
```

The algorithm repeatedly shrinks the boundaries:

```text
n
↓
n - 2
↓
n - 4
↓
n - 6
↓
...
```

Therefore, the worst-case time complexity is:

```text
O(n)
```

### Space Complexity

This implementation uses recursion.

Each recursive call remains on the call stack until the search finishes.

When the search range is repeatedly halved:

```text
O(log n)
```

When duplicates force the boundaries to shrink one element from each side:

```text
O(n)
```

Therefore:

```text
Best/typical: O(log n)
Worst case:   O(n)
```

An iterative implementation could use `O(1)` auxiliary space because it does not need a recursive call stack.

## Comparison

| Approach | Time | Space |
|---|---|---|
| Linear Search | `O(n)` | `O(1)` |
| Regular Binary Search | `O(log n)` | `O(log n)` recursive |
| Modified Recursive Binary Search | `O(log n)` typical, `O(n)` worst | `O(log n)` typical, `O(n)` worst |
| Modified Iterative Binary Search | `O(log n)` typical, `O(n)` worst | `O(1)` |

The important difference is that duplicates can prevent binary search from eliminating half of the search space.

## Key Insight

The main insight is:

**Even though the array is rotated, at least one half of the current search range is sorted.**

We use that sorted portion to determine where the target could exist.

But when duplicates make the sorted portion ambiguous, we shrink both boundaries.

The important pattern is:

```text
Find middle
     ↓
Check target
     ↓
Handle duplicates
     ↓
Identify sorted half
     ↓
Determine where target can exist
     ↓
Eliminate part of search space
     ↓
Repeat
```

This problem demonstrates an important variation of Divide and Conquer: binary search with an additional condition for handling duplicate values.

## What I Learned

- How to search in a rotated sorted array.
- How to identify the sorted half of a rotated array.
- How to modify binary search to handle duplicates.
- Why `nums[left] == nums[mid] == nums[right]` creates ambiguity.
- Why shrinking both boundaries handles duplicate ambiguity.
- Why binary search can have `O(n)` worst-case time with duplicates.
- How recursion represents the repeated reduction of the search range.
- The difference between regular and modified binary search.

## Related Concepts

- Arrays
- Binary Search
- Rotated Sorted Arrays
- Recursion
- Divide and Conquer
- Duplicate Elements
- Search Algorithms
- Time Complexity
- Space Complexity
- Recursive Call Stack
