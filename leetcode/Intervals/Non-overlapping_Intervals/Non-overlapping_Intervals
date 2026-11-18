from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # Sort intervals by their starting values.
        intervals.sort(key=lambda x: x[0])

        # Count how many intervals must be removed.
        count = 0

        # Track the ending point of the last kept interval.
        end = intervals[0][1]

        # Process the remaining intervals.
        for i in range(1, len(intervals)):

            # If the current interval starts after or at the previous end,
            # there is no overlap.
            if end <= intervals[i][0]:
                end = intervals[i][1]

            # Otherwise, the intervals overlap.
            else:
                count += 1

                # Keep the interval that ends earlier.
                # This leaves more room for future intervals.
                end = min(intervals[i][1], end)

        return count


# Time Complexity: O(n log n) — sorting the intervals.
# Space Complexity: O(n) worst-case auxiliary space for Python sorting.
# The greedy scanning process itself uses O(1) extra space.
