from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # create hashmap 
        countText = Counter(text)
        balloon = Counter("balloon")
        

        # create result variable to store max number of instances stored
        res = len(text)
        # result can't be bigger than the length of the word

        # step 3 - loop through the hashmap
        for c in balloon:
            res = min(res, countText[c] // balloon [c])
        return res
    
    
# test cases
solution = Solution()
text = "bbaaaaallooooooonsss"
print(f"Testing 1: ", solution.maxNumberOfBalloons(text))

# test case 2
text = "loonbalxballpoon"
print(f"Testing 2: ", solution.maxNumberOfBalloons(text))