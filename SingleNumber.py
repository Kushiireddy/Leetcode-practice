#Leetcode 136

from collections import Counter

class Solution:
    def singleNumber(self, nums: list[int]):  #"Define a function called singleNumber that belongs to the Solution class. It receives a list of integers called nums."

        # Count how many times each number appears
        counts = Counter(nums)

        # Check each number and its frequency
        for num, count in counts.items():

            # Find the number that appears only once
            if count == 1:
                return num
