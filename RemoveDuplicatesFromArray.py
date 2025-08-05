
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.


from typing import List



class Solution:
    def removeDup(self, nums: List[int]) -> int:
        # start from the first element assuming it is always unique
        
        
        i = 0
        # base case - if empty return 0
        if not nums:
            return 0
        
        # use j to track the other elements
        for j in range(1, len(nums)):
            # check if the elements are unique
            if nums[i] != nums[j]:
                # move to the next i
                i += 1
                # override the element
                nums[i] = nums[j]
        # otherwise we skip the duplicates
        return i + 1


# testing
solution = Solution()
nums = [0,1,2,2,3,4,4]
print(f"Testing 1: ", solution.removeDup(nums))
        
nums = []
print(f"Testing 2: ", solution.removeDup(nums))