# Lecture 6 — Binary Trees

This folder contains notes and implementations from MIT 6.006 Lecture 6 / Recitation 6, focusing on binary trees, their traversal order, and how to use one as a Set (a Binary Search Tree).

## What This Covers

- **Binary Trees** — nodes with an item, a parent, a left child and a right child.
- **Traversal Order** — left subtree, then the node, then right subtree.
- **Tree Navigation** — first, last, successor, predecessor.
- **Dynamic Operations** — insert before / after a node, delete a node.
- **Top-Level Data Structure** — a tree that stores its root and size.
- **Application: Set** — Binary Search Tree with find, find_next, find_prev, insert, delete.
- **Exercises** — building a balanced tree, and iterating with successor.

## Files

| File | What it contains |
|---|---|
| `notes.md` | Full notes, intuition, examples, complexity, common mistakes |
| `binary_node.py` | Binary_Node: traversal, navigation, insert, delete |
| `binary_tree.py` | Binary_Tree: root, size, iteration, balanced build |
| `set_binary_tree.py` | BST_Node and Set_Binary_Tree (Binary Search Tree) |
| `tree_exercises.py` | Iterative traversal with successor, height helper |
| `README.md` | Overview of this folder |

## Key Ideas

### 1. Binary Tree

Each node stores:

```
item     the stored item
parent   the node above (None for the root)
left     left child  (or None)
right    right child (or None)
```

- **Root**: the only node without a parent.
- **Depth** of a node: path length from the root to it.
- **Height** of a node: the largest depth in its subtree.
- **Leaf**: a node with no children.

A linked list can have nodes n hops from the head. A binary tree can have every node within O(log n) hops of the root.

### 2. Traversal Order

```
every node in the left subtree  comes BEFORE the node
every node in the right subtree comes AFTER the node
```

Listing it: left subtree, the node, right subtree. This takes O(n).

### 3. Navigation and Dynamic Operations

```
subtree_first / subtree_last     walk left / right      O(h)
successor / predecessor          walk down or up        O(h)
subtree_insert_before / after    walk down, add a leaf  O(h)
subtree_delete                   swap down to a leaf    O(h)
```

All of them keep the traversal order of the other items.

### 4. Binary Search Tree (Set)

Store items so that traversal order = increasing key order.

```
left subtree keys  <  node key  <  right subtree keys
```

Then find, find_next, find_prev, insert and delete all walk one path down the tree: **O(h)**.

## Complexity at a Glance

| Operation | Time |
|---|---|
| subtree_iter / iterate whole tree | O(n) |
| first, last, successor, predecessor | O(h) |
| insert before / after, delete | O(h) |
| find, find_next, find_prev | O(h) |
| find_min, find_max | O(h) |
| build balanced tree from an array | O(n) |
| build BST by n inserts | O(n h) |

If h = O(log n), every operation is O(log n). In the worst case (a chain) h = n − 1.

## Key Takeaway

> A binary tree turns "how far is this node from the start?" from O(n) (linked list) into O(h). The traversal order gives an ordered Set, and every operation costs the height of the tree.

Next step: keep h = O(log n) automatically (balancing), because plain insertion can build a chain.

See `notes.md` for the detailed concepts and the Python files for implementations.
