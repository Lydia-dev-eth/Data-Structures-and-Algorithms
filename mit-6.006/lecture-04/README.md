# Lecture 4 — Hashing & Direct Access Arrays

This folder contains notes and implementations from MIT 6.006 Lecture 4 / Recitation 4, focusing on why search needs Ω(log n) comparisons, and how hashing beats it.

## What This Covers

- **Comparison Model** — why any comparison-based search needs Ω(log n).
- **Direct Access Array** — O(1) find by using the key as the array index.
- **Hashing** — shrinking the key space from u to m = O(n) slots.
- **Chaining** — handling collisions by storing a chain per slot.
- **Hash Functions** — division method (bad) vs universal hashing (good).
- **Hash Table Set** — implementation with resizing.
- **Duplicates problem** — O(n²) → O(n log n) → expected O(n).

## Files

| File | What it contains |
|---|---|
| `notes.md` | Full notes, intuition, proofs, complexity, common mistakes |
| `direct_access_array.py` | Direct Access Array implementation |
| `hash_table_set.py` | Hash Table Set with chaining and resizing |
| `duplicates.py` | The three Duplicates solutions |
| `README.md` | Overview of this folder |

## Key Ideas

### 1. Comparison Model Lower Bound

A comparison search is a **binary decision tree**.

```
leaves needed  ≥ n + 1   (n items + "not found")
tree height    ≥ lg(n+1) − 1 = Ω(log n)
```

- Worst-case comparisons = height of the tree.
- A binary tree of height h has at most 2^(h+1) − 1 nodes.
- Any constant branching factor gives the same Ω(log n).

So sorted arrays and balanced BSTs are **optimal** for find in this model.

**To go faster we must stop using only comparisons.**

### 2. Direct Access Array

Store item with key k at index k. Random access in memory gives **huge branching** in one step.

```
find   → O(1)
insert → O(1)
delete → O(1)
order operations → O(u)
space  → O(u)
```

Problem: u can be enormous. Ten-letter names: 26^10 ≈ 9.5 × 10^13 slots → ~17.6 TB even as a bit array.

### 3. Hashing

Use a smaller table of size m = O(n) and a hash function:

```
h(k) : {0, ..., u−1} → {0, ..., m−1}
```

If u > m, collisions are unavoidable (**pigeonhole principle**).

### 4. Chaining

Each slot holds a chain (linked list / dynamic array).

- `insert(x)` → insert into chain at h(x.key)
- `find(k)` / `delete(k)` → search that chain
- Chains short → operations fast. All keys in one chain → O(n).

(Open addressing is the other strategy — used in practice, harder to analyze.)

### 5. Hash Functions

| Method | Idea | Verdict |
|---|---|---|
| Division | h(k) = k mod m | Bad — adversarial keys (same remainder) break it |
| Universal | h(k) = ((ak + b) mod p) mod m, random a, b, prime p > u | Good |

Universal family guarantee:

```
Pr[h(ki) = h(kj)] ≤ 1/m   for any ki ≠ kj
```

Expected chain length:

```
E[chain size] ≤ 1 + (n − 1)/m = O(1)   when m = Ω(n)
```

**The expectation is over the random choice of hash function, not over the input keys.**

### 6. Resizing

Keep m = O(n): when the table gets too full/empty, rebuild with a new size and a new hash function, reinsert everything. Same idea as dynamic arrays → **amortized** O(1).

## Complexity at a Glance

| Structure | build | find | insert / delete | find_min/max, prev/next |
|---|---|---|---|---|
| Array | n | n | n | n |
| Sorted Array | n log n | log n | n | 1 / log n |
| Direct Access Array | u | 1 | 1 | u |
| Hash Table | n (expected) | 1 (expected) | 1 (amortized, expected) | n |

## Duplicates Exercise

| Approach | Time |
|---|---|
| Check all pairs | O(n²) |
| Sort, then scan adjacent | O(n log n) |
| Insert into hash table, check chain | expected O(n) |
| Values ≤ k < n | O(1) — pigeonhole guarantees a duplicate |
| Values ≤ k, n ≤ k | O(k) — direct access array |

## Common Mistakes

- Thinking hash tables beat Ω(log n) **in the comparison model** — they work because they use random access, not comparisons.
- Saying the expected O(1) is over random inputs — it's over the random hash function.
- Using hash tables for order operations (min, max, next, prev) — these are O(n).
- Forgetting that collisions are unavoidable when m < u.
- Using `k mod m` and assuming it is safe for any input.

## Key Takeaway

> Hashing trades the wasted space of a direct access array for a small chance of collisions — and randomization makes the expected cost constant, whatever the input.

Fast find and insert, but **no useful ordering**. Order queries need sorted structures.

See `notes.md` for detailed concepts and the Python files for implementations.
