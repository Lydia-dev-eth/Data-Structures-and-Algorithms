"""
MIT 6.006 — Lecture 7: Sequence AVL

Use the traversal order of an AVL tree as the Sequence order. To reach the
i-th item fast, every node is augmented with the size of its subtree.

    1. size(A) = 1 + size(left) + size(right), computed in O(1) from the children.
    2. subtree_at(A, i): compare i with the size L of the left subtree:
       i < L go left; i > L go right with index i - L - 1; i == L this node.
    3. The Sequence operations (get_at, set_at, insert_at, delete_at, ...)
       are the binary tree operations applied to the i-th node.

Complexity (n = number of items):
    subtree_at / get_at / set_at:           O(log n)
    insert_at / delete_at:                  O(log n)
    insert_first / last, delete_first / last:  O(log n)
    build(X):                               O(n)
    iteration:                              O(n)

Properties:
    The tree stays balanced (AVL), so h = O(log n).
    build uses the balanced-build idea from Recitation 6: middle item at the
    root, recurse on both halves.

Source: Recitation 7 code with two marked changes in build():
    - `A[c]` is `X[c]` (the PDF refers to a name `A` that does not exist);
    - an empty input is handled (the PDF would crash).
"""

from avl_node import Binary_Node, Binary_Tree


class Size_Node(Binary_Node):
    def subtree_update(A):                        # O(1)
        super().subtree_update()
        A.size = 1
        if A.left: A.size += A.left.size
        if A.right: A.size += A.right.size

    def subtree_at(A, i):                         # O(h)
        assert 0 <= i
        if A.left: L_size = A.left.size
        else: L_size = 0
        if i < L_size: return A.left.subtree_at(i)
        elif i > L_size: return A.right.subtree_at(i - L_size - 1)
        else: return A


class Seq_Binary_Tree(Binary_Tree):
    def __init__(self): super().__init__(Size_Node)

    def build(self, X):
        def build_subtree(X, i, j):
            c = (i + j) // 2
            root = self.Node_Type(X[c])           # CHANGED: PDF writes A[c]
            if i < c:
                root.left = build_subtree(X, i, c - 1)
                root.left.parent = root
            if c < j:
                root.right = build_subtree(X, c + 1, j)
                root.right.parent = root
            root.subtree_update()
            return root
        if len(X) == 0: return                    # CHANGED: empty input guard
        self.root = build_subtree(X, 0, len(X) - 1)
        self.size = self.root.size

    def get_at(self, i):
        assert self.root
        return self.root.subtree_at(i).item

    def set_at(self, i, x):
        assert self.root
        self.root.subtree_at(i).item = x

    def insert_at(self, i, x):
        new_node = self.Node_Type(x)
        if i == 0:
            if self.root:
                node = self.root.subtree_first()
                node.subtree_insert_before(new_node)
            else:
                self.root = new_node
        else:
            node = self.root.subtree_at(i - 1)
            node.subtree_insert_after(new_node)
        self.size += 1

    def delete_at(self, i):
        assert self.root
        node = self.root.subtree_at(i)
        ext = node.subtree_delete()
        if ext.parent is None: self.root = None
        self.size -= 1
        return ext.item

    def insert_first(self, x): self.insert_at(0, x)
    def delete_first(self): return self.delete_at(0)
    def insert_last(self, x): self.insert_at(len(self), x)
    def delete_last(self): return self.delete_at(len(self) - 1)


if __name__ == "__main__":
    # The exercise example from the PDF.
    T = Seq_Binary_Tree()
    T.build([10, 6, 8, 5, 1, 3])
    print(list(T))                         # [10, 6, 8, 5, 1, 3]
    print(T.get_at(4))                     # 1
    T.set_at(4, -4)
    print(list(T))                         # [10, 6, 8, 5, -4, 3]
    T.insert_at(4, 18)
    print(list(T))                         # [10, 6, 8, 5, 18, -4, 3]
    T.insert_at(4, 12)
    print(list(T))                         # [10, 6, 8, 5, 12, 18, -4, 3]
    T.delete_at(2)
    print(list(T))                         # [10, 6, 5, 12, 18, -4, 3]
    print(T.root.item, T.root.height, T.root.size)   # 12 2 7  (the PDF's last tree)
