# [
#     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", "6", "."],
#     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", "6", ".", ".", ".", ".", "2", "8", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
# ]


# [
#     [".", ".", ".", ".", "5", ".", ".", "1", "."],
#     [".", "4", ".", "3", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", "3", ".", ".", "1"],
#     ["8", ".", ".", ".", ".", ".", ".", "2", "."],
#     [".", ".", "2", ".", "7", ".", ".", ".", "."],
#     [".", "1", "5", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", "2", ".", ".", "."],
#     [".", "2", ".", "9", ".", ".", ".", ".", "."],
#     [".", ".", "4", ".", ".", ".", ".", ".", "."],
# ]


from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        # Rows
        for r in range(9):
            for c in range(9):
                if board[r][c] in rows[r] or cols[c] or squares[r / 3, c / 3]:
                    return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[r / 3, c / 3].add(board[r][c])
        return True


obj = Solution()
obj.isValidSudoku(
    [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
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
