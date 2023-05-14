from collections import defaultdict

# SOLVED

# ----- IDEA -----:
# To validate rows and cols is easy, just have a set for each row and col,
# iterate through the sudoku board (matrix), check if current value is present in the current row or col
# set, if it is, return false. If not, add the value in the respective row and col set.

# To validate the 9 squares present in the sudoku board, first split the board into 3 rows and 3 columns.
#   0 1 2
# 0[ , ,
# 1  , ,
# 2  , , ]
# Top left square is indexed (0,0), the next square is (0,1), the last square is (2,2)
# To know which square the current element is in, divide it's row and cols co-ordinate each by 3
# So if an element is placed at (4,4), it would be in the square index (1,1)
# Each square would have its own set just as the rows and cols
# Check if the current element value has not already been in the current square's set.
# If yes, return false, if no, add it to the set and continue


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Create sets for to validate each: rows, cols and squares
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(0, 9):  # rows
            for col in range(0, 9):  # cols
                if board[row][col] != ".":
                    if (
                        board[row][col] in rows[row]
                        or board[row][col] in squares[(row // 3, col // 3)]
                        or board[row][col] in cols[col]
                    ):
                        return False
                    else:
                        rows[row].add(board[row][col])
                        cols[col].add(board[row][col])
                        squares[(row // 3, col // 3)].add(board[row][col])
        return True


obj = Solution()
print(
    obj.isValidSudoku(
        [
            ["5", "3", ".", ".", "8", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
