# Path Sum

> LeetCode 112 — Binary Tree / DFS / Recursion

## Problem

Given the root of a binary tree and an integer `targetSum`, determine whether the tree has a root-to-leaf path such that the sum of all values along that path equals `targetSum`.

A **leaf** is a node that has no left or right children.

Return `True` if such a path exists. Otherwise, return `False`.

### Example 1

```text
Input:
root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
targetSum = 22

Output: True
```

The tree looks like:

```text
          5
         / \
        4   8
       /   / \
     11   13  4
    /  \       \
   7    2       1
```

One valid root-to-leaf path is:

```text
5 → 4 → 11 → 2
```

The sum is:

```text
5 + 4 + 11 + 2 = 22
```

Therefore, we return:

```python
True
```

### Example 2

```text
Input:
root = [1,2,3]
targetSum = 5

Output: False
```

The tree looks like:

```text
    1
   / \
  2   3
```

The possible root-to-leaf paths are:

```text
1 → 2 = 3
1 → 3 = 4
```

Neither path adds up to `5`.

Therefore:

```python
False
```

### Example 3

```text
Input:
root = []
targetSum = 0

Output: False
```

An empty tree contains no root-to-leaf path.

Therefore, we return `False`.

---

## Approach — Recursive Depth-First Search (DFS)

The key idea is to recursively explore every possible path from the root to a leaf while keeping track of the remaining target sum.

Instead of calculating the entire path sum at every step, we subtract the current node's value from the target.

The solution uses:

```python
self.hasPathSum(root, targetSum)
```

At each node, we:

1. Check whether the current node exists.
2. Check whether the current node is a leaf.
3. Subtract the current node's value from `targetSum`.
4. Recursively search the left and right subtrees.
5. Return `True` if either subtree contains a valid path.

The main idea is:

```text
          Root
           |
    Subtract Root Value
           |
      ┌────┴────┐
      ↓         ↓
  Left Path  Right Path
      |         |
  Subtract   Subtract
   Values     Values
      |         |
      └────┬────┘
           ↓
     Reach a Leaf?
           ↓
   Check Remaining Sum
           ↓
    Return True / False
```

## Step 1 — Check if the Node Is Empty

```python
if not root:
    return False
```

If the current node is `None`, there is no path to explore.

Therefore, we return `False`.

This is the base case that stops the recursion.

For example:

```text
    5
   /
 None
```

When we attempt to visit the left child, we encounter `None`.

So we return:

```python
False
```

**Important:** An empty node cannot be considered a valid root-to-leaf path.

## Step 2 — Check if the Current Node Is a Leaf

```python
if not root.left and not root.right:
    return targetSum == root.val
```

A leaf is a node that has no left or right children.

This is the most important condition in the algorithm.

Why?

Because the problem specifically asks for a **root-to-leaf path**.

We cannot return `True` just because the remaining sum becomes zero at an internal node.

We must reach an actual leaf.

For example:

```text
      5
     / \
    4   8
```

Suppose:

```python
targetSum = 5
```

At node `5`, the remaining sum is zero after subtracting its value.

However, node `5` is not a leaf because it has children.

Therefore, we cannot return `True` yet.

We must continue exploring until we reach a leaf.

When we reach a leaf, we check:

```python
targetSum == root.val
```

If both values are equal, we have found a valid root-to-leaf path.

Otherwise, we return `False`.

## Step 3 — Subtract the Current Node's Value

```python
targetSum - root.val
```

Instead of continuously adding node values to a separate variable, we subtract each visited node's value from the remaining target.

For example:

```text
       5
      /
     4
    /
   11
  /
 2
```

Suppose:

```python
targetSum = 22
```

At the root:

```python
22 - 5 = 17
```

At node `4`:

```python
17 - 4 = 13
```

At node `11`:

```python
13 - 11 = 2
```

At the leaf `2`:

```python
2 == 2
```

We found a valid path.

The important idea is that we carry the remaining target sum into each recursive call.

## Step 4 — Recursively Search the Left and Right Subtrees

```python
return (
    self.hasPathSum(root.left, targetSum - root.val) or
    self.hasPathSum(root.right, targetSum - root.val)
)
```

After processing the current node, we recursively explore both subtrees.

We subtract the current node's value before moving to either child.

### Search the Left Subtree

```python
self.hasPathSum(root.left, targetSum - root.val)
```

This explores the left subtree using the updated remaining target.

For example:

```text
      5
     /
    4
   /
  11
```

If the target is `22`, the remaining sum after visiting node `5` becomes:

```text
22 - 5 = 17
```

We pass `17` to the left subtree.

### Search the Right Subtree

```python
self.hasPathSum(root.right, targetSum - root.val)
```

We also explore the right subtree using the same remaining target.

Why use `or`?

Because we only need one valid root-to-leaf path.

If either the left or right subtree contains a valid path, the entire expression returns `True`.

For example:

```text
       5
      / \
     4   8
    /     \
   11      4
```

If the left subtree contains a valid path, we do not need the right subtree to also contain one.

**Important:** Python's `or` uses short-circuit evaluation. If the left recursive call returns `True`, the right recursive call is not executed.

---

## Why Does This Work?

The key idea is that every root-to-leaf path can be evaluated by continuously subtracting the values of the nodes we visit from the target sum.

We handle three situations:

### Case 1 — Empty Node

```python
if not root:
    return False
```

If there is no node, there is no valid path.

### Case 2 — Leaf Node

```python
if not root.left and not root.right:
    return targetSum == root.val
```

If we reach a leaf, we check whether its value equals the remaining target.

If they match, we found a valid root-to-leaf path.

### Case 3 — Internal Node

```python
self.hasPathSum(root.left, targetSum - root.val) or
self.hasPathSum(root.right, targetSum - root.val)
```

If the current node is not a leaf, we continue exploring both subtrees with the reduced target.

The process looks like:

```text
          Current Node
                |
         Is Node Empty?
                |
          ┌─────┴─────┐
         Yes           No
          ↓             ↓
        False       Is it a Leaf?
                         |
                   ┌─────┴─────┐
                  Yes           No
                   ↓             ↓
             Check Remaining   Subtract
                  Sum          Node Value
                   ↓             ↓
              True/False     Explore Both
                              Subtrees
                                  |
                                  ↓
                            True if Either
                            Path Is Valid
```

---

## Example Walkthrough

Consider:

```python
root = [5,4,8,11,None,13,4,7,2,None,None,None,1]
targetSum = 22
```

The tree looks like:

```text
          5
         / \
        4   8
       /   / \
     11   13  4
    /  \       \
   7    2       1
```

Initially, we call:

```python
self.hasPathSum(root, 22)
```

### Step 1 — Visit Node 5

Node `5` is not a leaf.

We subtract its value:

```text
22 - 5 = 17
```

Now we explore its left and right subtrees using `17`.

### Step 2 — Visit Node 4

We move to the left child.

The remaining target becomes:

```text
17 - 4 = 13
```

Node `4` is not a leaf, so we continue exploring.

### Step 3 — Visit Node 11

We move to the left child of node `4`.

The remaining target becomes:

```text
13 - 11 = 2
```

Node `11` has two children, so we continue.

### Step 4 — Visit Node 7

We first explore the left child.

The remaining target is:

```text
2
```

Node `7` is a leaf.

We check:

```python
2 == 7
```

This is false.

Therefore, this path is not valid.

We return `False` and backtrack to node `11`.

### Step 5 — Visit Node 2

Now we explore the right child of node `11`.

The remaining target is still:

```text
2
```

Node `2` is a leaf.

We check:

```python
2 == 2
```

This is true.

We found a valid path:

```text
5 → 4 → 11 → 2
```

Its sum is:

```text
5 + 4 + 11 + 2 = 22
```

Therefore, the final result is:

```python
True
```

The algorithm stops exploring further because the left recursive call has already returned `True`.

---

## Complexity

### Time Complexity

**`O(n)`**

In the worst case, we may need to visit every node in the binary tree.

For each node, we perform constant-time operations:

- Check whether the node exists.
- Check whether it is a leaf.
- Subtract its value from the remaining target.
- Explore its children.

Therefore:

```text
O(n)
```

Where `n` is the total number of nodes in the tree.

The algorithm may finish earlier if it finds a valid path.

### Space Complexity

**`O(h)` auxiliary space**

The solution uses recursion.

Each recursive call remains on the call stack until its execution finishes.

The maximum recursion depth depends on the height of the tree.

For a balanced binary tree:

```text
O(log n)
```

For a completely unbalanced tree:

```text
O(n)
```

Therefore:

```text
Recursive Call Stack: O(h)

Balanced Tree:        O(log n)
Worst Case:           O(n)
```

The algorithm does not need an additional list to store the current path because it tracks the remaining sum directly.

---

## Comparison

| Approach | Time | Auxiliary Space | Main Idea |
|---|---|---|---|
| Recursive DFS | `O(n)` | `O(h)` | Explore root-to-leaf paths using recursion |
| Iterative DFS | `O(n)` | `O(n)` worst case | Use a stack to track nodes and remaining sums |
| BFS | `O(n)` | `O(w)` | Explore paths level by level |

Where:

- `h` is the height of the tree.
- `w` is the maximum width of the tree.

The solution in `solution.py` uses **Recursive DFS**.

---

## Key Insight

The main insight is:

> **Instead of calculating the sum of every path from scratch, subtract each visited node's value from the remaining target sum.**

The important pattern is:

```text
Start with Target Sum
         |
         ↓
   Visit Current Node
         |
         ↓
 Subtract Node Value
         |
         ↓
   Is It a Leaf?
         |
    ┌────┴────┐
   Yes        No
    ↓          ↓
Compare     Explore Left
Remaining   and Right
Sum          Subtrees
    ↓          ↓
True/False  Repeat
```

The most important detail is that we only check the remaining sum when we reach a leaf.

This ensures that we find a complete root-to-leaf path rather than a path that simply ends at an internal node.

---

## What I Learned

- How to determine whether a binary tree contains a root-to-leaf path with a given sum.
- How Depth-First Search explores different paths.
- How recursion naturally represents root-to-leaf traversal.
- Why an empty node returns `False`.
- Why we must check whether a node is a leaf.
- How subtracting node values tracks the remaining target sum.
- Why `or` allows us to stop once a valid path is found.
- How backtracking allows the algorithm to explore alternative paths.
- Why the time complexity is `O(n)`.
- How tree height determines recursive call stack space.

---

## Related Concepts

- Binary Trees
- Binary Tree Traversal
- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Recursion
- Root-to-Leaf Paths
- Path Sum
- Backtracking
- Tree Height
- Recursive Call Stack
- Time Complexity
- Space Complexity
