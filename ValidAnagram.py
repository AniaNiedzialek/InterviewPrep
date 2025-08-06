# Given two strings s and t, return true if t is an anagram of s, and false otherwise.



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS, mapT = {}, {}
        
        for i in s:
            # initialize the letters in the hashmap
            if i not in mapS:
                mapS[i] = 0
            # adjust the number of occurrence
            mapS[i] += 1
            
        for j in t:
            if j not in mapT:
                mapT[j] = 0
            mapT[j] += 1
        
        return mapS == mapT
            
            
            
# testing
solution = Solution()
s = "anagram"
t = "nagaram"
print(f"Testing 1: ", solution.isAnagram(s, t)) # true

# case 2
s = "hello"
t = "bye"
print(f"Testing 2: ", solution.isAnagram(s, t)) # expected false

