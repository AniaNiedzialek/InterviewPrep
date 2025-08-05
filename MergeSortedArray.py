# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



from typing import List
class Solution:
    def merge(self, nums1: List[int], nums2: List[int], m: int, n: int) -> None:
        
        # to get the last indices
        i = m - 1
        j = n - 1
        last = m + n - 1
        
      

        while last >= 0:
            #  case 1: elements left only in nums2
            if i < 0:
                nums1[last] = nums2[j]
                j -= 1
            # case 2: elements left only in nums1            
            elif j < 0:
                nums1[last] = nums1[i]
                i -= 1
            elif nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1
                
                
            # move last to the left
            last -= 1
        print(nums1)
            
        
        
            
# testing
solution = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
print(f"Testing 1: ", solution.merge(nums1, nums2, 3, 3))
        
        
        