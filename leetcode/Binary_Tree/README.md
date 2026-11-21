# Binary Tree Inorder Traversal

> LeetCode 94 — Binary Tree / DFS / Recursion

## Problem

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Inorder traversal visits the nodes in this order:

1. Left subtree
2. Root node
3. Right subtree

### Example 1

```text
Input: root = [1,null,2,3]

Output: [1,3,2]
```

The tree looks like:

```text
    1
     \
      2
     /
    3
```

The traversal process is:

```text
Visit 1
    ↓
Visit left subtree (empty)
    ↓
Visit right subtree
    ↓
Visit 2
    ↓
Visit left subtree
    ↓
Visit 3
```

Result:

```text
[1,3,2]
```

### Example 2

```text
Input: root = []

Output: []
```

An empty tree contains no nodes, so the result is an empty list.

### Example 3

```text
Input: root = [1]

Output: [1]
```

There is only one node, so we return its value.

---

## Approach — Recursive Depth-First Search (DFS)

The key idea is to recursively traverse the binary tree using the inorder traversal order:

```text
Left → Root → Right
```

Instead of manually moving between nodes, we use recursion to explore each subtree.

The solution uses:

```python
order(root)
```

This helper function recursively visits the left subtree, processes the current node, and then visits the right subtree.

We also initialize:

```python
result = []
```

This list stores the values in inorder traversal order.

The main idea is:

```text
       Root
        |
   Visit Left
        |
   Visit Root
        |
  Visit Right
        |
   Return Result
```

## Step 1 — Initialize the Result List

```python
result = []
```

We create an empty list to store the values of the nodes as we visit them.

For example:

```text
result = []
```

As we traverse the tree, we append each node's value to this list.

## Step 2 — Check if the Node Is Empty

```python
if not root:
    return
```

If the current node is `None`, there is nothing to visit.

We simply return.

This is the base case that stops the recursion.

For example:

```text
    1
   /
 None
```

When we try to visit the left child of node `1`, we encounter `None`.

So the recursive call stops.

Without this condition, the recursion would have no stopping point.

## Step 3 — Visit the Left Subtree

```python
order(root.left)
```

We recursively visit the entire left subtree before processing the current node.

For example:

```text
       1
      / \
     2   3
    /
   4
```

Starting from node `1`, we first move to its left child:

```text
       1
      /
     2
    /
   4
```

We continue moving left until we reach a node with no left child.

The leftmost node is visited first.

For this tree:

```text
4
```

is the first value added to the result.

## Step 4 — Visit the Current Node

```python
result.append(root.val)
```

After completely visiting the left subtree, we process the current node.

We add its value to the result list.

For example:

```text
       1
      /
     2
    /
   4
```

After visiting node `4`, we return to node `2`.

Now we append:

```python
result.append(2)
```

The result becomes:

```python
[4,2]
```

This is why inorder traversal visits the root after its left subtree.

## Step 5 — Visit the Right Subtree

```python
order(root.right)
```

After processing the current node, we recursively visit its right subtree.

For example:

```text
       1
      / \
     2   3
    /
   4
```

After visiting `2`, we return to `1`.

We append `1`, then visit its right child `3`.

The result becomes:

```python
[4,2,1,3]
```

This completes the inorder traversal.

## Step 6 — Start Traversal From the Root

```python
order(root)
```

We call the helper function using the original root node.

This starts the recursive traversal of the entire tree.

After every node has been visited, the recursive calls finish.

Finally:

```python
return result
```

returns the inorder traversal.

---

## Why Does This Work?

The key property is the definition of inorder traversal:

**Left → Root → Right**

For every node, we follow the same three steps:

1. Recursively visit the left subtree.
2. Process the current node.
3. Recursively visit the right subtree.

Because each recursive call follows this exact order, every node is visited in the correct inorder sequence.

### Example

Consider:

```text
       1
      / \
     2   3
    / \
   4   5
```

The traversal follows:

```text
        1
       / \
      2   3
     / \
    4   5
```

First, visit the left subtree of `1`.

Inside node `2`, visit its left child:

```text
4
```

Then visit node `2`:

```text
2
```

Next, visit its right child:

```text
5
```

After completing the left subtree, visit node `1`:

```text
1
```

Finally, visit the right subtree:

```text
3
```

The final result is:

```python
[4,2,5,1,3]
```

---

## Example Walkthrough

Consider:

```text
root = [1,null,2,3]
```

The tree looks like:

```text
    1
     \
      2
     /
    3
```

Initially:

```python
result = []
```

### Step 1 — Start at Node 1

```python
order(root)
```

First, call:

```python
order(root.left)
```

Node `1` has no left child.

So we reach:

```python
if not root:
    return
```

The call returns to node `1`.

### Step 2 — Visit Node 1

```python
result.append(root.val)
```

The result becomes:

```python
[1]
```

### Step 3 — Visit the Right Subtree

```python
order(root.right)
```

We move to node `2`.

First, we visit its left child:

```text
    2
   /
  3
```

### Step 4 — Visit Node 3

Node `3` has no left child.

We append:

```python
result.append(3)
```

Now:

```python
result = [1,3]
```

Node `3` also has no right child, so the recursive call returns.

### Step 5 — Return to Node 2

After completing its left subtree, we visit node `2`.

```python
result.append(2)
```

Now:

```python
result = [1,3,2]
```

Node `2` has no right child, so the traversal finishes.

Final output:

```python
[1,3,2]
```

---

## Complexity

### Time Complexity

**`O(n)`**

Every node in the binary tree is visited exactly once.

For each node, we perform constant-time operations:

- Check whether the node exists.
- Visit its left child.
- Append its value.
- Visit its right child.

Therefore:

```text
O(n)
```

Where `n` is the total number of nodes in the tree.

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

The result list also stores all `n` node values:

```text
O(n)
```

Therefore:

```text
Recursive Call Stack: O(h)
Output Space:         O(n)

Worst-case Auxiliary Space: O(n)
```

---

## Comparison

| Approach | Time | Auxiliary Space | Main Idea |
|---|---|---|---|
| Recursive Inorder | `O(n)` | `O(h)` | Use recursion to visit Left → Root → Right |
| Iterative Inorder | `O(n)` | `O(h)` | Use an explicit stack |
| Morris Traversal | `O(n)` | `O(1)` | Temporarily modify tree pointers to traverse without a stack |

The solution in `solution.py` uses **Recursive Inorder Traversal**.

---

## Key Insight

The main insight is:

> **Inorder traversal visits the left subtree first, then the current node, and finally the right subtree.**

The important pattern is:

```text
       Root
        |
        ↓
   Left Subtree
        |
        ↓
    Visit Root
        |
        ↓
  Right Subtree
        |
        ↓
    Return Result
```

The recursive structure naturally represents this traversal order.

---

## What I Learned

- How binary trees are traversed using recursion.
- What Depth-First Search (DFS) means.
- How inorder traversal follows Left → Root → Right.
- How recursive function calls explore subtrees.
- Why a base case is necessary to stop recursion.
- How to use a result list to collect visited node values.
- Why every node is visited exactly once.
- How tree height determines recursive stack space.
- The difference between recursive, iterative, and Morris traversal.

---

## Related Concepts

- Binary Trees
- Binary Tree Traversal
- Depth-First Search (DFS)
- Inorder Traversal
- Preorder Traversal
- Postorder Traversal
- Recursion
- Tree Height
- Stack
- Divide and Conquer
- Time Complexity
- Space Complexity
- Recursive Call Stack
