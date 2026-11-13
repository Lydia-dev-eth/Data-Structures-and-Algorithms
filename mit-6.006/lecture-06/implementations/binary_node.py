"""
MIT 6.006 — Lecture 6: Binary Node

A binary node is a linked node with a constant number of fields:
an item, a parent pointer, a left child pointer and a right child pointer.
A binary tree is a set of binary nodes joined by these pointers.

    1. Traversal order: everything in the left subtree comes before the node,
       everything in the right subtree comes after it.
    2. Navigation: subtree_first / subtree_last walk down; successor /
       predecessor walk down or up.
    3. Dynamic operations: insert before / after a node, and delete a node
       (swap its item down the tree until it sits in a leaf, then cut the leaf).

Complexity (h = height of the tree, n = number of nodes):
    subtree_iter:                           O(n)
    subtree_first / subtree_last:           O(h)
    successor / predecessor:                O(h)
    subtree_insert_before / after:          O(h)
    subtree_delete:                         O(h)
    Space:                                  O(1) per node

Properties:
    Every operation only walks along one root-to-leaf path, so it costs O(h).
    If h = O(log n) every operation is O(log n); if the tree is a chain, h = n.
    All operations preserve the traversal order of the other items.

Source: Recitation 6 code, unchanged (the PDF names the node `A`, not `self`).
"""


class Binary_Node:
    def __init__(A, x):                           # O(1)
        A.item = x
        A.left = None
        A.right = None
        A.parent = None
        # A.subtree_update()                      # wait for R07!

    def subtree_iter(A):                          # O(n)
        if A.left: yield from A.left.subtree_iter()
        yield A
        if A.right: yield from A.right.subtree_iter()

    def subtree_first(A):                         # O(h)
        if A.left: return A.left.subtree_first()
        else: return A

    def subtree_last(A):                          # O(h)
        if A.right: return A.right.subtree_last()
        else: return A

    def successor(A):                             # O(h)
        if A.right: return A.right.subtree_first()
        while A.parent and (A is A.parent.right):
            A = A.parent
        return A.parent

    def predecessor(A):                           # O(h)
        if A.left: return A.left.subtree_last()
        while A.parent and (A is A.parent.left):
            A = A.parent
        return A.parent

    def subtree_insert_before(A, B):              # O(h)
        if A.left:
            A = A.left.subtree_last()
            A.right, B.parent = B, A
        else:
            A.left, B.parent = B, A
        # A.maintain()                            # wait for R07!

    def subtree_insert_after(A, B):               # O(h)
        if A.right:
            A = A.right.subtree_first()
            A.left, B.parent = B, A
        else:
            A.right, B.parent = B, A
        # A.maintain()                            # wait for R07!

    def subtree_delete(A):                        # O(h)
        if A.left or A.right:
            if A.left: B = A.predecessor()
            else: B = A.successor()
            A.item, B.item = B.item, A.item
            return B.subtree_delete()
        if A.parent:
            if A.parent.left is A: A.parent.left = None
            else: A.parent.right = None
            # A.parent.maintain()                 # wait for R07!
        return A


if __name__ == "__main__":
    #         D
    #       /   \
    #      B     F
    #     / \   / \
    #    A   C E   G
    nodes = {c: Binary_Node(c) for c in "ABCDEFG"}
    def link(p, l, r):
        for child, side in ((l, "left"), (r, "right")):
            setattr(nodes[p], side, nodes[child])
            nodes[child].parent = nodes[p]
    link("D", "B", "F"); link("B", "A", "C"); link("F", "E", "G")
    root = nodes["D"]

    print([n.item for n in root.subtree_iter()])        # ['A','B','C','D','E','F','G']
    print(root.subtree_first().item, root.subtree_last().item)   # A G
    print(nodes["C"].successor().item)                  # D
    print(nodes["D"].successor().item)                  # E
    print(nodes["G"].successor())                       # None
    print(nodes["D"].predecessor().item)                # C

    root.subtree_insert_before(Binary_Node("X"))
    print([n.item for n in root.subtree_iter()])        # A B C X D E F G
    print(root.subtree_delete().item)                   # D  (the item removed)
    print([n.item for n in root.subtree_iter()])        # A B C X E F G
