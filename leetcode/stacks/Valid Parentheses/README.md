# LeetCode 20 — Valid Parentheses

## Problem

Given a string `s` containing only the characters:

- `(` and `)`
- `{` and `}`
- `[` and `]`

Determine whether the input string is valid.

A string is valid if:

1. Every opening bracket has a corresponding closing bracket of the same type.
2. Brackets must close in the correct order.
3. Every closing bracket must have a matching opening bracket.

### Examples

**Example 1:**
```python
Input: s = "()"
Output: True
```
Explanation: Every opening bracket has a matching closing bracket.

**Example 2:**
```python
Input: s = "()[]{}"
Output: True
```
Explanation: All brackets are correctly matched and closed.

**Example 3:**
```python
Input: s = "(]"
Output: False
```
Explanation: The opening parenthesis `(` cannot be closed by `]`.

**Example 4:**
```python
Input: s = "([])"
Output: True
```
Explanation: The brackets are correctly nested.

**Example 5:**
```python
Input: s = "([)]"
Output: False
```
Explanation: The brackets are not closed in the correct order.

---

## Approach

We use a **Stack**.

A stack is a data structure that follows the principle:

**LIFO — Last In, First Out.**

Think of a stack of plates.

When you put plates on top of each other, the last plate you place is the first one you remove.

This is exactly what we need for parentheses.

Why?

Consider:

```text
([]) 
```

We encounter the opening brackets in this order:

1. `(`
2. `[` 

But we must close them in the opposite order:

1. `]`
2. `)`

The last opening bracket must be the first one closed.

A stack naturally handles this behavior.

Our algorithm:

1. If the string has an odd length, return `False`.
2. Create a dictionary mapping closing brackets to their corresponding opening brackets.
3. Use a stack to store opening brackets.
4. When we encounter an opening bracket, push it onto the stack.
5. When we encounter a closing bracket:
   - Check whether the stack is empty.
   - Remove the most recent opening bracket.
   - Check whether it matches the closing bracket.
6. After processing the string, return `True` only if the stack is empty.

---

## Step-by-Step Explanation

### Step 1: Check the length

```python
if len(s) % 2 != 0:
    return False
```

Every opening bracket needs a closing bracket.

Therefore, the total number of brackets must be even.

For example:

```text
"(()"
```

There are 3 characters.

Since 3 is odd, the string cannot be valid.

We immediately return `False`.

This is an optimization: we reject impossible strings before processing them.

### Step 2: Create the mapping dictionary

```python
mapping = {
    ')': '(',
    ']': '[',
    '}': '{'
}
```

This dictionary connects every closing bracket to its matching opening bracket.

For example:

```python
mapping[')']
```

Returns:

```python
'('
```

Notice that the closing brackets are the dictionary keys.

Why?

Because when we encounter a closing bracket, we need to know which opening bracket should match it.

### Step 3: Create an empty stack

```python
stack = []
```

We use this list as our stack.

It will store opening brackets that we have encountered but have not yet matched with closing brackets.

For example, if we encounter:

```text
([
```

Our stack becomes:

```python
['(', '[']
```

The last element, `[`, is the most recent opening bracket.

### Step 4: Iterate through the string

```python
for i in s:
```

We examine every character in the string, one at a time.

For each character, we determine whether it is an opening or closing bracket.

### Step 5: Handle opening brackets

```python
if i not in mapping:
    stack.append(i)
```

Remember, our dictionary contains only closing brackets as keys.

Therefore:

```python
i not in mapping
```

means the current character is an opening bracket.

We push it onto the stack using:

```python
stack.append(i)
```

For example:

```text
s = "(["
```

After processing both characters:

```python
stack = ['(', '[']
```

### Step 6: Handle closing brackets

```python
else:
```

If the character exists in `mapping`, it is a closing bracket.

Now we need to find its matching opening bracket.

**First, check whether the stack is empty.**

```python
if not stack:
    return False
```

Imagine this string:

```text
")("
```

The first character is a closing bracket.

But we have not encountered any opening bracket yet.

There is nothing in the stack to match it with.

Therefore, the string is invalid.

**Next, remove the most recent opening bracket.**

```python
last = stack.pop()
```

The `pop()` operation removes and returns the last element of the stack.

For example:

```python
stack = ['(', '[']
last = stack.pop()
```

Now:

```python
last = '['
stack = ['(']
```

We remove the most recent opening bracket because it must be the one closed next.

**Finally, check whether the brackets match.**

```python
if mapping[i] != last:
    return False
```

Remember:

```python
mapping[i]
```

gives us the opening bracket that should match the current closing bracket.

For example, if:

```python
i = ']'
```

Then:

```python
mapping[i] == '['
```

We compare that expected opening bracket with the one we removed from the stack.

If they are different, the string is invalid.

---

## Complete Code

```python
class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determines whether a string contains valid parentheses
        using a stack to match opening and closing brackets.
        """

        # A valid string must contain an even number of brackets.
        if len(s) % 2 != 0:
            return False

        # Map each closing bracket to its matching opening bracket.
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        # Store opening brackets that have not been matched yet.
        stack = []

        # Process each character in the string.
        for i in s:

            # If it is not a closing bracket, it is an opening bracket.
            if i not in mapping:
                stack.append(i)

            else:

                # A closing bracket cannot appear without an opening bracket.
                if not stack:
                    return False

                # Remove the most recent opening bracket.
                last = stack.pop()

                # Check whether the brackets match.
                if mapping[i] != last:
                    return False

        # All opening brackets must have been matched.
        return not stack


# Time Complexity: O(n) — each character is processed once.
# Space Complexity: O(n) — the stack can store up to n/2 opening brackets.
```

---

## Why Does This Work?

The important property is that **the most recently opened bracket must be the first one closed**.

Consider:

```text
([{}])
```

We encounter opening brackets in this order:

```text
(
[
{
```

We must close them in reverse order:

```text
}
]
)
```

A stack guarantees that we always compare a closing bracket with the most recently encountered opening bracket.

If the brackets do not match, we immediately know the string is invalid.

If we finish processing the string and the stack is empty, every opening bracket has been matched.

If the stack is not empty, some opening brackets were never closed.

Therefore, the algorithm correctly identifies valid parentheses.

---

## Example Walkthrough

Let's trace the algorithm using:

```python
s = "([])"
```

Initially:

```python
stack = []
```

**Iteration 1: `i = '('`**

Check:

```python
i not in mapping
```

This is `True` because `(` is not a closing bracket.

We execute:

```python
stack.append(i)
```

Stack:

```python
['(']
```

**Iteration 2: `i = '['`**

Again, `[` is an opening bracket.

We push it onto the stack.

Stack:

```python
['(', '[']
```

**Iteration 3: `i = ']'`**

This is a closing bracket.

First:

```python
if not stack:
```

The stack is not empty, so we continue.

Next:

```python
last = stack.pop()
```

We remove `[`.

Now:

```python
last = '['
stack = ['(']
```

Next:

```python
mapping[i] != last
```

Since:

```python
mapping[']'] == '['
```

We compare:

```python
'[' != '['
```

This is `False`.

The brackets match, so we continue.

**Iteration 4: `i = ')'`**

This is another closing bracket.

The stack is not empty.

We pop the last opening bracket:

```python
last = stack.pop()
```

Now:

```python
last = '('
stack = []
```

We compare:

```python
mapping[')'] != last
```

Which becomes:

```python
'(' != '('
```

This is `False`.

The brackets match.

**After the loop**

We execute:

```python
return not stack
```

Our stack is empty:

```python
stack = []
```

An empty list evaluates to `False` in Python.

Therefore:

```python
not stack
```

evaluates to `True`.

Final result:

```python
True
```

---

## Another Walkthrough: Invalid Ordering

Consider:

```python
s = "([)]"
```

| Character | Action | Stack |
|---|---|---|
| `(` | Push `(` | `['(']` |
| `[` | Push `[` | `['(', '[']` |
| `)` | Pop `[` and compare with `(` | `['(']` |

At the third character:

```python
last = '['
mapping[')'] = '('
```

We compare:

```python
'(' != '['
```

This is `True`.

Therefore, we immediately return:

```python
False
```

Why?

Because `)` tries to close `(`, but the most recent opening bracket is `[`.

The brackets are not nested correctly.

---

## Complexity Analysis

Let `n` represent the length of the input string.

### Time Complexity: O(n)

We iterate through the string once.

For every character, we perform a constant amount of work:

- Check whether it is an opening or closing bracket.
- Push or pop from the stack.
- Compare brackets.

Each character is processed at most once.

Therefore:

**Time Complexity = O(n)**

### Space Complexity: O(n)

In the worst case, the string contains only opening brackets:

```text
(((((((
```

Every character gets pushed onto the stack.

Therefore, the stack can contain up to `n` elements.

So:

**Space Complexity = O(n)**

More precisely, a valid string has an even number of characters, so at most `n/2` opening brackets can be stored. This is still O(n).

---

## Comparison Table

| Approach | Time Complexity | Space Complexity |
|---|---|---|
| Stack | O(n) | O(n) |
| Repeated string replacement | Can be O(n²) | Depends on implementation |

The stack approach is efficient because each bracket is pushed and popped at most once.

---

## Key Insight

The most important idea is:

**The last opening bracket must be the first one closed.**

This is exactly the behavior of a stack.

Whenever a problem involves matching nested structures or processing things in reverse order, a stack is often a good data structure to consider.

---

## What I Learned

1. A stack follows LIFO: Last In, First Out.
2. `append()` pushes an element onto a stack.
3. `pop()` removes and returns the most recently added element.
4. A dictionary can map closing brackets to their matching opening brackets.
5. We must check whether the stack is empty before popping.
6. The final stack must be empty for the string to be valid.
7. A stack can solve this problem in O(n) time.

---

## Related Concepts

- Stack data structure
- LIFO principle
- Hash maps / dictionaries
- Nested structures
- Matching parentheses
- Time and space complexity
