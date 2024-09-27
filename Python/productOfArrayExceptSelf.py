from typing import List


class Solution:
    def getSuffix(self, nums):
        suffix  = [0] * len(nums)
        suffix[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums)-2, -1, -1):
           suffix[i] = nums[i] * suffix[i+1]
        return suffix

    def getPrefix(self, nums):
        prefix = [1] * len(nums) 
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
          prefix[i] = nums[i] * prefix[i-1]
        return prefix

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = self.getSuffix(nums)
        prefix = self.getPrefix(nums)
        res = [0] * len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                res[i] = suffix[i+1]
            elif i == len(nums) -1:
                res[i] = prefix[i-1]
            else:
                res[i] = suffix[i+1] * prefix[i-1]
        return res

obj = Solution()
print(obj.productExceptSelf([1,2,3,4])) 