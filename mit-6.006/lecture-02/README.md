Lecture 02 — Sequences: Arrays, Linked Lists & Dynamic Arrays

This folder contains my notes and implementations based on MIT 6.006 — Introduction to Algorithms, Lecture 2.

The lecture introduces the Sequence interface and explores three different data structures that implement it, highlighting the trade-offs between access, insertion, deletion, and memory usage.

📂 Contents

File| Description
""notes.md"" (./notes.md)| Detailed notes covering sequences, interfaces, arrays, linked lists, dynamic arrays, complexity, and amortized analysis.
""array_seq.py"" (./array_seq.py)| Array-based implementation of the Sequence interface.
""linked_list_seq.py"" (./linked_list_seq.py)| Linked-list implementation of the Sequence interface.
""dynamic_array_seq.py"" (./dynamic_array_seq.py)| Dynamic-array implementation using table doubling.

🧠 Key Concepts

- Sequence Interface — An ordered collection where elements are identified by their position, or rank.
- Set Interface — A different abstraction where elements are organized by their keys rather than their positions.
- Arrays — Provide fast random access but require shifting elements for insertion and deletion.
- Linked Lists — Make insertion and deletion efficient at known nodes but require traversal to reach arbitrary positions.
- Dynamic Arrays — Combine fast random access with efficient amortized append/pop operations by resizing when necessary.
- Amortized Analysis — Analyzing the average cost of operations over a sequence of operations rather than considering each operation independently.

⚖️ Data Structure Trade-offs

Structure| Random Access| Insert/Delete| Main Trade-off
Array Sequence| O(1)| O(n)| Fast access, expensive modification
Linked List| O(n)| O(1) at known node/head| Fast modification, slow access
Dynamic Array| O(1)| O(n) middle / O(1) amortized append| Fast access with efficient resizing

💡 Key Takeaway

There is no single data structure that is best for every operation.

The choice depends on what operations the application performs most frequently.

Need fast random access?
        ↓
      Array
        │
        │
Need fast insertion/deletion at a known node?
        ↓
   Linked List
        │
        │
Need fast access + efficient append?
        ↓
  Dynamic Array

🔗 Related

- ""Notes"" (./notes.md)
- ""Array Sequence"" (./array_seq.py)
- ""Linked List Sequence"" (./linked_list_seq.py)
- ""Dynamic Array Sequence"" (./dynamic_array_seq.py)
- "MIT 6.006" (../README.md)
