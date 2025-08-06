# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

class Solution():
    def reverseWords(self, s: str) -> str:
        # step 1 - split into separate words
        splitted = s.split()

        # step 2 - reverse the words
        reverse = list(reversed(splitted))
        print(reverse)
        
        # return 
        return ' '.join(reverse)


solution = Solution()
s = "the sky is blue"
print(f"Testing 1: ", solution.reverseWords(s))

