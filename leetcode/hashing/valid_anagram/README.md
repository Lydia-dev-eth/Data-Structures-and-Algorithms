# Valid Anagram

## Problem

Given two strings `s` and `t`, determine whether `t` is an anagram of `s`.

An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once.

Both strings must contain the same characters with the same frequencies.

### Example 1

**Input:**
```python
s = "anagram"
t = "nagaram"
```

**Output:**
```python
True
```

Both strings contain the same characters with the same frequencies.

### Example 2

**Input:**
```python
s = "rat"
t = "car"
```

**Output:**
```python
False
```

The strings contain different characters.

---

## Approach — Hash Map (Frequency Counting)

We can solve this problem using a dictionary (hash map) to keep track of how many times each character appears.

Instead of sorting both strings, we count the frequency of every character in `s` and then use `t` to verify those frequencies.

The key idea is:

**Every character in both strings must have exactly the same frequency.**

We use a dictionary called:

```python
store = {}
```

The dictionary stores:
- Key: A character.
- Value: The number of times that character appears.

For example:

```python
s = "aabbc"
```

The dictionary becomes:

```python
{
    "a": 2,
    "b": 2,
    "c": 1
}
```

---

## Step 1 — Check if Both Strings Have the Same Length

```python
if len(s) != len(t):
    return False
```

Anagrams must contain exactly the same number of characters.

For example:

```python
s = "rat"
t = "rats"
```

Their lengths are:

```python
len(s) = 3
len(t) = 4
```

Since their lengths are different, they cannot be anagrams.

We immediately return:

```python
False
```

This check also prevents us from doing unnecessary work.

---

## Step 2 — Create an Empty Dictionary

```python
store = {}
```

We create an empty dictionary to count the frequency of characters in `s`.

Initially:

```python
store = {}
```

We will gradually populate it as we iterate through the string.

---

## Step 3 — Count the Characters in String s

```python
for i in s:
    if i in store:
        store[i] += 1
    else:
        store[i] = 1
```

We iterate through every character in `s`.

There are two possible situations.

### Case 1 — The Character Already Exists

```python
if i in store:
    store[i] += 1
```

If the character already exists in our dictionary, we increase its frequency by one.

For example:

```python
s = "aab"
```

First iteration:

```python
i = "a"
```

Since `"a"` does not exist:

```python
store["a"] = 1
```

Dictionary:

```python
{"a": 1}
```

Second iteration:

```python
i = "a"
```

Now `"a"` already exists.

We increase its count:

```python
store["a"] += 1
```

Dictionary:

```python
{"a": 2}
```

### Case 2 — The Character Does Not Exist

```python
else:
    store[i] = 1
```

If the character is not in the dictionary, we create a new entry and initialize its frequency to 1.

For example:

```python
i = "b"
```

Since `"b"` does not exist:

```python
store["b"] = 1
```

Dictionary:

```python
{
    "a": 2,
    "b": 1
}
```

After finishing the first loop, we have counted every character in `s`.

---

## Step 4 — Iterate Through String t

```python
for i in t:
```

Now we iterate through the second string.

Instead of building another dictionary, we use the existing dictionary to verify the character frequencies.

The idea is simple:

- If a character exists in `store`, we decrease its frequency.
- If a character does not exist, the strings cannot be anagrams.

Think of the dictionary as a balance.

The first string adds character counts, and the second string removes them.

---

## Step 5 — Check if the Character Exists

```python
if i not in store:
    return False
```

Before decreasing a character's frequency, we check whether that character exists in our dictionary.

Why?

Because if a character in `t` does not exist in `s`, the strings cannot be anagrams.

For example:

```python
s = "rat"
t = "car"
```

After counting `s`:

```python
store = {
    "r": 1,
    "a": 1,
    "t": 1
}
```

We start iterating through `t`.

First:

```python
i = "c"
```

We check:

```python
"c" not in store
```

This is `True`.

Therefore, we immediately return:

```python
False
```

There is no reason to continue.

---

## Step 6 — Decrease the Character Frequency

```python
store[i] -= 1
```

If the character exists, we decrease its frequency by one.

Why?

Because we are matching the characters from `t` against the characters we counted from `s`.

For example:

```python
s = "aab"
t = "aba"
```

After processing `s`:

```python
store = {
    "a": 2,
    "b": 1
}
```

Now process `t`.

First iteration:

```python
i = "a"
```

Decrease its frequency:

```python
store["a"] -= 1
```

Dictionary:

```python
{
    "a": 1,
    "b": 1
}
```

Second iteration:

```python
i = "b"
```

Decrease its frequency:

```python
store["b"] -= 1
```

Dictionary:

```python
{
    "a": 1,
    "b": 0
}
```

Third iteration:

```python
i = "a"
```

Decrease its frequency:

```python
store["a"] -= 1
```

Dictionary:

```python
{
    "a": 0,
    "b": 0
}
```

Every character from `t` has now been matched against the corresponding character count from `s`.

---

## Step 7 — Delete Characters Whose Frequency Becomes Zero

```python
if store[i] == 0:
    del store[i]
```

Once a character's frequency reaches zero, we remove it from the dictionary.

Why?

Because that character has been completely matched.

For example:

```python
store = {
    "a": 1,
    "b": 0
}
```

When `"b"` reaches zero:

```python
del store["b"]
```

The dictionary becomes:

```python
{
    "a": 1
}
```

This makes our dictionary represent only the characters that still have unmatched frequencies.

**Important:** Deleting an entry is not necessary for the algorithm to work. We could keep zero-frequency entries and check their values at the end. However, deleting them makes the final verification simpler.

---

## Step 8 — Check Whether the Dictionary Is Empty

```python
return not store
```

This is the final verification.

If both strings contain exactly the same characters with exactly the same frequencies, every entry will have been removed.

Therefore:

```python
store = {}
```

In Python:

```python
bool({})
```

returns:

```python
False
```

Consequently:

```python
not store
```

returns:

```python
True
```

If the dictionary still contains entries, some characters have unmatched frequencies.

For example:

```python
store = {
    "a": 1
}
```

Then:

```python
not store
```

returns:

```python
False
```

Therefore, we return `True` only when the dictionary is empty.

---

## Complete Code

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        store = {}

        for i in s:
            if i in store:
                store[i] += 1
            else:
                store[i] = 1

        for i in t:
            if i not in store:
                return False

            store[i] -= 1

            if store[i] == 0:
                del store[i]

        return not store
```

---

## Example Walkthrough

Consider:

```python
s = "anagram"
t = "nagaram"
```

### First Loop — Count s

After iterating through `"anagram"`:

```python
store = {
    "a": 3,
    "n": 1,
    "g": 1,
    "r": 1,
    "m": 1
}
```

### Second Loop — Process t

We iterate through `"nagaram"`.

| Iteration | Character | Dictionary after processing |
|---|---|---|
| 1 | n | a: 3, g: 1, r: 1, m: 1, n removed |
| 2 | a | a: 2, g: 1, r: 1, m: 1 |
| 3 | g | a: 2, r: 1, m: 1 |
| 4 | a | a: 1, r: 1, m: 1 |
| 5 | r | a: 1, m: 1 |
| 6 | a | m: 1 |
| 7 | m | {} |

At the end:

```python
store = {}
```

Therefore:

```python
return not store
```

returns:

```python
True
```

The strings are anagrams!

---

## Why Does This Work?

The algorithm works because anagrams must have identical character frequencies.

Our dictionary acts as a frequency tracker.

**First loop:**

We add the frequency of every character in `s`.

**Second loop:**

We subtract the frequency of every character in `t`.

There are three possible situations:

1. A character in `t` does not exist in `s`: return `False`.
2. A character appears more times in `t` than in `s`: eventually, it will not exist in the dictionary, so return `False`.
3. All character frequencies match: the dictionary becomes empty, so return `True`.

The dictionary effectively verifies that every character count balances to zero.

---

## Complexity

### Time Complexity

**O(n)**

Where `n` is the length of the strings.

We perform three main operations:

1. Check the lengths: O(1).
2. Iterate through `s` to count characters: O(n).
3. Iterate through `t` to subtract frequencies: O(n).

Dictionary lookups, insertions, updates, and deletions take O(1) on average.

Therefore:

O(1) + O(n) + O(n) = O(n)

### Space Complexity

**O(k)**

Where `k` is the number of distinct characters in `s`.

The dictionary stores one entry for each distinct character.

In the worst case, every character is different, so:

O(n)

Therefore, the worst-case space complexity is **O(n)**.

---

## Comparison

| Approach | Time | Space | Main Idea |
|---|---|---|---|
| Sorting | O(n log n) | Depends on sorting implementation | Sort both strings and compare |
| Hash Map | O(n) | O(k) | Count and match character frequencies |

Our solution uses a hash map because it avoids sorting and processes both strings in linear time.

---

## Key Insight

The main insight is:

**Instead of comparing the two strings directly, we can count the characters in one string and use the second string to cancel those counts out.**

The important operations are:

```python
store[i] += 1
```

Increase the frequency when counting `s`.

```python
store[i] -= 1
```

Decrease the frequency when processing `t`.

```python
del store[i]
```

Remove a character once its frequency reaches zero.

```python
return not store
```

Check whether all character frequencies have been matched.

---

## What I Learned

- How to use a dictionary as a frequency counter.
- How to count occurrences of characters using a hash map.
- How to use dictionary membership checks with `in` and `not in`.
- How to update dictionary values.
- How to delete dictionary entries using `del`.
- How to use two loops to compare character frequencies.
- Why matching character frequencies is sufficient to establish whether two strings are anagrams.
- How to use `not store` to check whether a dictionary is empty.
- How hash maps can improve an algorithm from O(n log n) to O(n).

---

## Related Concepts

- Strings
- Arrays
- Hash Maps
- Dictionaries
- Frequency Counting
- Character Counting
- Dictionary Operations
- Linear Time Complexity
- Space Complexity
- Anagrams
- Two-Pass Algorithms
