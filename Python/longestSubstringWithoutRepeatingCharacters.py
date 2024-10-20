class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxLength = 0
        left = right = 0
        occ = set()
        while right < len(s):
            while s[right] in occ:
                occ.remove(s[left])
                left += 1
            else:
                occ.add(s[right])
                right += 1
            maxLength = max(maxLength, right - left)
        return maxLength


obj = Solution()
print(obj.lengthOfLongestSubstring("pwwkew"))
