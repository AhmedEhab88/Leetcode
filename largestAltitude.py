class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        start = 0
        maxSoFar = start
        for i in range(0, len(gain)):
            start += gain[i]
            if start > maxSoFar:
                maxSoFar = start

        return maxSoFar

obj = Solution()
print(obj.largestAltitude([-4,-3,-2,-1,4,3,2])) 