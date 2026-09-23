# Product of Array Except Self

## Problem

Given an integer array `nums`, return an array `answer` such that:

```text
answer[i] = product of every element in nums except nums[i]
```

The solution must run in **O(n)** time and should not use division.

### Example

Input:

```text
nums = [1, 2, 3, 4]
```

Output:

```text
[24, 12, 8, 6]
```

Because:

```text
answer[0] = 2 × 3 × 4 = 24
answer[1] = 1 × 3 × 4 = 12
answer[2] = 1 × 2 × 4 = 8
answer[3] = 1 × 2 × 3 = 6
```

---

## Approach — Prefix and Suffix Products

For every position `i`, we need:

```text
product of everything to the LEFT
×
product of everything to the RIGHT
```

So instead of calculating the product for every position separately, I calculate these two parts efficiently.

```text
answer[i]
=
prefix product × suffix product
```

---

## Step 1 — Build the Prefix Products

I first create the output array:

```python
product_list = [1] * len(nums)
```

Then I traverse from left to right using `prefix`.

```python
prefix = 1
```

At each index, `prefix` represents the product of all elements **before** that index.

For:

```text
nums = [1, 2, 3, 4]
```

the prefix values are:

```text
index 0 → 1
index 1 → 1
index 2 → 1 × 2 = 2
index 3 → 1 × 2 × 3 = 6
```

So after the first pass:

```text
product_list = [1, 1, 2, 6]
```

The important part is:

```python
product_list[i] = prefix
prefix *= nums[i]
```

We store the prefix **before** multiplying by the current number because `nums[i]` must be excluded from its own answer.

---

## Step 2 — Multiply by the Suffix Products

Now I traverse from right to left.

```python
sufix = 1
```

Here, `sufix` represents the product of all elements **after** the current index.

For:

```text
nums = [1, 2, 3, 4]
```

the suffix products are:

```text
index 3 → 1
index 2 → 4
index 1 → 4 × 3 = 12
index 0 → 4 × 3 × 2 = 24
```

At each position:

```python
product_list[i] *= sufix
```

So the prefix product already stored in `product_list[i]` is multiplied by the suffix product.

For example, at index `2`:

```text
prefix = 1 × 2 = 2
suffix = 4
```

Therefore:

```text
answer[2] = 2 × 4 = 8
```

---

## Putting the Two Passes Together

For:

```text
nums = [1, 2, 3, 4]
```

### After the prefix pass

```text
product_list = [1, 1, 2, 6]
```

### After the suffix pass

```text
[1, 1, 2, 6]
       ↓
[24, 12, 8, 6]
```

The final result is:

```text
[24, 12, 8, 6]
```

---

## Why Not Multiply Everything for Every Index?

A straightforward approach would calculate the product separately for every index.

For example:

```text
index 0 → multiply 2 × 3 × 4
index 1 → multiply 1 × 3 × 4
index 2 → multiply 1 × 2 × 4
index 3 → multiply 1 × 2 × 3
```

That repeats a lot of multiplication.

With `n` elements, this can take:

```text
O(n²)
```

The prefix/suffix approach avoids repeating the same work.

---

## Complexity

### Time Complexity

```text
O(n)
```

There are two passes through the array.

Each pass is `O(n)`:

```text
O(n) + O(n) = O(n)
```

### Space Complexity

```text
O(1) extra space
```

The output array `product_list` is required by the problem and is not counted as extra space.

Apart from that output array, only a few variables are used:

```text
prefix
sufix
i
```

---

## Key Insight

The main insight is to break each answer into two independent parts:

```text
answer[i]
=
product of elements before i
×
product of elements after i
```

Instead of calculating those products repeatedly, I can calculate them while traversing the array.

This gives:

```text
Left products  → prefix pass
Right products → suffix pass
                ↓
              answer
```

The current element is automatically excluded because the prefix is recorded **before** multiplying by `nums[i]`, and the suffix is applied from the opposite direction.

---

## What I Learned

* How to use prefix information to avoid repeated calculations.
* How to calculate suffix information with a reverse traversal.
* How two passes can still have `O(n)` total time complexity.
* How to solve the problem without division.
* How the output array can be reused to store intermediate results.
* The importance of excluding the current element when building prefix and suffix products.
* How a problem that appears to require many repeated multiplications can be reduced to linear time.

---

## Related Concepts

* Arrays
* Prefix Products
* Suffix Products
* Prefix/Suffix Technique
* Multiple Passes
* In-Place / Output Array Reuse
* Time Complexity
* Space Complexity
