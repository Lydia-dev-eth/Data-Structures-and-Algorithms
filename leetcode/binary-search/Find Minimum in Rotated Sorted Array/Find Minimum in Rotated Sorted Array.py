```python
class Solution:
    def findMin(self, nums: List[int]) -> int:

        def binary_search(left, right):
            # When one element remains, it is the minimum.
            if left == right:
                return nums[left]

            # Find the middle of the current search range.
            mid = (left + right) // 2

            # The minimum must be to the right of mid.
            if nums[mid] > nums[right]:
                return binary_search(mid + 1, right)

            # The minimum is at mid or somewhere to its left.
            else:
                return binary_search(left, mid)

        # Start searching the entire array.
        return binary_search(0, len(nums) - 1)


# Time Complexity: O(log n)
# Space Complexity: O(log n) — recursive call stack
```
