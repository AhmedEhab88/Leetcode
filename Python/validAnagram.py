class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        occ = {}
        for letter in s:
            occ[letter] = occ.get(letter, 0) + 1
        for letter in t:
            if letter in occ:
                occ[letter] = occ.get(letter) - 1
                if occ[letter] < 0:
                    return False
            else: 
                return False
        return True

obj = Solution()
print(obj.isAnagram("anagram", "granama"))
