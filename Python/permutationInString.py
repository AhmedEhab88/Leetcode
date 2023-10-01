class Solution:
    # Solved with help from neetcode: https://youtu.be/UbyhOgBN834

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hashS1, hashS2 = [0] * 26, [0] * 26

        for i in range(len(s1)):
            hashS1[ord(s1[i]) - ord("a")] += 1
            hashS2[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(0, 26):
            if hashS1[i] == hashS2[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            hashS2[index] += 1

            if hashS1[index] == hashS2[index]:
                matches += 1
            elif hashS1[index] + 1 == hashS2[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            hashS2[index] -= 1

            if hashS1[index] == hashS2[index]:
                matches += 1
            elif hashS1[index] - 1 == hashS2[index]:
                matches -= 1

        return False


obj = Solution()
print(obj.checkInclusion("abc", "ccccbbbbaaaa"))
print(obj.checkInclusion("ab", "eidbaooo"))
print(obj.checkInclusion("ab", "eidboaoo"))
print(obj.checkInclusion("adc", "dcda"))
