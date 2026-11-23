# Maximum Depth of Binary Tree

> LeetCode 104 — Binary Tree / DFS / Recursion

## Problem

Given the root of a binary tree, return its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

### Example 1

```text
Input:  root = [3,9,20,null,null,15,7]

Output: 3
```

The tree looks like:

```text
       3
      / \
     9   20
        /  \
       15   7
```

The longest path is:

```text
3 → 20 → 15
```

It contains 3 nodes.

Therefore, the maximum depth is:

```text
3
```

### Example 2

```text
Input:  root = [1,null,2]

Output: 2
```

The tree looks like:

```text
1
 \
  2
```

The longest path contains 2 nodes.

Therefore:

```text
2
```

### Example 3

```text
Input:  root = []

Output: 0
```

An empty tree has no nodes, so its maximum depth is `0`.

---

## Approach — Recursive Depth-First Search (DFS)

The key idea is to calculate the depth of the left and right subtrees recursively.

For every node, we:

1. Calculate the maximum depth of its left subtree.
2. Calculate the maximum depth of its right subtree.
3. Choose the larger depth.
4. Add `1` for the current node.

The solution uses the recursive function:

```python
self.maxDepth(root)
```

The main formula is:

```python
1 + max(left_depth, right_depth)
```

Why do we add `1`?

Because we must also count the current node.

The main idea is:

```text
          Root
           |
      ┌────┴────┐
      ↓         ↓
  Left Depth  Right Depth
      |         |
      └────┬────┘
           ↓
    Choose Maximum
           ↓
       Add 1
           ↓
    Return Max Depth
```

## Step 1 — Check if the Node Is Empty

```python
if not root:
    return 0
```

If the current node is `None`, there is no node to count.

Therefore, we return `0`.

This is the base case that stops the recursion.

For example:

```text
    1
   /
 None
```

When we try to visit the left child of node `1`, we encounter `None`.

So we return:

```python
0
```

Without this condition, the recursion would have no stopping point.

## Step 2 — Calculate the Left Subtree Depth

```python
left_depth = self.maxDepth(root.left)
```

We recursively calculate the maximum depth of the left subtree.

For example:

```text
       1
      / \
     2   3
    /
   4
```

Starting at node `1`, we recursively explore its left child.

The left subtree looks like:

```text
    2
   /
  4
```

Its maximum depth is:

```text
2
```

So:

```python
left_depth = 2
```

The recursive call calculates this value automatically.

## Step 3 — Calculate the Right Subtree Depth

```python
right_depth = self.maxDepth(root.right)
```

Similarly, we recursively calculate the maximum depth of the right subtree.

For example:

```text
       1
      / \
     2   3
        /
       5
```

The right subtree looks like:

```text
    3
   /
  5
```

Its maximum depth is:

```text
2
```

So:

```python
right_depth = 2
```

Now we have the depths of both subtrees.

## Step 4 — Choose the Larger Depth and Add 1

```python
return 1 + max(left_depth, right_depth)
```

This is the most important part of the algorithm.

We use:

```python
max(left_depth, right_depth)
```

because we need the longest path, not the shortest one.

Then we add `1` to count
