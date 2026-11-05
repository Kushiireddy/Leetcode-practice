## LeetCode 217 — Contains Duplicate

class Solution:
    def containsDuplicate(self, nums):

        # Create an empty set to store numbers we've already seen
        seen = set()

        # Traverse through each number in the list
        for num in nums:

            # Check whether this number already exists in the set
            if num in seen:
                return True

            # If it's new, add it to the set
            seen.add(num)

        # If the loop finishes, no duplicates were found
        return False
