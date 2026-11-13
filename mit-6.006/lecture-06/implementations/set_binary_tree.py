"""
MIT 6.006 — Lecture 6: Set Binary Tree (Binary Search Tree)

Use the traversal order to store items sorted by key. This is the
Binary Search Tree property: keys in a node's left subtree are smaller than
the node's key, keys in its right subtree are larger.

    1. find(k): walk down from the root, going left or right by comparing k.
    2. find_next(k) / find_prev(k): same walk, remembering the last node
       where we turned left (or right).
    3. insert(x): walk down to the leaf position, then insert before / after.
    4. delete(k): find the node, then subtree_delete (swap down to a leaf).

Complexity (h = height of the tree):
    find / find_next / find_prev:      O(h)
    find_min / find_max:               O(h)
    insert / delete:                   O(h)
    build(X):                          O(n h)  (n inserts)
    iter_order:                        O(n)
    Space:                             O(n)

Properties:
    O(h) is O(log n) only if the tree stays balanced; inserting sorted keys
    in order builds a chain with h = n - 1 (next lectures fix this).
    Order operations are as fast as find, unlike a hash table (O(n)).
    Inserting an existing key replaces its item and returns False.

Source: Recitation 6 code. The PDF text of Set_Binary_Tree is scrambled by
the PDF layout; the methods below are put back in order, unchanged.
"""

from binary_node import Binary_Node
from binary_tree import Binary_Tree


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


class Set_Binary_Tree(Binary_Tree):               # Binary Search Tree
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
    #        8
    #       / \
    #      3   10
    #     / \    \
    #    1   6    14
    S = Set_Binary_Tree()
    S.build(Item(k, f"v{k}") for k in (8, 3, 10, 1, 6, 14))

    print([x.key for x in S.iter_order()])   # [1, 3, 6, 8, 10, 14]
    print(len(S))                            # 6
    print(S.find(6))                         # Item(6, 'v6')
    print(S.find(7))                         # None
    print(S.find_min(), S.find_max())        # Item(1, 'v1') Item(14, 'v14')
    print(S.find_next(6))                    # Item(8, 'v8')
    print(S.find_prev(8))                    # Item(6, 'v6')
    print(S.insert(Item(6, "new")))          # False  (key exists: item replaced)
    print(S.delete(3))                       # Item(3, 'v3')
    print([x.key for x in S.iter_order()])   # [1, 6, 8, 10, 14]
