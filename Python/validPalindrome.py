class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        s = s.casefold()
        newString = ""
        for c in s:
            if (ord(c) >= 97 and ord(c) <= 122) or c.isdigit():
                newString += c
        if len(newString) == 0:
            return True

        left = 0
        right = len(newString) - 1

        while left <= right:
            if newString[left] != newString[right]:
                return False
            left += 1
            right -= 1
        return True


obj = Solution()
print(obj.isPalindrome("0P"))
