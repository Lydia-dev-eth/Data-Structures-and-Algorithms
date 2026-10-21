 class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        def binary_search(nums, left, right, target):
            # If the search range is empty, left is the insertion position.
            if left > right:
                return left

            # Find the middle of the current search range.
            mid = (left + right) // 2

            # Target found.
            if target == nums[mid]:
                return mid

            # Target is greater than the middle value.
            if target > nums[mid]:
                return binary_search(nums, mid + 1, right, target)

            # Target is smaller than the middle value.
            else:
                return binary_search(nums, left, mid - 1, target)

        # Start searching the entire array.
        return binary_search(nums, 0, len(nums) - 1, target)


# Time Complexity: O(log n)
# Space Complexity: O(log n) — recursive call stack
 
