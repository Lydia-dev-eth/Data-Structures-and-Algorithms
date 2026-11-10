Lecture 4 — Hashing & Direct Access Arrays

# 1. Where We Are

So far we have two ways to build a Set:

| Structure | build | find | insert / delete | order ops |
|---|---|---|---|---|
| Array | n | n | n | n |
| Sorted Array | n log n | log n | n | 1 / log n |

The sorted array already gives `find` in O(log n), which is very close to O(1).

The question for this lecture:

**Can we do `find(k)` faster than O(log n)?**

Answer:

- With only comparisons → **No**.
- If we are allowed to do more than comparisons → **Yes** (hashing).

---

# 2. The Comparison Model

## Idea

In the comparison model, items are **black boxes**.

The only thing we can do with two items is compare them:

```
<   <=   >   >=   =   !=
```

Each comparison takes two items and returns `True` or `False`.

A search algorithm must return:

- the item with key k, or
- "not found"

(We assume all keys are unique.)

## Decision Tree

Any deterministic comparison algorithm can be drawn as a **binary decision tree**.

```
            compare(k, A[3])
             /           \
         k < A[3]       k > A[3]
           /                \
   compare(k, A[1])     compare(k, A[5])
        ...                  ...
```

- Each **internal node** = one comparison.
- Each **leaf** = one possible output.
- Running the algorithm = walking one path from the root to a leaf.

Worst-case number of comparisons = **height of the tree** (longest root-to-leaf path).

---

# 3. Why Search Needs Ω(log n)

## Counting leaves

Possible outputs of a search on n items:

```
item 1, item 2, ..., item n, or "not found"
```

That is **n + 1 outputs**, so the tree needs at least **n + 1 leaves**.

## How short can a tree be?

A binary tree of height h has at most:

```
T(h) = 2^(h+1) − 1   nodes
```

Why? Height 0 → 1 node. A tree of height h has a root plus two subtrees of height h − 1:

```
T(h) = 2·T(h−1) + 1
T(0) = 1
```

Check: 2·(2^h − 1) + 1 = 2^(h+1) − 1 ✓

So with n nodes:

```
n ≤ 2^(h+1) − 1
h ≥ lg(n+1) − 1 = Ω(log n)
```

A tree with n + 1 leaves has more than n nodes, so:

**height = Ω(log n)**

## Small example

```
n = 7 items → 8 possible outputs → at least 8 leaves
a tree of height 2 has at most 4 leaves
a tree of height 3 has at most 8 leaves
→ need height ≥ 3
```

So at least 3 comparisons are needed in the worst case. Binary search on 7 items does exactly that.

## Conclusion

```
Any comparison-based search → Ω(log n)
```

Sorted arrays and balanced BSTs are **asymptotically optimal** for `find` in this model.

## The key observation

It does not matter that comparisons have 2 outcomes.

**Any constant branching factor** gives a tree of height Ω(log n).

To beat log n, we need an operation with **non-constant branching factor**, ω(1).

---

# 4. Direct Access Arrays

## The special operation

One thing a computer can do is **random access**: read any memory address in O(1).

That is a step that branches into as many outcomes as there are memory slots.

## Idea

Store an item with key k **at index k**.

```
keys: {2, 5, 7},  u = 10

index:  0     1     2    3     4     5    6     7    8     9
      [None, None, x₂, None, None, x₅, None, x₇, None, None]
```

- `u` = size of the key range (keys are integers in 0 … u−1).
- To find key 5, just look at `A[5]`.

(Keys must be integers. Anything in memory can be turned into an integer — its bits or its address — so this is not a real limitation.)

## Code

```python
class DirectAccessArray:
    def __init__(self, u): self.A = [None] * u   # O(u)
    def find(self, k):     return self.A[k]      # O(1)
    def insert(self, x):   self.A[x.key] = x     # O(1)
    def delete(self, k):   self.A[k] = None      # O(1)
```

## Complexity

```
find   → O(1)
insert → O(1)
delete → O(1)
build  → O(u)
space  → O(u)
```

## Order operations are slow

`find_next`, `find_max`, `delete_max` have to scan:

```
[None, None, x₂, None, None, x₅, None, x₇, None, None]
```

We do not know where the next item is, so we may check every slot → **O(u)**.

## The problem: space

We need a slot for **every possible key**, even if we store few items.

Example: ten-letter names.

```
u = 26^10 ≈ 9.5 × 10^13 slots
even one bit per slot → ≈ 17.6 TB
```

Impossible in practice.

**Goal:** keep O(1) search, but use only O(n) space when n ≪ u.

---

# 5. Hashing

## Idea

Use a smaller table with **m = O(n)** slots, and a function that maps each key to a slot:

```
h(k) : {0, ..., u−1} → {0, ..., m−1}
```

- `h` = hash function
- the small table = **hash table**
- `h(k)` = the **hash** of key k

If h never maps two stored keys to the same slot, then the table behaves exactly like a direct access array → O(1) worst case.

## The catch: collisions

If m < u, then by the **pigeonhole principle** some keys must share a slot.

```
u = 10 keys, m = 4 slots → at least one slot gets ≥ 3 keys
```

If h(k₁) = h(k₂) for k₁ ≠ k₂, we say the keys **collide**.

If we do not know in advance which keys will be stored, avoiding all collisions is extremely unlikely.

(If we do know the keys in advance, **perfect hashing** can avoid collisions. Not needed here.)

## Where do colliding items go?

Two strategies:

| Strategy | Idea |
|---|---|
| Open addressing | Store them somewhere else in the same table. Used in practice, harder to analyze. |
| **Chaining** | Store them in a separate structure per slot. **This is what we use.** |

---

# 6. Chaining

## Idea

Every slot holds a **chain**: a small separate set (linked list or dynamic array).

```
m = 5,  h(k) = k mod 5,  keys: 12, 7, 22, 3

slot 0: (empty)
slot 1: (empty)
slot 2: 12 → 7 → 22      ← collision, chain of length 3
slot 3: 3
slot 4: (empty)
```

## Operations

```
insert(x) → insert x into the chain at h(x.key)
find(k)   → search the chain at h(k)
delete(k) → delete k from the chain at h(k)
```

The chain can be any structure whose operations take at most linear time.

## Cost

```
cost of an operation = O(size of the chain at that slot)
```

- Chains of constant size → O(1) operations.
- All keys in one chain → O(n) operations (this is the worst case).

So the real question is: **how do we choose h so chains stay small?**

---

# 7. Hash Functions

## Division method (bad)

```
h(k) = k mod m
```

Works well **if keys are spread uniformly**.

But if all keys have the same remainder mod m:

```
m = 5,  keys: 5, 10, 15, 20, 25  →  all go to slot 0
```

One long chain → O(n) for everything.

The performance depends on the keys we are given. We want performance that does **not** depend on the input.

## Universal hashing (good)

For large u, **every** fixed hash function is bad for some input set (pigeonhole again).

So instead: **choose the hash function randomly** from a family.

One universal family:

```
H(m, p) = { h_ab(k) = ((a·k + b) mod p) mod m }
          with a, b ∈ {0, ..., p−1}, a ≠ 0
```

- `p` is a prime larger than u.
- Choosing concrete `a` and `b` picks one function from the family.

### Universal means

For any two different keys:

```
Pr[ h(kᵢ) = h(kⱼ) ] ≤ 1/m
```

where the probability is over the random choice of h.

(The proof that this family is universal is beyond 6.006.)

## Expected chain length

Let:

- n = number of stored keys
- m = table size
- kᵢ = the key we are looking at
- Xᵢⱼ = 1 if kᵢ and kⱼ hash to the same slot, 0 otherwise
- Xᵢ = Σⱼ Xᵢⱼ = number of keys in kᵢ's chain

Then:

```
E[Xᵢ] = Σⱼ E[Xᵢⱼ]
      = 1 + Σ_{j≠i} E[Xᵢⱼ]          (Xᵢᵢ = 1: the key collides with itself)
      = 1 + Σ_{j≠i} Pr[h(kᵢ) = h(kⱼ)]
      ≤ 1 + (n − 1) · (1/m)
      = 1 + (n − 1)/m
```

If **m = Ω(n)**, then (n − 1)/m = O(1), so:

```
expected chain size = O(1)
```

So `find`, `insert`, `delete` take **expected O(1)** time.

## Important: what is "expected"?

```
✓ Expectation over our random choice of hash function
✗ NOT expectation over random input keys
```

The input can be anything, even chosen by an adversary. The guarantee still holds, because the adversary does not know which h we picked.

---

# 8. Keeping m = O(n): Resizing

The bound needs m = Ω(n), and we also want space O(n).

But n changes as we insert and delete. So we **rebuild** the table when it gets too full or too empty:

1. Choose a new size m = O(n).
2. Rehash every item into the new table.

This is the same idea as dynamic arrays → **amortized** O(1) per insert/delete.

## Implementation walk-through

```python
class Hash_Table_Set:
    def __init__(self, r = 200):
        self.chain_set = Set_from_Seq(Linked_List_Seq)   # chains
        self.A = []
        self.size = 0                 # n
        self.r = r                    # 100/r = fill ratio
        self.p = 2**31 - 1            # prime
        self.a = randint(1, self.p - 1)   # random hash parameter
        self._compute_bounds()
        self._resize(0)
```

**Hash function:**

```python
def _hash(self, k, m):
    return ((self.a * k) % self.p) % m
```

Same shape as the universal family (with b = 0).

**Resize bounds:**

```python
def _compute_bounds(self):
    self.upper = len(self.A)                          # m
    self.lower = len(self.A) * 100*100 // (self.r*self.r)
```

With r = 200:

```
upper = m
lower = m · 10000 / 40000 = m/4
```

**Resize:**

```python
def _resize(self, n):
    if (self.lower >= n) or (n >= self.upper):   # too empty or too full
        f = ceil(r / 100)                        # r = 200 → f = 2
        m = max(n, 1) * f                        # new table size ≈ 2n
        A = [self.chain_set() for _ in range(m)]
        for x in self:
            A[self._hash(x.key, m)].insert(x)    # rehash everything
        self.A = A
        self._compute_bounds()
```

Cost: O(n) when it happens, but it happens rarely → amortized.

**Operations:**

```python
def find(self, k):                       # expected O(1)
    h = self._hash(k, len(self.A))
    return self.A[h].find(k)

def insert(self, x):                     # amortized, expected O(1)
    self._resize(self.size + 1)
    h = self._hash(x.key, len(self.A))
    added = self.A[h].insert(x)
    if added: self.size += 1
    return added

def delete(self, k):                     # amortized, expected O(1)
    h = self._hash(k, len(self.A))
    x = self.A[h].delete(k)
    self.size -= 1
    self._resize(self.size)
    return x
```

## Order operations are slow

`find_min`, `find_max`, `find_next`, `find_prev` loop through **every** item:

```
O(n)
```

Hashing scatters keys on purpose, so there is no order to use.

`iter_order` calls `find_next` n times:

```
n · O(n) = O(n²)
```

---

# 9. Complexity Table

| Structure | build | find | insert / delete | find_min/max, prev/next |
|---|---|---|---|---|
| Array | n | n | n | n |
| Sorted Array | n log n | log n | n | 1 / log n |
| Direct Access Array | u | 1 | 1 | u |
| Hash Table | n (expected) | 1 (expected) | 1 (amortized, expected) | n |

Notation: (e) = expected, (a) = amortized.

## Main trade-off

```
Hash Table
     ↓
Fast find / insert / delete: expected O(1)
     ↓
No useful order: min, max, next, prev = O(n)
```

---

# 10. Exercise — Duplicates

**Problem:** given an unsorted array A of n positive integers, is there any value that appears twice?

## 1) Brute force — O(n²)

Check all pairs:

```
n(n−1)/2 = O(n²) pairs, O(1) per comparison
```

## 2) Sorting — O(n log n)

```
sort A (merge sort, O(n log n))
scan adjacent pairs → equal neighbors = duplicate (O(n))
```

Equal values end up next to each other after sorting.

## 3) Hashing — expected O(n)

```
for each integer:
    insert into a hash table
    while inserting, compare against its chain
    if equal value is already there → duplicate
```

Each insert is expected O(1), so the total is expected O(n).

## 4) Values ≤ k, and k < n — O(1)

```
n integers, but only k < n possible values
→ pigeonhole: a duplicate must exist
→ answer: True
```

## 5) Values ≤ k, and n ≤ k — O(k)

Use a direct access array of length k:

```
create array of size k              → O(k)
for each integer a:
    if slot a is filled → duplicate
    else fill slot a                → O(1) each
```

Total O(k).

## Pattern

```
O(n²)  →  O(n log n)  →  expected O(n)
 pairs      sorting        hashing
```

---

# 11. Common Mistakes

## Mistake 1 — Thinking hashing breaks the Ω(log n) bound

The bound is for the **comparison model**.

Hash tables are faster because they use **random access** (large branching), not comparisons.

## Mistake 2 — Saying the expectation is over the input

```
Expected O(1) is over the random hash function,
not over random keys.
```

## Mistake 3 — Using `k mod m` and calling it safe

Keys with the same remainder all collide. The performance then depends on the input.

## Mistake 4 — Using a hash table for order queries

`find_min`, `find_max`, `find_next`, `find_prev` are O(n).

If you need order, use a sorted structure.

## Mistake 5 — Expecting no collisions

If m < u, collisions **must** happen (pigeonhole). The goal is short chains, not zero collisions.

## Mistake 6 — Forgetting m = Ω(n)

If m stays small while n grows, chains grow like n/m and O(1) is lost. That is why we resize.

## Mistake 7 — Saying a Direct Access Array is "always better"

O(1) everything, but O(u) space and O(u) order operations. For large u it is unusable.

---

# 12. Lecture 4 Mental Map

```
                    LECTURE 4
                        │
        ┌───────────────┼───────────────┐
        │               │               │
  Comparison Model  Direct Access    Hashing
        │             Array              │
  Decision tree          │         ┌─────┴─────┐
        │            key = index   │           │
   Ω(log n) find         │       Chaining   Hash functions
        │            find O(1)       │           │
  Sorted array       space O(u)   chain size  Division (bad)
  is optimal              │            │      Universal (good)
                    u too large?       │           │
                          └──────► m = O(n) ◄──────┘
                                       │
                          expected O(1) find/insert/delete
                                       │
                          But no ordering: order ops O(n)
```

## Core Takeaways

1. **Comparisons alone cannot beat Ω(log n) for search.**
   - Decision tree needs n + 1 leaves, so its height is Ω(log n).

2. **To go faster, use random access.**
   - A direct access array gives O(1) find, but costs O(u) space.

3. **Hashing shrinks the table to O(n).**
   - Price: collisions, which are unavoidable (pigeonhole).

4. **Chaining handles collisions.**
   - Operation cost = chain size.

5. **Randomness protects against bad inputs.**
   - Universal hashing: collision probability ≤ 1/m for any two keys.
   - Expected chain size ≤ 1 + (n − 1)/m = O(1) when m = Ω(n).

6. **Resize to keep m = O(n).**
   - Rebuild occasionally → amortized O(1).

7. **Always ask what the structure is trading.**

```
Time?
Space?
Worst case or expected?
Which operations become slow?
```
