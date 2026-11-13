# Happy Number

## Problem

A happy number is a number defined by the following process:

1. Start with any positive integer.
2. Replace the number with the sum of the squares of its digits.
3. Repeat this process until the number becomes `1` or enters a cycle that never reaches `1`.

If the number eventually becomes `1`, it is a happy number.

Return `True` if `n` is a happy number, otherwise return `False`.

### Example 1

**Input:**
```python
n = 19
```

**Output:**
```python
True
```

Explanation:

We repeatedly calculate the sum of the squares of the digits.

```python
19
1² + 9² = 82

82
8² + 2² = 68

68
6² + 8² = 100

100
1² + 0² + 0² = 1
```

Since we eventually reach `1`, `19` is a happy number.

### Example 2

**Input:**
```python
n = 2
```

**Output:**
```python
False
```

Explanation:

```python
2
2² = 4

4
4² = 16

16
1² + 6² = 37

37
3² + 7² = 58

58
5² + 8² = 89

89
8² + 9² = 145

145
1² + 4² + 5² = 42

42
4² + 2² = 20

20
2² + 0² = 4
```

Notice something important:

We reached `4` again!

The sequence has entered a cycle:

```python
4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4
```

It will continue repeating these numbers forever.

Therefore, `2` is not a happy number.

---

## Approach — Floyd's Cycle Detection Algorithm (Slow and Fast Pointers)

We can solve this problem using Floyd's Cycle Detection Algorithm.

This algorithm is commonly used to detect cycles in linked lists.

However, we can also apply it to this problem because repeatedly transforming a number creates a sequence of numbers.

The key idea is:

**A number is happy if its sequence eventually reaches 1. Otherwise, it enters a cycle.**

Instead of storing every previously encountered number in a set, we use two pointers:

- `slow`: Moves one transformation at a time.
- `fast`: Moves two transformations at a time.

If the sequence contains a cycle, the fast pointer will eventually catch up with the slow pointer.

If the number is happy, the fast pointer eventually reaches `1`.

We use two variables:

```python
slow = n
fast = self.add_digits(n)
```

The function `add_digits()` calculates the sum of the squares of a number's digits.

---

## Step 1 — Understand the Transformation

Before understanding the pointers, we need to understand how we transform a number.

For example:

```python
n = 19
```

We calculate:

```python
1² + 9² = 82
```

The new number becomes:

```python
82
```

We repeat the same process:

```python
8² + 2² = 68
```

The new number becomes:

```python
68
```

Therefore, we can think of the transformation as a function:

```python
f(n) = sum of the squares of its digits
```

For example:

```python
f(19) = 82
f(82) = 68
f(68) = 100
f(100) = 1
```

This transformation creates a sequence.

For a happy number:

```python
19 → 82 → 68 → 100 → 1
```

For an unhappy number:

```python
2 → 4 → 16 → 37 → 58 → 89 → ...
```

Our goal is to determine whether this sequence reaches `1` or enters a cycle.

---

## Step 2 — Initialize Slow and Fast Pointers

```python
slow = n
fast = self.add_digits(n)
```

We initialize two pointers.

### Slow Pointer

```python
slow = n
```

The slow pointer starts at the original number.

For example:

```python
n = 19
```

Therefore:

```python
slow = 19
```

### Fast Pointer

```python
fast = self.add_digits(n)
```

The fast pointer starts one transformation ahead.

Since:

```python
self.add_digits(19) = 82
```

We have:

```python
fast = 82
```

Our initial positions are:

```python
slow = 19
fast = 82
```

Why do we initialize them differently?

Because we want the fast pointer to move through the sequence twice as quickly as the slow pointer.

This is the same principle used in Floyd's Cycle Detection Algorithm.

---

## Step 3 — Check Whether We Have Reached 1 or Detected a Cycle

```python
while fast != 1 and slow != fast:
```

This condition allows the algorithm to continue while two things are true:

1. The fast pointer has not reached `1`.
2. The slow and fast pointers have not met.

There are two possible situations.

### Case 1 — The Fast Pointer Reaches 1

```python
fast == 1
```

This means the sequence has reached `1`.

Therefore, we have found a happy number.

We stop the loop.

### Case 2 — The Slow and Fast Pointers Become Equal

```python
slow == fast
```

This means both pointers have reached the same number.

If the sequence has not reached `1`, this indicates that we have detected a cycle.

We stop the loop because continuing would repeat the same sequence forever.

---

## Step 4 — Move the Slow Pointer One Step

```python
slow = self.add_digits(slow)
```

The slow pointer moves forward by one transformation.

For example:

```python
slow = 19
```

We calculate:

```python
self.add_digits(19) = 82
```

Therefore:

```python
slow = 82
```

The slow pointer moves one position forward in the sequence.

---

## Step 5 — Move the Fast Pointer Two Steps

```python
fast = self.add_digits(self.add_digits(fast))
```

This is the most important part of Floyd's Cycle Detection Algorithm.

The fast pointer moves two transformations at once.

Let's break it down.

Suppose:

```python
fast = 82
```

First, the inner function executes:

```python
self.add_digits(82)
```

This produces:

```python
68
```

Then the outer function executes:

```python
self.add_digits(68)
```

This produces:

```python
100
```

Therefore:

```python
fast = 100
```

The fast pointer moved two positions:

```python
82 → 68 → 100
```

Meanwhile, the slow pointer moved only one:

```python
19 → 82
```

This difference in speed is what allows us to detect cycles.

---

## Step 6 — Return Whether the Fast Pointer Reached 1

```python
return fast == 1
```

After the loop finishes, we check whether the fast pointer reached `1`.

If:

```python
fast == 1
```

We return:

```python
True
```

Otherwise, the pointers met because the sequence entered a cycle.

We return:

```python
False
```

---

## Step 7 — Understand the add_digits() Function

```python
def add_digits(self, n):
    added = 0

    while n != 0:
        added += (n % 10) ** 2
        n = n // 10

    return added
```

This helper function calculates the sum of the squares of a number's digits.

Let's understand how it works.

Consider:

```python
n = 19
```

We need to calculate:

```python
1² + 9²
```

### Initialize the Result

```python
added = 0
```

We create a variable to store the sum.

Initially:

```python
added = 0
```

### Extract the Last Digit

```python
n % 10
```

The modulo operator `%` gives us the remainder.

For example:

```python
19 % 10 = 9
```

Therefore, we extract the last digit.

### Square the Digit

```python
(n % 10) ** 2
```

Since the last digit is `9`:

```python
9 ** 2 = 81
```

We add it to our result:

```python
added += 81
```

Now:

```python
added = 81
```

### Remove the Last Digit

```python
n = n // 10
```

Integer division removes the last digit.

For example:

```python
19 // 10 = 1
```

Now:

```python
n = 1
```

The loop continues.

### Process the Remaining Digit

Now:

```python
1 % 10 = 1
```

Square it:

```python
1 ** 2 = 1
```

Add it:

```python
added = 81 + 1
```

Now:

```python
added = 82
```

Remove the last digit:

```python
1 // 10 = 0
```

The loop stops because:

```python
n == 0
```

Finally:

```python
return added
```

Returns:

```python
82
```

Therefore:

```python
add_digits(19) = 82
```

---
