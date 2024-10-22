from collections import Counter
import math


class Solution:
    def is_satisfied(self, one, two):
        for char, count in one.items():
            if two.get(char, 0) < count:
                return False  # If any count in two is less than in one, return False
        return True  # All counts are satisfied

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        # if len(s) == 1:
        #     if s[0] == t[0]:
        #         return s[0]
        #     else:
        #         return ""
        countT = {}
        for char in t:
            countT[char] = 1 + countT.get(t, 0)

        minimum = math.inf
        l = 0
        countS = {}
        res = ""
        for r in range(len(s)):
            if s[r] in countT:
                countS[s[r]] = 1 + countS.get(s[r], 0)

            if self.is_satisfied(countT, countS):
                while l < r and s[l] not in countT:
                    l += 1
                if r - l + 1 < minimum:
                    res = s[l : r + 1]
                    minimum = r - l + 1
                # all character found
                if s[l] in countS:
                    countS[s[l]] -= 1
                    l += 1
        return res


obj = Solution()
print(obj.minWindow("ADOBECODEBANC", "ABC"))
# print(obj.minWindow("a", "a"))
print(obj.minWindow("ab", "b"))
