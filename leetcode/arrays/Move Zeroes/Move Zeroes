```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        slow = 0
        count = 0

        # Move all non-zero elements to the front.
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            else:
                count += 1

        # Fill the remaining positions with zeros.
        i = len(nums) - count

        while count > 0:
            nums[i] = 0
            i += 1
            count -= 1


# Time Complexity: O(n)
# Space Complexity: O(1)
```
