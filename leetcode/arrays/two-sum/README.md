 # 🧩 LeetCode — Algorithm & Problem-Solving Practice

> **Applying algorithms and data structures to solve interview-style problems.**

This directory contains my **LeetCode solutions and problem-solving practice**, organized by topic.

The goal is not to collect as many solved problems as possible. The goal is to develop the ability to:

* Recognize patterns
* Choose appropriate data structures
* Develop solutions independently
* Analyze time and space complexity
* Improve inefficient solutions
* Explain the reasoning behind a solution
* Transfer concepts learned from MIT 6.006 to unfamiliar problems

---

# 📂 Structure

```text
leetcode/
│
├── README.md
│
├── arrays/
├── strings/
├── hashing/
├── two-pointers/
├── sliding-window/
├── stacks/
├── queues/
├── linked-lists/
├── binary-search/
├── sorting/
├── trees/
├── heaps/
├── graphs/
├── greedy/
├── backtracking/
├── dynamic-programming/
└── ...
```

Problems are primarily organized by **algorithmic topic**, making it easy to revisit a specific data structure or technique.

---

# 🧠 How Each Problem Is Organized

Each topic contains the problems belonging to that category.

For example:

```text
arrays/
│
├── two-sum/
│   ├── README.md
│   └── solution.py
│
├── best-time-to-buy-and-sell-stock/
│   ├── README.md
│   └── solution.py
│
└── maximum-subarray/
    ├── README.md
    └── solution.py
```

The exact structure can grow as more problems are solved.

---

# 📝 Problem README

Each problem can contain a short `README.md` documenting the reasoning behind the solution.

A typical problem README includes:

```text
Problem
   ↓
Approach
   ↓
Brute Force
   ↓
Optimization
   ↓
Complexity
   ↓
Key Insight
```

For example:

### Problem

**Two Sum**

### Brute Force

Try every pair of numbers.

```text
Time: O(n²)
Space: O(1)
```

### Optimized Approach

Use a hash table to remember previously seen values.

```text
Time: O(n) expected
Space: O(n)
```

### Key Insight

Instead of repeatedly searching the array, use a hash table to perform expected O(1) lookups.

The purpose is to document **why the optimized solution works**, not just store the final code.

---

# 🔄 Solution Evolution

I keep the **final clean solution** in the problem folder rather than creating files such as:

```text
solution_v1.py
solution_v2.py
solution_final.py
solution_final2.py
```

Instead, Git tracks the evolution of the solution.

For example:

```text
solve two sum using brute force
optimize two sum using hash table
refactor solution
add complexity analysis
```

This keeps the repository clean while preserving the development history.

---

# 🐢 Brute Force → ⚡ Optimization

When appropriate, I document the progression from a straightforward solution to a more efficient one.

```text
Understand the problem
        ↓
Find a simple solution
        ↓
Implement brute force
        ↓
Analyze complexity
        ↓
Identify the bottleneck
        ↓
Find a better data structure / pattern
        ↓
Optimize
        ↓
Analyze again
```

The brute-force solution is **not something to be ashamed of**.

It is often the first step toward discovering the optimized solution.

---

# 🔗 Connection to MIT 6.006

LeetCode is used as a practical extension of my MIT 6.006 studies.

```text
MIT 6.006
     ↓
Learn algorithm / data structure
     ↓
Implement it from scratch
     ↓
Understand complexity
     ↓
MIT Problem Sets
     ↓
LeetCode
     ↓
Apply the idea to unfamiliar problems
```

For example:

```text
MIT 6.006
    ↓
Learn Hash Tables
    ↓
Understand expected O(1) lookup
    ↓
Implement a hash table
    ↓
Solve hash-based problems
    ↓
Recognize when hashing is useful
```

The goal is to move from **learning an algorithm** to **recognizing when an algorithmic idea is useful**.

---

# 🧩 Patterns

Patterns are not treated as a separate collection of duplicate solutions.

Instead, patterns are **ideas that emerge across multiple problems**.

For example:

```text
Two Pointers
├── Problem A
├── Problem B
└── Problem C

Sliding Window
├── Problem D
├── Problem E
└── Problem F
```

When I notice that several problems use the same underlying technique, I can document that insight in the relevant topic or problem notes.

The individual problems remain organized by topic, while the pattern is the **reusable idea connecting them**.

---

# 📊 Complexity

Every solution should aim to include:

| Metric | Description                             |
| ------ | --------------------------------------- |
| Time   | How running time grows with input size  |
| Space  | Additional memory used by the algorithm |

For example:

```text
Time:  O(n)
Space: O(n)
```

The goal is not to memorize complexity numbers, but to understand **where the cost comes from**.

---

# 🎯 Problem-Solving Principles

### 1. Understand before coding

Identify:

* What is the input?
* What is the output?
* What constraints matter?
* What makes the problem difficult?

### 2. Start simple

If I cannot immediately see the optimal solution, I first try to develop a correct straightforward approach.

### 3. Find the bottleneck

Ask:

> **What part of my solution is making it slow?**

### 4. Choose the right tool

Consider whether a different:

* Data structure
* Algorithm
* Traversal strategy
* Mathematical observation
* Problem-solving pattern

can remove the bottleneck.

### 5. Verify the solution

Test:

* Normal cases
* Edge cases
* Small inputs
* Large inputs
* Duplicate values
* Empty inputs where applicable

---

# 📚 Topics

The repository currently focuses on:

* Arrays
* Strings
* Hashing
* Two Pointers
* Sliding Window
* Stacks
* Queues
* Linked Lists
* Binary Search
* Sorting
* Trees
* Heaps
* Graphs
* Greedy Algorithms
* Backtracking
* Dynamic Programming

More topics will be added as I encounter them.

---

# 🎯 Goal

The ultimate goal of this section is to develop **interview-ready problem-solving ability**, rather than simply maximizing the number of problems solved.

I want to be able to look at an unfamiliar problem and reason:

```text
What is the problem asking?
        ↓
What information do I need to track?
        ↓
What is the simplest correct approach?
        ↓
Where is the bottleneck?
        ↓
What pattern or data structure could remove it?
        ↓
What is the resulting complexity?
        ↓
Can I explain why it works?
```

> **Solve problems to learn how to think, not just to increase the solved count.**
