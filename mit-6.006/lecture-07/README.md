# Lecture 7 — Balanced Binary Trees (AVL)

This folder contains notes and implementations from MIT 6.006 Lecture 7 / Recitation 7, focusing on keeping a binary tree balanced with AVL balancing, and using it as a Set and as a Sequence.

## What This Covers

- **Balanced Binary Trees** — a tree on n nodes is balanced if its height is O(log n).
- **AVL Property** — the left and right subtrees of every node differ in height by at most 1.
- **Rotations** — O(1) local changes that keep the traversal order.
- **Maintaining Height-Balance** — rebalance every ancestor of a changed leaf.
- **Augmentation** — storing subtree height (and later size) at each node.
- **Application: Set** — Set AVL.
- **Application: Sequence** — Sequence AVL with subtree sizes.
- **Exercises** — the Sequence AVL example, and counting ones in a bit sequence.

## Files

| File | What it contains |
|---|---|
| `notes.md` | Full notes, intuition, examples, complexity, common mistakes |
| `avl_node.py` | Binary_Node with AVL balancing (heights, rotations, maintain) |
| `seq_avl.py` | Size_Node and Seq_Binary_Tree (Sequence AVL) |
| `set_avl.py` | Set AVL (the Recitation 6 Set on the AVL node) |
| `bit_sequence.py` | Exercise: counting ones in a bit sequence |
| `README.md` | Overview of this folder |

## Key Ideas

### 1. Height-Balance

```
skew(A) = height(A.right) − height(A.left)      (empty subtree has height −1)
node is height-balanced  ⟺  skew ∈ {−1, 0, 1}
tree is height-balanced  ⟺  every node is height-balanced
```

Height-balanced ⇒ balanced:

```
F(h) = fewest nodes in a height-balanced tree of height h
F(h) = 1 + F(h−1) + F(h−2) ≥ 2·F(h−2)   ⇒   F(h) ≥ 2^(h/2)   ⇒   h = O(log n)
```

### 2. Rotations

```
        D                          B
       / \    rotate_right(D)     / \
      B   E   ───────────────►   A   D
     / \      ◄───────────────      / \
    A   C     rotate_left(B)       C   E
```

O(1) time, and the traversal order A B C D E does not change.

### 3. Maintaining Height-Balance

After adding or removing a leaf, only the ancestors of that leaf can change skew, and only up to magnitude 2. Walk from the leaf to the root and rebalance each node (at most two rotations).

```
rebalance(A):  skew 2:  if right child skew < 0: rotate_right(right child);  rotate_left(A)
               skew −2: if left child skew > 0:  rotate_left(left child);    rotate_right(A)
maintain(A):   rebalance(A); update A's height; continue with A's parent
```

### 4. Augmentation

Computing a height by recursion costs Ω(n). Instead every node stores its own subtree height and recomputes it from its children in O(1).

To augment nodes with a property P(X), (1) define P(X) for X's subtree and (2) show how to compute it in O(1) from the children's augmentations.

### 5. Set AVL and Sequence AVL

- **Set AVL:** the Recitation 6 Set on the AVL node. All operations O(log n), except build O(n log n).
- **Sequence AVL:** traversal order = sequence order. Each node also stores its subtree **size**, so the i-th node is found in O(log n).

## Complexity at a Glance

| Operation | Time |
|---|---|
| skew, subtree_update, rotation, rebalance | O(1) |
| maintain | O(log n) |
| first, last, successor, predecessor | O(log n) |
| insert before / after, delete | O(log n) |
| Set AVL operations | O(log n) |
| Set AVL build(X) | O(n log n) |
| Sequence AVL build(X) | O(n) |
| subtree_at(i) | O(h) = O(log n) |
| iteration | O(n) |

## Key Takeaway

> Storing each node's height lets us check balance in O(1), and a few rotations along the path to the root keep every operation at O(log n).

The same augmentation idea (subtree size, number of ones) gives new fast operations without breaking the O(log n) bounds.

See `notes.md` for the detailed concepts and the Python files for implementations.
