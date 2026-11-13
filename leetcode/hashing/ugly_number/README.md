# LeetCode 263 — Ugly Number

## Problem

An **ugly number** is a positive integer whose prime factors are limited to `2`, `3`, and `5`.

In other words, a number is ugly if we can divide it repeatedly by `2`, `3`, or `5` until we eventually reach `1`.

Given an integer `n`, return `True` if it is an ugly number. Otherwise, return `False`.

### Examples

**Example 1:**
```python
Input: n = 6
Output: True
```
Explanation:

- 6 ÷ 2 = 3
- 3 ÷ 3 = 1

We reached `1`, so 6 is an ugly number.

**Example 2:**
```python
Input: n = 1
Output: True
```
Explanation:

1 is considered an ugly number because it has no prime factors outside the allowed set.

**Example 3:**
```python
Input: n = 14
Output: False
```
Explanation:

- 14 ÷ 2 = 7
- 7 cannot be divided evenly by 2, 3, or 5.

We are left with 7, which is not 1. Therefore, 14 is not an ugly number.

---

## Approach

We use **repeated division**.

The main idea is simple:

If a number is ugly, all its prime factors must be `2`, `3`, or `5`.

Therefore, we repeatedly remove these factors from the number by dividing it.

If the number eventually becomes `1`, it is ugly.

If we cannot divide it anymore and it is not `1`, it is not ugly.

---

## Step-by-Step Explanation

### Step 1: Handle zero

```python
if n == 0:
    return False
```

An ugly number must be positive.

Zero is not an ugly number, so we immediately return `False`.

### Step 2: Check the allowed factors

```python
for divider in [2, 3, 5]:
```

We iterate through the three numbers that are allowed to be prime factors:

- `2`
- `3`
- `5`

We check each one separately.

### Step 3: Divide repeatedly

```python
while n % divider == 0:
    n //= divider
```

This is the most important part.

Let's understand both lines.

**First:**
```python
n % divider == 0
```

The modulo operator `%` gives us the remainder after division.

If the remainder is zero, the number is divisible by `divider`.

For example:

```python
6 % 2 == 0
```

This is `True` because 6 is divisible by 2.

**Second:**
```python
n //= divider
```

This divides `n` by the current divider using integer division and updates `n`.

For example:

```python
n = 6
n //= 2
```

Now `n` becomes 3.

Why do we use a `while` loop instead of an `if` statement?

Because the same factor might appear multiple times.

For example, consider 12:

```text
12 ÷ 2 = 6
 6 ÷ 2 = 3
 3 ÷ 2 = not divisible
```

We must remove both factors of 2 before moving to the next divider.

### Step 4: Check the final number

```python
return n == 1
```

After removing every possible factor of 2, 3, and 5, we check what remains.

- If `n == 1`, all prime factors were allowed. Return `True`.
- Otherwise, an unallowed factor remains. Return `False`.

---

## Complete Code

```python
class Solution:
    def isUgly(self, n: int) -> bool:
        """
        Determines whether a number is ugly.

        An ugly number has only 2, 3, and 5 as its prime factors.
        """

        # Zero and negative numbers are not ugly numbers.
        if n == 0:
            return False

        # Try removing every allowed prime factor.
        for divider in [2, 3, 5]:

            # Keep dividing while the current factor divides n evenly.
            while n % divider == 0:
                n //= divider

        # If nothing remains except 1, the number is ugly.
        return n == 1


# Time Complexity: O(log n) — repeated division reduces n.
# Space Complexity: O(1) — only a constant amount of extra space is used.
```

---

## Why Does This Work?

Every positive integer greater than 1 can be represented as a product of prime numbers.

For example:

```text
30 = 2 × 3 × 5
```

All its prime factors belong to the allowed set, so it is ugly.

But:

```text
14 = 2 × 7
```

The factor 7 is not allowed.

Our algorithm removes every occurrence of 2, 3, and 5. If the remaining number is 1, there are no other prime factors.

That is why checking `n == 1` gives us the correct answer.

---

## Example Walkthrough

Let's trace the algorithm with:

```python
n = 30
```

Initially:

```text
n = 30
```

**First iteration: divider = 2**

```python
while 30 % 2 == 0:
    n //= 2
```

- 30 % 2 == 0 → True
- n becomes 30 // 2 = 15
- 15 % 2 == 0 → False

We move to the next divider.

**Second iteration: divider = 3**

```python
while 15 % 3 == 0:
    n //= 3
```

- 15 % 3 == 0 → True
- n becomes 15 // 3 = 5
- 5 % 3 == 0 → False

We move to the next divider.

**Third iteration: divider = 5**

```python
while 5 % 5 == 0:
    n //= 5
```

- 5 % 5 == 0 → True
- n becomes 5 // 5 = 1
- 1 % 5 == 0 → False

Now we finish the loop.

Finally:

```python
return n == 1
```

Since `n` is 1, we return:

```python
True
```

Therefore, 30 is an ugly number.

---

## Complexity Analysis

Let `n` be the original input.

### Time Complexity: O(log n)

Every successful division reduces the number.

For example, repeatedly dividing by 2 takes logarithmic time:

```text
n → n/2 → n/4 → n/8 → ...
```

The number of divisions is proportional to the logarithm of the original number.

We process only three possible dividers, so the overall time complexity is O(log n).

### Space Complexity: O(1)

We only use:

- The variable `n`.
- The variable `divider`.
- A fixed list containing 2, 3, and 5.

The extra space does not grow with the input size.

Therefore, space complexity is O(1).

---

## Comparison Table

| Approach | Time Complexity | Space Complexity |
|---|---|---|
| Repeated division | O(log n) | O(1) |
| Prime factorization | O(log n) | O(1) |

Repeated division is simple and efficient because we only need to check three possible factors.

---

## Key Insight

We do not need to calculate all the prime factors of a number.

Instead, we repeatedly remove the factors that are allowed.

If the final result is 1, the number is ugly.

**The key idea is to remove what is allowed and check whether anything remains.**

---

## What I Learned

1. The modulo operator `%` checks whether a number is divisible by another number.
2. Integer division `//` removes a factor while keeping the result an integer.
3. A `while` loop is useful when a factor can appear multiple times.
4. Prime factorization helps us understand why removing certain factors works.
5. We can solve the problem in O(log n) time and O(1) extra space.

---

## Related Concepts

- Prime numbers
- Prime factorization
- Modulo operator
- Integer division
- Repeated division
- Time and space complexity
