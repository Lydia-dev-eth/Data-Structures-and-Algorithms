class Solution:
    def isHappy(self, n: int) -> bool:
      
        # Initialize slow and fast pointers.
        slow = n
        fast = self.add_digits(n)

        # Continue until we reach 1 or detect a cycle.
        while fast != 1 and slow != fast:

            # Slow pointer moves one step.
            slow = self.add_digits(slow)

            # Fast pointer moves two steps.
            fast = self.add_digits(self.add_digits(fast))

        # If fast reaches 1, the number is happy.
        return fast == 1

    def add_digits(self, n):
        """
        Calculates the sum of the squares of a number's digits.
        """

        added = 0

        while n != 0:

            # Extract the last digit and add its square.
            added += (n % 10) ** 2

            # Remove the last digit.
            n = n // 10

        return added


# Time Complexity: O(log n) per digit transformation;
# overall O(log n) for the bounded sequence of transformations.
# Space Complexity: O(1) — only slow and fast pointers are used.
