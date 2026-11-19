"""
MIT 6.006 — Lecture 7: Binary Node with AVL Balancing

An AVL tree keeps every node height-balanced: the heights of its left and
right subtrees differ by at most 1. Every node stores its own subtree
height (augmentation), so the skew of a node is read in O(1).

    1. skew(A) = height(right subtree) - height(left subtree); the height of
       an empty subtree is -1. A node is height-balanced if its skew is -1, 0 or 1.
    2. A rotation changes the structure locally in O(1) without changing the
       traversal order.
    3. After inserting or deleting a leaf, maintain(A) walks from that leaf up to
       the root: rebalance each node (at most two rotations), then update its height.

Complexity (n = number of nodes):
    subtree_update / skew:                  O(1)
    subtree_rotate_left / right:            O(1)
    rebalance:                              O(1)
    maintain:                               O(log n)
    subtree_first / last, successor,
    predecessor:                            O(log n)
    subtree_insert_before / after,
    subtree_delete:                         O(log n)
    subtree_iter:                           O(n)

Properties:
    A height-balanced tree is balanced: the fewest nodes F(h) in a height-balanced
    tree of height h satisfies F(h) = 1 + F(h-1) + F(h-2) >= 2 F(h-2), so
    F(h) >= 2^(h/2) and therefore h = O(log n).
    Rotations keep the traversal order, so the root object never changes.

Source: Recitation 7 code, unchanged. The base class Binary_Tree at the bottom
comes from Recitation 6 (it is needed by Seq_Binary_Tree and Set_Binary_Tree).
"""


def height(A):
    if A: return A.height
    else: return -1


class Binary_Node:
    def __init__(A, x):                           # O(1)
        A.item = x
        A.left = None
        A.right = None
        A.parent = None
        A.subtree_update()

    def subtree_update(A):                        # O(1)
        A.height = 1 + max(height(A.left), height(A.right))

    def skew(A):                                  # O(1)
        return height(A.right) - height(A.left)

    def subtree_iter(A):                          # O(n)
        if A.left: yield from A.left.subtree_iter()
        yield A
        if A.right: yield from A.right.subtree_iter()

    def subtree_first(A):                         # O(log n)
        if A.left: return A.left.subtree_first()
        else: return A

    def subtree_last(A):                          # O(log n)
        if A.right: return A.right.subtree_last()
        else: return A

    def successor(A):                             # O(log n)
        if A.right: return A.right.subtree_first()
        while A.parent and (A is A.parent.right):
            A = A.parent
        return A.parent

    def predecessor(A):                           # O(log n)
        if A.left: return A.left.subtree_last()
        while A.parent and (A is A.parent.left):
            A = A.parent
        return A.parent

    def subtree_insert_before(A, B):              # O(log n)
        if A.left:
            A = A.left.subtree_last()
            A.right, B.parent = B, A
        else:
            A.left, B.parent = B, A
        A.maintain()

    def subtree_insert_after(A, B):               # O(log n)
        if A.right:
            A = A.right.subtree_first()
            A.left, B.parent = B, A
        else:
            A.right, B.parent = B, A
        A.maintain()

    def subtree_delete(A):                        # O(log n)
        if A.left or A.right:
            if A.left: B = A.predecessor()
            else: B = A.successor()
            A.item, B.item = B.item, A.item
            return B.subtree_delete()
        if A.parent:
            if A.parent.left is A: A.parent.left = None
            else: A.parent.right = None
            A.parent.maintain()
        return A

    def subtree_rotate_right(D):                  # O(1)
        assert D.left
        B, E = D.left, D.right
        A, C = B.left, B.right
        D, B = B, D
        D.item, B.item = B.item, D.item
        B.left, B.right = A, D
        D.left, D.right = C, E
        if A: A.parent = B
        if E: E.parent = D
        B.subtree_update()
        D.subtree_update()

    def subtree_rotate_left(B):                   # O(1)
        assert B.right
        A, D = B.left, B.right
        C, E = D.left, D.right
        B, D = D, B
        B.item, D.item = D.item, B.item
        D.left, D.right = B, E
        B.left, B.right = A, C
        if A: A.parent = B
        if E: E.parent = D
        B.subtree_update()
        D.subtree_update()

    def rebalance(A):                             # O(1)
        if A.skew() == 2:
            if A.right.skew() < 0:
                A.right.subtree_rotate_right()
            A.subtree_rotate_left()
        elif A.skew() == -2:
            if A.left.skew() > 0:
                A.left.subtree_rotate_left()
            A.subtree_rotate_right()

    def maintain(A):                              # O(log n)
        A.rebalance()
        A.subtree_update()
        if A.parent: A.parent.maintain()


# ---------------------------------------------------------------------------
# From Recitation 6, unchanged: the top-level tree used as base class.
# ---------------------------------------------------------------------------

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


if __name__ == "__main__":
    # Insert 1, 2, 3, 4, 5, 6, 7 in order. Without balancing this builds a chain
    # (height 6); with AVL balancing the height stays small.
    T = Binary_Tree()
    for x in range(1, 8):
        node = Binary_Node(x)
        if T.root is None:
            T.root = node
        else:
            T.root.subtree_last().subtree_insert_after(node)
        T.size += 1

    print(list(T))                    # [1, 2, 3, 4, 5, 6, 7]
    print(T.root.height)              # 2
    print(T.root.item)                # 4
    print(T.root.skew())              # 0
