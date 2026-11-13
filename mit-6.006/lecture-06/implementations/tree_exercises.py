"""
MIT 6.006 — Lecture 6: Exercises (balanced build, iterative traversal)

    1. Build a binary tree of height O(log n) from an array in O(n) time,
       keeping the array order as the traversal order.
       (solution: Binary_Tree.build in binary_tree.py)
    2. Show that listing the nodes with successor() takes O(n) time:
       start at subtree_first() and call successor() until it returns None.
       Each edge of the tree is walked twice (once down, once back up), and
       a tree with n nodes has n - 1 edges, so the total work is O(n).

Complexity:
    tree_iter:   O(n)
    height:      O(n)   (helper, visits every node)

Note: tree_iter is the PDF code. The PDF writes it with `T.subtree_first()`,
so T is a node (the root of the subtree); the code below is unchanged.
`height` is a helper that is not in the PDF.
"""

from binary_node import Binary_Node
from binary_tree import Binary_Tree


def tree_iter(T):
    node = T.subtree_first()
    while node:
        yield node
        node = node.successor()


def height(node):
    "Height of the subtree rooted at node (a single node has height 0)."
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))


if __name__ == "__main__":
    T = Binary_Tree()
    T.build(range(15))
    print([n.item for n in tree_iter(T.root)])    # [0, 1, ..., 14]
    print(height(T.root))                         # 3   (15 items -> perfect tree)

    T = Binary_Tree()
    T.build(range(1000))
    print(height(T.root))                         # 9   (floor(log2 1000))
