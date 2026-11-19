"""
MIT 6.006 — Lecture 7: Exercise — Counting Ones in a Bit Sequence

Maintain a sequence of n bits with two operations in O(log n) time:
    flip(i):             flip the bit at index i
    count_ones_upto(i):  number of 1 bits in the prefix up to index i

Idea: store the bits in a Sequence AVL and augment each node A with
A.subtree_ones, the number of 1 bits in its subtree. It is computed in O(1)
from the augmentations of the children.

    1. update(A): A.subtree_ones = A.item + ones(left) + ones(right).
    2. subtree_count_ones_upto(A, i): if i falls in the left subtree, recurse
       left; otherwise add the left ones, then the node's bit, then recurse
       right on the remaining index. One recursive call per level.
    3. flip(i): find the i-th node, flip its bit, then redo update(A) at the node
       and at every ancestor (walking up the tree).

Complexity (n = number of bits):
    update:                  O(1)
    count_ones_upto:         O(log n)
    flip:                    O(log n)

Properties:
    count_ones_upto(i) means subtree_count_ones_upto(T.root, i).
    A node's augmentation depends only on its children, so it can be
    maintained during rebalancing without changing the O(log n) bounds.

Source: Recitation 7 code for update() and subtree_count_ones_upto(), unchanged.
The PDF describes flip in words only (no code), so it is not implemented here.
`Ones_Node` is glue so the PDF's update() is called whenever a node is updated.
"""

from seq_avl import Size_Node, Seq_Binary_Tree


def update(A):
    A.subtree_ones = A.item
    if A.left:
        A.subtree_ones += A.left.subtree_ones
    if A.right:
        A.subtree_ones += A.right.subtree_ones


def subtree_count_ones_upto(A, i):
    assert 0 <= i < A.size
    out = 0
    if A.left:
        if i < A.left.size:
            return subtree_count_ones_upto(A.left, i)
        out += A.left.subtree_ones
        i -= A.left.size
    out += A.item
    if i > 0:
        assert A.right
        out += subtree_count_ones_upto(A.right, i - 1)
    return out


class Ones_Node(Size_Node):                       # glue (not in the PDF)
    def subtree_update(A):
        super().subtree_update()
        update(A)


if __name__ == "__main__":
    T = Seq_Binary_Tree()
    T.Node_Type = Ones_Node
    T.build([1, 0, 1, 1, 0, 1, 0])

    print([subtree_count_ones_upto(T.root, i) for i in range(7)])   # [1, 1, 2, 3, 3, 4, 4]
    print(T.root.subtree_ones)                                       # 4
