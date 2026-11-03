#LeetCode 20 — Valid Parentheses

class Solution:
    def isValid(self, s):
        # Store opening brackets that haven't been matched yet
        stack = []

        # Match each closing bracket with its opening bracket
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        # Check each character in the string
        for char in s:

            # If it's an opening bracket, store it
            if char in ("(", "[", "{"):
                stack.append(char)

            else:

                # No opening bracket is available to match
                if not stack:
                    return False

                # Check whether the latest opening bracket matches
                if stack[-1] != pairs[char]:
                    return False

                # The brackets match, so remove the opening bracket
                stack.pop()

        # Valid only if no unmatched opening brackets remain
        return len(stack) == 0
