# Lecture 3 — Sorted Arrays & Sorting

## 1. Set vs Sequence

A **Sequence** and a **Set** can both store multiple items, but they organize those items differently.

### Sequence

A Sequence is organized by **rank/position**. 

```text
[A, B, C, D]
 0  1  2  3
```

The position tells us where an item is.

For example:

```text
get_at(2) → C
```

The order is determined by **where we put the item**.

### Set

A Set is organized by the **key of each item**.

```text
key:  10 → 20 → 30 → 40
```

The key determines the ordering.

For example:

```text
find(30) → item with key 30
```

### The main difference

```text
Sequence:
"What is at position 2?"

Set:
"What item has key 30?"
```

This distinction connects Lecture 3 to Lecture 2:

* Lecture 2 → different ways to implement a **Sequence**
* Lecture 3 → implementing a **Set** using a sorted array

---

# 2. Sorted Array Set

## Intuition

Keep items sorted by key → use **binary search** instead of scanning the entire array.

For example:

```text
[1, 3, 5, 8, 9]
```

Because the array is sorted, we can eliminate half of the possible positions after each comparison.

---

## How It Works

### `find(k)`

Use binary search to find the position of key `k`.

For example:

```text
A = [1, 3, 5, 8, 9]

find(8)
```

Binary search repeatedly narrows the search range until it finds `8`.

**Time:** O(log n)

---

### `find_next(k)`

Find the smallest key greater than `k`.

Example:

```text
A = [1, 3, 5, 8, 9]

find_next(6) → 8
```

Binary search finds where `6` would belong, then we look at the appropriate position.

**Time:** O(log n)

---

### `find_prev(k)`

Find the largest key smaller than `k`.

Example:

```text
A = [1, 3, 5, 8, 9]

find_prev(6) → 5
```

**Time:** O(log n)

---

### `find_min()`

Because the array is sorted, the smallest item is at index `0`.

```text
[1, 3, 5, 8, 9]
 ↑
 min
```

**Time:** O(1)

---

### `find_max()`

The largest item is at the last index.

```text
[1, 3, 5, 8, 9]
             ↑
            max
```

**Time:** O(1)

---

## Insert

To insert an item:

1. Use binary search to find where it belongs.
2. Shift elements to make room.
3. Insert the new item.

Example:

```text
Before:

[1, 3, 5, 8, 9]

Insert 6:

[1, 3, 5, 6, 8, 9]
```

Binary search is fast:

```text
O(log n)
```

But shifting the array can require moving many elements:

```text
O(n)
```

Therefore:

**Insert = O(n)**

---

## Delete

To delete an item:

1. Use binary search to find it.
2. Remove it.
3. Shift the elements after it to close the gap.

Therefore:

**Delete = O(n)**

The binary search is O(log n), but the shifting can take O(n).

---

## Sorted Array Set Complexity

| Operation   |       Time |
| ----------- | ---------: |
| `build`     | O(n log n) |
| `find`      |   O(log n) |
| `insert`    |       O(n) |
| `delete`    |       O(n) |
| `find_min`  |       O(1) |
| `find_max`  |       O(1) |
| `find_prev` |   O(log n) |
| `find_next` |   O(log n) |

### Main Trade-off

```text
Sorted array
     ↓
Fast lookup: O(log n)
     ↓
Expensive insertion/deletion: O(n)
```

The sorted order gives us fast searching, but maintaining that order makes modifications expensive.

---

# 3. Binary Search

## Main Idea

Because the array is sorted, every comparison allows us to eliminate approximately half of the remaining elements.

Suppose:

```text
[1, 3, 5, 8, 9, 12, 15]
```

We want to find `12`.

Instead of checking:

```text
1 → 3 → 5 → 8 → 9 → 12
```

we check the middle first.

```text
        8
       / \
    1,3,5  9,12,15
```

Since `12 > 8`, we can completely ignore the left half.

The search becomes:

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

**Binary Search = O(log n)**

---

## Recursive Binary Search

A recursive binary search can be expressed as:

```text
if search range is empty:
    return insertion position

find middle

if target < middle:
    search left half

if target > middle:
    search right half

otherwise:
    target found
```

The important idea is not the recursion itself.

The important idea is:

> Each step eliminates half of the remaining search space.

---

# 4. Selection Sort

## Idea

Repeatedly find the maximum element in the unsorted portion and move it to the end.

```text
for i from n-1 down to 1:
    find maximum in A[0:i+1]
    swap it with A[i]
```

Example:

```text
[4, 2, 7, 1]

Find max → 7
Swap with last position:

[4, 2, 1, 7]

Find max of [4, 2, 1] → 4

[1, 2, 4, 7]
```

The sorted portion grows from the **right side**.

---

## Complexity

The algorithm always scans the unsorted portion to find its maximum.

Therefore:

**Comparisons: Θ(n²)**

The number of swaps is much smaller:

**Swaps: O(n)**

because there is at most one swap per outer-loop iteration.

### Properties

* **In-place:** Yes
* **Stable:** No, by the standard swapping implementation
* **Time:** Θ(n²)

---

# 5. Insertion Sort

## Idea

Build a sorted prefix one element at a time.

Think of sorting playing cards in your hand.

You already have:

```text
[1, 3, 5]
```

and pick up:

```text
2
```

You move `2` left until it reaches its correct position:

```text
[1, 2, 3, 5]
```

The algorithm grows the sorted portion from the **left side**.

```text
for i from 1 to n-1:
    move A[i] left while it is smaller than its neighbor
```

---

## Example

```text
[5, 2, 4, 1]
```

Start with:

```text
[5] | [2, 4, 1]
```

Insert `2`:

```text
[2, 5] | [4, 1]
```

Insert `4`:

```text
[2, 4, 5] | [1]
```

Insert `1`:

```text
[1, 2, 4, 5]
```

---

## Complexity

### Best case

If the array is already sorted:

```text
[1, 2, 3, 4, 5]
```

Very little work is required.

**Best case: Θ(n)**

### Worst case

If the array is in reverse order:

```text
[5, 4, 3, 2, 1]
```

many elements must be moved.

**Worst case: Θ(n²)**

### Properties

* **In-place:** Yes
* **Stable:** Yes
* **Best:** Θ(n)
* **Average:** Θ(n²)
* **Worst:** Θ(n²)

---

# 6. Selection Sort vs Insertion Sort

The main difference is what each algorithm considers its sorted portion.

### Selection Sort

Grows the sorted portion of the **largest elements**:

```text
[unsorted | sorted]
             ↑
        grows this way
```

It repeatedly selects the maximum.

### Insertion Sort

Grows a sorted **prefix**:

```text
[sorted | unsorted]
   ↑
grows this way
```

It repeatedly inserts the next element into the correct position.

### Mental Models

```text
Selection Sort:
"Find the biggest remaining item and put it at the end."

Insertion Sort:
"Take the next item and insert it into the sorted part."
```

---

# 7. Merge Sort

## Idea

Merge Sort uses **divide and conquer**.

The basic strategy is:

```text
Divide
   ↓
Solve smaller problems
   ↓
Merge the results
```

First, divide the array into two halves.

Then recursively sort each half.

Finally, merge the two sorted halves.

---

## Example

```text
[8, 3, 5, 4]
```

Divide:

```text
[8, 3]    [5, 4]
```

Divide again:

```text
[8] [3]    [5] [4]
```

Sort the small pieces:

```text
[3, 8]    [4, 5]
```

Merge:

```text
[3, 4, 5, 8]
```

---

## The Merge Step

If we have:

```text
[2, 6, 9]
[1, 4, 8]
```

compare the first elements:

```text
2 vs 1 → take 1
2 vs 4 → take 2
6 vs 4 → take 4
6 vs 8 → take 6
9 vs 8 → take 8
```

Result:

```text
[1, 2, 4, 6, 8, 9]
```

The merge takes **O(n)** time because each element is processed once.

---

## Recurrence

Merge Sort produces two subproblems of size `n/2` and performs O(n) work to merge them.

Therefore:

```text
T(n) = 2T(n/2) + Θ(n)
```

Using the Master Theorem:

```text
T(n) = Θ(n log n)
```

---

## Properties

* **Time:** Θ(n log n)
* **Extra space:** O(n)
* **In-place:** No, in the standard implementation
* **Stable:** Yes, if the merge chooses the left element when keys are equal

Merge Sort is asymptotically faster than quadratic sorting algorithms for large inputs because:

```text
log n << n
```

---

# 8. Sorting Comparison

| Algorithm      |       Best |    Average |      Worst | Extra Space | Stable |
| -------------- | ---------: | ---------: | ---------: | ----------: | ------ |
| Selection Sort |      Θ(n²) |      Θ(n²) |      Θ(n²) |        O(1) | No     |
| Insertion Sort |       Θ(n) |      Θ(n²) |      Θ(n²) |        O(1) | Yes    |
| Merge Sort     | Θ(n log n) | Θ(n log n) | Θ(n log n) |        O(n) | Yes*   |

* Merge Sort is stable when the merge operation preserves the relative order of equal elements.

---

# 9. In-Place vs Stable

## In-Place

An algorithm is **in-place** when it uses only a small amount of additional memory while modifying the original data structure.

For example:

```text
Selection Sort → O(1) extra space
Insertion Sort → O(1) extra space
```

Merge Sort normally needs additional space for merging:

```text
Merge Sort → O(n) extra space
```

---

## Stable

A sorting algorithm is **stable** if equal-key elements maintain their original relative order.

Imagine:

```text
(John, 20)
(Alice, 20)
```

If the original order is:

```text
John → Alice
```

a stable sort keeps:

```text
John → Alice
```

even though they have the same key.

Insertion Sort is stable.

Selection Sort is not stable by default.

Merge Sort can be stable depending on how ties are handled during merging.

---

# 10. Master Theorem

For recurrences of the form:

```text
T(n) = aT(n/b) + Θ(n^c)
```

compare:

```text
c
```

with:

```text
log_b(a)
```

| Case | Condition    | Result        | Intuition       |
| ---- | ------------ | ------------- | --------------- |
| 1    | c < log_b(a) | Θ(n^log_b(a)) | Leaves dominate |
| 2    | c = log_b(a) | Θ(n^c log n)  | Balanced        |
| 3    | c > log_b(a) | Θ(n^c)        | Root dominates  |

The general Master Theorem also handles more general `f(n)` terms.

---

# 11. Recurrence Patterns

### Linear chain

```text
T(n) = T(n-1) + O(1)
```

Result:

```text
O(n)
```

Think:

```text
n → n-1 → n-2 → ...
```

---

### Linear chain with growing work

```text
T(n) = T(n-1) + O(n)
```

Result:

```text
O(n²)
```

because:

```text
1 + 2 + 3 + ... + n = O(n²)
```

---

### Two recursive branches

```text
T(n) = 2T(n-1) + O(1)
```

Result:

```text
O(2^n)
```

Think of a binary tree whose depth is `n`.

---

### Binary search

```text
T(n) = T(n/2) + O(1)
```

Result:

```text
O(log n)
```

Each step cuts the problem in half.

---

### Merge Sort

```text
T(n) = 2T(n/2) + O(n)
```

Result:

```text
O(n log n)
```

Two half-sized problems plus linear merge work.

---

### Two half-sized problems with n log n work

```text
T(n) = 2T(n/2) + O(n log n)
```

Result:

```text
O(n log² n)
```

The standard polynomial-form Master Theorem does not directly apply because the non-recursive work is `n log n`.

---

### Four half-sized problems

```text
T(n) = 4T(n/2) + O(n)
```

Result:

```text
O(n²)
```

because:

```text
log₂(4) = 2
```

---

# 12. Common Mistakes

### Mistake 1 — Thinking binary search makes insertion O(log n)

Binary search only finds the position quickly.

The array may still need to shift many elements.

Therefore:

```text
find position → O(log n)
shift elements → O(n)

insert → O(n)
```

---

### Mistake 2 — Confusing Set and Sequence

A Sequence is organized by **rank**.

A Set is organized by **key**.

```text
Sequence → "where is it?"
Set      → "what is its key?"
```

---

### Mistake 3 — Forgetting Insertion Sort's best case

Insertion Sort is not always O(n²).

Already sorted:

```text
[1, 2, 3, 4, 5]
```

requires only one pass.

Best case:

```text
Θ(n)
```

---

### Mistake 4 — Assuming Selection Sort is stable

The standard swapping version of Selection Sort is not stable.

Swapping a distant element can change the relative order of equal-key elements.

---

### Mistake 5 — Assuming Merge Sort is in-place

Standard Merge Sort requires additional memory during merging.

Therefore:

```text
Merge Sort → O(n) extra space
```

---

# 13. Lecture 3 Mental Map

The main ideas of the lecture connect together like this:

```text
                    LECTURE 3
                        │
            ┌───────────┴───────────┐
            │                       │
           SET                   SORTING
            │                       │
     Sorted Array Set       ┌───────┼────────┐
            │               │       │        │
     Binary Search      Selection  Insertion Merge
            │            Sort       Sort     Sort
            │               │       │        │
          O(log n)         O(n²)   O(n²)   O(n log n)
            │
     Fast search
            │
     But O(n) insertion/
        deletion
```

## Core Takeaways

1. **Sorted data gives us information.**

   * This is why binary search can achieve O(log n).

2. **Fast searching and fast modification are different goals.**

   * A sorted array searches quickly but requires shifting for insertion/deletion.

3. **Different sorting algorithms make different tradeoffs.**

   * Selection Sort → few swaps, but Θ(n²) comparisons.
   * Insertion Sort → excellent for nearly/already sorted data.
   * Merge Sort → Θ(n log n), but requires extra memory.

4. **Recurrences describe recursive algorithms.**

   * Binary Search → O(log n)
   * Merge Sort → O(n log n)

5. **Always ask what the algorithm is trading.**

   * Time?
   * Space?
   * Stability?
   * Number of modifications?
   * Ability to work in-place?
