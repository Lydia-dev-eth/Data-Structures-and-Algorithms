# Reverse Linked List

## Problem

Given the head of a singly linked list, reverse the linked list and return the new head.

### Example

Input:

```text
1 → 2 → 3 → 4 → 5 → None
```

Output:

```text
5 → 4 → 3 → 2 → 1 → None
```

---

## Approach 1 — Recursion

My first approach was to use recursion.

The idea is to recursively move to the end of the linked list first. Once we reach the last node, we treat it as the new head of the reversed list.

For example:

```text
1 → 2 → 3 → None
```

The recursion goes:

```text
reverse(1)
    ↓
reverse(2)
    ↓
reverse(3)
```

When `3` is reached, it is returned as the new head.

Then, while the recursive calls return, the links are reversed.

For example, when `head` is `2`:

```python
head.next.next = head
```

This changes:

```text
2 → 3
```

into:

```text
2 ← 3
```

Then:

```python
head.next = None
```

removes the old connection from `2` to `3`.

The process continues until the entire list becomes:

```text
1 ← 2 ← 3
```

The new head is `3`.

### Complexity

* **Time:** O(n)
* **Space:** O(n) because of the recursive call stack

---

## Approach 2 — Iteration

The recursive solution works, but it uses O(n) extra space because every recursive call is stored on the call stack.

I then solved the problem iteratively using two variables:

* `x` — the current node
* `prev_x` — the previous node in the reversed portion

Initially:

```text
prev_x = None
x = 1
```

For:

```text
1 → 2 → 3 → None
```

First, I save the next node:

```python
x_next = x.next
```

This is important because the next step changes `x.next`.

Then I reverse the pointer:

```python
x.next = prev_x
```

The list now looks like:

```text
None ← 1    2 → 3
```

Then I move both variables forward:

```python
prev_x, x = x, x_next
```

Now:

```text
prev_x = 1
x = 2
```

The same process continues until `x` becomes `None`.

At that point:

```text
None ← 1 ← 2 ← 3
```

`prev_x` points to `3`, so it becomes the new head.

### Complexity

* **Time:** O(n)
* **Space:** O(1)

---

## Comparison

| Approach  | Time | Space | Main Idea                                               |
| --------- | ---: | ----: | ------------------------------------------------------- |
| Recursion | O(n) |  O(n) | Reach the end first, then reverse links while returning |
| Iteration | O(n) |  O(1) | Reverse each pointer while traversing                   |

The iterative approach is more space-efficient because it does not use the recursive call stack.

---

## Key Insight

The core of this problem is **changing the direction of the `next` pointers**.

The most important thing in the iterative solution is to save the next node **before** changing the current node's pointer:

```python
x_next = x.next
x.next = prev_x
```

If I changed `x.next` first without saving it, I could lose access to the remaining part of the list.

This problem also shows that the same algorithmic idea can often be implemented in different ways. Recursion and iteration both reverse the same pointers, but they manage the process differently.

---

## What I Learned

* How to reverse a singly linked list by changing `next` pointers.
* How recursion can be used to reverse a linked list.
* How to reverse a linked list iteratively using `prev` and `current` nodes.
* Why the next node must be saved before changing a pointer.
* The difference between recursive and iterative solutions.
* How recursion can use O(n) stack space while iteration can achieve O(1) extra space.
* How the same problem can have multiple correct approaches with different space requirements.

---

## Related Concepts

* Linked Lists
* Pointers / References
* Recursion
* Iteration
* Call Stack
* Time Complexity
* Space Complexity
* Pointer Manipulation
