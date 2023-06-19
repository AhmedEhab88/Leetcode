class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        l = r = 0
        res = []
        while l < len(nums) and r < len(nums):
          if r < (len(nums) - 1) and nums[r+1] - nums[r] == 1:
             r += 1
          else: 
             if r == l:
                res.append(f"{nums[r]}")
                l += 1
                r += 1
             else:
                res.append(f"{nums[l]}->{nums[r]}")
                r += 1
                l = r
        return res
test = Solution()
print(test.summaryRanges([0,2,3,4,6,8,9]))