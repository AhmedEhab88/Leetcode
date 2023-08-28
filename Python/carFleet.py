from typing import List

# Solved with help from neetcode: https://youtu.be/Pr6T-3yB9RM


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        stack = []

        for i in range(len(position)):
            pair.append([position[i], speed[i]])

        pair.sort(key=lambda x: x[0])

        for i in range(len(pair) - 1, -1, -1):
            if len(stack) == 0:
                stack.append(pair[i])
            else:
                # calculate time that current element will reach the dest
                time = (target - pair[i][0]) / pair[i][1]
                currentFleet = stack.pop()
                timeOfFleet = (target - currentFleet[0]) / currentFleet[1]
                stack.append(currentFleet)
                if time > timeOfFleet:
                    stack.append(pair[i])
        return len(stack)


obj = Solution()

print(obj.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
