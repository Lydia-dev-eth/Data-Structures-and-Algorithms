# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:

        # Store the inorder traversal.
        result = []

        def order(root):

            # If the node is empty, stop the recursion.
            if not root:
                return

            # Visit the left subtree first.
            order(root.left)

            # Visit the current node.
            result.append(root.val)

            # Visit the right subtree.
            order(root.right)

        # Start traversal from the root.
        order(root)

        return result


# Time Complexity: O(n) — every node is visited once.
# Space Complexity: O(h) — recursive call stack, where h is tree height.
# Output Space: O(n) — stores the values of all nodes.
# Worst-case auxiliary space: O(n) for a completely unbalanced tree.
