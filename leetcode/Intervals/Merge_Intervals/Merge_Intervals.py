from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        def binary_search(left, right):
            # If the search range is empty, the target does not exist.
            if left > right:
                return False

            # Find the middle of the current search range.
            mid = (left + right) // 2

            # Target found.
            if nums[mid] == target:
                return True

            # If left, mid, and right have the same value,
            # we cannot determine which half is sorted.
            # Shrink both boundaries to remove the duplicates.
            if nums[left] == nums[mid] == nums[right]:
                return binary_search(left + 1, right - 1)

            # Check if the left half is sorted.
            elif nums[left] <= nums[mid]:

                # Target belongs to the sorted left half.
                if nums[left] <= target < nums[mid]:
                    return binary_search(left, mid - 1)

                # Otherwise, search the right half.
                else:
                    return binary_search(mid + 1, right)

            # Otherwise, the right half is sorted.
            else:

                # Target belongs to the sorted right half.
                if nums[mid] < target <= nums[right]:
                    return binary_search(mid + 1, right)

                # Otherwise, search the left half.
                else:
                    return binary_search(left, mid - 1)

        # Start searching the entire array.
        return binary_search(0, len(nums) - 1)


# Time Complexity: O(n) worst case, O(log n) when the search space is halved.
# Space Complexity: O(n) worst case, O(log n) when the search space is halved.
# Space is used by the recursive call stack.
