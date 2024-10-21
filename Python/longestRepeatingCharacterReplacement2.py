from typing import List


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        occ = {}
        left = right = 0

        while right < len(s):
            occ[s[right]] = 1 + occ.get(s[right], 0)
            windowSize = right - left + 1
            if (windowSize - max(occ.values())) > k:
                # invalid window
                occ[s[left]] -= 1
                left += 1
            maxLength = max(maxLength, windowSize)
            right += 1
        return maxLength


obj = Solution()
print(obj.characterReplacement("AABABBA", 1))
