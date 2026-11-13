Lecture 6 — Binary Trees

# 1. Where We Are

Set implementations so far:

| Structure | build | find | insert / delete | find_min/max, prev/next |
|---|---|---|---|---|
| Array | n | n | n | n |
| Sorted Array | n log n | log n | n | 1 / log n |
| Direct Access Array | u | 1 | 1 | u |
| Hash Table | n (e) | 1 (e) | 1 (a)(e) | n |

Each one is slow at something:

- Sorted array: slow insert / delete (shifting).
- Hash table: slow order operations.
- Direct access array: huge space.

**Goal:** fast find, fast order operations, and fast insert / delete **together**.

Idea: store the items in a **binary tree** and make every operation cost the **height** of the tree.

---

# 2. Binary Trees

## Binary node

A binary node stores four things:

```
item     pointer to the stored item
parent   pointer to the parent node (None for the root)
left     pointer to the left child  (None if absent)
right    pointer to the right child (None if absent)
```

```python
class Binary_Node:
    def __init__(A, x):          # O(1)
        A.item = x
        A.left = None
        A.right = None
        A.parent = None
```

(The PDF calls the node `A` instead of `self`.)

## Why "binary"?

A node connects to **three** nodes: parent, left child, right child. It is called binary because it has **two children**. The parent is treated differently.

## Terms

| Term | Meaning |
|---|---|
| Root | The only node with no parent |
| Ancestors of X | Nodes passed going from X up to the root |
| Depth of X | Length of the path from X up to the root |
| Height of X | Largest depth of any node in the subtree rooted at X |
| Leaf | A node with no children |

## Example

```
        D            root = D, depth 0
      /   \
     B     F         depth 1
    / \   / \
   A   C E   G       depth 2  (leaves: A, C, E, G)

height(D) = 2,   height(B) = 1,   height(A) = 0
ancestors of C = B, D
```

## Why use a tree instead of a linked list?

- Linked list: a node can be n pointer hops from the head → O(n).
- Balanced binary tree: every node is within O(log n) hops of the root → height h = O(log n).

If every operation costs O(h), then:

```
h = O(log n)  →  every operation is O(log n)
```

That is much closer to O(1) than to O(n).

---

# 3. Traversal Order

## Definition

The left / right choice gives the tree a natural order:

```
every node in the LEFT  subtree of X comes BEFORE X
every node in the RIGHT subtree of X comes AFTER  X
```

## Listing the nodes

Recursively list the left subtree, then the node itself, then the right subtree.

```python
def subtree_iter(A):                     # O(n)
    if A.left:  yield from A.left.subtree_iter()
    yield A
    if A.right: yield from A.right.subtree_iter()
```

On the example tree:

```
subtree_iter(D):
    subtree_iter(B):  A, B, C
    D
    subtree_iter(F):  E, F, G

traversal order = A B C D E F G
```

## Complexity

Every node is visited once with O(1) work → **O(n)**.

## Important

For now the traversal order has **no meaning** for the items. We only promise to **preserve** it. Next, we give it a meaning (sequence order, or key order for a Set).

---

# 4. Tree Navigation

## First and last

```python
def subtree_first(A):                    # O(h)
    if A.left:  return A.left.subtree_first()
    else:       return A

def subtree_last(A):                     # O(h)
    if A.right: return A.right.subtree_last()
    else:       return A
```

Everything on the left comes first, so keep walking left. The last node is the mirror.

```
subtree_first(D) → D → B → A     (A has no left child) → A
subtree_last(D)  → D → F → G     → G
```

Each step goes down one level → O(h).

## Successor

The successor of A is the next node in traversal order.

```python
def successor(A):                        # O(h)
    if A.right: return A.right.subtree_first()
    while A.parent and (A is A.parent.right):
        A = A.parent
    return A.parent
```

**Case 1: A has a right child.** The next node is the first node of the right subtree. Only walks **down**.

**Case 2: A has no right child.** Everything after A is above it. Walk up while A is a **right** child. The first time A is a left child, its parent comes right after A. Only walks **up**.

### Examples on the tree above

```
successor(D): D has right child F → subtree_first(F) = E          → E
successor(C): C has no right child.
              C is the right child of B → A = B.
              B is the left child of D  → loop stops with A = B.
              Return A.parent = D.                              → D
successor(G): G is right child of F → A = F
              F is right child of D → A = D
              D has no parent → stop. Return D.parent = None → no successor
```

## Predecessor

Mirror image: swap left and right.

```python
def predecessor(A):                      # O(h)
    if A.left: return A.left.subtree_last()
    while A.parent and (A is A.parent.left):
        A = A.parent
    return A.parent
```

## Complexity

Case 1 only walks down, case 2 only walks up, each at most h steps → **O(h)**.

---

# 5. Dynamic Operations

We must change the tree **without changing the order of the other items**.

## Insert before a node

To insert B just before A in traversal order:

```python
def subtree_insert_before(A, B):         # O(h)
    if A.left:
        A = A.left.subtree_last()
        A.right, B.parent = B, A
    else:
        A.left, B.parent = B, A
```

- **A has no left child:** make B the left child of A.
- **A has a left child:** the node just before A is the last node of A's left subtree. That node has no right child, so make B its right child.

### Example: insert X before D

```
D has a left child B → last node of B's subtree = C (no right child)
X becomes the right child of C

        D
      /   \
     B     F
    / \   / \
   A   C E   G
        \
         X

traversal: A B C X D E F G   ✓
```

Insert **after** is the mirror image (use `right`, `subtree_first`, `left`).

Both walk down one path → **O(h)**.

## Delete

```python
def subtree_delete(A):                   # O(h)
    if A.left or A.right:                # A is not a leaf
        if A.left: B = A.predecessor()
        else:      B = A.successor()
        A.item, B.item = B.item, A.item  # swap items
        return B.subtree_delete()        # delete the other node
    if A.parent:                         # A is a leaf
        if A.parent.left is A: A.parent.left = None
        else:                  A.parent.right = None
    return A
```

- **A is a leaf:** cut it from its parent.
- **A is not a leaf:** swap its item with the item of its predecessor (or successor), which is **lower** in the tree, and delete that node instead. Repeat until the item sits in a leaf.

Why swapping is safe: the predecessor is the item right before A in traversal order. Swapping two neighbors' items and then removing the node that now holds the unwanted item keeps the order of all other items.

### Example: delete D (the root)

```
D has a left child → B = predecessor(D) = last of B's subtree = C
swap items: the root now holds C's item, the old C node holds D's item
the old C node is a leaf → cut it

        C
      /   \
     B     F
    /     / \
   A     E   G

traversal: A B C E F G   ✓  (D is gone)
```

**The returned node is the one that was cut**, and it holds the deleted item. It is not always the node you called delete on.

Each step goes down the tree → **O(h)**.

---

# 6. Top-Level Data Structure

The node operations work on any subtree. A tree object keeps a pointer to the root and the size.

```python
class Binary_Tree:
    def __init__(T, Node_Type = Binary_Node):
        T.root = None
        T.size = 0
        T.Node_Type = Node_Type

    def __len__(T): return T.size
    def __iter__(T):
        if T.root:
            for A in T.root.subtree_iter():
                yield A.item
```

`Node_Type` lets a subclass use a different kind of node (the BST uses `BST_Node`).

---

# 7. Exercises

## Exercise 1: Build a balanced tree from an array in O(n)

**Task:** from items (a₀, ..., aₙ₋₁), build a tree where (1) the i-th node in traversal order holds aᵢ, and (2) the height is O(log n).

**Idea:** put the **middle** item at the root, build the left half as the left subtree and the right half as the right subtree.

```python
def build_subtree(A, i, j):
    c = (i + j) // 2                         # middle index
    root = Node_Type(A[c])
    if i < c:                                # items left of c
        root.left = build_subtree(A, i, c - 1)
        root.left.parent = root
    if c < j:                                # items right of c
        root.right = build_subtree(A, c + 1, j)
        root.right.parent = root
    return root
```

### Example: A = [a0, a1, a2, a3, a4, a5, a6]

```
build(0, 6): c = 3 → root a3
  build(0, 2): c = 1 → a1
    build(0, 0): a0
    build(2, 2): a2
  build(4, 6): c = 5 → a5
    build(4, 4): a4
    build(6, 6): a6

          a3
        /    \
      a1      a5
     /  \    /  \
    a0  a2  a4  a6
```

Traversal order: a0 a1 a2 a3 a4 a5 a6 ✓.

**Height:** each level halves the number of items: H(n) = 1 + H(n/2) → H(n) = O(log n).

**Time:** each node is created once with O(1) work → O(n).

## Exercise 2: Iterate with successor in O(n)

```python
def tree_iter(T):
    node = T.subtree_first()
    while node:
        yield node
        node = node.successor()
```

One call to successor costs O(h), but the whole loop is only O(n), not O(n·h). The loop walks **every edge exactly twice**: once going down, once coming back up. A tree with n nodes has n − 1 edges → about 2(n − 1) steps in total → **O(n)**.

---

# 8. Application: Set (Binary Search Tree)

## Idea

Use the traversal order to store items **sorted by key**.

**Binary Search Tree property:**

```
keys in the left subtree  <  key at the node  <  keys in the right subtree
```

## Example

Insert 8, 3, 10, 1, 6, 14 one by one:

```
        8
      /   \
     3     10
    / \      \
   1   6      14

traversal: 1 3 6 8 10 14   (sorted ✓)
```

## find(k)

Compare k with the node's key and go left or right.

```python
def subtree_find(A, k):                  # O(h)
    if k < A.item.key:
        if A.left:  return A.left.subtree_find(k)
    elif k > A.item.key:
        if A.right: return A.right.subtree_find(k)
    else: return A
    return None
```

```
find(6): 6 < 8 → left (3);  6 > 3 → right (6);  found
find(7): 7 < 8 → left (3);  7 > 3 → right (6);  7 > 6 → no right child → None
```

## find_next(k): smallest key greater than k

```python
def subtree_find_next(A, k):             # O(h)
    if A.item.key <= k:
        if A.right: return A.right.subtree_find_next(k)
        else:       return None
    elif A.left:
        B = A.left.subtree_find_next(k)
        if B: return B
    return A
```

- If this node's key is **≤ k**, the answer must be in the right subtree.
- Otherwise this node is a **candidate**. Look for something smaller (but still > k) on the left. If nothing is there, this node is the answer.

```
find_next(6): at 8: 8 > 6, look left. At 3: 3 ≤ 6 → right. At 6: 6 ≤ 6 → no right child → None.
              Left search failed → answer = 8
find_next(8): at 8: 8 ≤ 8 → right. At 10: 10 > 8, no left child → answer = 10
```

`find_prev(k)` is the mirror image.

## insert(x)

Walk down to where x belongs, then insert before / after.

```python
def subtree_insert(A, B):                # O(h)
    if B.item.key < A.item.key:
        if A.left: A.left.subtree_insert(B)
        else:      A.subtree_insert_before(B)
    elif B.item.key > A.item.key:
        if A.right: A.right.subtree_insert(B)
        else:       A.subtree_insert_after(B)
    else: A.item = B.item                # same key: replace the item
```

If the key already exists, the item is replaced and `insert` returns False (the new node was never attached, so its parent is still None).

## delete(k)

Find the node with `subtree_find`, then call `subtree_delete`. The tree object also fixes `root` and `size`.

```
delete(3) in the example:
  3 has a left child → predecessor = 1
  swap items, cut the old leaf

        8
      /   \
     1     10
      \      \
       6      14

traversal: 1 6 8 10 14 ✓
```

## find_min / find_max

```python
def find_min(self):  return self.root.subtree_first().item     # O(h)
def find_max(self):  return self.root.subtree_last().item      # O(h)
```

## Building a Set

`build(X)` inserts the items one by one: n inserts × O(h) = **O(n·h)**.

---

# 9. Complexity Summary

h is the height of the tree.

| Structure | build | find | insert / delete | find_min/max | find_prev/next |
|---|---|---|---|---|---|
| Array | n | n | n | n | n |
| Sorted Array | n log n | log n | n | 1 | log n |
| Direct Access Array | u | 1 | 1 | u | u |
| Hash Table | n (e) | 1 (e) | 1 (a)(e) | n | n |
| Binary Search Tree | n·h | h | h | h | h |

The BST row is my summary of the operations above. With h = O(log n) every row entry is O(log n), better than a sorted array for insert / delete and better than a hash table for order operations.

## The catch: h can be n − 1

Insert 1, 2, 3, 4, 5 in this order:

```
1
 \
  2
   \
    3
     \
      4
       \
        5
```

Every key is bigger than the previous one, so it always goes right. The tree is a **chain**: h = n − 1 and every operation is O(n), as slow as a linked list.

Keeping h = O(log n) automatically is what the next lecture is about. (The code comments `# wait for R07!` mark where that will be added.)

---

# 10. Common Mistakes

## Mistake 1 — Saying BST operations are O(log n)

They are **O(h)**. They are O(log n) only if the tree is balanced.

## Mistake 2 — Treating the successor as "the right child"

Only when a right child exists is the successor in the right subtree (its first node, not the child itself). If there is no right child, walk **up** to the lowest ancestor whose **left** subtree contains the node.

## Mistake 3 — Forgetting the parent pointer

Inserting must set **both** the child pointer and `B.parent`. Without `parent`, successor, predecessor and delete break.

## Mistake 4 — Deleting an internal node by just unlinking it

That would lose or reorder its subtrees. Instead swap items down to a leaf, then cut the leaf.

## Mistake 5 — Using the node you called delete on

`subtree_delete` returns the node that was **actually removed**. Its item is the deleted item.

## Mistake 6 — Confusing traversal order with insertion order

Traversal order is the left-to-right order of the tree. A node inserted later can come first.

## Mistake 7 — Mixing up depth and height

- **Depth** of a node: how far **down** from the root.
- **Height** of a node: how far **down** the deepest node below it is.

## Mistake 8 — Expecting find_min to be O(1)

In a sorted array it is O(1). In a BST you walk down the left side: **O(h)**.

## Mistake 9 — Inserting sorted keys and expecting speed

Sorted input creates a chain. The recursive code can even hit Python's recursion limit for a few thousand nodes.

---

# 11. Lecture 6 Mental Map

```
                      LECTURE 6
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
   Binary Node        Operations         Application
 item, parent,            │                  │
 left, right    ┌─────────┼─────────┐    Set = Binary
        │       │         │         │    Search Tree
 Traversal    Navigation  Insert   Delete       │
  order       first/last  before/  swap down    │
 left, node,  successor/  after    to a leaf   find, find_next,
   right      predecessor   │         │        find_prev, insert,
        │         │         └────┬────┘        delete  → all O(h)
      O(n)      O(h)           O(h)               │
                                          h = O(log n) → fast
                                          h = n        → chain
```

## Core Takeaways

1. **A binary node has item, parent, left, right.**
   - Left subtree comes before the node, right subtree after it.

2. **Traversal order is the order of the whole structure.**
   - Listing it costs O(n).

3. **Every navigation and update operation walks one path.**
   - Cost: O(h).

4. **Insert adds a leaf next to the right neighbor; delete swaps down to a leaf.**
   - Both keep the order of the other items.

5. **A balanced tree can be built from an array in O(n).**
   - Middle item at the root, recurse on both halves.

6. **A Binary Search Tree stores the items in key order.**
   - find, find_next, find_prev, insert, delete: O(h).

7. **h is the whole story.**
   - h = O(log n): fast everything.
   - h = n − 1: no better than a linked list.

```
How tall is the tree?
Which operation walks up and which walks down?
Did I update both child and parent pointers?
Is the traversal order still correct?
```
