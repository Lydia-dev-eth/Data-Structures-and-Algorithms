class Solution:
    def isUgly(self, n: int) -> bool:

        # Zero and negative numbers are not ugly numbers.
        if n == 0:
            return False

        # Check the three allowed prime factors.
        for divider in [2, 3, 5]:

            # Keep removing the current factor while possible.
            while n % divider == 0:
                n //= divider

        # If the remaining number is 1, it is ugly.
        return n == 1


# Time Complexity: O(log n) — repeated division reduces n.
# Space Complexity: O(1) — constant extra space.
