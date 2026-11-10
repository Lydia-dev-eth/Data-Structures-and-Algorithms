# Problem Set 2

> MIT 6.006 — Introduction to Algorithms

## Overview

This problem set focuses on solving recurrences, choosing sorting algorithms for different cost models, binary-search-style algorithm design, database design with linked structures, and divide and conquer.

The problems combine theoretical reasoning with algorithm design and implementation. The programming portion implements `satisfying_booking(R)`, which computes the room-booking schedule for a set of talk requests by merging schedules with divide and conquer.

## Topics

* Solving recurrences (recursion trees, Master Theorem, substitution)
* Comparing sorting algorithms under different operation costs
* Exponential search and binary search
* Database design with linked lists and sorted arrays
* Merging sorted sequences
* Divide and conquer
* Time and space complexity

## Problems

| # | Focus                | Main Concepts                                   | Status |
| - | -------------------- | ----------------------------------------------- | ------ |
| 1 | Solving recurrences  | Recursion trees, Master Theorem, substitution   | ✅      |
| 2 | Sorting sorts        | Selection, insertion, merge sort; cost models   | ✅      |
| 3 | Friend finder        | Exponential search, binary search               | ✅      |
| 4 | MixBookTube.tv chat  | Linked list, sorted array, per-viewer lists     | ✅      |
| 5 | Beaver bookings      | Merging schedules, divide and conquer           | ✅      |

## Problem 1 — Solving Recurrences

Find tight bounds for four recurrences. Parts (a)–(c) are solved with a recursion tree and with the Master Theorem. Part (d) is solved by substitution.

| Recurrence                    | Result                                       |
| ----------------------------- | -------------------------------------------- |
| `T(n) = 4T(n/2) + O(n)`       | `Θ(n²)`                                      |
| `T(n) = 3T(n/√2) + O(n⁴)`     | `O(n⁴)` and `Ω(n^(2 lg 3))`                  |
| `T(n) = 2T(n/2) + 5n log n`   | `Θ(n log² n)`                                |
| `T(n) = T(n − 2) + Θ(n)`      | `Θ(n²)`                                      |

Key ideas:

* Work per level of the recursion tree, and whether it grows, shrinks, or stays balanced
* Which Master Theorem case applies (case 1, case 3, and case 2 with a log factor)
* Proving upper and lower bounds separately in substitution

## Problem 2 — Sorting Sorts

Choose the best sort for each scenario and justify it.

| Scenario                                          | Choice         | Why                                                        |
| ------------------------------------------------- | -------------- | ---------------------------------------------------------- |
| In-place sort, `set_at` costs `Θ(n log n)`        | Selection sort | Only `O(n)` writes, so `O(n² log n)` total                 |
| Comparisons cost `Θ(log n)`                       | Merge sort     | Only `O(n log n)` comparisons, so `O(n log² n)` total      |
| Sorted array with `log log n` adjacent swaps      | Insertion sort | Runs in `O(n + inversions)`, so `O(n)`                     |

The main focus is that the best algorithm depends on which operation is expensive, not only on the number of steps.

## Problem 3 — Friend Finder

Find Datum, who is `k` kilometers from the nearest end of the island, after visiting only `O(log k)` locations.

The solution searches from both ends at once:

```text
probe 2^i and n - 2^i for i = 0, 1, 2, ...
stop when Datum is bracketed, then binary search the bracket
```

### Main concepts

* Exponential (doubling) search
* Binary search on a bracketed range
* Running time that depends on the distance `k`, not on `n`

## Problem 4 — MixBookTube.tv Chat

Design a database for a chat room where banned viewers have all their messages removed.

The solution keeps two structures:

* A doubly linked list `L` of all undeleted messages in sending order
* A sorted array `S` of viewer IDs, each pointing to a list of pointers to that viewer's messages in `L`

### Complexity

| Operation   | Complexity        |
| ----------- | ----------------: |
| `build(V)`  |      `O(n log n)` |
| `send`      |        `O(log n)` |
| `recent(k)` |            `O(k)` |
| `ban(v)`    | `O(n_v + log n)`  |

All bounds are worst-case.

## Problem 5 — Beaver Bookings

Compute the unique booking schedule that satisfies a set of talk requests.

### Parts

* **(a)** Merge two booking schedules in `O(n)` time. Each booking becomes a start event and an end event, the two sorted event lists are merged, and one sweep outputs a booking whenever the room count changes.
* **(b)** Compute the schedule for `n` requests in `O(n log n)` time by splitting the requests in half, solving each half, and merging with part (a).
* **(c)** Implement `satisfying_booking(R)` in Python.

### Complexity

| Part                  | Complexity   |
| --------------------- | -----------: |
| Merge two schedules   |       `O(n)` |
| `satisfying_booking`  | `O(n log n)` |

The recurrence is `T(n) = 2T(n/2) + O(n)`, which is Master Theorem case 2.

## Files

```text
 ps2/
├── ps2-solutions.tex
├── satisfying_booking.py
├── macros-sp20.tex
└── tests.py
```

* `README.md` — overview and notes for this problem set
* `ps2-solutions.tex` — completed written solutions using the MIT LaTeX template
* `satisfying_booking.py` — programming implementation using the MIT Python template
* `tests.py` — provided tests for the programming portion
* `macros-sp20.tex` — provided MIT LaTeX macros used by the template

## Key Takeaways

* Recursion trees show where the work in a recurrence is concentrated, and the Master Theorem confirms it.
* The best sorting algorithm depends on which operation is expensive.
* Searching from both ends with doubling steps gives running time that depends on `k` instead of `n`.
* Extra pointers between structures (like the per-viewer lists) make deletions cost only as much as the items removed.
* Merging two sorted sequences in linear time is the key step that makes divide and conquer work.

## Related Material

### MIT 6.006

* Lectures covering recurrences and the Master Theorem
* Sorting: selection, insertion, and merge sort
* Binary search and sequences

### LeetCode

Related topics for later practice:

* [Binary Search](../../leetcode/binary-search/)
* [Sorting](../../leetcode/sorting/)
* [Intervals](../../leetcode/intervals/)

## Reflection

### What was difficult?

Choosing the right bounds for the recurrence in part 1(b), and handling all the cases when merging two booking schedules.

### What became clearer?

How the cost of individual operations (writes, comparisons, pointer updates) decides which algorithm or data structure is best.

### What would I revisit?

* Master Theorem case 3 conditions
* Substitution proofs for upper and lower bounds
* Edge cases when merging schedules

## Status

* [x] Written solutions completed
* [x] Programming solutions completed
* [x] Complexity analyzed
* [ ] Concepts reviewed

**Status:** 🔄 In Progress
