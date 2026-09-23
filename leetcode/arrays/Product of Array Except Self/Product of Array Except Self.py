```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_list = [1] * len(nums)

        # Build prefix products.
        prefix = 1

        for i in range(len(nums)):
            product_list[i] = prefix
            prefix *= nums[i]

        # Multiply by suffix products.
        suffix = 1

        for i in range(len(nums) - 1, -1, -1):
            product_list[i] *= suffix
            suffix *= nums[i]

        return product_list


# Time Complexity: O(n)
# Space Complexity: O(1) extra space
# (Output array is not counted as extra space.)
```
