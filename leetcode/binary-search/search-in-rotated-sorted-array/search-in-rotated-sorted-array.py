class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(nums, left, right):
            # If the search range is empty, the target does not exist.
            if left > right:
                return -1

            # Find the middle of the current search range.
            mid = (left + right) // 2

            # Target found.
            if nums[mid] == target:
                return mid

            # Check if the left half is sorted.
            if nums[left] <= nums[mid]:

                # Target belongs to the sorted left half.
                if nums[left] <= target < nums[mid]:
                    return binary_search(nums, left, mid - 1)

                # Otherwise, search the right half.
                else:
                    return binary_search(nums, mid + 1, right)

            # Otherwise, the right half is sorted.
            else:
 
                 # Target belongs to the sorted right half.
                if nums[mid] < target <= nums[right]:
                    return binary_search(nums, mid + 1, right)

                # Otherwise, search the left half.
                else:
                    return binary_search(nums, left, mid - 1)

        # Start searching the entire array.
        return binary_search(nums, 0, len(nums) - 1)


# Time Complexity: O(log n)
# Space Complexity: O(log n) — recursive call stack
