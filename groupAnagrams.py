from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mapA = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            mapA[key].append(word)
        
        return list(mapA.values())
    
# testing 
solution = Solution()
strs = ["eat", "ate", "big", "gib", "tea"]
print(f"Testing 1: ", solution.groupAnagrams(strs))