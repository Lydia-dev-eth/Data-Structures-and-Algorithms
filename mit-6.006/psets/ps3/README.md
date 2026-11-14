# Problem Set 3

> MIT 6.006 — Introduction to Algorithms

## Overview

This problem set focuses on hashing, universal hash families, linear-time sorting (counting sort and radix sort), and using hash tables to speed up search.

The problems combine hand computation, probability arguments, and algorithm design. The programming portion implements `count_anagram_substrings(T, S)`, which counts how many substrings of `T` are anagrams of each string in `S`.

## Topics

* Hash tables and collisions
* Universal hash families
* Counting sort and radix sort
* Comparison-model lower bound
* Hash tables for expected `O(n)` algorithms
* Two-finger (two-pointer) sweep on a sorted array
* Frequency tables and sliding windows

## Problems

| # | Focus                | Main Concepts                                     | Status |
| - | -------------------- | ------------------------------------------------- | ------ |
| 1 | Hash practice        | Chaining, collisions, pigeonhole                  | ✅      |
| 2 | Dorm hashing         | Universal hashing, collision probability          | ✅      |
| 3 | Ice cores            | Radix sort, counting sort, merge sort             | ✅      |
| 4 | Pushing paper        | Hash table lookup, radix sort, two-finger sweep   | ✅      |
| 5 | Anagram archaeology  | Frequency tables, sliding window, hashing         | ✅      |

## Problem 1 — Hash Practice

Insert keys into a table of size 7 with `h(k) = (10k + 4) mod 7`, then find the smallest `c` for which `h(k) = ((10k + 4) mod c) mod 7` has no collisions on the same keys.

| Result                   | Value                                   |
| ------------------------ | --------------------------------------- |
| Slot 0                   | `36 → 92`                               |
| Slot 4                   | `56`                                    |
| Slot 5                   | `47 → 61 → 33`                          |
| Slot 6                   | `52`                                    |
| Smallest `c` with no collisions | `13`                             |

## Problem 2 — Dorm Hashing

Decide whether two students can pick IDs that guarantee the same room under each hash family.

| Family                                        | Result                                 |
| --------------------------------------------- | -------------------------------------- |
| `(ak + b) mod n`                              | Guaranteed: pick `k1 ≡ k2 mod n`       |
| `(⌊kn/u⌋ + a) mod n`                          | Guaranteed: pick `k1 = 1, k2 = 2`      |
| `((ak + b) mod p) mod n` (universal)          | Not guaranteed: probability at most `1/n` |

## Problem 3 — The Cold Is Not Bothersome Anyway

Choose the best sorting algorithm for each kind of key.

| Part | Key                               | Algorithm     | Time         |
| ---- | --------------------------------- | ------------- | -----------: |
| (a)  | Strings of `O(log n)` characters  | Radix sort    |       `Θ(n)` |
| (b)  | Ages up to 800,000                | Counting sort |       `Θ(n)` |
| (c)  | Thickness `m / n³`                | Radix sort    |       `Θ(n)` |
| (d)  | Only pairwise comparison          | Merge sort    | `Θ(n log n)` |

The main idea is to read each key as an integer bounded by a polynomial in `n`, so radix sort in base `n` takes a constant number of passes.

## Problem 4 — Pushing Paper

Find two boxes close to each other whose reams add up to `r`.

* **(a)** Store every `(b_i, i)` in a hash table, then look up `r − b_i` for each box. Expected `O(n)`.
* **(b)** With `r < n²`, drop values `≥ r`, radix sort the rest, and sweep with two fingers from both ends. Worst-case `O(n)`.

### Main concepts

* Hash table lookup instead of scanning
* Radix sort on bounded integers
* Two-finger sweep on a sorted array
* Handling a box that would pair with itself

## Problem 5 — Anagram Archaeology

Count substrings that are anagrams of a given string.

The solution represents each string by a table of 26 letter counts. Two strings are anagrams exactly when their tables are equal.

* **(a)** Slide a window of length `k` over `A`, updating the table in `O(1)` per step, and store the count of each table in a hash table.
* **(b)** Build this once for `T`, then answer each `S_i` with one lookup.
* **(c)** Implement `count_anagram_substrings(T, S)` in Python.

### Complexity

| Part                       | Complexity            |
| -------------------------- | --------------------: |
| Build (part a)             | expected `O(|A|)`     |
| Query (part a)             | expected `O(k)`       |
| All queries (part b)       | expected `O(|T| + nk)` |

## Files

```text
 ps3/
├── ps3-solutions.tex
├── count_anagram_substrings.py
├── macros-sp20.tex
└── tests.py
```

* `README.md` — overview and notes for this problem set
* `ps3-solutions.tex` — completed written solutions using the MIT LaTeX template
* `count_anagram_substrings.py` — programming implementation using the MIT Python template
* `tests.py` — provided tests for the programming portion
* `macros-sp20.tex` — provided MIT LaTeX macros used by the template

## Key Takeaways

* A hash table turns a search over all boxes into an expected `O(1)` lookup.
* Universal hashing gives a collision probability of at most `1/n` for any two keys, but no guarantee.
* Radix sort in base `n` sorts integers bounded by a polynomial in `n` in `O(n)` time.
* A sorted array lets a two-finger sweep replace a hash table when a worst-case bound is needed.
* A sliding window with a frequency table avoids recomputing counts for every substring.

## Related Material

### MIT 6.006

* Lectures covering hashing and universal hash families
* Comparison sorting lower bound, counting sort, and radix sort

### LeetCode

Related topics for later practice:

* [Hash Tables](../../leetcode/hash-tables/)
* [Two Pointers](../../leetcode/two-pointers/)
* [Sliding Window](../../leetcode/sliding-window/)

## Reflection

### What was difficult?

Seeing that fixed-length strings and fractions can be turned into integers so radix sort applies, and handling the "distinct values" detail in the two-finger sweep.

### What became clearer?

How hashing and sorting give different ways to reach `O(n)`: one in expectation, one in the worst case.

### What would I revisit?

* Universal hash families
* Radix sort running time for different bases
* Sliding window updates for frequency tables

## Status

* [x] Written solutions completed
* [x] Programming solutions completed
* [x] Complexity analyzed
* [ ] Concepts reviewed

**Status:** 🔄 In Progress
