from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs)):
            res += strs[i]
            res += "-"
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        word = ''
        for c in s:
          if c != "-":
              word += c 
          else:
              res.append(word)
              word = ''
        return res
    
obj = Solution()
encodedString = obj.encode(["neet","code","love","you"])
decodedString = obj.decode(encodedString)
encodedString2 = obj.encode(["we","say",":","yes","!@#$%^&*()"])
decodedString2 = obj.decode(encodedString2)
print(decodedString2)