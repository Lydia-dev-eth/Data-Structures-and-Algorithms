Lecture 5 — Linear-Time Sorting

# 1. Where We Are

Sorting algorithms so far:

| Algorithm | Time |
|---|---|
| Selection Sort | Θ(n²) |
| Insertion Sort | Θ(n²) worst case |
| Merge Sort | Θ(n log n) |

Lecture 4 showed that **search** needs Ω(log n) comparisons, and that using random access (direct access arrays) beats that bound.

The question for this lecture:

**Can we sort faster than Θ(n log n)?**

Answer:

- With only comparisons → **No**.
- With integer keys and direct access → **Yes**, in linear time.

---

# 2. Comparison Sorting Lower Bound

## Idea

Use the same decision-tree argument as for search.

- Each internal node = one comparison.
- Each leaf = one possible output.

## Counting leaves

A sorting algorithm on n items can output any of the **n! permutations**.

So the tree needs at least **n! leaves**.

A binary tree with n! leaves has height:

```
h ≥ lg(n!)
```

## Why lg(n!) = Ω(n log n)

Look at the product n! = n · (n−1) · ... · 1.

The top half of the terms are each at least n/2, so:

```
n! > (n/2)^(n/2)
lg(n!) > (n/2) · lg(n/2) = Ω(n log n)
```

(Stirling's approximation gives the same result: n! ≈ √(2πn) · (n/e)^n.)

## Small example

```
n = 3 → 3! = 6 outputs
height 2 → at most 4 leaves  (not enough)
height 3 → at most 8 leaves  (enough)
→ at least 3 comparisons needed in the worst case
```

## Conclusion

```
Any comparison sort → Ω(n log n)
```

Merge sort is **asymptotically optimal** in the comparison model.

To do better we must use something other than comparisons: **direct access** (random access to memory).

---

# 3. Direct Access Array Sort

## Idea

If the keys are **distinct integers** in {0, ..., u−1}:

1. Create an array D of length u.
2. Put each item x at `D[x.key]`.
3. Read D from left to right and output the items that exist.

## Example

```
keys: [5, 2, 9, 0, 7],  u = 10

D = [x₀, _, x₂, _, _, x₅, _, x₇, _, x₉]
read left to right → 0, 2, 5, 7, 9
```

## Code

```python
def direct_access_sort(A):
    u = 1 + max([x.key for x in A])    # O(n) find maximum key
    D = [None] * u                     # O(u) direct access array
    for x in A:                        # O(n) insert items
        D[x.key] = x
    i = 0
    for key in range(u):               # O(u) read out items in order
        if D[key] is not None:
            A[i] = D[key]
            i += 1
```

## Complexity

```
find max       → O(n)
create array   → O(u)
insert items   → O(n)
scan array     → O(u)

Total → Θ(n + u)
```

If u = O(n), this is **linear**.

## Two drawbacks

1. **Duplicate keys** — two items with the same key want the same slot, so one overwrites the other.
2. **Large key ranges** — u may be huge compared to n, so Θ(n + u) is not linear (and the array may not fit in memory).

---

# 4. Counting Sort

## Fix 1: chains (handles duplicates)

Like in hashing, put a **chain** at each index. Items with the same key go in the same chain, **in input order**.

```
keys: [2, 0, 2, 1]   (items a, b, c, d),  u = 3

D[0] = [b]
D[1] = [d]
D[2] = [a, c]

read out → b, d, a, c
```

```python
def counting_sort(A):
    u = 1 + max([x.key for x in A])    # O(n)
    D = [[] for i in range(u)]         # O(u) chains
    for x in A:                        # O(n)
        D[x.key].append(x)
    i = 0
    for chain in D:                    # O(u)
        for x in chain:
            A[i] = x
            i += 1
```

**Stable:** `a` came before `c` in the input and still comes before `c` in the output. The chain must keep insertion order (a queue).

## Fix 2: cumulative sums (moves each item once)

Instead of chains, **count** the keys, then compute where each key's block ends.

```python
def counting_sort(A):
    u = 1 + max([x.key for x in A])    # O(n)
    D = [0] * u                        # O(u)
    for x in A:                        # O(n) count keys
        D[x.key] += 1
    for k in range(1, u):              # O(u) cumulative sums
        D[k] += D[k - 1]
    for x in list(reversed(A)):        # O(n) move items into place
        A[D[x.key] - 1] = x
        D[x.key] -= 1
```

### Step-by-step example

Items in order: a(2), b(0), c(2), d(1), so u = 3.

```
count:        D = [1, 1, 2]       one 0, one 1, two 2s
cumulative:   D = [1, 2, 4]       D[k] = number of items with key ≤ k
```

So key 0 ends at index 0, key 1 ends at index 1, key 2 ends at index 3.

Now walk the input **backwards**:

```
d(1): index D[1]−1 = 1 → A[1] = d,  D[1] = 1
c(2): index D[2]−1 = 3 → A[3] = c,  D[2] = 3
b(0): index D[0]−1 = 0 → A[0] = b,  D[0] = 0
a(2): index D[2]−1 = 2 → A[2] = a,  D[2] = 2

A = [b, d, a, c]
```

### Why backwards?

`D[k]` points just past the **last** slot for key k, and we fill that block from its end towards its start.

The last item with key k in the input must go to the last slot, so we must process the input from the **end**. That keeps equal keys in input order → **stable**.

## Complexity

```
find max           → O(n)
initialize D       → O(u)
count keys         → O(n)
cumulative sums    → O(u)
move items         → O(n)

Total → Θ(n + u)
```

When u = O(n), counting sort is **linear** and allows duplicates.

## Properties

```
Time:     Θ(n + u)
Space:    O(n + u)
In-place: No
Stable:   Yes
```

## Remaining problem

If u is much larger than n (for example u = n²), Θ(n + u) is **not** linear.

Idea: break big keys into small **digits** and sort each digit. For that we need a way to sort by several keys.

---

# 5. Tuple Sort

## Idea

Sort objects that have several keys:

```
x.k1  (most important)
x.k2
x.k3  (least important)
```

The order is **lexicographic**: compare k1 first; if tied, compare k2; and so on.

## Algorithm

Use a **stable** sort repeatedly:

1. Sort by the **least** important key.
2. Then by the next least important key.
3. ...
4. Finally by the **most** important key.

## Example

Sort pairs (k1, k2):

```
start:               (2,1) (1,2) (2,0) (1,1)

sort by k2 (stable): (2,0) (2,1) (1,1) (1,2)
sort by k1 (stable): (1,1) (1,2) (2,0) (2,1)   ✓
```

During the second pass, (1,1) stays before (1,2) because the sort is stable. That order was set by the first pass.

## Why stability is required

The last sort uses the most important key. Ties in that key must keep the order set by the earlier (less important) sorts.

If the subroutine is **not stable**, a later pass can scramble the order from earlier passes, and the final result is wrong.

It is the same as sorting a spreadsheet by column B, then by column A.

---

# 6. Radix Sort

## Idea

Break each integer key into **digits in base n**, then tuple-sort the digits with counting sort.

```
n = number of items
base = n
c = number of digits = ceil(log_n u)
```

Sort by the **least significant digit first**, up to the most significant digit.

Each pass is a counting sort on keys in {0, ..., n−1}, so it costs Θ(n + n) = Θ(n).

## Example (base 10)

Sort `329, 457, 657, 839, 436, 720, 355`:

```
start:        329  457  657  839  436  720  355

ones digit:   720  355  436  457  657  329  839
tens digit:   720  329  436  839  355  457  657
hundreds:     329  355  436  457  657  720  839   ✓
```

Check the tens pass: the digits are 720→2, 329→2, 436→3, 839→3, 355→5, 457→5, 657→5. Items with equal digits keep the order from the ones pass (stable).

## Code idea

```python
def radix_sort(A):
    n = len(A)
    u = 1 + max([x.key for x in A])
    # c digits in base n
    for each digit i from least to most significant:
        counting_sort(A) using digit i as the key     # Θ(n)
```

## Complexity

```
c passes × Θ(n) per pass = Θ(n · c)
```

If the largest key satisfies u ≤ n^c:

```
Θ(n · c) time
```

- c constant → **Θ(n), linear**.
- Example: keys up to n³ → c = 3 → 3 counting sorts → linear.
- Example: keys up to 2^n → c = n / lg n → Θ(n² / log n), not linear.

## Properties

```
Time:     Θ(n · c), c = ceil(log_n u)
Space:    O(n)
In-place: No
Stable:   Yes
```

---

# 7. Exercises

## 1) Base-10 radix sort

See the example in section 6.

```
(329, 457, 657, 839, 436, 720, 355) → (329, 355, 436, 457, 657, 720, 839)
```

## 2) Sort n integers from the range [−n², ..., n³] in linear time

```
add n² to every key        → range becomes [0, ..., n³ + n²]
radix sort                 → u ≤ n³ + n² + 1 ≤ n⁴, so c ≤ 4, Θ(n)
subtract n² from every key
```

Radix sort needs non-negative keys, so we shift. The range size is polynomial in n, so c is constant.

## 3) Sort n strings, each with k English letters, in linear time

```
map letters to {0, ..., 25}
for position from k−1 down to 0:        # right to left
    counting sort the strings by the character at that position
```

```
k rounds × Θ(n + 26) = Θ(n · k)
```

This is **linear in the input size**, because the input has n · k characters.

---

# 8. Common Mistakes

## Mistake 1 — Thinking linear-time sorting contradicts Ω(n log n)

The bound is for the **comparison model**. Counting and radix sort use keys as **array indices**, which is not a comparison.

## Mistake 2 — Using direct access array sort with duplicate keys

Items with equal keys overwrite each other. Use counting sort instead.

## Mistake 3 — Saying counting sort is always linear

It is Θ(n + u). If u is much larger than n (for example u = n²), it is **not** linear. That is the reason radix sort exists.

## Mistake 4 — Walking the input forwards in the cumulative-sum version

`D[k]` points to the end of key k's block. Walking forwards puts equal keys in **reverse** order → **not stable**, and radix sort breaks.

## Mistake 5 — Sorting the most significant digit first in radix sort

Radix sort goes from the **least** significant digit to the most significant. Tuple sort sorts the **least important** key first.

## Mistake 6 — Using an unstable sort inside tuple sort or radix sort

Later rounds destroy the order built by earlier rounds, so the final result is wrong.

## Mistake 7 — Forgetting negative keys

Counting sort needs keys in {0, ..., u−1}. Shift negative keys by adding a constant first, then shift back.

## Mistake 8 — Choosing too few digits

You need base^c ≥ u, otherwise the top digits of large keys are cut off and the result is wrong.

---

# 9. Complexity Summary

| Algorithm | Time | Extra Space | Stable | Needs |
|---|---|---|---|---|
| Selection Sort | Θ(n²) | O(1) | No | comparisons |
| Insertion Sort | Θ(n²) | O(1) | Yes | comparisons |
| Merge Sort | Θ(n log n) | O(n) | Yes* | comparisons |
| Direct Access Array Sort | Θ(n + u) | O(u) | n/a | distinct integer keys |
| Counting Sort | Θ(n + u) | O(n + u) | Yes | integer keys < u |
| Radix Sort | Θ(n · c) | O(n) | Yes | integer keys ≤ n^c |

---

# 10. Lecture 5 Mental Map

```
                      LECTURE 5
                          │
          ┌───────────────┴───────────────┐
          │                               │
   Comparison Sorting             Beyond Comparisons
          │                               │
   Decision tree, n! leaves     ┌──────────┼───────────┐
          │                     │          │           │
    Ω(n log n)           Direct Access  Counting    Radix Sort
          │                 Sort         Sort           │
   Merge sort is        (distinct keys) (duplicates)  Tuple Sort
      optimal             Θ(n + u)      Θ(n + u)         +
                                           │        Counting Sort
                                    u too large?        │
                                           └────►  digits in base n
                                                        │
                                                  Θ(n · c), linear
                                                  when u ≤ n^c
```

## Core Takeaways

1. **Comparison sorting needs Ω(n log n).**
   - n! outputs → n! leaves → height Ω(log n!) = Ω(n log n).

2. **Direct access removes the limit.**
   - Keys as indices give Θ(n + u) sorting.

3. **Counting sort allows duplicates.**
   - Cumulative sums give each item its final index; walk backwards for stability.

4. **Tuple sort sorts by several keys.**
   - Stable sort by the least important key first.

5. **Radix sort handles large integers.**
   - Base-n digits + counting sort = Θ(n · c).
   - Linear when u ≤ n^c with c constant.

6. **Stability is what makes the whole construction work.**

7. **Always ask what the algorithm assumes.**

```
Comparisons only, or integer keys?
Size of the key range u compared to n?
Duplicates allowed?
Stable?
Extra space?
```
