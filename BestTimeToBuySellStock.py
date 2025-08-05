# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# ===============================================================  

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy_price = prices[0]
        sell_price = 0
        resMax = 0
        
        for i in range(1, len(prices)):
            print(f"prices of i is {prices[i]}")
            # change to the new point since the previous one was too high
            if prices[i] < buy_price:
                print(f"hello")
                buy_price = prices[i]
                
            # otherwise, compute the global max
            else:
                sell_price = prices[i]
                
            if sell_price - buy_price > resMax:
                resMax = sell_price - buy_price
            
                
        
        return resMax
    
# testing
solution = Solution()
prices = [7,1,5,3,6,4]
print("Testing 1: ", solution.maxProfit(prices)) # expected: 5 

# case 2:
prices = [7,6,4,3,1]
print(f"Testing 2: ", solution.maxProfit(prices)) # expected: 0