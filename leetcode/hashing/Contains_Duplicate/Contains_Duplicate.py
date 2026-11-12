class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Determines whether an array contains any duplicate elements
        using a hash map to track previously seen numbers.
        """

        # Store numbers that have already been encountered.
        store = {}

        for i in range(len(nums)):

            # If the number already exists, a duplicate is found.
            if nums[i] in store:
                return True

            # Mark the number as seen.
            else:
                store[nums[i]] = True

        # No duplicate elements were found.
        return False


# Time Complexity: O(n) — iterate through the array once.
# Space Complexity: O(n) — hash map stores previously seen elements.
