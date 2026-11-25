# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:

        # If the node is empty, no valid path exists.
        if not root:
            return False

        # Check if the current node is a leaf.
        if not root.left and not root.right:

            # Check whether the remaining target equals the leaf value.
            return targetSum == root.val

        # Subtract the current node's value from the target.
        # Recursively search the left and right subtrees.
        return (
            self.hasPathSum(root.left, targetSum - root.val) or
            self.hasPathSum(root.right, targetSum - root.val)
        )


# Time Complexity: O(n) — every node may be visited once.
# Space Complexity: O(h) — recursive call stack, where h is tree height.
# Balanced Tree: O(log n) auxiliary space.
# Worst-case (unbalanced tree): O(n) auxiliary space.
