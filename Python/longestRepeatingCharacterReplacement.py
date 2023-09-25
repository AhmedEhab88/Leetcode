class Solution:
    # Solved with neetcode help: https://youtu.be/gqXU1UyA8pk
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, res = 0, 0, 1
        hashMap = {}

        while r < len(s):
            if s[r] not in hashMap:
                hashMap[s[r]] = 1
            else:
                hashMap[s[r]] += 1
            lengthOfWindow = r - l + 1
            largestFrequency = self.findLargestFrequency(hashMap)
            if lengthOfWindow - largestFrequency > k:
                hashMap[s[l]] -= 1
                l += 1
                r += 1
            else:
                res = max(res, lengthOfWindow)
                r += 1
        return res

    def findLargestFrequency(self, hashMap):
        maxSoFar = -1
        for key in hashMap:
            maxSoFar = max(maxSoFar, hashMap[key])
        return maxSoFar


obj = Solution()
# print(obj.characterReplacement("ABBCDE", 2))
print(obj.characterReplacement("AABABBA", 1))
