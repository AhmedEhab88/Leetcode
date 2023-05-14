class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        sum = 0
        width = len(mat[0])
        for i in range(0, width):
            sum += mat[i][i]  # Primary diagonal
            sum += mat[i][width - 1 - i]  # Secondary Diagonal

        # Take away middle element calculated twice
        if width % 2 != 0:
            sum -= mat[width // 2][width // 2]

        return sum

    def main(self):
        print(self.diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


obj = Solution()
obj.main()
