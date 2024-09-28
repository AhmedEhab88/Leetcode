from typing import List


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


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        appended = False
        for str in strs: 
            appended = False
            if len(res) == 0:
                res.append([str])
            else:
                for i in range(0, len(res)):
                    if self.isAnagram(str, res[i][0]):
                        res[i].append(str)
                        appended = True
                        break
                if appended is False:
                    res.append([str])
        return res
    
obj = Solution()
print(obj.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))