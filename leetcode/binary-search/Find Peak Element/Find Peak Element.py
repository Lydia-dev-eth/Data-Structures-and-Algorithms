```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(nums, left, right):
            # If the search range is empty, the target does not exist.
            if left > right:
                return -1

            # Check the middle element.
            mid = (left + right) // 2

            # Target found.
            if nums[mid] == target:
                return mid

            # Target is larger, so search the right half.
            elif nums[mid] < target:
                return binary_search(nums, mid + 1, right)

            # Target is smaller, so search the left half.
            else:
                return binary_search(nums, left, mid - 1)

        # Start with the entire array.
        return binary_search(nums, 0, len(nums) - 1)


# Time Complexity: O(log n)
# Space Complexity: O(log n) — recursive call stack
```
