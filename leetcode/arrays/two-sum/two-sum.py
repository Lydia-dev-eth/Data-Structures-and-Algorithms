class Solution:
    def twoSum(self, nums, target):
        # Store numbers we have already seen and their indices.
        seen = {}

        for i, num in enumerate(nums):
            # Find the value needed to reach the target.
            complement = target - num

            # If we have already seen the complement, we found the pair.
            if complement in seen:
                return [seen[complement], i]

            # Store the current number and its index.
            seen[num] = i


# Time Complexity: O(n) expected
# Space Complexity: O(n)
