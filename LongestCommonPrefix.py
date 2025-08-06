# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) ->  str:
        
        if not strs:
            return ""
        
        # using first word as a reference
        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs[i:]:
                if i >= len(s) or char != s[i]:
                    return strs[0][:i]
                    
        return strs[0]
    
    
# testing
solution = Solution()
strs = ["flower", "flour", "flow", "flop"] 
print(f"Testing 1: ", solution.longestCommonPrefix(strs)) # expected: flo

# test case 2
strs = [""]
print(f"Testing 2: ", solution.longestCommonPrefix(strs)) # expected: ""

# test case 3
strs = ["car", "drink", "interview", "Tesla"]
print(f"Testing 3: ", solution.longestCommonPrefix(strs)) # expected: ""

# test case 4
strs = ["join", "joke", "job", "joan"]
print(f"Testing 4: ", solution.longestCommonPrefix(strs)) # expected: jo