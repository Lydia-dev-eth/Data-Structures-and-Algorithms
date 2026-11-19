Lecture 7 — Balanced Binary Trees (AVL)

# 1. Where We Are

Lecture 6: binary trees where every operation costs **O(h)**, h = height of the tree. The height was not controlled, so h could be large.

The goal now:

**Keep the tree balanced** — a tree on n nodes is balanced if its height is O(log n). Then all the O(h) operations become O(log n).

There are many ways to do this (Red-Black Trees, B-Trees, 2-3 Trees, Splay Trees, ...). The oldest and perhaps simplest is the **AVL Tree**.

---

# 2. The AVL Property

## Skew

```
skew(node) = height(right subtree) − height(left subtree)
```

The height of an **empty** subtree is **−1**.

## Height-balanced

- A node is **height-balanced** if its skew is −1, 0 or 1 (its left and right subtrees differ in height by at most 1).
- A tree is height-balanced if **every** node is height-balanced.

## Example

```
        D           skew(D) = height(F) − height(B) = 1 − 1 = 0
      /   \
     B     F        skew(B) = 0 − 0 = 0
    / \   /
   A   C E          skew(F) = height(E) − (−1) = 0 + 1 = 1   ✓ allowed
```

(`F` has no right child, so its right height is −1.)

## Exercise: a height-balanced tree is balanced

**Claim:** height-balanced ⇒ h = O(log n).

**Idea:** show that a height-balanced tree of height h has at least exponentially many nodes in h. Then n ≥ 2^Ω(h), so h = O(log n).

Let **F(h)** be the fewest nodes in any height-balanced tree of height h. The root's two subtrees have heights h − 1 and h − 2 and should each have as few nodes as possible:

```
F(h) = 1 + F(h−1) + F(h−2)  ≥  2·F(h−2)
F(0) = 1,   F(1) = 2
```

Small values:

```
F(0) = 1
F(1) = 2
F(2) = 1 + F(1) + F(0) = 4
F(3) = 1 + F(2) + F(1) = 7
F(4) = 1 + F(3) + F(2) = 12
```

Doubling every 2 levels gives:

```
F(h) ≥ 2^(h/2) = 2^Ω(h)
```

So height-balance **implies** balance.

---

# 3. Rotations

## Idea

When we add or remove nodes, the tree can become imbalanced. A **rotation** is a local operation that changes the structure **without changing the traversal order**, hoping to make the tree more balanced.

It takes O(1) time.

## The two configurations

```
        D                          B
       / \    rotate_right(D)     / \
      B   E   ───────────────►   A   D
     / \      ◄───────────────      / \
    A   C     rotate_left(B)       C   E
```

A, C, E stand for whole subtrees.

```
traversal order, left configuration:   A B C D E
traversal order, right configuration:  A B C D E   ← same
```

What changes: the **depth** of the nodes in subtrees A and E (A gets one level closer to the top, E one level farther in `rotate_right`).

## Code (rotate_right)

```python
def subtree_rotate_right(D):             # O(1)
    assert D.left
    B, E = D.left, D.right
    A, C = B.left, B.right
    D, B = B, D
    D.item, B.item = B.item, D.item
    B.left, B.right = A, D
    D.left, D.right = C, E
    if A: A.parent = B
    if E: E.parent = D
    B.subtree_update()
    D.subtree_update()
```

### Line by line

Call it on the node object called `D` (item `d`), whose left child is the node object `B` (item `b`).

```
B, E = D.left, D.right        B = left child,  E = right child of D
A, C = B.left, B.right        A, C = the two subtrees of B
D, B = B, D                   the NAMES swap: D now names the old left child object,
                                              B now names the old top object
D.item, B.item = B.item, D.item
                              the ITEMS swap: the old top object now holds item b,
                                              the old left child object now holds item d
B.left, B.right = A, D        top object:       left = A,  right = the other object
D.left, D.right = C, E        other object:     left = C,  right = E
if A: A.parent = B            A now hangs under the top object
if E: E.parent = D            E now hangs under the other object
B.subtree_update()            recompute heights
D.subtree_update()
```

Result: top object holds `b` with children A and (object holding `d` with children C and E) — the right configuration.

`rotate_left` is the mirror image.

---

# 4. Maintaining Height-Balance

## What can go wrong

Suppose a height-balanced AVL tree gets one insertion or deletion of a **leaf**. Then either the tree is still height-balanced, or some node now has |skew| > 1.

- Only the **ancestors** of that leaf have changed subtrees (at most O(h) of them), so only their skew can change.
- Each skew changes by at most 1, so the magnitude is **at most 2**.

Given a subtree whose root has skew 2 and where every other node is height-balanced, balance can be restored with **at most two rotations**. (The case analysis was done in lecture; the full argument is not repeated in the recitation.)

So: walk from the leaf up to the root, rebalancing each node → **O(log n) rotations in total**.

## Code

```python
def rebalance(A):                        # O(1)
    if A.skew() == 2:
        if A.right.skew() < 0:
            A.right.subtree_rotate_right()
        A.subtree_rotate_left()
    elif A.skew() == -2:
        if A.left.skew() > 0:
            A.left.subtree_rotate_left()
        A.subtree_rotate_right()

def maintain(A):                         # O(log n)
    A.rebalance()
    A.subtree_update()
    if A.parent: A.parent.maintain()
```

- skew 2 (right-heavy): if the right child leans **left** (skew < 0), first rotate the right child right, then rotate A left.
- skew −2 (left-heavy): mirror image.
- `maintain` rebalances A, updates A's height, then continues with A's parent until the root.

## Example from the PDF: Sequence AVL, `insert_at(4, 12)`

Tree before (sequence 10 6 8 5 18 −4 3):

```
              8
           /     \
         10       -4
         /       /   \
        6       5     3
                 \
                  18
```

Item 12 goes between 5 and 18, so it becomes the **left child of 18**:

```
         5               skew(5) = height(18) − (−1) = 1 + 1 = 2
          \
           18            skew(18) = height(none) − height(12) = −1 − 0 = −1  (< 0)
          /
        12
```

`rebalance(5)`: skew is 2 and `5.right.skew() < 0`, so:

```
1. rotate_right(18):         5            2. rotate_left(5):        12
                              \                                    /  \
                               12                                 5    18
                                 \
                                  18
```

Subtree of 5 is now `12 (5, 18)`, with traversal 5 12 18 — the order is unchanged, and the height of this subtree went from 2 to 1.

---

# 5. Augmentation

## Why we need it

`skew` needs the heights of both children. Computing a height by recursion visits the whole subtree:

```python
def height(A):                           # Ω(n)
    if A is None: return -1
    return 1 + max(height(A.left), height(A.right))
```

Rebalancing checks at least Ω(log n) heights in the worst case, so with this version it could not run in O(log n). We need the height of a node in **O(1)**.

## Idea

Every node **stores its own subtree height**. Reading it is O(1). When the tree changes, recompute the heights of the nodes that changed.

```python
def height(A):
    if A: return A.height
    else: return -1

def subtree_update(A):                   # O(1)
    A.height = 1 + max(height(A.left), height(A.right))
```

In Lecture 6 the code had commented-out calls (`# A.maintain()`, `# A.subtree_update()`, `# wait for R07!`). Now they are active: every node whose subtree changed during an insertion, deletion or rotation is updated.

A rebalancing insertion or deletion calls `subtree_update` on at most O(log n) nodes. So as long as one update takes O(1), maintaining the augmentation fits in **O(log n)**.

## Augmenting in general

To store a property P(X) of X's subtree at every node X:

1. **Define** exactly which property of X's subtree P(X) is.
2. **Show** how to compute P(X) in **O(1)** from the augmentations of X's children.

Then P can be stored and maintained without affecting the O(log n) cost of rebalancing insertions and deletions.

(The PDF mentions an earlier example: PS1, a singly linked list augmented with back pointers to find a node's predecessor faster.)

---

# 6. Binary Node with AVL Balancing

The Lecture 6 node with these changes:

```python
class Binary_Node:
    def __init__(A, x):                  # O(1)
        A.item = x
        A.left = None
        A.right = None
        A.parent = None
        A.subtree_update()               # sets A.height

    def subtree_update(A): ...           # O(1)
    def skew(A): ...                     # O(1)
    # subtree_iter                       O(n)
    # subtree_first / subtree_last       O(log n)
    # successor / predecessor            O(log n)
    # subtree_insert_before / after      O(log n), end with A.maintain()
    # subtree_delete                     O(log n), ends with A.parent.maintain()
    # subtree_rotate_right / left        O(1)
    # rebalance                          O(1)
    # maintain                           O(log n)
```

Since the tree is balanced, the O(h) operations of Lecture 6 are now **O(log n)**.

A new node has height 0 (no children, so 1 + max(−1, −1) = 0).

---

# 7. Application: Set (Set AVL)

Use the **Binary Tree Set from Lecture 6** with the new balanced node. It needs no changes.

```
find, find_next, find_prev, find_min, find_max, insert, delete   → O(log n)
build(X)  → O(n log n)    (n inserts)
iter()    → O(n)
```

This is what is normally called an AVL tree; here it is called a **Set AVL**.

---

# 8. Application: Sequence (Sequence AVL)

## Idea

Use the **traversal order** as the **Sequence order**. We need the i-th item fast, but walking the traversal would take O(n).

If we knew how many items are in the **left subtree**, we could compare that size to i and go left or right.

So we **augment each node with the size of its subtree**:

```
size(A) = 1 + size(A.left) + size(A.right)       (missing child counts as 0)
```

Computed in O(1) from the children.

## Code

```python
class Size_Node(Binary_Node):
    def subtree_update(A):               # O(1)
        super().subtree_update()         # height
        A.size = 1
        if A.left: A.size += A.left.size
        if A.right: A.size += A.right.size

    def subtree_at(A, i):                # O(h)
        assert 0 <= i
        if A.left: L_size = A.left.size
        else: L_size = 0
        if i < L_size: return A.left.subtree_at(i)
        elif i > L_size: return A.right.subtree_at(i - L_size - 1)
        else: return A
```

### Example: find index 4 in the first tree of the PDF example

Sequence [10, 6, 8, 5, 1, 3], tree:

```
          8  (size 6)
        /   \
      10     1  (size 3)
        \   / \
         6 5   3
```

```
subtree_at(root=8, i=4): left size L = 2 (nodes 10, 6)
    4 > 2 → go right with index 4 − 2 − 1 = 1
subtree_at(node 1, i=1): left size L = 1 (node 5)
    1 == 1 → this node.   → item 1   ✓ (index 4 of [10, 6, 8, 5, 1, 3])
```

The rule: `i < L` → left, `i == L` → here, `i > L` → right, with the index reduced by L + 1 (the left subtree and this node are skipped).

## Sequence operations

Once the i-th node can be found in O(log n), the other Sequence operations are direct uses of the binary tree operations. Building a tree from a sequence takes **O(n)** using the balanced build from Lecture 6 (middle item at the root, recurse on halves; each node also calls `subtree_update`).

```python
class Seq_Binary_Tree(Binary_Tree):
    def __init__(self): super().__init__(Size_Node)
    def build(self, X): ...              # O(n)
    def get_at(self, i): ...             # subtree_at(i).item
    def set_at(self, i, x): ...          # subtree_at(i).item = x
    def insert_at(self, i, x): ...
    def delete_at(self, i): ...
    def insert_first(self, x): self.insert_at(0, x)
    def delete_first(self): return self.delete_at(0)
    def insert_last(self, x): self.insert_at(len(self), x)
    def delete_last(self): return self.delete_at(len(self) - 1)
```

`insert_at(i, x)`:

- `i == 0`: insert **before** the first node (or make it the root if the tree is empty).
- otherwise: find the node at index `i − 1` and insert **after** it.

`delete_at(i)`: find the i-th node, `subtree_delete()` it, return the item of the removed node.

This is called a **Sequence AVL**.

---

# 9. Exercise: Sequence AVL Example

```python
T = Seq_Binary_Tree()
T.build([10,6,8,5,1,3])
T.get_at(4)
T.set_at(4, -4)
T.insert_at(4, 18)
T.insert_at(4, 12)
T.delete_at(2)
```

Reminder from the PDF: update subtree heights and sizes as you modify the tree. Notation `8H2#6` = item 8, height 2, size 6.

```
build:            8H2#6
                /       \
            10H1#2       1H1#3
               \         /   \
              6H0#1   5H0#1  3H0#1

get_at(4)  → 1                      (no change)

set_at(4, -4):    the item 1 becomes -4

insert_at(4, 18): 8H3#7
                /       \
            10H1#2       -4H2#4
               \         /     \
              6H0#1   5H1#2    3H0#1
                          \
                         18H0#1

insert_at(4, 12): 18 gets left child 12, then node 5 has skew 2 and
                  its right child has skew −1  →  rotate_right(18), rotate_left(5)
                  (shown in section 4)

                  8H3#8
                /       \
            10H1#2       -4H2#5
               \         /     \
              6H0#1   12H1#3   3H0#1
                      /    \
                  5H0#1   18H0#1
```

`delete_at(2)`: index 2 is the item 8 (the root). It has a left child, so its predecessor, 6, is used:

```
swap items 8 and 6:  root holds 6, the old 6-node holds 8 and is a leaf → cut it
maintain from the parent (node 10):
    node 10 is now a leaf (height 0).
    root: skew = height(-4 subtree) − height(10) = 2 − 0 = 2
          right child (-4) has skew = 0 − 1 = −1 < 0
    → rotate_right(-4 node), then rotate_left(root)
```

Final tree (the PDF's last picture):

```
              12H2#7
            /        \
        6H1#3         -4H1#3
        /    \        /    \
   10H0#1  5H0#1  18H0#1  3H0#1

traversal: 10 6 5 12 18 -4 3
```

---

# 10. Exercise: Counting Ones in a Bit Sequence

**Task:** maintain a sequence of n bits with two operations, each in O(log n):

- `flip(i)`: flip the bit at index i.
- `count_ones_upto(i)`: number of 1 bits in the prefix up to index i.

## Solution idea

Store the bits in a **Sequence Tree** and augment each node A with:

```
A.subtree_ones = number of 1 bits in A's subtree
```

Computed in O(1) from the children:

```python
def update(A):
    A.subtree_ones = A.item
    if A.left:
        A.subtree_ones += A.left.subtree_ones
    if A.right:
        A.subtree_ones += A.right.subtree_ones
```

## flip(i)

1. Find the i-th node A with `subtree_at(i)`.
2. Flip the bit stored in `A.item`.
3. Update the augmentation at A and at **every ancestor**, walking up the tree → O(log n).

## count_ones_upto(i)

`count_ones_upto(i)` means `subtree_count_ones_upto(T.root, i)`, which counts the 1 bits of the subtree of A that are at index ≤ i **inside A's subtree**.

```python
def subtree_count_ones_upto(A, i):
    assert 0 <= i < A.size
    out = 0
    if A.left:
        if i < A.left.size:
            return subtree_count_ones_upto(A.left, i)    # all in the left subtree
        out += A.left.subtree_ones                       # whole left subtree counts
        i -= A.left.size                                 # index inside (node + right)
    out += A.item                                        # this node
    if i > 0:
        assert A.right
        out += subtree_count_ones_upto(A.right, i - 1)   # part of the right subtree
    return out
```

Each call makes **at most one** recursive call on a child → O(log n).

### Example

Bits `[1, 0, 1, 1, 0, 1, 0]`. Balanced tree:

```
               (idx3: 1)
             /           \
       (idx1: 0)        (idx5: 1)
        /     \          /     \
   (idx0:1) (idx2:1) (idx4:0) (idx6:0)
```

`count_ones_upto(4)` → bits at indices 0..4 = 1, 0, 1, 1, 0 → answer 3:

```
root (idx3): left size = 3, i = 4 ≥ 3
    out += left.subtree_ones = 1 + 0 + 1 = 2
    i = 4 − 3 = 1
    out += root item = 1                 → out = 3
    i > 0 → out += count(right subtree, i − 1 = 0)
        node idx5: left size = 1, i = 0 < 1 → count(left = node idx4, 0)
            node idx4: no left; out += item = 0; i = 0 → return 0
    out = 3 + 0 = 3 ✓
```

---

# 11. Common Mistakes

## Mistake 1 — Computing height by recursion

That costs Ω(n) per call. Rebalancing needs at least Ω(log n) height checks, so it would no longer run in O(log n). Store the height in each node.

## Mistake 2 — Forgetting to update stored values

Every node whose subtree changed (insertion, deletion, **rotation**) must call `subtree_update`. Heights and sizes go wrong otherwise.

## Mistake 3 — Using the wrong height for an empty subtree

An empty subtree has height **−1**. A leaf has height 0 and skew 0.

## Mistake 4 — Thinking a rotation changes the traversal order

It does not. Only the structure and the depths of subtrees A and E change.

## Mistake 5 — Rotating only once in the "zig-zag" case

If A has skew 2 and its right child has skew < 0 (or skew −2 and the left child has skew > 0), first rotate the **child**, then rotate A.

## Mistake 6 — Rebalancing only the changed node

Walk from the changed leaf **up to the root**. Every ancestor can change skew.

## Mistake 7 — An augmentation that needs the whole subtree

A property must be computable in **O(1) from the children's augmentations**. Otherwise maintaining it breaks the O(log n) bound.

## Mistake 8 — Forgetting the index shift in subtree_at

Going right means skipping the left subtree **and** the node: use `i − L_size − 1`.

## Mistake 9 — Mixing up the build times

- Set AVL: `build(X)` = n inserts → **O(n log n)**.
- Sequence AVL: balanced build from the sequence → **O(n)**.

---

# 12. Lecture 7 Mental Map

```
                         LECTURE 7
                             │
        ┌────────────────────┼─────────────────────┐
        │                    │                     │
   AVL Property          Maintaining          Augmentation
   skew ∈ {−1,0,1}       Balance              (store a property
        │                    │                 of each subtree)
  height-balanced      ┌─────┴──────┐                │
  ⇒ balanced           │            │         ┌──────┴───────┐
  (F(h) ≥ 2^(h/2))  Rotations   rebalance /    height         size
                     O(1),      maintain      O(1) skew     i-th node
                     keep order O(log n)                     O(log n)
                                                  │            │
                                              Set AVL     Sequence AVL
                                           all O(log n)   get_at, insert_at,
                                           build O(n log n) delete_at O(log n)
                                                           build O(n)
                                                               │
                                                  more augmentations,
                                                  e.g. number of ones
```

## Core Takeaways

1. **Balanced means h = O(log n).**
   - Then every O(h) tree operation is O(log n).

2. **AVL: every node has skew −1, 0 or 1.**
   - This forces at least 2^(h/2) nodes, so the tree is balanced.

3. **Rotations restore balance in O(1) and keep the traversal order.**

4. **After a leaf is added or removed, only its ancestors can be unbalanced.**
   - Rebalance each one on the way up: at most two rotations per node, O(log n) rotations in total.

5. **Store the height in every node.**
   - Then skew costs O(1) and rebalancing fits in O(log n).

6. **Augmentation = store extra subtree information.**
   - Define the property, compute it in O(1) from the children.

7. **The same balanced tree gives a Set (by key) and a Sequence (by index, using subtree sizes).**

```
What does each node store?
Can I compute it in O(1) from the children?
Did I update every node that changed?
Is the tree still balanced after the update?
```
