from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            cur = nums[left] + nums[right]
            if cur == target:
                return [nums[left], nums[right]]
            elif cur < target:
                left += 1
            elif cur > target:
                right -= 1
        return None

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    sol.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
        return sol


obj = Solution()

print(obj.threeSum([-1, 0, 1, 2, -1, -4]))
# print(obj.threeSum([0, 0, 0]))
