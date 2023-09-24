class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        hashmap = {}
        start, end, counter, maxSoFar = 0, 1, 1, 1
        hashmap[s[start]] = start
        while end < len(s):
            if s[end] in hashmap:
                oldStart = start
                start = hashmap[s[end]] + 1
                for i in range(oldStart, start):
                    hashmap.pop(s[i])
                hashmap[s[end]] = end
                counter = len(hashmap)
                end += 1
                continue
            hashmap[s[end]] = end
            counter += 1
            end += 1
            maxSoFar = max(counter, maxSoFar)
        return maxSoFar
