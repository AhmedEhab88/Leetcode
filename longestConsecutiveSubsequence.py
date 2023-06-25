class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        ans = 0
        for i in range(0, len(nums)):
            if(nums[i] - 1 not in s):
                #This is the beginning of a new sequence
                current = nums[i]
                while current in s:
                    current += 1
                ans = max(ans, current - nums[i])
        return ans
test = Solution()
print(test.longestConsecutive([100,4,200,1,3,2]))                    
                    
                    