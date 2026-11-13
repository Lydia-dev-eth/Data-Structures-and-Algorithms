"""
MIT 6.006 — Lecture 6: Binary Tree (top-level data structure)

A Binary_Tree stores a pointer to the root node and the number of items,
so that the node operations can be used on a whole tree.

    1. __iter__ lists the items in traversal order (via subtree_iter).
    2. build(X) turns an array into a balanced tree whose traversal order
       is the array order:
         - store the middle item in the root,
         - build the left half as the left subtree,
         - build the right half as the right subtree.

Complexity:
    __len__:   O(1)
    __iter__:  O(n)
    build:     O(n)   (every node is created once, with O(1) work)
    height of the built tree: O(log n), since H(n) = 1 + H(n/2)

Properties:
    The i-th node in traversal order holds item a_i of the input array.
    Not a search structure yet: traversal order has no relation to keys
    until we use it as a Set or Sequence.

Source: Recitation 6 code. build() is the exercise solution from the PDF,
with two marked changes: it sets `size` (the PDF never does) and handles an
empty input (the PDF would crash).
"""

from binary_node import Binary_Node


class Binary_Tree:
    def __init__(T, Node_Type = Binary_Node):
        T.root = None
        T.size = 0
        T.Node_Type = Node_Type

    def __len__(T): return T.size

    def __iter__(T):
        if T.root:
            for A in T.root.subtree_iter():
                yield A.item

    def build(self, X):                               # O(n)  (exercise solution)
        A = [x for x in X]
        def build_subtree(A, i, j):
            c = (i + j) // 2
            root = self.Node_Type(A[c])
            if i < c:       # needs to store more items in left subtree
                root.left = build_subtree(A, i, c - 1)
                root.left.parent = root
            if c < j:       # needs to store more items in right subtree
                root.right = build_subtree(A, c + 1, j)
                root.right.parent = root
            return root
        if A:                                         # CHANGED: empty input guard
            self.root = build_subtree(A, 0, len(A) - 1)
        self.size = len(A)                            # CHANGED: PDF never sets size


if __name__ == "__main__":
    T = Binary_Tree()
    T.build("abcdefg")
    print(list(T), len(T))                    # ['a', ..., 'g'] 7
    print(T.root.item)                        # d  (the middle item)
    print(T.root.left.item, T.root.right.item)    # b f
