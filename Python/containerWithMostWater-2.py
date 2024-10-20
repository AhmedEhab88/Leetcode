from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxA = 0

        while left <= right:
            area = min(height[left], height[right]) * (right - left)
            maxA = max(maxA, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maxA


obj = Solution()

# print(obj.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(obj.maxArea([1, 1]))
