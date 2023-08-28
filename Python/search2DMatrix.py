from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lm = ln = 0
        rm, rn = len(matrix) - 1, len(matrix[0]) - 1
        arrayFound = False

        while lm < len(matrix) and rm >= 0:
            midm = lm + (rm - lm) // 2  # Array
            midn = ln + (rn - ln) // 2  # Element in array

            if arrayFound:
                while ln <= rn:
                    midn = ln + (rn - ln) // 2
                    if target < matrix[midm][midn]:
                        rn = midn - 1
                    elif target > matrix[midm][midn]:
                        ln = midn + 1
                    else:
                        return True
                return False
            elif target < matrix[midm][midn]:
                if target < matrix[midm][0]:
                    rm -= 1
                elif target > matrix[midm][0]:
                    arrayFound = True
                else:
                    return True
            elif target > matrix[midm][midn]:
                if target > matrix[midm][rn]:
                    lm += 1
                elif target < matrix[midm][rn]:
                    arrayFound = True
                else:
                    return True
            elif target == matrix[midm][midn]:
                return True
        return False


obj = Solution()

# print(obj.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(obj.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 5))
# print(obj.searchMatrix([[1, 3]], 3))
