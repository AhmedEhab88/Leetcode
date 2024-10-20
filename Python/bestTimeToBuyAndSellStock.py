class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = curProfit = 0
        left, right = 0, 1
        while right < len(prices):
            curProfit = max(prices[right] - prices[left], 0)
            maxProfit = max(maxProfit, curProfit)
            if curProfit == 0:
                left += 1
                right = left + 1
            else:
                right += 1
        return maxProfit

obj = Solution()
obj.maxProfit([7,6,4,3,1])
