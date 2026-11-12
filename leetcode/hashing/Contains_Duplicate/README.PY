# Contains Duplicate

## Problem

Given an integer array `nums`, determine whether any value appears at least twice.

Return:

- `True` if any element appears more than once.
- `False` if every element is unique.

### Example 1

**Input:**
```python
nums = [1, 2, 3, 1]
```

**Output:**
```python
True
```

The number `1` appears twice.

### Example 2

**Input:**
```python
nums = [1, 2, 3, 4]
```

**Output:**
```python
False
```

Every element appears exactly once.

### Example 3

**Input:**
```python
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
```

**Output:**
```python
True
```

Several numbers appear more than once.

---

## Approach — Hash Map (Tracking Previously Seen Elements)

We can solve this problem using a dictionary (hash map) to keep track of the numbers we have already encountered.

Instead of comparing every element with every other element, we store previously encountered numbers in a dictionary.

Before storing a new number, we check whether it already exists.

The key idea is:

**If a number already exists in our dictionary, we have found a duplicate.**

We use:

```python
store = {}
```

The dictionary stores:
- Key: A number from the array.
- Value: `True`, indicating that we have already encountered that number.

For example:

```python
nums = [1, 2, 3]
```

Our dictionary will eventually become:

```python
{
    1: True,
    2: True,
    3: True
}
```

---

## Step 1 — Create an Empty Dictionary

```python
store = {}
```

We create an empty dictionary to remember the numbers we have already visited.

Initially:

```python
store = {}
```

Whenever we encounter a new number, we add it to this dictionary.

Think of the dictionary as a checklist.

Every time we encounter a number, we check whether it is already on our checklist.

---

## Step 2 — Iterate Through the Array

```python
for i in range(len(nums)):
```

We use a loop to visit every index in the array.

For example:

```python
nums = [1, 2, 3, 1]
```

The loop visits these indices:

```python
0, 1, 2, 3
```

At each iteration, we access the corresponding number using:

```python
nums[i]
```

For example:

| i | nums[i] |
|---|---|
| 0 | 1 |
| 1 | 2 |
| 2 | 3 |
| 3 | 1 |

---

## Step 3 — Check Whether the Number Already Exists

```python
if nums[i] in store:
    return True
```

Before adding a number to the dictionary, we check whether it already exists.

The expression:

```python
nums[i] in store
```

checks whether the number exists as a key in the dictionary.

Consider:

```python
nums = [1, 2, 3, 1]
```

### First Iteration

```python
i = 0
nums[i] = 1
```

We check:

```python
1 in store
```

Our dictionary is empty:

```python
store = {}
```

Therefore, the condition is `False`.

We continue to the `else` block.

### Second Iteration

```python
i = 1
nums[i] = 2
```

We check:

```python
2 in store
```

Our dictionary currently contains:

```python
{
    1: True
}
```

Since `2` does not exist, the condition is `False`.

We continue.

### Fourth Iteration

```python
i = 3
nums[i] = 1
```

We check:

```python
1 in store
```

Our dictionary currently contains:

```python
{
    1: True,
    2: True,
    3: True
}
```

This time, the condition is `True`.

Why?

Because we encountered `1` before.

Therefore:

```python
return True
```

We immediately stop because we have found a duplicate.

---

## Step 4 — Store Numbers We Have Not Seen Before

```python
else:
    store[nums[i]] = True
```

If the number does not exist in our dictionary, we add it.

For example:

```python
nums[i] = 1
```

Since `1` does not exist in our dictionary:

```python
store[1] = True
```

Our dictionary becomes:

```python
{
    1: True
}
```

The value `True` simply indicates that we have already encountered this number.

We are not using the dictionary to count occurrences. We only need to remember whether a number has appeared before.

---

## Step 5 — Return False If No Duplicate Is Found

```python
return False
```

This statement executes only if the loop finishes without finding a duplicate.

Consider:

```python
nums = [1, 2, 3, 4]
```

After processing every element:

```python
store = {
    1: True,
    2: True,
    3: True,
    4: True
}
```

The loop finishes because no number appeared twice.

Therefore:

```python
return False
```

This means every element in the array is unique.

---

## Complete Code

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Determines whether an array contains any duplicate elements
        using a hash map to track previously seen numbers.
        """

        # Store numbers that have already been encountered.
        store = {}

        for i in range(len(nums)):

            # If the number already exists, a duplicate is found.
            if nums[i] in store:
                return True

            # Mark the number as seen.
            else:
                store[nums[i]] = True

        # No duplicate elements were found.
        return False


# Time Complexity: O(n) — iterate through the array once.
# Space Complexity: O(n) — hash map stores previously seen elements.
```

---

## Why Does This Work?

The algorithm works because a dictionary allows us to check whether a number has appeared before.

Instead of comparing every number with all the other numbers, we remember the numbers we have already encountered.

For every element, there are two possible situations:

**Case 1 — The number already exists in the dictionary.**

This means we have encountered it before.

Therefore, a duplicate exists, and we return `True`.

**Case 2 — The number does not exist in the dictionary.**

This means it is the first time we have encountered it.

We add it to the dictionary and continue.

If we finish processing the entire array without finding a duplicate, we return `False`.

---

## Example Walkthrough

Consider:

```python
nums = [1, 2, 3, 1]
```

Initially:

```python
store = {}
```

### First Iteration

```python
i = 0
nums[i] = 1
```

Check:

```python
1 in store
```

Result: `False`

Add:

```python
store[1] = True
```

Dictionary:

```python
{1: True}
```

### Second Iteration

```python
i = 1
nums[i] = 2
```

Check:

```python
2 in store
```

Result: `False`

Add:

```python
store[2] = True
```

Dictionary:

```python
{
    1: True,
    2: True
}
```

### Third Iteration

```python
i = 2
nums[i] = 3
```

Check:

```python
3 in store
```

Result: `False`

Add:

```python
store[3] = True
```

Dictionary:

```python
{
    1: True,
    2: True,
    3: True
}
```

### Fourth Iteration

```python
i = 3
nums[i] = 1
```

Check:

```python
1 in store
```

Result: `True`

Since `1` already exists, we immediately return:

```python
True
```

We do not need to process any remaining elements.

---

## Complexity

### Time Complexity

**O(n)**

Where `n` is the length of the array.

We iterate through the array at most once.

For every element, we perform:

1. A dictionary lookup.
2. A dictionary insertion if the element has not appeared before.

Dictionary lookups and insertions take O(1) time on average.

Therefore:

O(n × 1) = O(n)

In the worst case, we examine every element.

### Space Complexity

**O(n)**

We use a dictionary to store previously encountered numbers.

In the worst case, every element is unique.

For example:

```python
nums = [1, 2, 3, 4, 5]
```

Our dictionary stores all five elements.

Therefore, the maximum auxiliary space grows proportionally to the array size.

Space Complexity: **O(n)**

---

## Comparison

| Approach | Time | Space | Main Idea |
|---|---|---|---|
| Brute Force | O(n²) | O(1) | Compare every element with the others |
| Sorting | O(n log n) | Depends on sorting implementation | Sort and check neighboring elements |
| Hash Map | O(n) | O(n) | Remember previously encountered elements |

Our solution uses a hash map because it allows us to detect duplicates without repeatedly comparing elements.

---

## Key Insight

The main insight is:

**We don't need to count how many times a number appears. We only need to know whether we have seen it before.**

The important operations are:

```python
if nums[i] in store:
```

Check whether the number has already appeared.

```python
store[nums[i]] = True
```

Remember the number for future iterations.

```python
return True
```

Stop immediately when a duplicate is found.

```python
return False
```

Return false if the entire array has been processed without finding duplicates.

---

## What I Learned

- How to use a dictionary as a way to track previously encountered elements.
- How to check whether a dictionary contains a particular key using `in`.
- How to insert elements into a dictionary.
- How early returns can stop unnecessary iterations.
- Why we don't need to count frequencies when checking for duplicates.
- How hash maps help avoid nested loops.
- How to improve an algorithm from O(n²) to O(n) using extra space.
- How to analyze the time and space complexity of a hash map solution.

---

## Related Concepts

- Arrays
- Hash Maps
- Dictionaries
- Hash Sets
- Membership Checking
- Duplicate Detection
- Early Return
- Linear Search
- Time Complexity
- Space Complexity
