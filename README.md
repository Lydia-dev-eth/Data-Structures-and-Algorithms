 # 🧠 Data Structures & Algorithms

> **Learn the fundamentals. Build from scratch. Recognize patterns. Solve problems.**

This repository documents my journey through **Data Structures & Algorithms**, combining structured study with hands-on problem solving.

My main learning path is built around **MIT 6.006 — Introduction to Algorithms**, followed by problem sets, algorithm implementations, and **LeetCode** practice organized by topic and problem-solving pattern.

The goal is not to memorize solutions, but to develop the ability to **understand, analyze, implement, and apply algorithms to unfamiliar problems.**

---

## 🗺️ Learning Path

```text
                    MIT 6.006
                        │
                        ▼
                Learn the concepts
                        │
                        ▼
             Implement from scratch
                        │
                        ▼
                  Problem Sets
                        │
                        ▼
              Understand the pattern
                        │
                        ▼
                   LeetCode
                        │
                        ▼
            Apply to unfamiliar problems
                        │
                        ▼
              Interview Readiness
```

Each stage has a different purpose:

| Stage                   | Purpose                                            |
| ----------------------- | -------------------------------------------------- |
| 🎓 **MIT 6.006**        | Build a strong theoretical foundation              |
| 🛠️ **Implementations** | Understand how algorithms and data structures work |
| 📝 **Problem Sets**     | Apply concepts to structured problems              |
| 🧩 **LeetCode Topics**  | Recognize and practice recurring patterns          |
| 🔁 **Review**           | Turn individual solutions into reusable knowledge  |

---
# ⚡ Quick Start

If you're exploring this repository for the first time, here's the recommended path:

### 1. 🎓 Start with MIT 6.006

Begin with the lecture material to build the theoretical foundation.

```text
mit-6.006/
└── lecture-01/
    ├── README.md
    ├── notes.md
    └── implementations/
```

Read the notes, work through the concepts, and study the implementations.

→ [`mit-6.006/`](./mit-6.006/)

---

### 2. 🛠️ Work through the Problem Sets

After learning the relevant concepts, use the problem sets to apply them in a more structured setting.

```text
mit-6.006/
└── problem-sets/
    ├── ps0/
    ├── ps1/
    ├── ps2/
    └── ...
```

→ [`problem-sets/`](./mit-6.006/problem-sets/)

---

### 3. 🧩 Study the LeetCode Topic

Before solving a collection of problems, review the topic's README to understand the underlying pattern.

For example:

```text
leetcode/
└── sliding-window/
    ├── README.md
    └── problems...
```

The README focuses on:

* What the pattern is
* When to use it
* How to recognize it
* Common variations
* Complexity
* Common mistakes

---

### 4. 💻 Solve LeetCode Problems

Apply the pattern to actual problems.

```text
leetcode/
└── sliding-window/
    ├── README.md
    ├── 0003-longest-substring-without-repeating-characters.py
    ├── 0076-minimum-window-substring.py
    └── ...
```

Try to solve each problem independently before looking at hints or solutions.

---

### 5. 🔍 Document Your Reasoning

For important problems, record the progression:

```text
Understand
    ↓
Attempt
    ↓
Brute Force
    ↓
Analyze
    ↓
Optimize
    ↓
Implement
    ↓
Reflect
    ↓
Review
```

This turns the repository from a collection of answers into a record of **problem-solving development**.

---

### 6. 🔄 Review and Revisit

Return to problems that were difficult.

The goal is to eventually recognize:

```text
New Problem
     ↓
"What does this remind me of?"
     ↓
Identify Pattern
     ↓
Choose Technique
     ↓
Derive Solution
```

rather than relying on memorized solutions.

---

## 🧭 Where Should I Go?

| I want to...                    | Go to                                                  |
| ------------------------------- | ------------------------------------------------------ |
| Learn the theory                | [`mit-6.006/`](./mit-6.006/)                           |
| Review lecture notes            | `mit-6.006/lecture-XX/notes.md`                        |
| Study implementations           | `mit-6.006/lecture-XX/implementations/`                |
| Practice structured assignments | [`mit-6.006/problem-sets/`](./mit-6.006/problem-sets/) |
| Learn a problem-solving pattern | `leetcode/<topic>/README.md`                           |
| Practice interview problems     | [`leetcode/`](./leetcode/)                             |
| Review a specific solution      | `leetcode/<topic>/<problem>.py`                        |
| See how my thinking evolved     | Git history                                            |

# 📁 Repository Structure

```text
data-structures-and-algorithms/
│
├── README.md
│
├── mit-6.006/
│   │
│   ├── README.md
│   │
│   ├── lecture-01/
│   │   ├── README.md
│   │   ├── notes.md
│   │   └── implementations/
│   │
│   ├── lecture-02/
│   │   ├── README.md
│   │   ├── notes.md
│   │   └── implementations/
│   │
│   ├── lecture-03/
│   │   ├── README.md
│   │   ├── notes.md
│   │   └── implementations/
│   │
│   ├── ...
│   │
│   └── problem-sets/
│       ├── ps0/
│       ├── ps1/
│       ├── ps2/
│       ├── ps3/
│       └── ...
│
└── leetcode/
    │
    ├── arrays/
    ├── hash-tables/
    ├── two-pointers/
    ├── sliding-window/
    ├── binary-search/
    ├── linked-lists/
    ├── stacks/
    ├── trees/
    ├── heaps/
    ├── graphs/
    ├── backtracking/
    ├── greedy/
    └── dynamic-programming/
```

---

# 🎓 MIT 6.006

The [`mit-6.006/`](./mit-6.006/) directory contains my work while studying **MIT 6.006 — Introduction to Algorithms**.

Each lecture is treated as a self-contained learning unit.

### A lecture contains:

```text
lecture-XX/
├── README.md
├── notes.md
└── implementations/
```

### `README.md`

A concise overview of:

* Topics covered
* Key ideas
* Algorithms/data structures implemented
* Related problem sets
* Important takeaways

### `notes.md`

My detailed notes and explanations from the lecture.

### `implementations/`

Implementations written while learning the concepts.

The purpose is to understand the mechanics and trade-offs rather than treating algorithms as black boxes.

---

# 📝 Problem Sets

Problem sets are kept separately from lectures because they represent **applied work and assignments**.

```text
problem-sets/
├── ps0/
├── ps1/
├── ps2/
├── ps3/
└── ...
```

Depending on the assignment, a PSet may contain:

* Written solutions
* Programming solutions
* Complexity analysis
* Notes and reflections

The exact internal structure may vary depending on the original assignment.

---

# 💻 LeetCode

The [`leetcode/`](./leetcode/) directory contains my interview-oriented problem solving.

Problems are organized primarily by **topic/pattern**, rather than by difficulty.

```text
leetcode/
├── arrays/
├── hash-tables/
├── two-pointers/
├── sliding-window/
├── binary-search/
├── linked-lists/
├── stacks/
├── trees/
├── heaps/
├── graphs/
├── backtracking/
├── greedy/
└── dynamic-programming/
```

### Why organize by topic?

Difficulty tells me:

> **How hard is this problem?**

The topic tells me:

> **What technique or way of thinking can solve this type of problem?**

For interview preparation, learning to recognize the underlying pattern is more valuable than simply remembering individual solutions.

Difficulty is still recorded inside each problem.

---

# 🧩 Topic READMEs

Each LeetCode topic can contain its own `README.md`.

For example:

```text
leetcode/
└── sliding-window/
    ├── README.md
    ├── 0003-longest-substring-without-repeating-characters.py
    ├── 0076-minimum-window-substring.py
    └── ...
```

The topic README explains the **general technique**.

For example:

```text
Sliding Window
│
├── What is it?
├── When should I use it?
├── How do I recognize it?
├── Common variations
├── Complexity
└── Common mistakes
```

The individual Python files then demonstrate how that technique is applied to actual problems.

So:

```text
README.md
    ↓
"What is the pattern?"
    ↓
LeetCode problems
    ↓
"Can I apply the pattern?"
```

---

# 🔍 Problem-Solving Process

For important problems, I follow a consistent process.

### 1. Understand

Clearly identify the inputs, outputs, constraints, and requirements.

### 2. Attempt

Try to solve the problem independently before looking at hints or solutions.

### 3. Brute Force

When useful, start with the simplest correct approach.

This helps establish a baseline and makes the optimization easier to understand.

```text
Brute Force
     ↓
Identify the bottleneck
     ↓
Find a better approach
```

### 4. Analyze

Determine:

* Time complexity
* Space complexity
* Main bottleneck

### 5. Optimize

Ask:

* Can I use a better data structure?
* Am I repeating work?
* Can I reduce unnecessary traversal?
* Is there a known pattern?
* Can I trade space for time?

### 6. Implement

Write a clean and readable solution.

### 7. Reflect

Record what I learned, including:

* Why the solution works
* Why the optimization works
* What pattern was used
* Important edge cases
* Common mistakes

### 8. Review

Revisit difficult problems until I can reproduce the **reasoning**, not just the code.

---

# 🧪 Brute Force → Optimization

I don't hide brute-force solutions when they are useful for demonstrating the evolution of my thinking.

For example:

```text
Two Sum

Brute Force
O(n²)
    │
    │ repeated searching
    ▼
Hash Table
O(n)
    │
    ▼
Faster lookup
```

The purpose is not to keep every version forever.

The purpose is to understand **why the optimized solution is better**.

---

# 🔄 Version Control

Git is used to track the evolution of my solutions.

Instead of creating files such as:

```text
solution-v1.py
solution-v2.py
solution-final.py
solution-final-final.py
```

I use Git history.

Example:

```text
feat: add brute force solution for Two Sum
feat: optimize Two Sum using hash table
fix: handle duplicate values
docs: add complexity analysis
```

This keeps the repository clean while preserving the development history.

---

# 🧠 What I Am Trying to Build

The goal is to move through these levels:

```text
Level 1
"I know what this data structure is."

        ↓

Level 2
"I can implement it."

        ↓

Level 3
"I understand its complexity and trade-offs."

        ↓

Level 4
"I recognize when a problem needs it."

        ↓

Level 5
"I can solve unfamiliar problems using it."

        ↓

Level 6
"I can explain and defend my solution in an interview."
```

That final step is the real objective.

---

# 📊 Progress

## MIT 6.006

| Area            | Status         |
| --------------- | -------------- |
| Lectures        | 🔄 In Progress |
| Implementations | 🔄 In Progress |
| Problem Sets    | 🔄 In Progress |

## LeetCode

| Topic               | Progress |
| ------------------- | -------: |
| Arrays              |        — |
| Hash Tables         |        — |
| Two Pointers        |        — |
| Sliding Window      |        — |
| Binary Search       |        — |
| Linked Lists        |        — |
| Stacks              |        — |
| Trees               |        — |
| Heaps               |        — |
| Graphs              |        — |
| Backtracking        |        — |
| Greedy              |        — |
| Dynamic Programming |        — |

> Progress is updated as I continue learning and practicing.

---

# 🛠️ Tools

* **Python**
* **MIT 6.006**
* **LeetCode**
* **Git**
* **GitHub**

---

# 🚀 Long-Term Direction

Data Structures & Algorithms is one part of my broader software engineering journey.

```text
Python
   ↓
Data Structures & Algorithms
   ↓
Problem-Solving Patterns
   ↓
Technical Interview Preparation
   ↓
Backend Development
   ↓
Databases & Networking
   ↓
Software Engineering
```

The purpose of this repository is therefore bigger than interview preparation.

It is about building the **fundamental problem-solving skills needed to become a stronger software engineer.**

---

## ⭐ Guiding Principles

> **Understand, don't memorize.**

> **Implement, don't just use.**

> **Recognize patterns, don't just remember problems.**

> **Optimize because you understand the bottleneck.**

> **Focus on depth, not just the number of problems solved.**

---

### 📌 Status

**🚧 Actively learning · Implementing · Practicing · Improving**
