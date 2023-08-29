from typing import List
import math


class Solution:
    def checkIfSpeedIsPossible(self, speed: int, piles: List[int], h: int):
        hoursSpent = 0
        for i in range(len(piles)):
            hoursSpent += math.ceil(piles[i] / speed)
            if hoursSpent > h:
                return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minSoFar = float("inf")

        while l <= r:
            mid = (l + r) // 2
            copyOfPiles = piles[:]
            isPossible = self.checkIfSpeedIsPossible(mid, copyOfPiles, h)
            if isPossible is True:
                if mid < minSoFar:
                    minSoFar = mid
                r = mid - 1
            else:
                l = mid + 1
        return minSoFar


obj = Solution()

# print(obj.minEatingSpeed([3, 6, 7, 11], 8))
# print(obj.minEatingSpeed([30, 11, 23, 4, 20], 5))
# print(obj.minEatingSpeed([30, 11, 23, 4, 20], 6))
print(obj.minEatingSpeed([312884470], 312884469))
