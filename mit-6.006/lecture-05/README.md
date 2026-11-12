# Lecture 5 — Linear-Time Sorting

This folder contains notes and implementations from MIT 6.006 Lecture 5 / Recitation 5, focusing on why comparison sorting needs Ω(n log n), and how to sort in linear time without comparisons.

## What This Covers

- **Comparison Sorting Lower Bound** — why any comparison sort needs Ω(n log n).
- **Direct Access Array Sort** — sorting by using keys as indices.
- **Counting Sort** — handling duplicate keys, stably.
- **Tuple Sort** — sorting by several keys with a stable subroutine.
- **Radix Sort** — sorting large integers digit by digit in linear time.
- **Exercises** — base-10 radix sort, negative integers, strings.

## Files

| File | What it contains |
|---|---|
| `lec6_note.md` | Full notes, intuition, proofs, complexity, common mistakes |
| `direct_access_sort.py` | Direct Access Array Sort |
| `counting_sort.py` | Counting Sort (cumulative sums and chains versions) |
| `tuple_sort.py` | Tuple Sort |
| `radix_sort.py` | Radix Sort, plus negative integers and strings |
| `README.md` | Overview of this folder |

## Key Ideas

### 1. Comparison Sorting Lower Bound

A comparison sort is a **binary decision tree**.

```
possible outputs = n!   (every permutation of the items)
leaves needed   ≥ n!
tree height     ≥ lg(n!) = Ω(n log n)
```

Why Ω(n log n)? n! > (n/2)^(n/2), so lg(n!) > (n/2) lg(n/2).

So merge sort is **optimal** among comparison sorts.

**To go faster we must stop using only comparisons.**

### 2. Direct Access Array Sort

Put the item with key k at index k, then read the array left to right.

```
Time  → Θ(n + u)
Space → O(u)
```

Two drawbacks:

- Cannot handle **duplicate keys**.
- Cannot handle **large key ranges** (u too big).

### 3. Counting Sort

Fixes duplicates: count how many items have each key, then use cumulative sums to find each item's final position.

```
Time  → Θ(n + u)
Stable → Yes (walk the input backwards)
```

Linear when u = O(n).

### 4. Tuple Sort

Sort by several keys with a **stable** sort: least important key first, most important key last.

Like sorting a spreadsheet by several columns.

### 5. Radix Sort

Write each key in base n with c digits, then tuple-sort the digits with counting sort.

```
c = ceil(log_n u)
Time → Θ(n · c)
```

If u ≤ n^c with c constant → **linear time**.

## Complexity at a Glance

| Algorithm | Time | Stable | Notes |
|---|---|---|---|
| Merge Sort | Θ(n log n) | Yes* | Comparison model, optimal |
| Direct Access Array Sort | Θ(n + u) | n/a | Distinct keys only |
| Counting Sort | Θ(n + u) | Yes | Linear when u = O(n) |
| Tuple Sort | d · (stable sort) | Yes | Needs a stable subroutine |
| Radix Sort | Θ(n · c) | Yes | Linear when u ≤ n^c, c constant |

## Key Takeaway

> Comparisons can never beat Ω(n log n) for sorting. Using keys as array indices (direct access) removes that limit — and radix sort extends it from small key ranges to any polynomial range.

Linear-time sorting works only for **integer keys in a bounded range**. For general comparable objects, merge sort is optimal.

See `notes.md` for the detailed concepts and the Python files for implementations.
