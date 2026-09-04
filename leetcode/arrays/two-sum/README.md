# Two Sum

## Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume that each input has exactly one solution, and you cannot use the same element twice.

### Example

```text
Input:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]
```

Because:

```text
nums[0] + nums[1] = 2 + 7 = 9
```

---

## Approach 1 — Brute Force

The simplest approach is to check every possible pair.

For each element, compare it with every element after it and check whether their sum equals `target`.

### Example

```text
[2, 7, 11, 15]
```

Check:

```text
2 + 7   → 9  ✓
```

So we return `[0, 1]`.

### Complexity

* **Time:** `O(n²)`
* **Space:** `O(1)`

The problem is that we may need to check almost every pair.

---

## Approach 2 — Hash Table

Instead of searching through the remaining elements repeatedly, we can store numbers we have already seen in a hash table.

For each number `x`, calculate:

```text
complement = target - x
```

Then ask:

> Have I already seen this complement?

If yes, we have found the answer.

### Example

```text
nums = [2, 7, 11, 15]
target = 9
```

Start with:

```text
x = 2
complement = 9 - 2 = 7
```

`7` has not been seen, so store:

```text
2 → index 0
```

Next:

```text
x = 7
complement = 9 - 7 = 2
```

`2` is already in the hash table at index `0`.

Therefore:

```text
[0, 1]
```

---

## Why This Is Faster

The brute-force solution repeatedly searches for a matching number.

The hash-table solution allows us to check whether the complement has already appeared in expected `O(1)` time.

So instead of:

```text
O(n²)
```

we can solve the problem in:

```text
O(n)
```

---

## Complexity

| Approach    |            Time |  Space |
| ----------- | --------------: | -----: |
| Brute Force |         `O(n²)` | `O(1)` |
| Hash Table  | `O(n)` expected |        |

The important idea is not simply "use a dictionary."

The key question is:

> **What information can I store while traversing the array so that I don't have to search for it again?**

For every number `x`, the required partner is:

```text
target - x
```

A hash table lets us remember previously seen numbers and find that partner efficiently.

---

## What I Learned

* How to recognize when brute force performs repeated searching.
* How a hash table can reduce search time.
* How to derive the complement instead of searching for a pair directly.
* The trade-off between time and space.
* How an `O(n²)` solution can be improved to expected `O(n)`.

---

## Related Concepts

* Arrays
* Hash Tables
* Dictionaries
* Time Complexity
* Space Complexity
* Brute Force → Optimization
