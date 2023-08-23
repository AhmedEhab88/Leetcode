from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        montonicStack = []

        for i in range(len(temperatures) - 1, -1, -1):
            while (len(montonicStack) != 0) and (
                temperatures[montonicStack[len(montonicStack) - 1]] <= temperatures[i]
            ):
                montonicStack.pop()
            if len(montonicStack) == 0:
                res.append(0)
            else:
                res.append(montonicStack[len(montonicStack) - 1] - i)
            montonicStack.append(i)
        res.reverse()
        return res


obj = Solution()
print(obj.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
