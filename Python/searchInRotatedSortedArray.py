from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.findMin(nums)
        right = self.binarySearch(pivot, len(nums) - 1, nums, target)
        left = self.binarySearch(0, pivot - 1, nums, target)

        if right != -1:
            return right
        elif left != -1:
            return left
        else:
            return -1

    def binarySearch(self, left, right, nums: List[int], target):
        while left <= right:
            mid = left + right // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def findMin(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] <= nums[r]:
                if nums[l] <= nums[res]:
                    res = l
                break
            m = (l + r) // 2
            if nums[m] <= nums[res]:
                res = m
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
