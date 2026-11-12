class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      
        # Strings with different lengths cannot be anagrams.
        if len(s) != len(t):
            return False

        # Store the frequency of each character in s.
        store = {}

        for i in s:
            if i in store:
                store[i] += 1
            else:
                store[i] = 1

        # Match characters in t against the stored frequencies.
        for i in t:
            if i not in store:
                return False

            store[i] -= 1

            # Remove characters whose frequency reaches zero.
            if store[i] == 0:
                del store[i]

        # If the dictionary is empty, all frequencies match.
        return not store


# Time Complexity: O(n)
# Space Complexity: O(k) — hash map storing distinct characters
