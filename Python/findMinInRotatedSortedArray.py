from typing import List

# Solved with help from neetcode: https://youtu.be/nIVW4P8b1VA


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res


obj = Solution()

# print(obj.findMin([3, 4, 5, 1, 2]))
# print(obj.findMin([4, 5, 6, 7, 0, 1, 2]))
# print(obj.findMin([11, 13, 15, 17]))
print(obj.findMin([1, 2]))
