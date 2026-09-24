# Lecture 3 — Sorted Arrays & Sorting

This folder contains notes and implementations from **MIT 6.006 Lecture 3**, focusing on Sets, sorted arrays, binary search, and fundamental sorting algorithms.

## What This Covers

* **Set vs Sequence** — how Sets are organized by keys while Sequences are organized by rank.
* **Sorted Array Set** — implementing a Set using a sorted array.
* **Binary Search** — using sorted data to search in `O(log n)` time.
* **Selection Sort** — repeatedly selecting the maximum element.
* **Insertion Sort** — building a sorted prefix one element at a time.
* **Merge Sort** — divide-and-conquer sorting in `O(n log n)`.
* **Recurrences & Master Theorem** — analyzing recursive algorithms.
* **Algorithm trade-offs** — time, space, stability, and in-place operations.

## Files

| File                  | What it contains                                                                             |
| --------------------- | -------------------------------------------------------------------------------------------- |
| `notes.md`            | Full lecture notes, intuition, complexity analysis, recurrence patterns, and common mistakes |
| `sorted_array_set.py` | Sorted Array Set implementation using an underlying `Array_Seq` and binary search            |
| `selection_sort.py`   | Selection Sort implementation                                                                |
| `insertion_sort.py`   | Insertion Sort implementation                                                                |
| `merge_sort.py`       | Merge Sort implementation                                                                    |
| `README.md`           | Overview of this lecture folder                                                              |

## Key Ideas

### Sorted Array Set

A sorted array allows efficient searching because its ordering lets us use binary search.

```text
find       → O(log n)
find_min   → O(1)
find_max   → O(1)
insert     → O(n)
delete     → O(n)
```

The important trade-off is:

> **Fast search, but expensive modification.**

### Sorting

The lecture compares three fundamental sorting algorithms:

```text
Selection Sort → Θ(n²)
Insertion Sort → Θ(n²) worst case, Θ(n) best case
Merge Sort     → Θ(n log n)
```

Each algorithm makes different trade-offs in terms of comparisons, modifications, memory usage, and stability.

## Complexity at a Glance

| Algorithm / Structure |              Key Complexity |
| --------------------- | --------------------------: |
| Binary Search         |                  `O(log n)` |
| Sorted Array `find`   |                  `O(log n)` |
| Sorted Array `insert` |                      `O(n)` |
| Sorted Array `delete` |                      `O(n)` |
| Selection Sort        |                     `Θ(n²)` |
| Insertion Sort        | `Θ(n)` best / `Θ(n²)` worst |
| Merge Sort            |                `Θ(n log n)` |

## Key Takeaway

Lecture 3 demonstrates an important idea in algorithm design:

> **Improving one operation often means making another operation more expensive.**

A sorted array gives us fast search, but maintaining the sorted order makes insertion and deletion expensive. Sorting algorithms make similar trade-offs between time, space, stability, and the number of modifications.

See [`notes.md`](./notes.md) for the detailed concepts and analysis, and the Python files for the corresponding implementations.
