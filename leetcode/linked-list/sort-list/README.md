# Sort List

## Problem

Given the head of a linked list, return the list sorted in ascending order.

The goal is to sort the linked list efficiently, with a time complexity of **O(n log n)**.

### Examples

**Example 1**

```text
Input: head = [4, 2, 1, 3]
Output: [1, 2, 3, 4]
```

Explanation: The nodes are rearranged into ascending order.

**Example 2**

```text
Input: head = [-1, 5, 3, 4, 0]
Output: [-1, 0, 3, 4, 5]
```

Explanation: The linked list is sorted from the smallest value to the largest.

**Example 3**

```text
Input: head = []
Output: []
```

Explanation: An empty linked list is already sorted.

---

## Approach — Merge Sort

This solution uses **merge sort**, a divide-and-conquer algorithm.

Instead of sorting the entire linked list at once, we:

1. Find the middle of the linked list.
2. Split the list into two halves.
3. Recursively sort each half.
4. Merge the two sorted halves.

We repeat these steps until every sublist contains only one node.

A single node is already sorted, so we can then merge the smaller sorted lists into larger sorted lists until the entire linked list is sorted.

### Step 1: Handle the base case

```python
if not head or not head.next:
    return head
```

Before sorting, we check whether the linked list is empty or contains only one node.

There are two cases:

**Case 1: Empty list**

```text
head = None
```

There are no nodes to sort, so we return `head`.

**Case 2: One node**

```text
head → 5 → None
```

A list containing one node is already sorted.

We return `head` without making any recursive calls.

**Why is this important?**

Merge sort repeatedly divides a list into smaller lists. Eventually, every sublist must contain one node.

Without a base case, the recursion would never stop.

---

### Step 2: Find the middle of the linked list

```python
slow = head
fast = head.next

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

We use two pointers:

* `slow` moves one node at a time.
* `fast` moves two nodes at a time.

Because `fast` moves twice as quickly as `slow`, when `fast` reaches the end, `slow` is positioned near the middle.

For example:

```text
4 → 2 → 1 → 3 → None
```

Initially:

```text
slow
 ↓
 4 → 2 → 1 → 3 → None
 ↑
fast
```

After the first iteration:

```text
slow
 ↓
 4 → 2 → 1 → 3 → None
      ↑
     fast
```

After the next iteration, `fast` reaches the end of the list, and `slow` points to the node containing `1`.

```text
4 → 2 → 1 → 3 → None
         ↑
        slow
```

We have found the node just before the start of the second half.

**Why initialize `fast = head.next` instead of `fast = head`?**

This initialization helps `slow` stop at the node before the second half, including when the list contains an even number of nodes.

That makes it straightforward to split the list using `slow.next`.

---

### Step 3: Split the linked list into two halves

```python
mid = slow.next
slow.next = None
```

Once we find the middle, we separate the list into two independent linked lists.

Consider:

```text
4 → 2 → 1 → 3 → None
```

After finding `slow`:

```text
4 → 2 → 1 → 3 → None
         ↑
        slow
```

First:

```python
mid = slow.next
```

`mid` points to the node containing `3`.

Then:

```python
slow.next = None
```

We disconnect the first half from the second half.

The result is:

```text
Left half:   4 → 2 → None

Right half:  1 → 3 → None
```

**Why do we set `slow.next = None`?**

Without this step, the two halves would remain connected.

The recursive call on the left side could continue receiving the original list instead of a smaller list, preventing the algorithm from making progress.

Setting `slow.next = None` creates two separate lists that can be sorted independently.

---

### Step 4: Recursively sort both halves

```python
left = self.sortList(head)
right = self.sortList(mid)
```

Now that the list is divided, we recursively sort each half.

For example:

```text
Original list:
4 → 2 → 1 → 3
```

After splitting:

```text
Left:  4 → 2

Right: 1 → 3
```

We sort each half using the same `sortList()` method.

The process continues until every sublist contains one node.

Conceptually:

```text
             4 → 2 → 1 → 3
               /         \
           4 → 2         1 → 3
           /   \         /   \
          4     2       1     3
```

Each individual node is already sorted.

Now we can begin merging.

The left half becomes:

```text
2 → 4
```

The right half becomes:

```text
1 → 3
```

Both halves are now sorted, but we still need to combine them into one sorted list.

---

### Step 5: Merge the two sorted halves

```python
return self.merge(left, right)
```

After recursively sorting both halves, we pass them to the `merge()` method.

The merge method compares the nodes from the two sorted lists and connects them in ascending order.

Let's examine how it works.

#### 5.1 Create a dummy node

```python
dummy = ListNode()
tail = dummy
```

We create a temporary dummy node and use `tail` to track the last node in the merged list.

Initially:

```text
dummy → None
  ↑
 tail
```

**Why use a dummy node?**

Without a dummy node, we would need special handling for the first node added to the merged list.

The dummy node provides a fixed starting point, making it easier to attach nodes consistently.

At the end, we return `dummy.next`, which points to the actual first node of the merged list.

#### 5.2 Compare the nodes

```python
while left and right:
    if left.val < right.val:
        tail.next = left
        left = left.next
    else:
        tail.next = right
        right = right.next

    tail = tail.next
```

As long as both lists contain nodes, we compare their current values.

We attach the smaller node to the merged list and advance the pointer for the list from which that node came.

For example:

```text
Left:  2 → 4
Right: 1 → 3
```

**First comparison:**

```text
left.val  = 2
right.val = 1
```

Since `1` is smaller, we attach the node containing `1`.

```text
Merged: 1
Left:   2 → 4
Right:  3
```

**Second comparison:**

```text
left.val  = 2
right.val = 3
```

Since `2` is smaller, we attach it.

```text
Merged: 1 → 2
Left:   4
Right:  3
```

**Third comparison:**

```text
left.val  = 4
right.val = 3
```

Since `3` is smaller, we attach it.

```text
Merged: 1 → 2 → 3
Left:   4
Right:  None
```

Now the right list is empty, so the loop ends.

#### 5.3 Attach the remaining nodes

```python
tail.next = left if left else right
```

When the loop finishes, at least one list is empty.

Any remaining nodes in the other list can be attached directly because that list is already sorted.

In our example:

```text
Merged:   1 → 2 → 3
Remaining: 4
```

We connect the remaining node:

```text
1 → 2 → 3 → 4 → None
```

Finally:

```python
return dummy.next
```

We return the head of the sorted linked list, skipping the temporary dummy node.

---

## Step-by-Step Walkthrough

Let's trace the complete algorithm using:

```text
head = 4 → 2 → 1 → 3 → None
```

### Phase 1: Divide the list

The first split produces:

```text
Left:  4 → 2
Right: 1 → 3
```

We recursively sort both halves.

The left half is split again:

```text
4
2
```

Both single-node lists are already sorted.

They are merged into:

```text
2 → 4
```

The right half is split:

```text
1
3
```

These single-node lists are merged into:

```text
1 → 3
```

At this point, we have two sorted lists:

```text
Left:  2 → 4
Right: 1 → 3
```

### Phase 2: Merge the sorted halves

Compare the first nodes:

```text
2 and 1
```

Choose `1`.

```text
Merged: 1
```

Compare:

```text
2 and 3
```

Choose `2`.

```text
Merged: 1 → 2
```

Compare:

```text
4 and 3
```

Choose `3`.

```text
Merged: 1 → 2 → 3
```

The right list is now empty, so attach the remaining `4`.

```text
Merged: 1 → 2 → 3 → 4
```

### Final result

```text
Input:  4 → 2 → 1 → 3 → None

Output: 1 → 2 → 3 → 4 → None
```

The linked list is now sorted in ascending order.

---

## Why Does This Work?

Merge sort works because it breaks a difficult problem into smaller problems that are easier to solve.

There are three important reasons this algorithm works.

### 1. Every list eventually becomes small enough to sort

Each recursive call divides the list into two smaller parts.

This continues until each part contains one node or is empty.

A list with one node is already sorted, which gives us the base case.

### 2. Merging two sorted lists produces another sorted list

Suppose we have:

```text
Left:  2 → 4 → 7
Right: 1 → 3 → 6
```

Both lists are sorted.

At every step, the smaller of the two front nodes is the smallest value among all remaining nodes.

Therefore, selecting that node and advancing its pointer preserves ascending order.

When one list becomes empty, the remaining nodes in the other list are already sorted and can be attached directly.

### 3. The sorted result contains all the original nodes

The algorithm rearranges the existing nodes by changing their `next` pointers.

It does not need to create a new node for every value.

Each half is sorted recursively, and the merge operation connects those nodes into the final sorted list.

Therefore, the final list contains the original values in ascending order.

---

## Complexity

### Time Complexity: O(n log n)

Let `n` be the number of nodes in the linked list.

**Dividing the list:**

Finding the middle requires traversing part or all of the current list, taking O(n) time at the top level.

**Merging the list:**

Merging two sorted lists takes linear time relative to the total number of nodes being merged.

At each level of recursion, the total work across all sublists is O(n).

The list is divided approximately in half at each level, producing O(log n) levels.

Therefore:

```text
O(n) work per level × O(log n) levels
= O(n log n)
```

**Overall time complexity: O(n log n)**

### Space Complexity: O(log n)

The recursive calls create a call stack.

Because the list is divided approximately in half at each step, the maximum recursion depth is O(log n).

The `merge()` method uses a dummy node and a few pointers. It reuses the existing linked-list nodes rather than creating separate lists of copied values.

Therefore, the auxiliary space complexity is:

**O(log n)** for the recursive call stack.

---

## Comparison

| Approach                       | Time Complexity | Auxiliary Space                           | Explanation                                                                      |
| ------------------------------ | --------------- | ----------------------------------------- | -------------------------------------------------------------------------------- |
| Bubble Sort                    | O(n²)           | O(1)                                      | Repeatedly compares and swaps values or nodes; inefficient for large lists.      |
| Convert to Array and Sort      | O(n log n)      | O(n) or more, depending on implementation | Copies values or references into an array, sorts them, and may rebuild the list. |
| Merge Sort — this solution     | O(n log n)      | O(log n)                                  | Splits the linked list and merges sorted halves using recursion.                 |
| Iterative Bottom-Up Merge Sort | O(n log n)      | O(1) auxiliary space                      | Merges progressively larger runs without recursive calls.                        |

### Why is merge sort suitable for linked lists?

Linked lists do not provide constant-time access to an element by index.

Unlike arrays, we cannot directly jump to the middle of a linked list.

However, merge sort works well because it can find the middle using slow and fast pointers and merge lists by changing their `next` pointers.

It also achieves O(n log n) time, unlike simple quadratic sorting algorithms.

One detail worth remembering: this particular implementation is **recursive merge sort**, so it uses O(log n) stack space. An iterative bottom-up merge sort can achieve O(1) auxiliary space.

---

## Key Insight

**Merge sort solves the problem by dividing the linked list until each part is trivially sorted, then merging those parts back together in order.**

The most important operations in your implementation are:

```python
mid = slow.next
slow.next = None
```

These lines split the list into two independent halves.

Then:

```python
left = self.sortList(head)
right = self.sortList(mid)
```

These calls recursively sort the halves.

Finally:

```python
return self.merge(left, right)
```

This combines the sorted halves into a single sorted list.

The overall pattern is:

```text
Divide → Sort each half → Merge
```

This is the divide-and-conquer strategy.

---

## What I Learned

* How merge sort applies to linked lists.
* How slow and fast pointers can find the middle of a linked list without knowing its length in advance.
* Why setting `slow.next = None` is necessary to split a linked list.
* How recursion breaks a large sorting problem into smaller problems.
* How to merge two sorted linked lists by comparing their front nodes.
* Why a dummy node simplifies linked-list construction.
* How merge sort achieves O(n log n) time complexity.
* Why recursive merge sort uses O(log n) auxiliary space for the call stack.
* How linked lists can be sorted efficiently by rearranging pointers instead of copying all values into an array.

---

## Related Concepts

* Merge Sort
* Divide and Conquer
* Recursion
* Linked Lists
* Slow and Fast Pointers
* Merging Sorted Lists
* Dummy Nodes
* Time and Space Complexity
