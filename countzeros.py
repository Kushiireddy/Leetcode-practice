#283 Move Zeros
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:

        # Pointer to track where the next non-zero number should go
        k = 0

        # Traverse through the list
        for i in range(len(nums)):

            # If the current number is non-zero
            if nums[i] != 0:

                # Move it to the next available position
                nums[k] = nums[i]

                # Move the pointer forward
                k += 1

        # Fill the remaining positions with zeros
        for i in range(k, len(nums)):
            nums[i] = 0
