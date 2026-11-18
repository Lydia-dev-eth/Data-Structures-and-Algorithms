from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        i = 0
        n = len(intervals)
        b = []

        while i < n and intervals[i][1] < newInterval[0]:
            b.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        b.append(newInterval)

        while i < n:
            b.append(intervals[i])
            i += 1

        return b


# Time Complexity: O(n)
# Space Complexity: O(n) — output list.
