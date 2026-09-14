```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        def binary_search(nums, left, right, target):

            if left > right:
                return left

            mid = (left + right) // 2

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                return binary_search(nums, mid + 1, right, target)

            else:
                return binary_search(nums, left, mid - 1, target)

        return binary_search(nums, 0, len(nums) - 1, target)


# Time Complexity: O(log n)
# Space Complexity: O(log n)
```
