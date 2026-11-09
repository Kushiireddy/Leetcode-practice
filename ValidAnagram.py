## 242. Valid Anagram

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str):

        # Check whether both strings have the same length
        if len(s) != len(t):
            return False

        # Count and compare the frequency of each character
        if Counter(s) == Counter(t):
            return True
        else:
            return False

  #Counter provides an efficient, one-line solution to check if two strings are valid anagrams.
