from typing import List
import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        for i in range(len(tokens)):
            if tokens[i] in operators:
                b = stack.pop()
                a = stack.pop()
                if tokens[i] == "+":
                    stack.append(a + b)
                elif tokens[i] == "-":
                    stack.append(a - b)
                elif tokens[i] == "*":
                    stack.append(a * b)
                elif tokens[i] == "/":
                    stack.append(math.trunc(a / b))
            else:
                stack.append(int(tokens[i]))
        return stack.pop()


obj = Solution()
print(
    obj.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
)
