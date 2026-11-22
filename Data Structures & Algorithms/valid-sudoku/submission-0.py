class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for _ in range(len(board))]
        col=[set() for _ in range(len(board))]
        boxes=[set() for _ in range(len(board))]
        
        for r in range(len(board)):
            for c in range(len(board)):
                value=board[r][c]
                if value==".":
                    continue
                box = (r//3) * 3 +(c//3)
                if value in row[r] or value in col[c] or value in boxes[box]:
                    return False
                row[r].add(value)
                col[c].add(value)
                boxes[box].add(value)
        return True




        