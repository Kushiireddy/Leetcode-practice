 #9.Palindrome Number

class Solution:
    def isPalindrome(self, x):
        # Convert the integer into a string
        str_val = str(x)

        # Reverse the string and compare it with the original
        if str_val == str_val[::-1]:
            # If both are the same, the number is a palindrome
            return True
        else:
            # If they differ, the number is not a palindrome
            return False
