from typing import List

class Solution:
    def TwoSum(self, nums: List[int], target: int) -> List[int]:
        
        res = []
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
                    
        return res
    
solution = Solution()
# test case 1
nums = [1,2,3,7]
target = 5
print(f"* Testing 1 *:", solution.TwoSum(nums, target)) # expected: [1, 2]

# test case 2
nums = []
target = 0
print("** Testing 2 **: ", solution.TwoSum(nums, target)) # expected: []


# test case 3:
nums = [0, 1, 4, 2, 8, 9, 10]
target = 3
print("*** Testing 3 *** :", solution.TwoSum(nums, target)) # expected: [1,3]

# test case 4:
nums = [123,1,221, 9, 8, 7, 36, 5, 4, 3, 2, 1, 0, 12, 143, 5235, 53, 23, 353, 2, 353, 4, 45, 354, 5, 394, 95, 53, 532, 4235, 23, 1234, 1321, 343, 6]
target = 129
print(f"**** Testing 4 ****: ", solution.TwoSum(nums, target))
    
    