Lecture 01 — Introduction to Algorithms

This folder contains my notes and implementations based on MIT 6.006 — Introduction to Algorithms, Lecture 1.

The lecture introduces the foundations of algorithmic problem solving, correctness, efficiency, and computational models.

📂 Contents

File| Description
""lec1_note.md"" (./lec1_note.md)| Detailed notes covering the main concepts, correctness, complexity analysis, Word-RAM, and the birthday-matching example.
""birthday_match.py"" (./birthday_match.py)| Implementations of the birthday-matching problem using a naïve approach and a hash-based approach.

🧠 Key Concepts

- Problems vs. Algorithms — A problem specifies the desired input-output relationship; an algorithm is a procedure for producing correct outputs.
- Correctness — Algorithms must produce correct results for all valid inputs; techniques such as induction and loop invariants help establish correctness.
- Efficiency — Analyze how the number of operations grows with input size using asymptotic notation.
- Word-RAM Model — A computational model used to reason about the cost of basic operations and memory access.
- Birthday Matching — An example demonstrating the difference between a naïve O(n²) approach and a hash-table-based O(n) expected approach.

🔬 Example: Birthday Matching

The lecture uses the birthday-matching problem to demonstrate how choosing a different algorithm can significantly improve efficiency.

Naïve approach
O(n²)
    ↓
Compare pairs

Hash-table approach
O(n) expected
    ↓
Store and look up birthdays

The implementation in ""birthday_match.py"" (./birthday_match.py) contains both approaches for comparison.

🎯 Learning Goal

The main goal of this lecture is to understand that solving a problem is not only about obtaining the correct answer, but also about designing an algorithm that remains efficient as the input grows.

---

🔗 Navigation

← "MIT 6.006" (../README.md)
