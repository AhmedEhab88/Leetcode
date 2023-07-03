import math


class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = -math.inf
        while l < r:
            currentHeight = min(height[l], height[r])
            width = r - l
            area = currentHeight * width
            maxArea = max(maxArea, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxArea


test = Solution()
print(test.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
