# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:

        # If the node is empty, its depth is 0.
        if not root:
            return 0

        # Recursively calculate the depth of the left subtree.
        left_depth = self.maxDepth(root.left)

        # Recursively calculate the depth of the right subtree.
        right_depth = self.maxDepth(root.right)

        # Return the larger depth plus 1 for the current node.
        return 1 + max(left_depth, right_depth)


# Time Complexity: O(n) — every node is visited once.
# Space Complexity: O(h) — recursive call stack, where h is tree height.
# Worst-case Auxiliary Space: O(n) for an unbalanced tree.
# Balanced Tree Auxiliary Space: O(log n).
