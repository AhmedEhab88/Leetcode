from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        if s[0] == ")" or s[0] == "]" or s[0] == "}":
            return False
        stack = deque()

        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif c == "]" or c == ")" or c == "}":
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if (
                    (c == ")" and popped != "(")
                    or (c == "]" and popped != "[")
                    or (c == "}" and popped != "{")
                ):
                    return False
        return len(stack) == 0


obj = Solution()

print(obj.isValid(s="(){}}{"))
