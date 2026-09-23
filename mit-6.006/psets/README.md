# MIT 6.006 Problem Sets

> MIT 6.006 — Introduction to Algorithms

This directory contains my solutions to the MIT 6.006 problem sets.

The problem sets are where I apply the concepts from the lectures through **written reasoning, algorithm analysis, data-structure design, and programming implementations**.

## Structure

Each problem set is kept in its own directory:

```text
problem-sets/
├── README.md
│
├── ps0/
│   ├── README.md
│   ├── ps0.tex
│   └── ps0.py
│
├── ps1/
│   ├── README.md
│   ├── ps1.tex
│   └── ps1.py
│
├── ps2/
│   ├── README.md
│   ├── ps2.tex
│   └── ps2.py
│
└── ...
```

The exact files may vary depending on the structure provided by MIT for each problem set.

## What Each PSet Contains

Each problem set may include:

| File          | Purpose                                                      |
| ------------- | ------------------------------------------------------------ |
| `README.md`   | Overview, topics, problems, takeaways, and reflection        |
| `psX.tex`     | Written solutions using the MIT-provided LaTeX template      |
| `psX.py`      | Programming solutions using the MIT-provided Python template |
| `test_psX.py` | Tests, when provided                                         |
| `psX.pdf`     | Compiled written submission, when useful                     |

The MIT-provided templates are kept as the primary submission files. The README serves as documentation around them.

## Problem-Solving Process

For each problem, I try to follow this process:

```text
Understand the problem
        ↓
Identify the relevant concept
        ↓
Develop an approach
        ↓
Analyze correctness and complexity
        ↓
Implement
        ↓
Test
        ↓
Reflect and review
```

The goal is not just to complete the assignment, but to understand **why the solution works and why the chosen approach has the required complexity**.

## How to Navigate

For a specific problem set:

```text
problem-sets/
└── ps1/
    ├── README.md
    ├── ps1.tex
    └── ps1.py
```

Start with the `README.md` to see:

* what the problem set covers
* the main concepts
* the problems and their focus
* key takeaways
* related MIT 6.006 material
* personal reflections

Then use the `.tex` and `.py` files for the actual solutions.

## Learning Goals

Through these problem sets, I am working toward being able to:

* Analyze algorithmic running time and space usage
* Choose appropriate data structures for a problem
* Design algorithms around required complexity bounds
* Implement data structures from scratch
* Reason about correctness
* Understand amortized and asymptotic analysis
* Recognize when a problem can be solved more efficiently
* Clearly explain algorithmic decisions

## Related Material

### MIT 6.006

The problem sets are studied alongside the corresponding lecture material:

```text
mit-6.006/
├── lecture-01/
├── lecture-02/
├── lecture-03/
├── ...
└── problem-sets/
```

### LeetCode

Concepts learned through the problem sets are later reinforced through topic-based LeetCode practice:

* [Arrays](../../leetcode/arrays/)
* [Hash Tables](../../leetcode/hash-tables/)
* [Linked Lists](../../leetcode/linked-lists/)
* [Stacks](../../leetcode/stacks/)
* [Trees](../../leetcode/trees/)
* [Graphs](../../leetcode/graphs/)
* [Dynamic Programming](../../leetcode/dynamic-programming/)

## Notes

The problem sets are kept close to the original MIT-provided structure. I avoid splitting individual problems into unnecessary files so that the repository remains easy to navigate and the original assignment context is preserved.

The purpose of this directory is to document **learning and problem-solving**, not simply to collect completed assignments.
