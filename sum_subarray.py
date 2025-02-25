'''
the problem is to find the sum of subb array 
and solution is first in inntialise the curent sum and max sum and update the 
both and finally return the maximum sum


'''


from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        
        return max_sum
    
ab = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = ab.maxSubArray(nums)
print(max_sum)