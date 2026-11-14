class Solution:
    def isValid(self, s: str) -> bool:
       

        # A valid string must contain an even number of brackets.
        if len(s) % 2 != 0:
            return False

        # Map each closing bracket to its matching opening bracket.
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        # Store opening brackets that have not been matched yet.
        stack = []

        # Process each character in the string.
        for i in s:

            # If it is not a closing bracket, it is an opening bracket.
            if i not in mapping:
                stack.append(i)

            else:

                # A closing bracket cannot appear without an opening bracket.
                if not stack:
                    return False

                # Remove the most recent opening bracket.
                last = stack.pop()

                # Check whether the brackets match.
                if mapping[i] != last:
                    return False

        # All opening brackets must have been matched.
        return not stack


# Time Complexity: O(n) — each character is processed once.
# Space Complexity: O(n) — the stack can store up to n/2 opening brackets.
