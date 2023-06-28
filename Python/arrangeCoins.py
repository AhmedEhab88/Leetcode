class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 1
        r = n
        res = 0
        while l<=r:
            m = l + ( r-l ) //2
            sum = ( (m) * (m+1) ) // 2
            if sum > n:
                r = m - 1
            else:
                l = m + 1
                res = max(res, m)
        return res

#O(Logn) solution with help from: https://asyncq.com/how-to-solve-arranging-coins-problem-leetcode-441
test = Solution()
print(test.arrangeCoins(5))