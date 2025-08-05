# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


# from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        string1 = ""
        # step 1 - change to all alphanumeric
        for c in s:
            if c.isalnum():
                string1 += c
        print(string1)
        
        # step 2 - change to lowercase
        string2 = ""
        for c in string1:
            string2 += c.lower()
        print(string2)

        # step 3 - check if it is a palindrome
        i = 0
        j = len(string2) - 1
        
        while j > i:
            # check each letter
            if string2[i] != string2[j]:
                return False
            # otherwise
            i += 1
            j -= 1
        return True
            
            
        
        
# testing
solution = Solution()
s = "!Kayak!"
print(f"Testing 1: ", solution.isPalindrome(s))

# case 2
s = "What a nice day!"
print(f"Testing 2: ", solution.isPalindrome(s))

        