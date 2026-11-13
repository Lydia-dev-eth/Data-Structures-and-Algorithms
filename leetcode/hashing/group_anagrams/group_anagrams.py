class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}

        for word in strs:

            # Sort the characters to create a common key for anagrams.
            key = ''.join(sorted(word))

            if key in store:

                # Add the word to its existing anagram group.
                store[key].append(word)

            else:

                # Create a new group for a previously unseen key.
                store[key] = [word]

        # Collect all anagram groups into the final result.
        list1 = []

        for i in store.values():
            list1.append(i)

        return list1


# Time Complexity: O(n * k log k)
# Space Complexity: O(n * k)
# n = number of words, k = maximum length of a word.
