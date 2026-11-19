"""
MIT 6.006 — Lecture 7: Set AVL

The Binary Search Tree Set from Recitation 6 is reused unchanged on top of
the AVL Binary_Node. Because every insert and delete now rebalances, all
operations cost O(h) = O(log n).

    1. BST_Node adds find / find_next / find_prev / insert by key.
    2. Set_Binary_Tree is the Set interface on top of a binary tree.
    3. With the AVL node, subtree_insert_before / after and subtree_delete
       call maintain(), so the height stays O(log n).

Complexity (n = number of items):
    find / find_next / find_prev:           O(log n)
    find_min / find_max:                    O(log n)
    insert / delete:                        O(log n)
    build(X):                               O(n log n)
    iteration (iter_order):                 O(n)

Properties:
    Same code as the Recitation 6 Set; only the node class underneath changed.
    Inserting an existing key replaces the item and returns False.

Source: Recitation 6 code (BST_Node and Set_Binary_Tree), unchanged, using the
Recitation 7 Binary_Node. The PDF of Recitation 7 does not repeat this code.
"""

from avl_node import Binary_Node, Binary_Tree


class Item:                                       # helper (not in the PDF)
    def __init__(self, key, value=None):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"Item({self.key}, {self.value!r})"


class BST_Node(Binary_Node):
    def subtree_find(A, k):                       # O(h)
        if k < A.item.key:
            if A.left: return A.left.subtree_find(k)
        elif k > A.item.key:
            if A.right: return A.right.subtree_find(k)
        else: return A
        return None

    def subtree_find_next(A, k):                  # O(h)
        if A.item.key <= k:
            if A.right: return A.right.subtree_find_next(k)
            else: return None
        elif A.left:
            B = A.left.subtree_find_next(k)
            if B: return B
        return A

    def subtree_find_prev(A, k):                  # O(h)
        if A.item.key >= k:
            if A.left: return A.left.subtree_find_prev(k)
            else: return None
        elif A.right:
            B = A.right.subtree_find_prev(k)
            if B: return B
        return A

    def subtree_insert(A, B):                     # O(h)
        if B.item.key < A.item.key:
            if A.left: A.left.subtree_insert(B)
            else: A.subtree_insert_before(B)
        elif B.item.key > A.item.key:
            if A.right: A.right.subtree_insert(B)
            else: A.subtree_insert_after(B)
        else: A.item = B.item


class Set_Binary_Tree(Binary_Tree):               # Set AVL
    def __init__(self): super().__init__(BST_Node)

    def iter_order(self): yield from self

    def build(self, X):
        for x in X: self.insert(x)

    def find_min(self):
        if self.root:
            return self.root.subtree_first().item

    def find_max(self):
        if self.root:
            return self.root.subtree_last().item

    def find(self, k):
        if self.root:
            node = self.root.subtree_find(k)
            if node: return node.item

    def find_next(self, k):
        if self.root:
            node = self.root.subtree_find_next(k)
            if node: return node.item

    def find_prev(self, k):
        if self.root:
            node = self.root.subtree_find_prev(k)
            if node: return node.item

    def insert(self, x):
        new_node = self.Node_Type(x)
        if self.root:
            self.root.subtree_insert(new_node)
            if new_node.parent is None: return False
        else:
            self.root = new_node
        self.size += 1
        return True

    def delete(self, k):
        assert self.root
        node = self.root.subtree_find(k)
        assert node
        ext = node.subtree_delete()
        if ext.parent is None: self.root = None
        self.size -= 1
        return ext.item


if __name__ == "__main__":
    S = Set_Binary_Tree()
    S.build(Item(k, f"v{k}") for k in range(1, 16))   # sorted keys: a chain without AVL

    print([x.key for x in S.iter_order()])   # [1, 2, ..., 15]
    print(S.root.height)                     # 3   (without balancing it would be 14)
    print(S.find(6))                         # Item(6, 'v6')
    print(S.find_next(6), S.find_prev(6))    # Item(7, 'v7') Item(5, 'v5')
    print(S.delete(8))                       # Item(8, 'v8')
    print([x.key for x in S.iter_order()])   # [1, ..., 7, 9, ..., 15]
    print(S.root.height)                     # 3
