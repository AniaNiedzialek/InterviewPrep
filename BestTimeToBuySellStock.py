# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# ===============================================================  

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        resMax = 0
        buy = prices[0]
        sell = 0
        
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]

            else: 
                sell = prices[i]
            if sell - buy > resMax:
                resMax = sell - buy
        return resMax            
            
    
# testing
solution = Solution()
prices = [7,1,5,3,6,4]
print("Testing 1: ", solution.maxProfit(prices)) # expected: 5 

# case 2:
prices = [7,6,4,3,1]
print(f"Testing 2: ", solution.maxProfit(prices)) # expected: 0

# case 3:
prices = [1]
print(f"Testing 3: ", solution.maxProfit(prices)) # expected: 0

# case 4:
prices = [2, 10, 11, 4, 3, 120]
print(f"Testing 5: ", solution.maxProfit(prices)) # expected: 118