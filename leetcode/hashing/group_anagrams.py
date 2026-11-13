# Group Anagrams

## Problem

Given an array of strings `strs`, group the anagrams together.

You can return the answer in any order.

Anagrams are words that contain exactly the same characters with the same frequencies, but their characters may appear in different orders.

### Example 1

**Input:**
```python
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
```

**Output:**
```python
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
```

Explanation:

- `"eat"`, `"tea"`, and `"ate"` contain the same characters.
- `"tan"` and `"nat"` contain the same characters.
- `"bat"` has no other matching anagram.

### Example 2

**Input:**
```python
strs = [""]
```

**Output:**
```python
[[""]]
```

### Example 3

**Input:**
```python
strs = ["a"]
```

**Output:**
```python
[["a"]]
```

---

## Approach — Hash Map + Sorting

We can solve this problem using a dictionary (hash map) to group words that are anagrams.

The key idea is:

**If two words are anagrams, sorting their characters alphabetically will produce the same string.**

For example:

```python
"eat" → "aet"
"tea" → "aet"
"ate" → "aet"
```

Although the original words are different, their sorted versions are identical.

We can use these sorted strings as dictionary keys.

Every word that produces the same sorted string belongs to the same group.

We create:

```python
store = {}
```

The dictionary stores:

- Key: The sorted version of a word.
- Value: A list containing all words that share that sorted version.

For example:

```python
{
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan", "nat"],
    "abt": ["bat"]
}
```

---

## Step 1 — Create an Empty Dictionary

```python
store = {}
```

We create an empty dictionary to organize the anagrams.

Initially:

```python
store = {}
```

As we iterate through the input strings, we will gradually populate this dictionary.

Remember that we are not storing individual words directly as keys.

Instead, we store their sorted versions.

This allows different words with the same characters to share the same dictionary key.

---

## Step 2 — Iterate Through Every Word

```python
for word in strs:
```

We iterate through every word in the input list.

For example:

```python
strs = ["eat", "tea", "tan", "ate"]
```

The loop visits:

```python
"eat"
"tea"
"tan"
"ate"
```

At every iteration, we take the current word and determine its sorted version.

---

## Step 3 — Sort the Characters of Each Word

```python
''.join(sorted(word))
```

This is the most important operation in our solution.

Let's understand it step by step.

Consider:

```python
word = "eat"
```

### First: sorted(word)

```python
sorted(word)
```

The `sorted()` function sorts the characters alphabetically.

It returns a list:

```python
['a', 'e', 't']
```

Notice that the result is a list, not a string.

### Second: ''.join()

```python
''.join(['a', 'e', 't'])
```

The `join()` method combines the characters into a single string.

The empty string `''` tells Python to join the characters without putting anything between them.

The result is:

```python
"aet"
```

Therefore:

```python
''.join(sorted("eat"))
```

produces:

```python
"aet"
```

Let's compare a few words:

| Original Word | Sorted Version |
|---|---|
| eat | aet |
| tea | aet |
| ate | aet |
| tan | ant |
| nat | ant |
| bat | abt |

This is how we identify which words are anagrams.

---

## Step 4 — Check Whether the Sorted Word Already Exists

```python
if ''.join(sorted(word)) in store:
```

After sorting the current word, we check whether its sorted version already exists as a key in our dictionary.

For example:

```python
word = "tea"
```

Its sorted version is:

```python
"aet"
```

Suppose our dictionary currently contains:

```python
store = {
    "aet": ["eat"]
}
```

We check:

```python
"aet" in store
```

This returns:

```python
True
```

Why?

Because we previously encountered `"eat"`, which produced the same sorted key.

Therefore, `"tea"` belongs to the same anagram group.

---

## Step 5 — Append the Word to an Existing Group

```python
store[''.join(sorted(word))].append(word)
```

If the sorted version already exists, we append the current word to the list associated with that key.

Let's understand this with an example.

Suppose:

```python
store = {
    "aet": ["eat"]
}
```

We encounter:

```python
word = "tea"
```

Its sorted version is:

```python
"aet"
```

Since `"aet"` already exists, we execute:

```python
store["aet"].append("tea")
```

The dictionary becomes:

```python
{
    "aet": ["eat", "tea"]
}
```

We use `.append()` because we want to add the new word to the existing group rather than replace the group.

If we assigned a new list instead, we would lose the words already stored.

For example, this would be incorrect:

```python
store["aet"] = ["tea"]
```

It would replace:

```python
["eat"]
```

with:

```python
["tea"]
```

We would lose `"eat"`.

Therefore, `.append()` is important.

---

## Step 6 — Create a New Group If the Key Does Not Exist

```python
else:
    store[''.join(sorted(word))] = [word]
```

If the sorted version does not exist in our dictionary, it means we have encountered a new anagram group.

We create a new dictionary entry.

For example:

```python
word = "tan"
```

Its sorted version is:

```python
"ant"
```

Suppose our dictionary contains:

```python
{
    "aet": ["eat", "tea"]
}
```

We check:

```python
"ant" in store
```

This returns:

```python
False
```

Therefore, we create a new entry:

```python
store["ant"] = ["tan"]
```

Our dictionary becomes:

```python
{
    "aet": ["eat", "tea"],
    "ant": ["tan"]
}
```

Notice that we use:

```python
[word]
```

instead of:

```python
word
```

Why?

Because the dictionary value must be a list of words, even if the group initially contains only one word.

---

## Step 7 — Create an Empty List for the Final Result

```python
list1 = []
```

After grouping all the anagrams, we need to return the groups as a list of lists.

Our dictionary currently looks like:

```python
store = {
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan", "nat"],
    "abt": ["bat"]
}
```

However, the problem asks us to return:

```python
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
```

We create an empty list to hold these groups.

---

## Step 8 — Extract the Dictionary Values

```python
for i in store.values():
    list1.append(i)
```

Let's understand `store.values()`.

A dictionary contains:

- Keys.
- Values.

For our dictionary:

```python
store = {
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan", "nat"],
    "abt": ["bat"]
}
```

The keys are:

```python
"aet", "ant", "abt"
```

The values are:

```python
["eat", "tea", "ate"]
["tan", "nat"]
["bat"]
```

When we write:

```python
store.values()
```

Python gives us access to all the dictionary values.

The loop iterates through these groups.

Every time, we append the current group to `list1`.

Eventually:

```python
list1 = [
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
```

---

## Step 9 — Return the Final Result

```python
return list1
```

After collecting all the dictionary values, we return the final list of anagram groups.

The result is:

```python
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
```

The problem allows us to return the groups in any order.

Therefore, we do not need to worry about the order of the groups.

---

## Complete Code

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups anagrams together using a hash map.
        Sorted versions of words are used as dictionary keys.
        """

        store = {}

        for word in strs:

            # Sort the characters to create a common key for anagrams.
            if ''.join(sorted(word)) in store:

                # Add the word to its existing anagram group.
                store[''.join(sorted(word))].append(word)

            else:

                # Create a new group for a previously unseen key.
                store[''.join(sorted(word))] = [word]

        # Collect all anagram groups into the final result.
        list1 = []

        for i in store.values():
            list1.append(i)

        return list1


# Time Complexity: O(n * k log k)
# Space Complexity: O(n * k)
# n = number of words, k = maximum length of a word.
```

---

## Why Does This Work?

The algorithm works because sorting gives anagrams a common representation.

For example:

```python
"listen" → "eilnst"
"silent" → "eilnst"
"enlist" → "eilnst"
```

All three words produce the same sorted string.

Therefore, they share the same dictionary key and are placed in the same group.

For every word, there are two possible situations:

**Case 1 — Its sorted version already exists.**

We know another word with the same characters has already been encountered.

We append the current word to that existing group.

**Case 2 — Its sorted version does not exist.**

We have encountered a new anagram group.

We create a new dictionary entry and initialize its value with the current word.

After processing every word, all anagrams are grouped together.

---

## Example Walkthrough

Consider:

```python
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
```

Initially:

```python
store = {}
```

### Iteration 1

```python
word = "eat"
```

Sorted version:

```python
"aet"
```

The key does not exist.

Create a new group:

```python
store = {
    "aet": ["eat"]
}
```

### Iteration 2

```python
word = "tea"
```

Sorted version:

```python
"aet"
```

The key already exists.

Append `"tea"`:

```python
store = {
    "aet": ["eat", "tea"]
}
```

### Iteration 3

```python
word = "tan"
```

Sorted version:

```python
"ant"
```

The key does not exist.

Create a new group:

```python
store = {
    "aet": ["eat", "tea"],
    "ant": ["tan"]
}
```

### Iteration 4

```python
word = "ate"
```

Sorted version:

```python
"aet"
```

The key already exists.

Append `"ate"`:

```python
store = {
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan"]
}
```

### Iteration 5

```python
word = "nat"
```

Sorted version:

```python
"ant"
```

Append `"nat"`:

```python
store = {
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan", "nat"]
}
```

### Iteration 6

```python
word = "bat"
```

Sorted version:

```python
"abt"
```

The key does not exist.

Create a new group:

```python
store = {
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan", "nat"],
    "abt": ["bat"]
}
```

Finally, we extract the dictionary values:

```python
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
```

---

## Complexity

Let:

- `n` = number of words in the input list.
- `k` = maximum length of a word.

### Time Complexity

**O(n × k log k)**

We perform the following operations:

1. Iterate through all `n` words: O(n).
2. Sort every word: O(k log k).
3. Join the sorted characters: O(k).
4. Perform dictionary lookups and insertions: O(1) on average.
5. Collect dictionary values: O(n) in total.

Sorting is the most expensive operation for each word.

Therefore:

O(n × k log k)

**Important optimization:** Your current implementation calculates `''.join(sorted(word))` more than once for each word. We can calculate it once and store it in a variable:

```python
key = ''.join(sorted(word))
```

Then use `key` for both the lookup and insertion.

This avoids unnecessary repeated sorting.

### Space Complexity

**O(n × k)**

We store every input word in the dictionary groups.

If there are `n` words and each word has at most `k` characters, the total storage for the grouped words is O(n × k).

The sorted dictionary keys also require space.

Therefore, the overall auxiliary space complexity is:

**O(n × k)**

---

## Comparison

| Approach | Time | Space | Main Idea |
|---|---|---|---|
| Sorting + Hash Map | O(n × k log k) | O(n × k) | Sort each word and group identical keys |
| Character Frequency + Hash Map | O(n × k) | O(n × k) | Use character frequencies as dictionary keys |

Our solution uses sorting because it provides a straightforward way to identify anagrams.

A frequency-counting approach can improve the time complexity because it avoids sorting each word.

---

## Key Insight

The main insight is:

**Two words are anagrams if sorting their characters produces the same string.**

For example:

```python
"eat" → "aet"
"tea" → "aet"
"ate" → "aet"
```

The important operations are:

```python
''.join(sorted(word))
```

Create a common key for anagrams.

```python
store[key].append(word)
```

Add a word to an existing anagram group.

```python
store[key] = [word]
```

Create a new anagram group.

```python
store.values()
```

Retrieve all the groups from the dictionary.

---

## What I Learned

- How to group related elements using a hash map.
- How sorting can create a common representation for anagrams.
- How to use `sorted()` to sort characters.
- How to use `join()` to convert a list of characters into a string.
- How dictionary keys can represent groups of related elements.
- How to store lists as dictionary values.
- How to use `.append()` to add elements to existing groups.
- How to use `.values()` to retrieve dictionary values.
- How to transform a dictionary of groups into a list of lists.
- How sorting affects time complexity.
- How a frequency-counting approach can optimize an anagram grouping algorithm.

---

## Related Concepts

- Arrays
- Strings
- Hash Maps
- Dictionaries
- Sorting
- Anagrams
- Character Frequency
- Dictionary Keys and Values
- Nested Lists
- `sorted()`
- `join()`
- `.append()`
- `.values()`
- Time Complexity
- Space Complexity
